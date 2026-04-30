import bpy
from bpy.types import Operator
from ..nodes import grass, clover, chamomile, macadam


def _create_patch_object(name, with_color_mask=True):
    """Создаёт фиктивный меш-объект с одной вершиной - носитель модификатора."""
    # БОЛЬШЕ НЕТ ПРОВЕРКИ. Всегда создаем новый меш и новый объект!
    # Blender сам добавит .001, .002 к имени, если такое уже есть.
    mesh = bpy.data.meshes.new(name + "_Mesh")
    mesh.from_pydata([(0, 0, 0)], [],[])
    
    if with_color_mask:
        mesh.color_attributes.new(name="ColorMask", type='BYTE_COLOR', domain='CORNER')
        
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.scene.collection.objects.link(obj)
    
    return obj


def _apply_modifier(obj, mod_name, node_group, mat=None):
    """Вешает FF-модификатор и прокидывает материал если есть."""
    if mod_name not in obj.modifiers:
        mod = obj.modifiers.new(name=mod_name, type='NODES')
    else:
        mod = obj.modifiers[mod_name]
        
    mod.node_group = node_group
    
    if mat and hasattr(node_group, "interface"):
        for item in node_group.interface.items_tree:
            if item.item_type == 'SOCKET' and item.name == "Material":
                mod[item.identifier] = mat
                break
    return mod


def _activate(obj, mod):
    """Активирует объект и модификатор, переключает на вкладку модификаторов."""
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


# ─────────────────────────────────────────────
#  ТРАВА
# ─────────────────────────────────────────────
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


# ─────────────────────────────────────────────
#  КЛЕВЕР
# ─────────────────────────────────────────────
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


# ─────────────────────────────────────────────
#  РОМАШКА
# ─────────────────────────────────────────────
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


# ─────────────────────────────────────────────
#  ЩЕБЁНКА
# ─────────────────────────────────────────────
class FF_OT_CreateMacadam(Operator):
    bl_idname = "ff.create_macadam"
    bl_label = "Создать щебёнку"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ng  = macadam.create_node_group()
        obj = _create_patch_object("Rocks_Patch", with_color_mask=False)
        # Щебёнка - всегда пересоздаём модификатор
        mod_name = "FF Rocks Modifier"
        if mod_name in obj.modifiers:
            obj.modifiers.remove(obj.modifiers[mod_name])
        mod = obj.modifiers.new(name=mod_name, type='NODES')
        mod.node_group = ng
        _activate(obj, mod)
        return {'FINISHED'}


classes = (FF_OT_CreateGrass, FF_OT_CreateClover, FF_OT_CreateChamomile, FF_OT_CreateMacadam)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)