"""
FF Butcher - "Мясник" в деле!
Этот скрипт нужен для подготовки травы к Data Baker.
Он берет процедурно сгенерированный пучок травы из Geometry Nodes, находит
уникальный атрибут fractal_id и безжалостно разрубает единый меш на 
десятки независимых травинок. 

А самое главное - он сам находит самую нижнюю точку (корень) каждой травинки 
и ставит Origin ровно туда. Без этого наш WPO ветер в Unreal Engine 
просто оторвет траву от земли! ╰(*°▽°*)╯
"""

import bpy
import bmesh
from bpy.types import Operator
from mathutils import Vector
from collections import defaultdict


class FF_OT_Butcher(Operator):
    bl_idname = "ff.butcher"
    bl_label = "Порционировать"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        
        # Защита от дурака. Вдруг я забыл выделить траву перед нажатием.
        if obj is None or obj.type != 'MESH':
            self.report({'ERROR'}, "Выдели меш-объект")
            return {'CANCELLED'}

        # Просим Блендер применить все модификаторы (включая Geometry Nodes) 
        # и отдать нам финальный сгенерированный меш со всеми запеченными атрибутами.
        depsgraph = context.evaluated_depsgraph_get()
        obj_eval  = obj.evaluated_get(depsgraph)
        mesh_eval = obj_eval.to_mesh()

        # Ищем нашу метку. Если её нет - значит ноды сгенерировали геометрию криво,
        # или я забыл прокинуть атрибут fractal_id в графе. Ругаемся и отменяем.
        if 'fractal_id' not in mesh_eval.attributes:
            obj_eval.to_mesh_clear()
            self.report({'ERROR'}, "fractal_id не найден - убедись что геоноды его записывают")
            return {'CANCELLED'}

        attr     = mesh_eval.attributes['fractal_id']
        vert_ids = [int(d.value) for d in attr.data]

        # Группируем полигоны. 
        # Смотрим на первую вершину каждого полигона, читаем её ID 
        # и складываем индексы полигонов в словарик по группам.
        face_groups = defaultdict(list)
        for poly in mesh_eval.polygons:
            fid = vert_ids[poly.vertices[0]]
            face_groups[fid].append(poly.index)

        unique_ids   = sorted(face_groups.keys())
        collection   = obj.users_collection[0] if obj.users_collection else context.scene.collection
        base_name    = obj.name
        world_matrix = obj.matrix_world.copy()
        created      = []

        # ИСПРАВЛЕНИЕ КРАША ЗДЕСЬ (чистая боль из прошлого):
        # Если мы возьмем материалы напрямую из Evaluated-меша, то после его удаления 
        # в памяти останутся висящие (удаленные в C++) указатели. Блендер просто схлопнется!
        # Поэтому мы берем строго оригинальные датаблоки материалов.
        materials_list = [getattr(mat, 'original', mat) for mat in mesh_eval.materials]

        # ОПТИМИЗАЦИЯ! 
        # Мы не читаем тяжелый меш в цикле. Мы один раз загружаем его в BMesh (bm_master)
        # и сразу отпускаем depsgraph, чтобы не жрал память. Дальше работаем с копиями.
        bm_master = bmesh.new()
        bm_master.from_mesh(mesh_eval)
        bm_master.faces.ensure_lookup_table()

        obj_eval.to_mesh_clear()
        # Всё, с этой строки mesh_eval / obj_eval / depsgraph больше не трогаем. Они свободны.

        # Начинаем рубить мясо! Для каждого уникального ID травинки:
        for fid in unique_ids:
            keep_faces = set(face_groups[fid])
            
            # Копируем мастер-меш. Да, выглядит как костыль, но удалять лишнее 
            # из копии работает в разы быстрее, чем собирать новый меш по крупицам.
            bm = bm_master.copy()
            bm.faces.ensure_lookup_table()
            
            # Безжалостно удаляем все полигоны, ребра и точки, которые не относятся к текущей травинке.
            del_f = [f for f in bm.faces if f.index not in keep_faces]
            bmesh.ops.delete(bm, geom=del_f, context='FACES')
            
            del_e = [e for e in bm.edges if not e.link_faces]
            bmesh.ops.delete(bm, geom=del_e, context='EDGES')
            
            del_v = [v for v in bm.verts if not v.link_edges]
            bmesh.ops.delete(bm, geom=del_v, context='VERTS')

            # Создаем новенький чистый меш для нашей травинки и переносим в него данные.
            new_mesh = bpy.data.meshes.new(f"{base_name}_{fid}")
            bm.to_mesh(new_mesh)
            bm.free()

            # Возвращаем наши безопасные (оригинальные) материалы на место.
            for mat in materials_list:
                new_mesh.materials.append(mat)

            new_obj = bpy.data.objects.new(f"{base_name}_{fid}", new_mesh)
            new_obj.matrix_world = world_matrix
            collection.objects.link(new_obj)

            # МАГИЯ КОРНЕЙ (Origin to Bottom Center) 🪄
            # Нам нужно, чтобы точка отсчета объекта была строго у земли.
            if new_mesh.vertices:
                # Находим минимальную высоту (самые нижние точки по Z) 
                # с небольшой погрешностью (tol), чтобы захватить весь "срез" корня.
                min_z      = min(v.co.z for v in new_mesh.vertices)
                max_z      = max(v.co.z for v in new_mesh.vertices)
                tol        = (max_z - min_z) * 0.01 + 1e-5
                base_verts = [v for v in new_mesh.vertices if v.co.z <= min_z + tol]
                
                # Вычисляем центр этого корня по осям X и Y.
                base_x     = sum(v.co.x for v in base_verts) / len(base_verts)
                base_y     = sum(v.co.y for v in base_verts) / len(base_verts)
                offset     = Vector((base_x, base_y, min_z))
                
                # Сдвигаем все вершины травинки вниз и в центр, чтобы корень оказался ровно в (0, 0, 0).
                for v in new_mesh.vertices:
                    v.co -= offset
                new_mesh.update()
                
                # А сам объект двигаем на то место, где травинка росла изначально.
                new_obj.location = world_matrix @ offset

            created.append(new_obj)

        # Очищаем память от нашего мастер-меша. Он отработал своё.
        bm_master.free()

        # Красиво выделяем новые кусочки ДО удаления старого объекта, 
        # чтобы я сразу видел результат работы "Мясника".
        bpy.ops.object.select_all(action='DESELECT')
        for new_obj in created:
            new_obj.select_set(True)
            
        if created:
            context.view_layer.objects.active = created[0]

        # Убиваем оригинальный сгенерированный пучок - он больше не нужен. 🪦
        bpy.data.objects.remove(obj, do_unlink=True)

        self.report({'INFO'}, f"Готово: {len(created)} объектов в '{collection.name}'")
        return {'FINISHED'}


classes = (FF_OT_Butcher,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()