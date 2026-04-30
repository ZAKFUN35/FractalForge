import bpy
from bpy.types import Operator
from ..nodes import blob

class FF_OT_ConvertBlob(Operator):
    bl_idname = "ff.convert_blob"
    bl_label = "Превратить в блобы"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        selected_objects =[obj for obj in context.selected_objects if obj.type == 'MESH']
        
        if not selected_objects:
            self.report({'WARNING'}, "Выберите хотя бы один Mesh-объект!")
            return {'CANCELLED'}

        geo_tree = blob.create_node_group()
        mat = blob.get_or_create_material()

        for obj in selected_objects:
            mod_name = "FF Blob Modifier"
            
            if mod_name not in obj.modifiers:
                mod = obj.modifiers.new(name=mod_name, type='NODES')
            else:
                mod = obj.modifiers[mod_name]
                
            mod.node_group = geo_tree
            
            if hasattr(geo_tree, "interface"):
                for item in geo_tree.interface.items_tree:
                    if item.item_type == 'SOCKET' and item.name == "Material":
                        mod[item.identifier] = mat
                        break
                        
        return {'FINISHED'}

classes = (FF_OT_ConvertBlob,)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)