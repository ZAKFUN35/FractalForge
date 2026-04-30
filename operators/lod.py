import bpy
import bmesh
from bpy.types import Operator
from collections import defaultdict


def _get_or_create_collection(name, parent):
    for child in parent.children:
        if child.name == name:
            return child
    col = bpy.data.collections.new(name)
    parent.children.link(col)
    return col


def _move_to_collection(obj, target):
    for coll in list(obj.users_collection):
        coll.objects.unlink(obj)
    target.objects.link(obj)


def _read_fractal_ids(obj):
    depsgraph = bpy.context.evaluated_depsgraph_get()
    obj_eval  = obj.evaluated_get(depsgraph)
    mesh_eval = obj_eval.to_mesh()
    if 'fractal_id' not in mesh_eval.attributes:
        obj_eval.to_mesh_clear()
        return None
    attr     = mesh_eval.attributes['fractal_id']
    vert_ids = [int(d.value) for d in attr.data]
    unique   = sorted(set(vert_ids))
    obj_eval.to_mesh_clear()
    return unique


def _cut_lod_mesh(obj, keep_ids, lod_name):
    depsgraph = bpy.context.evaluated_depsgraph_get()
    obj_eval  = obj.evaluated_get(depsgraph)
    mesh_eval = obj_eval.to_mesh()
    attr     = mesh_eval.attributes['fractal_id']
    vert_ids = [int(d.value) for d in attr.data]
    keep_set = set(keep_ids)
    face_keep = {poly.index for poly in mesh_eval.polygons
                 if vert_ids[poly.vertices[0]] in keep_set}
    bm = bmesh.new()
    bm.from_mesh(mesh_eval)
    bm.faces.ensure_lookup_table()
    del_f = [f for f in bm.faces if f.index not in face_keep]
    bmesh.ops.delete(bm, geom=del_f, context='FACES')
    del_e = [e for e in bm.edges if not e.link_faces]
    bmesh.ops.delete(bm, geom=del_e, context='EDGES')
    del_v = [v for v in bm.verts if not v.link_edges]
    bmesh.ops.delete(bm, geom=del_v, context='VERTS')
    new_mesh = bpy.data.meshes.new(lod_name + "_Mesh")
    bm.to_mesh(new_mesh)
    bm.free()
    for mat in mesh_eval.materials:
        new_mesh.materials.append(mat)
    obj_eval.to_mesh_clear()
    return new_mesh


class FF_OT_CreateLOD(Operator):
    bl_idname = "ff.create_lod"
    bl_label = "Создать LOD"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
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
            keep_count = max(1, int(total * (s.ratio ** level)))
            keep_ids   = unique_ids[:keep_count]
            lod_name   = f"{base_name}_lod{level}"
            lod_coll   = _get_or_create_collection(f"lod{level}", parent_coll)

            if level == 0:
                obj.name = lod_name
                _move_to_collection(obj, lod_coll)
            else:
                lod_mesh = _cut_lod_mesh(obj, keep_ids, lod_name)
                lod_obj  = bpy.data.objects.new(lod_name, lod_mesh)
                lod_obj.matrix_world = obj.matrix_world.copy()
                lod_coll.objects.link(lod_obj)

        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        context.view_layer.objects.active = obj
        self.report({'INFO'}, f"LOD создан: {s.levels} уровней")
        return {'FINISHED'}


classes = (FF_OT_CreateLOD,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
