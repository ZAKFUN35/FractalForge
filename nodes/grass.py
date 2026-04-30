import bpy
import math

def get_or_create_material():
    mat_name = "M_Grass"
    if mat_name in bpy.data.materials:
        return bpy.data.materials[mat_name]

    def srgb(c): return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    def hex_to_lin(h):
        h = h.lstrip('#')
        r, g, b = (int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4))
        return (srgb(r), srgb(g), srgb(b), 1.0)

    mat = bpy.data.materials.new(name=mat_name)
    mat.use_nodes = True
    nt = mat.node_tree
    bsdf = nt.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = hex_to_lin("00FF00")
        col_attr = nt.nodes.new("ShaderNodeAttribute")
        col_attr.attribute_name = "ColorMask"
        col_attr.location = (bsdf.location.x - 300, bsdf.location.y - 150)
        nt.links.new(col_attr.outputs["Color"], bsdf.inputs["Base Color"])
    return mat

def create_node_group():
    group_name = "FF Grass Nodes"
    

    if group_name in bpy.data.node_groups:
        return bpy.data.node_groups[group_name]

    nt = bpy.data.node_groups.new(type='GeometryNodeTree', name=group_name)
    nt.color_tag = 'GEOMETRY'

    if hasattr(nt, "interface"):
        nt.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
        pf = nt.interface.new_panel("Placement")
        pm = nt.interface.new_panel("Blade Shape")
        pd = nt.interface.new_panel("Detail")
        seed_val   = nt.interface.new_socket(name="Seed",         in_out='INPUT', socket_type='NodeSocketInt',      parent=pf)
        count_val  = nt.interface.new_socket(name="Count",        in_out='INPUT', socket_type='NodeSocketInt',      parent=pf)
        patch_rad  = nt.interface.new_socket(name="Patch Radius", in_out='INPUT', socket_type='NodeSocketFloat',    parent=pf)
        min_scale  = nt.interface.new_socket(name="Min Scale",    in_out='INPUT', socket_type='NodeSocketFloat',    parent=pf)
        max_scale  = nt.interface.new_socket(name="Max Scale",    in_out='INPUT', socket_type='NodeSocketFloat',    parent=pf)
        res_x      = nt.interface.new_socket(name="Resolution X", in_out='INPUT', socket_type='NodeSocketInt',      parent=pm)
        res_y      = nt.interface.new_socket(name="Resolution Y", in_out='INPUT', socket_type='NodeSocketInt',      parent=pm)
        blade_h    = nt.interface.new_socket(name="Height",       in_out='INPUT', socket_type='NodeSocketFloat',    parent=pm)
        blade_w    = nt.interface.new_socket(name="Width",        in_out='INPUT', socket_type='NodeSocketFloat',    parent=pm)
        blade_bend = nt.interface.new_socket(name="Bend Strength",in_out='INPUT', socket_type='NodeSocketFloat',    parent=pm)
        mat_socket = nt.interface.new_socket(name="Material",     in_out='INPUT', socket_type='NodeSocketMaterial', parent=pd)
        shade_s    = nt.interface.new_socket(name="Smooth Shading",in_out='INPUT',socket_type='NodeSocketBool',     parent=pd)
        col_base   = nt.interface.new_socket(name="Grass Color",  in_out='INPUT', socket_type='NodeSocketColor',    parent=pd)
    else:
        nt.outputs.new('NodeSocketGeometry', "Geometry")
        seed_val   = nt.inputs.new('NodeSocketInt',      "Seed")
        count_val  = nt.inputs.new('NodeSocketInt',      "Count")
        patch_rad  = nt.inputs.new('NodeSocketFloat',    "Patch Radius")
        min_scale  = nt.inputs.new('NodeSocketFloat',    "Min Scale")
        max_scale  = nt.inputs.new('NodeSocketFloat',    "Max Scale")
        res_x      = nt.inputs.new('NodeSocketInt',      "Resolution X")
        res_y      = nt.inputs.new('NodeSocketInt',      "Resolution Y")
        blade_h    = nt.inputs.new('NodeSocketFloat',    "Height")
        blade_w    = nt.inputs.new('NodeSocketFloat',    "Width")
        blade_bend = nt.inputs.new('NodeSocketFloat',    "Bend Strength")
        mat_socket = nt.inputs.new('NodeSocketMaterial', "Material")
        shade_s    = nt.inputs.new('NodeSocketBool',     "Smooth Shading")
        col_base   = nt.inputs.new('NodeSocketColor',    "Grass Color")

    seed_val.default_value = 0; count_val.default_value = 10
    patch_rad.default_value = 0.130; min_scale.default_value = 0.800; max_scale.default_value = 1.000
    res_x.default_value = 2; res_x.min_value = 2
    res_y.default_value = 2; res_y.min_value = 2
    blade_h.default_value = 1.000; blade_w.default_value = 0.100; blade_bend.default_value = 0.080
    shade_s.default_value = True; col_base.default_value = (0.0, 1.0, 0.0, 1.0)

    nodes = nt.nodes; links = nt.links
    gi = nodes.new("NodeGroupInput");  gi.location = (-4000, 0)
    go = nodes.new("NodeGroupOutput"); go.is_active_output = True; go.location = (2800, 0)

    blade_grid = nodes.new("GeometryNodeMeshGrid")
    blade_grid.inputs['Size X'].default_value = 2.0; blade_grid.inputs['Size Y'].default_value = 2.0
    links.new(gi.outputs["Resolution X"], blade_grid.inputs['Vertices X'])
    links.new(gi.outputs["Resolution Y"], blade_grid.inputs['Vertices Y'])

    pos = nodes.new("GeometryNodeInputPosition")
    sep = nodes.new("ShaderNodeSeparateXYZ")
    links.new(pos.outputs[0], sep.inputs[0])

    map_v = nodes.new("ShaderNodeMapRange")
    map_v.inputs[1].default_value = -1.0; map_v.inputs[2].default_value = 1.0
    map_v.inputs[3].default_value = 0.0;  map_v.inputs[4].default_value = 1.0
    links.new(sep.outputs['Y'], map_v.inputs[0])

    inv_v = nodes.new("ShaderNodeMath"); inv_v.operation = 'SUBTRACT'; inv_v.inputs[0].default_value = 1.0
    links.new(map_v.outputs[0], inv_v.inputs[1])

    shape_x_base = nodes.new("ShaderNodeMath"); shape_x_base.operation = 'MULTIPLY'
    links.new(sep.outputs['X'], shape_x_base.inputs[0]); links.new(inv_v.outputs[0], shape_x_base.inputs[1])

    map_u = nodes.new("ShaderNodeMapRange")
    map_u.inputs[1].default_value = -1.0; map_u.inputs[2].default_value = 1.0
    map_u.inputs[3].default_value = 0.0;  map_u.inputs[4].default_value = 1.0
    links.new(shape_x_base.outputs[0], map_u.inputs[0])

    uv_comb = nodes.new("ShaderNodeCombineXYZ")
    links.new(map_u.outputs[0], uv_comb.inputs['X']); links.new(map_v.outputs[0], uv_comb.inputs['Y'])

    store_uv = nodes.new("GeometryNodeStoreNamedAttribute")
    store_uv.data_type = 'FLOAT2'; store_uv.domain = 'CORNER'; store_uv.inputs["Name"].default_value = "UVMap"
    links.new(blade_grid.outputs[0], store_uv.inputs["Geometry"]); links.new(uv_comb.outputs[0], store_uv.inputs["Value"])

    store_col = nodes.new("GeometryNodeStoreNamedAttribute")
    store_col.data_type = 'FLOAT_COLOR'; store_col.domain = 'CORNER'; store_col.inputs["Name"].default_value = "ColorMask"
    links.new(store_uv.outputs[0], store_col.inputs["Geometry"]); links.new(gi.outputs["Grass Color"], store_col.inputs["Value"])

    shape_x = nodes.new("ShaderNodeMath"); shape_x.operation = 'MULTIPLY'
    links.new(shape_x_base.outputs[0], shape_x.inputs[0]); links.new(gi.outputs["Width"], shape_x.inputs[1])

    b_safe = nodes.new("ShaderNodeMath"); b_safe.operation = 'ADD'; b_safe.inputs[1].default_value = 0.0001
    links.new(gi.outputs["Bend Strength"], b_safe.inputs[0])

    radius = nodes.new("ShaderNodeMath"); radius.operation = 'DIVIDE'
    links.new(gi.outputs["Height"], radius.inputs[0]); links.new(b_safe.outputs[0], radius.inputs[1])

    theta = nodes.new("ShaderNodeMath"); theta.operation = 'MULTIPLY'
    links.new(map_v.outputs[0], theta.inputs[0]); links.new(b_safe.outputs[0], theta.inputs[1])

    sin_theta = nodes.new("ShaderNodeMath"); sin_theta.operation = 'SINE'
    links.new(theta.outputs[0], sin_theta.inputs[0])
    cos_theta = nodes.new("ShaderNodeMath"); cos_theta.operation = 'COSINE'
    links.new(theta.outputs[0], cos_theta.inputs[0])

    shape_z = nodes.new("ShaderNodeMath"); shape_z.operation = 'MULTIPLY'
    links.new(radius.outputs[0], shape_z.inputs[0]); links.new(sin_theta.outputs[0], shape_z.inputs[1])

    one_minus_cos = nodes.new("ShaderNodeMath"); one_minus_cos.operation = 'SUBTRACT'; one_minus_cos.inputs[0].default_value = 1.0
    links.new(cos_theta.outputs[0], one_minus_cos.inputs[1])

    shape_y_base = nodes.new("ShaderNodeMath"); shape_y_base.operation = 'MULTIPLY'
    links.new(radius.outputs[0], shape_y_base.inputs[0]); links.new(one_minus_cos.outputs[0], shape_y_base.inputs[1])

    shape_y = nodes.new("ShaderNodeMath"); shape_y.operation = 'MULTIPLY'; shape_y.inputs[1].default_value = -1.0
    links.new(shape_y_base.outputs[0], shape_y.inputs[0])

    comb_pos = nodes.new("ShaderNodeCombineXYZ")
    links.new(shape_x.outputs[0], comb_pos.inputs['X'])
    links.new(shape_y.outputs[0], comb_pos.inputs['Y'])
    links.new(shape_z.outputs[0], comb_pos.inputs['Z'])

    set_pos = nodes.new("GeometryNodeSetPosition")
    links.new(store_col.outputs[0], set_pos.inputs['Geometry']); links.new(comb_pos.outputs[0], set_pos.inputs['Position'])

    merge_tip = nodes.new("GeometryNodeMergeByDistance"); merge_tip.inputs["Distance"].default_value = 0.001
    links.new(set_pos.outputs[0], merge_tip.inputs["Geometry"])

    set_smooth = nodes.new("GeometryNodeSetShadeSmooth")
    links.new(merge_tip.outputs[0], set_smooth.inputs[0]); links.new(gi.outputs["Smooth Shading"], set_smooth.inputs[2])

    points = nodes.new("GeometryNodePoints")
    so1 = nodes.new("ShaderNodeMath"); so1.operation = 'ADD'; so1.inputs[1].default_value = 1337
    so2 = nodes.new("ShaderNodeMath"); so2.operation = 'ADD'; so2.inputs[1].default_value = 99
    so3 = nodes.new("ShaderNodeMath"); so3.operation = 'ADD'; so3.inputs[1].default_value = 7

    rand_angle = nodes.new("FunctionNodeRandomValue"); rand_angle.data_type = 'FLOAT'
    rand_angle.inputs["Min"].default_value = 0.0; rand_angle.inputs["Max"].default_value = math.pi * 2.0
    rand_radius = nodes.new("FunctionNodeRandomValue"); rand_radius.data_type = 'FLOAT'
    rand_radius.inputs["Min"].default_value = 0.0; rand_radius.inputs["Max"].default_value = 1.0

    m_sqrt = nodes.new("ShaderNodeMath"); m_sqrt.operation = 'POWER'; m_sqrt.inputs[1].default_value = 0.5
    m_rad  = nodes.new("ShaderNodeMath"); m_rad.operation = 'MULTIPLY'
    m_cos  = nodes.new("ShaderNodeMath"); m_cos.operation = 'COSINE'
    m_sin  = nodes.new("ShaderNodeMath"); m_sin.operation = 'SINE'
    m_px   = nodes.new("ShaderNodeMath"); m_px.operation = 'MULTIPLY'
    m_py   = nodes.new("ShaderNodeMath"); m_py.operation = 'MULTIPLY'
    v_pos  = nodes.new("ShaderNodeCombineXYZ")
    spp    = nodes.new("GeometryNodeSetPosition")

    links.new(gi.outputs["Count"], points.inputs["Count"])
    links.new(gi.outputs["Seed"], rand_angle.inputs["Seed"])
    links.new(gi.outputs["Seed"], so1.inputs[0]); links.new(so1.outputs[0], rand_radius.inputs["Seed"])
    links.new(rand_radius.outputs["Value"], m_sqrt.inputs[0])
    links.new(m_sqrt.outputs[0], m_rad.inputs[0]); links.new(gi.outputs["Patch Radius"], m_rad.inputs[1])
    links.new(rand_angle.outputs["Value"], m_cos.inputs[0]); links.new(rand_angle.outputs["Value"], m_sin.inputs[0])
    links.new(m_cos.outputs[0], m_px.inputs[0]); links.new(m_rad.outputs[0], m_px.inputs[1])
    links.new(m_sin.outputs[0], m_py.inputs[0]); links.new(m_rad.outputs[0], m_py.inputs[1])
    links.new(m_px.outputs[0], v_pos.inputs[0]); links.new(m_py.outputs[0], v_pos.inputs[1])
    links.new(points.outputs["Points"], spp.inputs["Geometry"]); links.new(v_pos.outputs[0], spp.inputs["Position"])

    rand_rot = nodes.new("FunctionNodeRandomValue"); rand_rot.data_type = 'FLOAT_VECTOR'
    rand_rot.inputs["Min"].default_value = (0.0, 0.0, -math.pi)
    rand_rot.inputs["Max"].default_value = (0.0, 0.0,  math.pi)
    rand_scale = nodes.new("FunctionNodeRandomValue"); rand_scale.data_type = 'FLOAT'

    links.new(gi.outputs["Seed"], so2.inputs[0]); links.new(so2.outputs[0], rand_rot.inputs["Seed"])
    links.new(gi.outputs["Seed"], so3.inputs[0]); links.new(so3.outputs[0], rand_scale.inputs["Seed"])
    links.new(gi.outputs["Min Scale"], rand_scale.inputs["Min"]); links.new(gi.outputs["Max Scale"], rand_scale.inputs["Max"])

    inst = nodes.new("GeometryNodeInstanceOnPoints")
    links.new(spp.outputs["Geometry"], inst.inputs["Points"])
    links.new(set_smooth.outputs[0],   inst.inputs["Instance"])
    links.new(rand_rot.outputs["Value"],   inst.inputs["Rotation"])
    links.new(rand_scale.outputs["Value"], inst.inputs["Scale"])

    idx          = nodes.new("GeometryNodeInputIndex")
    store_fid    = nodes.new("GeometryNodeStoreNamedAttribute")
    store_fid.data_type = 'INT'; store_fid.domain = 'INSTANCE'; store_fid.inputs["Name"].default_value = "fractal_id"
    realize      = nodes.new("GeometryNodeRealizeInstances")
    set_mat      = nodes.new("GeometryNodeSetMaterial")

    links.new(inst.outputs["Instances"],    store_fid.inputs["Geometry"])
    links.new(idx.outputs["Index"],         store_fid.inputs["Value"])
    links.new(store_fid.outputs[0],         realize.inputs["Geometry"])
    links.new(realize.outputs["Geometry"],  set_mat.inputs["Geometry"])
    links.new(gi.outputs["Material"],       set_mat.inputs["Material"])
    links.new(set_mat.outputs["Geometry"],  go.inputs["Geometry"])

    def arrange_and_frame(node_list, frame_label, start_x, start_y, color, cols=6):
        frame = nodes.new("NodeFrame")
        frame.label = frame_label
        frame.use_custom_color = True
        frame.color = color
        for i, n in enumerate(node_list):
            n.location = (start_x + (i % cols) * 200, start_y - (i // cols) * 220)
            n.parent = frame

    arrange_and_frame([blade_grid, pos, sep, map_v, inv_v, shape_x_base], "Base Logic", -3600, 200, (0.2, 0.3, 0.2), 6)
    arrange_and_frame([map_u, uv_comb, store_uv, store_col], "UV & ColorMask", -2200, 300, (0.3, 0.3, 0.2), 4)
    arrange_and_frame([shape_x, b_safe, radius, theta, sin_theta, cos_theta, shape_z, one_minus_cos, shape_y_base, shape_y, comb_pos, set_pos, merge_tip, set_smooth], "Zero-Stretch Bend Math", -2200, -100, (0.2, 0.2, 0.3), 7)
    arrange_and_frame([points, so1, so2, so3, rand_angle, rand_radius, m_sqrt, m_rad, m_cos, m_sin, m_px, m_py, v_pos, spp], "Distribution Logic", -2800, -600, (0.3, 0.2, 0.2), 7)
    arrange_and_frame([rand_rot, rand_scale, inst, idx, store_fid, realize, set_mat], "Instancing & Butcher ID", 0, 200, (0.4, 0.2, 0.2), 4)

    return nt