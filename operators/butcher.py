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
        if obj is None or obj.type != 'MESH':
            self.report({'ERROR'}, "Выдели меш-объект")
            return {'CANCELLED'}

        depsgraph = context.evaluated_depsgraph_get()
        obj_eval  = obj.evaluated_get(depsgraph)
        mesh_eval = obj_eval.to_mesh()

        if 'fractal_id' not in mesh_eval.attributes:
            obj_eval.to_mesh_clear()
            self.report({'ERROR'}, "fractal_id не найден - убедись что геоноды его записывают")
            return {'CANCELLED'}

        attr     = mesh_eval.attributes['fractal_id']
        vert_ids = [int(d.value) for d in attr.data]

        face_groups = defaultdict(list)
        for poly in mesh_eval.polygons:
            fid = vert_ids[poly.vertices[0]]
            face_groups[fid].append(poly.index)

        unique_ids   = sorted(face_groups.keys())
        collection   = obj.users_collection[0] if obj.users_collection else context.scene.collection
        base_name    = obj.name
        world_matrix = obj.matrix_world.copy()
        created      = []

        for fid in unique_ids:
            keep_faces = set(face_groups[fid])
            bm = bmesh.new()
            bm.from_mesh(mesh_eval)
            bm.faces.ensure_lookup_table()
            del_f = [f for f in bm.faces if f.index not in keep_faces]
            bmesh.ops.delete(bm, geom=del_f, context='FACES')
            del_e = [e for e in bm.edges if not e.link_faces]
            bmesh.ops.delete(bm, geom=del_e, context='EDGES')
            del_v = [v for v in bm.verts if not v.link_edges]
            bmesh.ops.delete(bm, geom=del_v, context='VERTS')

            new_mesh = bpy.data.meshes.new(f"{base_name}_{fid}")
            bm.to_mesh(new_mesh)
            bm.free()

            new_obj = bpy.data.objects.new(f"{base_name}_{fid}", new_mesh)
            new_obj.matrix_world = world_matrix
            collection.objects.link(new_obj)

            if new_mesh.vertices:
                min_z      = min(v.co.z for v in new_mesh.vertices)
                max_z      = max(v.co.z for v in new_mesh.vertices)
                tol        = (max_z - min_z) * 0.01 + 1e-5
                base_verts = [v for v in new_mesh.vertices if v.co.z <= min_z + tol]
                base_x     = sum(v.co.x for v in base_verts) / len(base_verts)
                base_y     = sum(v.co.y for v in base_verts) / len(base_verts)
                offset     = Vector((base_x, base_y, min_z))
                for v in new_mesh.vertices:
                    v.co -= offset
                new_mesh.update()
                new_obj.location = world_matrix @ offset

            created.append(new_obj)

        obj_eval.to_mesh_clear()
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
