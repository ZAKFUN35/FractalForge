"""
FF LOD Generator - Наш контроллер уровней детализации ╰(*°▽°*)╯
Этот скрипт решает проблему жестких просадок FPS на дальних дистанциях. 
У нас тут два стула (два типа LOD):
1. Кластерные LOD (для травы и листвы) - вместо того чтобы уродовать геометрию 
   децимацией, мы просто удаляем часть травинок целиком по их "fractal_id". 
   Идеальный 2D-силуэт сохраняется, а полигонаж падает!
2. Unit LOD - классическая децимация для обычных объектов (камни, статичные меши).
"""

import re
import bpy
import bmesh
from bpy.props import BoolProperty
from bpy.types import Operator
from collections import defaultdict
from ..properties import sync_unit_objects


def _get_or_create_collection(name, parent):
    """
    Костыль для безопасной работы с коллекциями.
    Ищем коллекцию по имени, и если ее нет - создаем, чтобы не плодить 
    дубликаты вида "MyCollection.001" при каждом клике.
    """
    for child in parent.children:
        if child.name == name:
            return child
    col = bpy.data.collections.new(name)
    parent.children.link(col)
    return col


def _move_to_collection(obj, target):
    """Аккуратно перекладываем объект в нужную папку, отвязывая от старых."""
    for coll in list(obj.users_collection):
        coll.objects.unlink(obj)
    target.objects.link(obj)


def _read_fractal_ids(obj):
    """
    Лезем под капот сгенерированного меша и читаем наш кастомный атрибут "fractal_id".
    Именно по нему мы будем понимать, сколько всего уникальных травинок или 
    кластеров листьев у нас в пучке.
    """
    depsgraph = bpy.context.evaluated_depsgraph_get()
    obj_eval  = obj.evaluated_get(depsgraph)
    mesh_eval = obj_eval.to_mesh()
    
    # Защита от дурака: если атрибута нет, значит геоноды отработали криво
    if 'fractal_id' not in mesh_eval.attributes:
        obj_eval.to_mesh_clear()
        return None
        
    attr     = mesh_eval.attributes['fractal_id']
    vert_ids = [int(d.value) for d in attr.data]
    unique   = sorted(set(vert_ids))
    
    # Очищаем память, иначе Блендер тихо сойдет с ума от утечек памяти (X_x)
    obj_eval.to_mesh_clear()
    return unique


def _cut_lod_mesh(obj, keep_ids, lod_name):
    """
    Хирургическое вмешательство BMesh (O_O)
    Мы не используем тяжелые модификаторы. Берем мастер-меш, находим полигоны, 
    чьи ID не попали в белый список "keep_ids", и безжалостно их удаляем. 
    Чистая, быстрая математика на уровне вершин.
    """
    depsgraph = bpy.context.evaluated_depsgraph_get()
    obj_eval  = obj.evaluated_get(depsgraph)
    mesh_eval = obj_eval.to_mesh()
    
    attr     = mesh_eval.attributes['fractal_id']
    vert_ids = [int(d.value) for d in attr.data]
    keep_set = set(keep_ids)
    
    # Собираем индексы полигонов, которые мы хотим оставить в живых
    face_keep = {poly.index for poly in mesh_eval.polygons
                 if vert_ids[poly.vertices[0]] in keep_set}
                 
    bm = bmesh.new()
    bm.from_mesh(mesh_eval)
    bm.faces.ensure_lookup_table()
    
    # Рубим полигоны, которые не прошли проверку
    del_f = [f for f in bm.faces if f.index not in face_keep]
    bmesh.ops.delete(bm, geom=del_f, context='FACES')
    
    # Вычищаем висящие ребра и точки (ошметки от удаленных полигонов)
    del_e = [e for e in bm.edges if not e.link_faces]
    bmesh.ops.delete(bm, geom=del_e, context='EDGES')
    del_v = [v for v in bm.verts if not v.link_edges]
    bmesh.ops.delete(bm, geom=del_v, context='VERTS')
    
    new_mesh = bpy.data.meshes.new(lod_name + "_Mesh")
    bm.to_mesh(new_mesh)
    bm.free()
    
    # Переносим оригинальные материалы на наш новый обрубок
    for mat in mesh_eval.materials:
        new_mesh.materials.append(mat)
        
    obj_eval.to_mesh_clear()
    return new_mesh


class FF_OT_CreateLOD(Operator):
    bl_idname = "ff.create_lod"
    bl_label = "Создать LOD"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        """
        Генератор LOD для кластеров (трава, листва).
        Уменьшает плотность пучка на заданный ratio с каждым шагом.
        Например: LOD0 = 100% травинок, LOD1 = 50%, LOD2 = 25%.
        """
        obj = context.active_object
        if obj is None or obj.type != 'MESH':
            self.report({'ERROR'}, "Выдели меш-объект")
            return {'CANCELLED'}

        unique_ids = _read_fractal_ids(obj)
        if unique_ids is None:
            self.report({'ERROR'}, "fractal_id не найден - объект должен быть из FF Кластеров")
            return {'CANCELLED'}

        s         = context.scene.ff_lod
        total     = len(unique_ids)
        base_name = obj.name

        origin_coll = obj.users_collection[0] if obj.users_collection else context.scene.collection
        parent_coll = _get_or_create_collection(f"{base_name}_LODs", origin_coll)

        for level in range(s.levels):
            # Вычисляем, сколько уникальных травинок должно дожить до этого уровня
            keep_count = max(1, int(total * (s.ratio ** level)))
            keep_ids   = unique_ids[:keep_count]
            
            lod_name   = f"{base_name}_lod{level}"
            lod_coll   = _get_or_create_collection(f"lod{level}", parent_coll)

            if level == 0:
                # LOD 0 - это наш оригинальный меш, просто перекладываем его в нужную папку
                obj.name = lod_name
                _move_to_collection(obj, lod_coll)
            else:
                # Для остальных уровней режем геометрию
                lod_mesh = _cut_lod_mesh(obj, keep_ids, lod_name)
                lod_obj  = bpy.data.objects.new(lod_name, lod_mesh)
                lod_obj.matrix_world = obj.matrix_world.copy()
                lod_coll.objects.link(lod_obj)

        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        context.view_layer.objects.active = obj
        
        self.report({'INFO'}, f"LOD создан: {s.levels} уровней")
        return {'FINISHED'}


