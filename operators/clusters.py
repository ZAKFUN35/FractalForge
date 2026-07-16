"""
FF Clusters - Спавнер растительности и окружения!
Этот скрипт отвечает за кнопки в UI, 
которые по одному клику создают готовые полянки травы, клевера, ромашек и облаков.
Всё максимально автоматизировано! ╰(*°▽°*)╯
"""

import bpy
from bpy.types import Operator
from ..nodes import grass, clover, chamomile, macadam, bridge

# Костыль для Linux и других регистрозависимых файловых систем, 
# чтобы ничего не отвалилось при переносе проекта на другую ОС.
try:
    from ..nodes import clouds
except ImportError:
    from ..nodes import Clouds as clouds


def _create_patch_object(name, with_color_mask=True):
    """
    Зачем нам фиктивный меш с одной вершиной, если в Blender 5.2+ геоноды можно вешать на Empty?
    А вот зачем: Empty не умеет хранить атрибуты цвета вершин (Vertex Colors)!
    А нам жизненно необходим атрибут "ColorMask", чтобы мы могли раскрашивать 
    нашу траву и облака процедурно прямо из интерфейса. 
    Поэтому создаем супер-дешевый меш из одной точки. 
    Оптимизация не пострадала! (⌐■_■)
    """
    mesh = bpy.data.meshes.new(name + "_Mesh")
    mesh.from_pydata([(0, 0, 0)], [],[])
    
    if with_color_mask:
        mesh.color_attributes.new(name="ColorMask", type='BYTE_COLOR', domain='CORNER')
        
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.scene.collection.objects.link(obj)
    
    return obj


def _apply_modifier(obj, mod_name, node_group, mat=None):
    """Вешает FF-модификатор и прокидывает материал, если он есть."""
    
    # 1. Создаем или получаем модификатор, чтобы не плодить дубликаты
    if mod_name not in obj.modifiers:
        mod = obj.modifiers.new(name=mod_name, type='NODES')
    else:
        mod = obj.modifiers[mod_name]
        
    # 2. Назначаем группу нод модификатору
    mod.node_group = node_group
    
    # 3. ФОРСИРОВАННО обновляем сцену! 
    # Блендер иногда тупит и не успевает "прочитать" группу нод. 
    # Эта строчка заставляет его очнуться и создать реальные сокеты в интерфейсе модификатора.
    bpy.context.view_layer.update()
    
    # 4. Проставляем материал именно в этот инстанс модификатора
    # (Наш любимый Blender 5.2+ API - смотри функцию в bridge.py).
    if mat:
        bridge.set_modifier_input(mod, node_group, "Material", mat)
                
    return mod


def _activate(obj, mod):
    """
    Просто наводим марафет после спавна: 
    Включаем видимость, выделяем объект, прячем сетку и активируем модификатор, 
    чтобы я мог сразу крутить ползунки в UI без лишних кликов.
    """
    obj.hide_viewport = False
    obj.hide_set(False)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    obj.show_wire = False
    obj.show_all_edges = False
    try:
        bpy.context.object.modifiers.active = mod
    except Exception:
        pass
    bpy.context.view_layer.update()


# ============================================================================
#  ТРАВА
# ============================================================================
class FF_OT_CreateGrass(Operator):
    bl_idname = "ff.create_grass"
    bl_label = "Создать траву"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        mat = grass.get_or_create_material()
        ng  = grass.create_node_group()
        obj = _create_patch_object("Grass_Patch", with_color_mask=True)
        mod = _apply_modifier(obj, "FF Grass Modifier", ng, mat)
        _activate(obj, mod)
        return {'FINISHED'}


# ============================================================================
#  КЛЕВЕР
# ============================================================================
class FF_OT_CreateClover(Operator):
    bl_idname = "ff.create_clover"
    bl_label = "Создать клевер"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        mat = clover.get_or_create_material()
        ng  = clover.create_node_group()
        obj = _create_patch_object("Clover_Patch", with_color_mask=True)
        mod = _apply_modifier(obj, "FF Clover Modifier", ng, mat)
        _activate(obj, mod)
        return {'FINISHED'}


# ============================================================================
#  РОМАШКА
# ============================================================================
class FF_OT_CreateChamomile(Operator):
    bl_idname = "ff.create_chamomile"
    bl_label = "Создать ромашку"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        mat = chamomile.get_or_create_material()
        ng  = chamomile.create_node_group()
        obj = _create_patch_object("Chamomile_Patch", with_color_mask=True)
        mod = _apply_modifier(obj, "FF Chamomile Modifier", ng, mat)
        _activate(obj, mod)
        return {'FINISHED'}


# ============================================================================
#  ЩЕБЕНКА
# ============================================================================
class FF_OT_CreateMacadam(Operator):
    bl_idname = "ff.create_macadam"
    bl_label = "Создать щебенку"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        mat = macadam.get_or_create_material()
        ng  = macadam.create_node_group()
        
        # Для камней маска цвета не нужна, они и так красивые!
        obj = _create_patch_object("Rocks_Patch", with_color_mask=False)
        
        mod_name = "FF Rocks Modifier"
        if mod_name in obj.modifiers:
            obj.modifiers.remove(obj.modifiers[mod_name])
            
        mod = _apply_modifier(obj, mod_name, ng, mat)
        _activate(obj, mod)
        return {'FINISHED'}


# ============================================================================
#  ОБЛАКА
# ============================================================================
class FF_OT_CreateClouds(Operator):
    bl_idname = "ff.create_clouds"
    bl_label = "Создать облака"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        mat = clouds.get_or_create_material()
        ng  = clouds.create_node_group()
        obj = _create_patch_object("Clouds_Patch", with_color_mask=True)
        mod = _apply_modifier(obj, "FF Clouds Modifier", ng, mat)
        _activate(obj, mod)
        return {'FINISHED'}


classes = (
    FF_OT_CreateGrass, 
    FF_OT_CreateClover, 
    FF_OT_CreateChamomile, 
    FF_OT_CreateMacadam,
    FF_OT_CreateClouds
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)