import bpy
from bpy.types import Operator


def _get_or_create_collection(name, parent):
    if name in bpy.data.collections:
        return bpy.data.collections[name]
    col = bpy.data.collections.new(name)
    parent.children.link(col)
    return col


def _move_to_collection(obj, target):
    for coll in list(obj.users_collection):
        coll.objects.unlink(obj)
    target.objects.link(obj)


def _create_fog_node_tree(fog_radius, voxel_size, volume_threshold):
    ng = bpy.data.node_groups.new("_FogGen", 'GeometryNodeTree')
    ng.interface.new_socket('Geometry', in_out='OUTPUT', socket_type='NodeSocketGeometry')
    ng.interface.new_socket('Geometry', in_out='INPUT',  socket_type='NodeSocketGeometry')
    nodes = ng.nodes; links = ng.links
    n_in  = nodes.new('NodeGroupInput');   n_in.location  = (0,   0)
    n_out = nodes.new('NodeGroupOutput');  n_out.location = (900, 0)
    m2p   = nodes.new('GeometryNodeMeshToPoints');   m2p.location = (200, 0)
    p2v   = nodes.new('GeometryNodePointsToVolume'); p2v.location = (450, 0)
    v2m   = nodes.new('GeometryNodeVolumeToMesh');   v2m.location = (700, 0)
    p2v.resolution_mode = 'VOXEL_SIZE'
    try:
        p2v.inputs['Radius'].default_value     = fog_radius
        p2v.inputs['Voxel Size'].default_value = voxel_size
        v2m.inputs['Threshold'].default_value  = volume_threshold
    except KeyError:
        p2v.inputs[2].default_value = fog_radius
        p2v.inputs[3].default_value = voxel_size
        v2m.inputs[1].default_value = volume_threshold
    links.new(n_in.outputs[0],       m2p.inputs['Mesh'])
    links.new(m2p.outputs['Points'], p2v.inputs['Points'])
    links.new(p2v.outputs['Volume'], v2m.inputs['Volume'])
    links.new(v2m.outputs['Mesh'],   n_out.inputs[0])
    return ng


def _fill_holes_on(obj):
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT')
    for _ in range(5):
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_non_manifold()
        bpy.ops.mesh.fill_holes(sides=0)
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.view_layer.update()


def _process_island(island, index, total, leaves_coll, node_tree, s):
    sub_coll = _get_or_create_collection(f"{index + 1} island leaves", leaves_coll)
    _move_to_collection(island, sub_coll)
    island.name = f"Island_{index + 1:03d}_leaves"

    bpy.ops.object.select_all(action='DESELECT')
    island.select_set(True)
    bpy.context.view_layer.objects.active = island
    bpy.ops.object.duplicate()
    fog_obj = bpy.context.active_object
    fog_obj.name = f"Island_{index + 1:03d}_fog"
    _move_to_collection(fog_obj, sub_coll)

    gn_mod = fog_obj.modifiers.new("FogGen", 'NODES')
    gn_mod.node_group = node_tree
    bpy.context.view_layer.objects.active = fog_obj
    bpy.ops.object.modifier_apply(modifier="FogGen")
    bpy.context.view_layer.update()

    if len(fog_obj.data.vertices) == 0:
        fog_obj.name += "_EMPTY"
        return

    remesh_mod            = fog_obj.modifiers.new("Remesh", 'REMESH')
    remesh_mod.mode       = 'VOXEL'
    remesh_mod.voxel_size = s.voxel_size
    bpy.ops.object.modifier_apply(modifier="Remesh")

    _fill_holes_on(fog_obj)

    smooth            = fog_obj.modifiers.new("Smooth", 'SMOOTH')
    smooth.factor     = s.smooth_factor
    smooth.iterations = s.smooth_iterations
    bpy.ops.object.modifier_apply(modifier="Smooth")

    _fill_holes_on(fog_obj)
    bpy.ops.object.shade_smooth()

    bpy.ops.object.select_all(action='DESELECT')
    island.select_set(True)
    bpy.context.view_layer.objects.active = island
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.mode_set(mode='OBJECT')

    try:
        island.data.use_auto_smooth = True
    except AttributeError:
        pass

    dt                  = island.modifiers.new("Transfer_Normals", 'DATA_TRANSFER')
    dt.object           = fog_obj
    dt.use_loop_data    = True
    dt.data_types_loops = {'CUSTOM_NORMAL'}
    dt.loop_mapping     = 'POLYINTERP_NEAREST'
    bpy.ops.object.modifier_apply(modifier="Transfer_Normals")

    fog_obj.hide_set(True)
    fog_obj.hide_render = True


class FF_OT_AutoNormals(Operator):
    bl_idname = "ff.auto_normals"
    bl_label = "Авто-нормали листвы"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        foliage_obj = context.active_object
        if not foliage_obj or foliage_obj.type != 'MESH':
            self.report({'ERROR'}, "Выдели меш листвы")
            return {'CANCELLED'}

        s = context.scene.ff_autonormals
        leaves_coll = _get_or_create_collection("Leaves", context.scene.collection)

        bpy.ops.object.select_all(action='DESELECT')
        foliage_obj.select_set(True)
        bpy.context.view_layer.objects.active = foliage_obj
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.separate(type='LOOSE')
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.update()

        islands =[o for o in context.selected_objects if o.type == 'MESH']
        total   = len(islands)
        if total == 0:
            self.report({'ERROR'}, "Острова не найдены")
            return {'CANCELLED'}

        node_tree = _create_fog_node_tree(s.fog_radius, s.voxel_size, s.volume_threshold)

        for i, island in enumerate(islands):
            _process_island(island, i, total, leaves_coll, node_tree, s)

        bpy.data.node_groups.remove(node_tree)
        self.report({'INFO'}, f"Готово: {total} островов обработано")
        return {'FINISHED'}


classes = (FF_OT_AutoNormals,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)