# ─────────────────────────────────────────────
#  LOD TYPE: UNIT (классическая децимация для обычных мешей)
# ─────────────────────────────────────────────

class FF_OT_LodUnitRefresh(Operator):
    bl_idname = "ff.lod_unit_refresh"
    bl_label = "Обновить список"
    bl_description = "Пересобрать список объектов сцены для Unit LOD"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        sync_unit_objects(context.scene)
        return {'FINISHED'}


class FF_OT_LodUnitSelectAll(Operator):
    bl_idname = "ff.lod_unit_select_all"
    bl_label = "Выделить все"
    bl_options = {'REGISTER', 'UNDO'}
    action: BoolProperty()

    def execute(self, context):
        s = context.scene.ff_lod
        for item in s.unit_objects:
            item.include = self.action
        return {'FINISHED'}


class FF_OT_LodUnitLinkSelected(Operator):
    bl_idname = "ff.lod_unit_link_selected"
    bl_label = "Привязать выделенные"
    bl_description = "Отметить/снять флаг для объектов, выделенных в 3D-вьюпорте"
    bl_options = {'REGISTER', 'UNDO'}
    action: BoolProperty()

    def execute(self, context):
        s = context.scene.ff_lod
        selected = set(context.selected_objects)
        if not selected:
            self.report({'WARNING'}, "Нет выделенных объектов во вьюпорте")
            return {'CANCELLED'}

        count = 0
        for item in s.unit_objects:
            if item.object_ref in selected:
                item.include = self.action
                count += 1
        return {'FINISHED'}


class FF_OT_LodUnitGenerate(Operator):
    bl_idname = "ff.lod_unit_generate"
    bl_label = "Создать LOD"
    bl_description = "Сгенерировать LOD-меши через последовательную децимацию для отмеченных объектов"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        """
        Генератор Unit LOD.
        Вместо того чтобы ломать оригинальный объект, мы делаем копию, 
        накидываем на нее модификатор "DECIMATE", запекаем меш, и повторяем 
        для каждого следующего уровня, умножая ratio.
        Меньше полигонов - счастливее видеокарта ^_____^
        """
        s = context.scene.ff_lod
        step_scale = s.unit_decimation_scale
        iterations = s.unit_iterations

        targets = [item for item in s.unit_objects if item.include]
        if not targets:
            self.report({'WARNING'}, "Не отмечено ни одного объекта (флаг include)")
            return {'CANCELLED'}

        for entry in targets:
            original_obj = entry.object_ref
            if not original_obj or original_obj.type != 'MESH':
                self.report({'WARNING'}, f"Объект {getattr(original_obj, 'name', 'Unknown')} не найден или не меш, пропущен.")
                continue

            base_name = re.sub(r"\.\d+$", "", original_obj.name)
            lod_collection_name = f"{base_name}"

            # Получаем или создаем коллекцию LOD
            if lod_collection_name in bpy.data.collections:
                target_collection = bpy.data.collections[lod_collection_name]
                # Вычищаем старые LOD-итерации, чтобы не мусорить. Оригинал не трогаем.
                for o in list(target_collection.objects):
                    if o != original_obj:
                        bpy.data.objects.remove(o, do_unlink=True)
            else:
                target_collection = bpy.data.collections.new(lod_collection_name)
                context.scene.collection.children.link(target_collection)

            # Прячем тяжелый оригинал от греха подальше
            original_obj.hide_set(True)
            original_obj.hide_render = True

            # LOD0 - это просто запеченный оригинал со всеми модификаторами
            lod0_mesh = bpy.data.meshes.new_from_object(original_obj.evaluated_get(context.evaluated_depsgraph_get()))
            lod0_obj = bpy.data.objects.new(f"{base_name}_LOD0", lod0_mesh)
            target_collection.objects.link(lod0_obj)

            current_obj = lod0_obj
            current_ratio = step_scale

            # Запускаем конвейер децимации
            for lod_level in range(1, iterations):
                temp_obj = current_obj.copy()
                temp_mesh = current_obj.data.copy()
                temp_obj.data = temp_mesh
                context.scene.collection.objects.link(temp_obj)

                # Вешаем модификатор и нещадно сжимаем сетку
                dec_mod = temp_obj.modifiers.new(name="FF_LodUnit_Decimate", type='DECIMATE')
                dec_mod.ratio = current_ratio

                dec_mesh = bpy.data.meshes.new_from_object(temp_obj.evaluated_get(context.evaluated_depsgraph_get()))
                
                # Убиваем временную пустышку
                bpy.data.objects.remove(temp_obj, do_unlink=True)

                new_obj = bpy.data.objects.new(f"{base_name}_LOD{lod_level}", dec_mesh)
                target_collection.objects.link(new_obj)

                current_obj = new_obj
                current_ratio *= step_scale

        self.report({'INFO'}, "Unit LOD генерация завершена (⌐■_■)")
        return {'FINISHED'}


classes = (
    FF_OT_CreateLOD,
    FF_OT_LodUnitRefresh,
    FF_OT_LodUnitSelectAll,
    FF_OT_LodUnitLinkSelected,
    FF_OT_LodUnitGenerate,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)