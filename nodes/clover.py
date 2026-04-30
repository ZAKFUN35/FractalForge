import bpy
import math

def get_or_create_material():
    mat_name = "M_Clover"
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
        bsdf.inputs["Base Color"].default_value = hex_to_lin("FFFFFF")
        uv_node = nt.nodes.new("ShaderNodeUVMap")
        uv_node.uv_map = "UVMap"
        uv_node.location = (bsdf.location.x - 300, bsdf.location.y)
        
        col_attr = nt.nodes.new("ShaderNodeAttribute")
        col_attr.attribute_name = "ColorMask"
        col_attr.location = (bsdf.location.x - 300, bsdf.location.y - 150)
        nt.links.new(col_attr.outputs["Color"], bsdf.inputs["Base Color"])
    return mat


def create_node_group():
    group_name = "FF Clover Nodes"
    
    if group_name in bpy.data.node_groups:
        return bpy.data.node_groups[group_name]
        
    nt = bpy.data.node_groups.new(type='GeometryNodeTree', name=group_name)
    nt.color_tag = 'GEOMETRY'
    
    if hasattr(nt, "interface"):
        nt.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
        panel_field = nt.interface.new_panel("Placement")
        panel_main = nt.interface.new_panel("Structure")
        panel_sphere = nt.interface.new_panel("Center Sphere")
        panel_stem = nt.interface.new_panel("Stem")
        panel_petal = nt.interface.new_panel("Petal Shape")
        panel_detail = nt.interface.new_panel("Detail")
        
        seed_val = nt.interface.new_socket(name="Seed", in_out='INPUT', socket_type='NodeSocketInt', parent=panel_field)
        count_val = nt.interface.new_socket(name="Count", in_out='INPUT', socket_type='NodeSocketInt', parent=panel_field)
        patch_rad = nt.interface.new_socket(name="Patch Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent=panel_field)
        min_scale = nt.interface.new_socket(name="Min Scale", in_out='INPUT', socket_type='NodeSocketFloat', parent=panel_field)
        max_scale = nt.interface.new_socket(name="Max Scale", in_out='INPUT', socket_type='NodeSocketFloat', parent=panel_field)
        
        petal_count = nt.interface.new_socket(name="Petals Count", in_out='INPUT', socket_type='NodeSocketInt', parent=panel_main)
        clover_rad = nt.interface.new_socket(name="Center Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent=panel_main)
        petal_scale = nt.interface.new_socket(name="Petal Scale", in_out='INPUT', socket_type='NodeSocketFloat', parent=panel_main)
        
        sphere_scale = nt.interface.new_socket(name="Scale", in_out='INPUT', socket_type='NodeSocketVector', parent=panel_sphere)
        sphere_subdiv = nt.interface.new_socket(name="Subdivisions", in_out='INPUT', socket_type='NodeSocketInt', parent=panel_sphere)
        
        stem_len = nt.interface.new_socket(name="Stem Length", in_out='INPUT', socket_type='NodeSocketFloat', parent=panel_stem)
        stem_thick = nt.interface.new_socket(name="Stem Thickness", in_out='INPUT', socket_type='NodeSocketFloat', parent=panel_stem)
        stem_res = nt.interface.new_socket(name="Stem Resolution", in_out='INPUT', socket_type='NodeSocketInt', parent=panel_stem)
        
        res_x = nt.interface.new_socket(name="Resolution X", in_out='INPUT', socket_type='NodeSocketInt', parent=panel_petal)
        res_y = nt.interface.new_socket(name="Resolution Y", in_out='INPUT', socket_type='NodeSocketInt', parent=panel_petal)
        center_dens = nt.interface.new_socket(name="Center Density", in_out='INPUT', socket_type='NodeSocketFloat', parent=panel_petal)
        sharpness = nt.interface.new_socket(name="Side Sharpness", in_out='INPUT', socket_type='NodeSocketFloat', parent=panel_petal)
        cleavage = nt.interface.new_socket(name="Cleavage Depth", in_out='INPUT', socket_type='NodeSocketFloat', parent=panel_petal)
        vert_crease = nt.interface.new_socket(name="Vertical Crease (X)", in_out='INPUT', socket_type='NodeSocketFloat', parent=panel_petal)
        horiz_curve = nt.interface.new_socket(name="Horizontal Curve (Y)", in_out='INPUT', socket_type='NodeSocketFloat', parent=panel_petal)
        
        mat_socket = nt.interface.new_socket(name="Material", in_out='INPUT', socket_type='NodeSocketMaterial', parent=panel_detail)
        shade_smooth = nt.interface.new_socket(name="Smooth Shading", in_out='INPUT', socket_type='NodeSocketBool', parent=panel_detail)
        col_petal = nt.interface.new_socket(name="Petal Color", in_out='INPUT', socket_type='NodeSocketColor', parent=panel_detail)
        col_center = nt.interface.new_socket(name="Center Color", in_out='INPUT', socket_type='NodeSocketColor', parent=panel_detail)
        col_stem = nt.interface.new_socket(name="Stem Color", in_out='INPUT', socket_type='NodeSocketColor', parent=panel_detail)
        
    else:
        nt.outputs.new('NodeSocketGeometry', "Geometry")
        seed_val = nt.inputs.new('NodeSocketInt', "Seed"); count_val = nt.inputs.new('NodeSocketInt', "Count"); patch_rad = nt.inputs.new('NodeSocketFloat', "Patch Radius"); min_scale = nt.inputs.new('NodeSocketFloat', "Min Scale"); max_scale = nt.inputs.new('NodeSocketFloat', "Max Scale"); petal_count = nt.inputs.new('NodeSocketInt', "Petals Count"); clover_rad = nt.inputs.new('NodeSocketFloat', "Center Radius"); petal_scale = nt.inputs.new('NodeSocketFloat', "Petal Scale"); 
        sphere_scale = nt.inputs.new('NodeSocketVector', "Scale"); sphere_subdiv = nt.inputs.new('NodeSocketInt', "Subdivisions")
        stem_len = nt.inputs.new('NodeSocketFloat', "Stem Length"); stem_thick = nt.inputs.new('NodeSocketFloat', "Stem Thickness"); stem_res = nt.inputs.new('NodeSocketInt', "Stem Resolution")
        res_x = nt.inputs.new('NodeSocketInt', "Resolution X"); res_y = nt.inputs.new('NodeSocketInt', "Resolution Y")
        center_dens = nt.inputs.new('NodeSocketFloat', "Center Density"); sharpness = nt.inputs.new('NodeSocketFloat', "Side Sharpness"); cleavage = nt.inputs.new('NodeSocketFloat', "Cleavage Depth"); vert_crease = nt.inputs.new('NodeSocketFloat', "Vertical Crease (X)"); horiz_curve = nt.inputs.new('NodeSocketFloat', "Horizontal Curve (Y)")
        mat_socket = nt.inputs.new('NodeSocketMaterial', "Material"); shade_smooth = nt.inputs.new('NodeSocketBool', "Smooth Shading")
        col_petal = nt.inputs.new('NodeSocketColor', "Petal Color"); col_center = nt.inputs.new('NodeSocketColor', "Center Color"); col_stem = nt.inputs.new('NodeSocketColor', "Stem Color")

    seed_val.default_value = 0; count_val.default_value = 3; patch_rad.default_value = 0.140
    min_scale.default_value = 0.050; max_scale.default_value = 0.120
    petal_count.default_value = 4; clover_rad.default_value = 0.050; petal_scale.default_value = 0.600   
    sphere_scale.default_value = (0.080, 0.080, 0.032); sphere_subdiv.default_value = 1
    stem_len.default_value = 2.000; stem_thick.default_value = 0.025; 
    stem_res.default_value = 3; stem_res.min_value = 3 
    res_x.default_value = 7; res_y.default_value = 3; res_y.min_value = 2
    center_dens.default_value = 1.500; sharpness.default_value = 1.000; cleavage.default_value = 0.750; vert_crease.default_value = -0.350; horiz_curve.default_value = 0.200   
    shade_smooth.default_value = True
    col_petal.default_value = (0.0, 1.0, 0.0, 1.0)
    col_center.default_value = (0.0, 1.0, 0.0, 1.0)
    col_stem.default_value = (0.0, 1.0, 0.0, 1.0)

    nodes = nt.nodes; links = nt.links
    group_input = nodes.new("NodeGroupInput"); group_input.location = (-3500, 0)
    group_output = nodes.new("NodeGroupOutput"); group_output.is_active_output = True; group_output.location = (2800, 0)

    step_sub=nodes.new("ShaderNodeMath"); step_sub.operation='SUBTRACT'; step_sub.inputs[1].default_value=1.0; step_div=nodes.new("ShaderNodeMath"); step_div.operation='DIVIDE'; step_div.inputs[1].default_value=2.0; step_floor=nodes.new("ShaderNodeMath"); step_floor.operation='FLOOR'; step_mul=nodes.new("ShaderNodeMath"); step_mul.operation='MULTIPLY'; step_mul.inputs[1].default_value=2.0; step_add=nodes.new("ShaderNodeMath"); step_add.operation='ADD'; step_add.inputs[1].default_value=1.0
    links.new(group_input.outputs["Resolution X"], step_sub.inputs[0]); links.new(step_sub.outputs[0], step_div.inputs[0]); links.new(step_div.outputs[0], step_floor.inputs[0]); links.new(step_floor.outputs[0], step_mul.inputs[0]); links.new(step_mul.outputs[0], step_add.inputs[0])

    pt_grid = nodes.new("GeometryNodeMeshGrid"); pt_grid.inputs['Size X'].default_value = 2.0; pt_grid.inputs['Size Y'].default_value = 2.0;
    links.new(step_add.outputs[0], pt_grid.inputs['Vertices X']); links.new(group_input.outputs["Resolution Y"], pt_grid.inputs['Vertices Y'])
    
    pt_pos = nodes.new("GeometryNodeInputPosition"); pt_sep = nodes.new("ShaderNodeSeparateXYZ"); links.new(pt_pos.outputs[0], pt_sep.inputs[0])
    
    math_abs_x = nodes.new("ShaderNodeMath"); math_abs_x.operation = 'ABSOLUTE'; links.new(pt_sep.outputs['X'], math_abs_x.inputs[0])
    math_sign = nodes.new("ShaderNodeMath"); math_sign.operation = 'SIGN'; links.new(pt_sep.outputs['X'], math_sign.inputs[0])
    math_pow = nodes.new("ShaderNodeMath"); math_pow.operation = 'POWER'; links.new(math_abs_x.outputs[0], math_pow.inputs[0]); links.new(group_input.outputs["Center Density"], math_pow.inputs[1])
    math_mul_sign = nodes.new("ShaderNodeMath"); math_mul_sign.operation = 'MULTIPLY'; links.new(math_sign.outputs[0], math_mul_sign.inputs[0]); links.new(math_pow.outputs[0], math_mul_sign.inputs[1])
    math_pi = nodes.new("ShaderNodeMath"); math_pi.operation = 'MULTIPLY'; math_pi.inputs[1].default_value = math.pi / 2.0; links.new(math_mul_sign.outputs[0], math_pi.inputs[0])
    math_sine = nodes.new("ShaderNodeMath"); math_sine.operation = 'SINE'; links.new(math_pi.outputs[0], math_sine.inputs[0])
    math_x_scale = nodes.new("ShaderNodeMath"); math_x_scale.operation = 'MULTIPLY'; links.new(math_sine.outputs[0], math_x_scale.inputs[0]); links.new(group_input.outputs["Side Sharpness"], math_x_scale.inputs[1])

    math_abs = nodes.new("ShaderNodeMath"); math_abs.operation = 'ABSOLUTE'; links.new(math_x_scale.outputs[0], math_abs.inputs[0])
    math_sqrt_1 = nodes.new("ShaderNodeMath"); math_sqrt_1.operation = 'SQRT'; links.new(math_abs.outputs[0], math_sqrt_1.inputs[0])
    math_cleavage = nodes.new("ShaderNodeMath"); math_cleavage.operation = 'MULTIPLY'; links.new(math_sqrt_1.outputs[0], math_cleavage.inputs[0]); links.new(group_input.outputs["Cleavage Depth"], math_cleavage.inputs[1])
    math_sqr = nodes.new("ShaderNodeMath"); math_sqr.operation = 'MULTIPLY'; links.new(math_x_scale.outputs[0], math_sqr.inputs[0]); links.new(math_x_scale.outputs[0], math_sqr.inputs[1])
    math_sub = nodes.new("ShaderNodeMath"); math_sub.operation = 'SUBTRACT'; math_sub.inputs[0].default_value = 1.0; links.new(math_sqr.outputs[0], math_sub.inputs[1])
    math_max = nodes.new("ShaderNodeMath"); math_max.operation = 'MAXIMUM'; math_max.inputs[1].default_value = 0.0; links.new(math_sub.outputs[0], math_max.inputs[0])
    math_sqrt_2 = nodes.new("ShaderNodeMath"); math_sqrt_2.operation = 'SQRT'; links.new(math_max.outputs[0], math_sqrt_2.inputs[0])
    math_top_y = nodes.new("ShaderNodeMath"); math_top_y.operation = 'ADD'; links.new(math_cleavage.outputs[0], math_top_y.inputs[0]); links.new(math_sqrt_2.outputs[0], math_top_y.inputs[1])
    math_bot_y = nodes.new("ShaderNodeMath"); math_bot_y.operation = 'SUBTRACT'; links.new(math_cleavage.outputs[0], math_bot_y.inputs[0]); links.new(math_sqrt_2.outputs[0], math_bot_y.inputs[1])
    
    map_range = nodes.new("ShaderNodeMapRange"); map_range.inputs[1].default_value = -1.0; map_range.inputs[2].default_value = 1.0; map_range.inputs[3].default_value = 0.0; map_range.inputs[4].default_value = 1.0; links.new(pt_sep.outputs[1], map_range.inputs[0])
    math_delta = nodes.new("ShaderNodeMath"); math_delta.operation = 'SUBTRACT'; links.new(math_top_y.outputs[0], math_delta.inputs[0]); links.new(math_bot_y.outputs[0], math_delta.inputs[1])
    math_mul_fac = nodes.new("ShaderNodeMath"); math_mul_fac.operation = 'MULTIPLY'; links.new(math_delta.outputs[0], math_mul_fac.inputs[0]); links.new(map_range.outputs[0], math_mul_fac.inputs[1])
    math_new_y = nodes.new("ShaderNodeMath"); math_new_y.operation = 'ADD'; links.new(math_bot_y.outputs[0], math_new_y.inputs[0]); links.new(math_mul_fac.outputs[0], math_new_y.inputs[1])

    pt_uv_map_x = nodes.new("ShaderNodeMapRange"); pt_uv_map_x.inputs[1].default_value = -1.1; pt_uv_map_x.inputs[2].default_value = 1.1; pt_uv_map_x.inputs[3].default_value = 0.0; pt_uv_map_x.inputs[4].default_value = 0.5 
    pt_uv_map_y = nodes.new("ShaderNodeMapRange"); pt_uv_map_y.inputs[1].default_value = -1.1; pt_uv_map_y.inputs[2].default_value = 1.1; pt_uv_map_y.inputs[3].default_value = 0.5; pt_uv_map_y.inputs[4].default_value = 1.0 
    links.new(math_x_scale.outputs[0], pt_uv_map_x.inputs[0])
    links.new(math_new_y.outputs[0], pt_uv_map_y.inputs[0])
    pt_uv_comb = nodes.new("ShaderNodeCombineXYZ"); links.new(pt_uv_map_x.outputs[0], pt_uv_comb.inputs[0]); links.new(pt_uv_map_y.outputs[0], pt_uv_comb.inputs[1])

    store_petal_uv = nodes.new("GeometryNodeStoreNamedAttribute"); store_petal_uv.data_type = 'FLOAT2'; store_petal_uv.domain = 'CORNER'; store_petal_uv.inputs["Name"].default_value = "UVMap"
    links.new(pt_grid.outputs[0], store_petal_uv.inputs["Geometry"]); links.new(pt_uv_comb.outputs[0], store_petal_uv.inputs["Value"])

    store_petal_col = nodes.new("GeometryNodeStoreNamedAttribute"); store_petal_col.data_type = 'FLOAT_COLOR'; store_petal_col.domain = 'CORNER'; store_petal_col.inputs["Name"].default_value = "ColorMask"
    links.new(store_petal_uv.outputs[0], store_petal_col.inputs["Geometry"]); links.new(group_input.outputs["Petal Color"], store_petal_col.inputs["Value"])

    abs_x = nodes.new("ShaderNodeMath"); abs_x.operation = 'ABSOLUTE'; links.new(pt_sep.outputs[0], abs_x.inputs[0])
    abs_y = nodes.new("ShaderNodeMath"); abs_y.operation = 'ABSOLUTE'; links.new(pt_sep.outputs[1], abs_y.inputs[0])
    falloff_x = nodes.new("ShaderNodeMath"); falloff_x.operation = 'SUBTRACT'; falloff_x.inputs[0].default_value = 1.0; links.new(abs_x.outputs[0], falloff_x.inputs[1])
    falloff_y = nodes.new("ShaderNodeMath"); falloff_y.operation = 'SUBTRACT'; falloff_y.inputs[0].default_value = 1.0; links.new(abs_y.outputs[0], falloff_y.inputs[1])
    calc_vert = nodes.new("ShaderNodeMath"); calc_vert.operation = 'MULTIPLY'; links.new(falloff_x.outputs[0], calc_vert.inputs[0]); links.new(group_input.outputs["Vertical Crease (X)"], calc_vert.inputs[1])
    calc_horiz_base = nodes.new("ShaderNodeMath"); calc_horiz_base.operation = 'MULTIPLY'; links.new(falloff_y.outputs[0], calc_horiz_base.inputs[0]); links.new(group_input.outputs["Horizontal Curve (Y)"], calc_horiz_base.inputs[1])
    mask_edges = nodes.new("ShaderNodeMath"); mask_edges.operation = 'MULTIPLY'; links.new(calc_horiz_base.outputs[0], mask_edges.inputs[0]); links.new(falloff_x.outputs[0], mask_edges.inputs[1])
    z_final = nodes.new("ShaderNodeMath"); z_final.operation = 'ADD'; links.new(calc_vert.outputs[0], z_final.inputs[0]); links.new(mask_edges.outputs[0], z_final.inputs[1])

    comb_xyz = nodes.new("ShaderNodeCombineXYZ"); links.new(math_x_scale.outputs[0], comb_xyz.inputs[0]); links.new(math_new_y.outputs[0], comb_xyz.inputs[1]); links.new(z_final.outputs[0], comb_xyz.inputs[2]) 
    
    pt_set_pos = nodes.new("GeometryNodeSetPosition")
    links.new(store_petal_col.outputs[0], pt_set_pos.inputs[0])
    links.new(comb_xyz.outputs[0], pt_set_pos.inputs[2])

    transform_petal = nodes.new("GeometryNodeTransform"); transform_petal.inputs[1].default_value = (0.0, 1.0, 0.0); transform_petal.inputs[3].default_value = (1.2, 1.0, 1.0); links.new(pt_set_pos.outputs[0], transform_petal.inputs[0])
    
    mesh_circle = nodes.new("GeometryNodeMeshCircle"); circle_pos = nodes.new("GeometryNodeInputPosition"); align_euler = nodes.new("FunctionNodeAlignEulerToVector"); align_euler.axis = 'Y'; align_euler.pivot_axis = 'Z'; scale_xyz = nodes.new("ShaderNodeCombineXYZ")
    inst_on_pts = nodes.new("GeometryNodeInstanceOnPoints"); realize_inst = nodes.new("GeometryNodeRealizeInstances")
    
    links.new(group_input.outputs["Petals Count"], mesh_circle.inputs[0]); links.new(group_input.outputs["Center Radius"], mesh_circle.inputs[1]); links.new(circle_pos.outputs[0], align_euler.inputs["Vector"])
    links.new(group_input.outputs["Petal Scale"], scale_xyz.inputs[0]); links.new(group_input.outputs["Petal Scale"], scale_xyz.inputs[1]); links.new(group_input.outputs["Petal Scale"], scale_xyz.inputs[2])
    links.new(mesh_circle.outputs[0], inst_on_pts.inputs[0]); links.new(transform_petal.outputs[0], inst_on_pts.inputs[2]); links.new(align_euler.outputs[0], inst_on_pts.inputs[5]); links.new(scale_xyz.outputs[0], inst_on_pts.inputs[6])
    links.new(inst_on_pts.outputs[0], realize_inst.inputs[0])

    icosphere = nodes.new("GeometryNodeMeshIcoSphere"); icosphere.inputs[0].default_value = 1.0; links.new(group_input.outputs["Subdivisions"], icosphere.inputs[1])
    cen_uv_pos = nodes.new("GeometryNodeInputPosition"); cen_uv_sep = nodes.new("ShaderNodeSeparateXYZ"); links.new(cen_uv_pos.outputs[0], cen_uv_sep.inputs[0])

    cen_uv_map_x = nodes.new("ShaderNodeMapRange"); cen_uv_map_x.inputs[1].default_value = -1.0; cen_uv_map_x.inputs[2].default_value = 1.0; cen_uv_map_x.inputs[3].default_value = 0.0; cen_uv_map_x.inputs[4].default_value = 0.5
    cen_uv_map_y = nodes.new("ShaderNodeMapRange"); cen_uv_map_y.inputs[1].default_value = -1.0; cen_uv_map_y.inputs[2].default_value = 1.0; cen_uv_map_y.inputs[3].default_value = 0.0; cen_uv_map_y.inputs[4].default_value = 0.5
    links.new(cen_uv_sep.outputs['X'], cen_uv_map_x.inputs[0]); links.new(cen_uv_sep.outputs['Y'], cen_uv_map_y.inputs[0])
    cen_uv_comb = nodes.new("ShaderNodeCombineXYZ"); links.new(cen_uv_map_x.outputs[0], cen_uv_comb.inputs[0]); links.new(cen_uv_map_y.outputs[0], cen_uv_comb.inputs[1])

    store_center_uv = nodes.new("GeometryNodeStoreNamedAttribute"); store_center_uv.data_type = 'FLOAT2'; store_center_uv.domain = 'CORNER'; store_center_uv.inputs["Name"].default_value = "UVMap"
    links.new(icosphere.outputs[0], store_center_uv.inputs["Geometry"]); links.new(cen_uv_comb.outputs[0], store_center_uv.inputs["Value"])

    store_center_col = nodes.new("GeometryNodeStoreNamedAttribute"); store_center_col.data_type = 'FLOAT_COLOR'; store_center_col.domain = 'CORNER'; store_center_col.inputs["Name"].default_value = "ColorMask"
    links.new(store_center_uv.outputs[0], store_center_col.inputs["Geometry"]); links.new(group_input.outputs["Center Color"], store_center_col.inputs["Value"])
    
    sphere_z_math = nodes.new("ShaderNodeMath"); sphere_z_math.operation = 'MULTIPLY'; links.new(group_input.outputs["Vertical Crease (X)"], sphere_z_math.inputs[0]); links.new(group_input.outputs["Petal Scale"], sphere_z_math.inputs[1])
    trans_sphere_vec = nodes.new("ShaderNodeCombineXYZ"); links.new(sphere_z_math.outputs[0], trans_sphere_vec.inputs[2])

    trans_sphere = nodes.new("GeometryNodeTransform"); links.new(store_center_col.outputs[0], trans_sphere.inputs[0])
    links.new(trans_sphere_vec.outputs[0], trans_sphere.inputs[1]); links.new(group_input.outputs["Scale"], trans_sphere.inputs[3])

    stem_grid = nodes.new("GeometryNodeMeshGrid"); stem_grid.inputs['Size X'].default_value = 1.0; stem_grid.inputs['Vertices Y'].default_value = 2
    
    stem_res_add = nodes.new("ShaderNodeMath"); stem_res_add.operation = 'ADD'; stem_res_add.inputs[1].default_value = 1.0
    links.new(group_input.outputs["Stem Resolution"], stem_res_add.inputs[0])
    links.new(stem_res_add.outputs[0], stem_grid.inputs['Vertices X'])
    links.new(group_input.outputs["Stem Length"], stem_grid.inputs['Size Y'])
    
    stem_pos = nodes.new("GeometryNodeInputPosition"); stem_sep = nodes.new("ShaderNodeSeparateXYZ"); links.new(stem_pos.outputs[0], stem_sep.inputs[0])

    stem_uv_map_x = nodes.new("ShaderNodeMapRange"); stem_uv_map_x.inputs[1].default_value = -0.5; stem_uv_map_x.inputs[2].default_value = 0.5; stem_uv_map_x.inputs[3].default_value = 0.9; stem_uv_map_x.inputs[4].default_value = 1.0
    stem_uv_div_y = nodes.new("ShaderNodeMath"); stem_uv_div_y.operation = 'DIVIDE'; links.new(stem_sep.outputs['Y'], stem_uv_div_y.inputs[0]); links.new(group_input.outputs["Stem Length"], stem_uv_div_y.inputs[1])
    stem_uv_map_y = nodes.new("ShaderNodeMapRange"); stem_uv_map_y.inputs[1].default_value = -0.5; stem_uv_map_y.inputs[2].default_value = 0.5; stem_uv_map_y.inputs[3].default_value = 0.0; stem_uv_map_y.inputs[4].default_value = 1.0
    links.new(stem_sep.outputs['X'], stem_uv_map_x.inputs[0]); links.new(stem_uv_div_y.outputs[0], stem_uv_map_y.inputs[0])
    
    stem_uv_comb = nodes.new("ShaderNodeCombineXYZ"); links.new(stem_uv_map_x.outputs[0], stem_uv_comb.inputs[0]); links.new(stem_uv_map_y.outputs[0], stem_uv_comb.inputs[1])

    store_stem_uv = nodes.new("GeometryNodeStoreNamedAttribute"); store_stem_uv.data_type = 'FLOAT2'; store_stem_uv.domain = 'CORNER'; store_stem_uv.inputs["Name"].default_value = "UVMap"
    links.new(stem_grid.outputs[0], store_stem_uv.inputs["Geometry"]); links.new(stem_uv_comb.outputs[0], store_stem_uv.inputs["Value"])

    stem_wrap_add_x = nodes.new("ShaderNodeMath"); stem_wrap_add_x.operation = 'ADD'; stem_wrap_add_x.inputs[1].default_value = 0.5
    stem_wrap_mul_ang = nodes.new("ShaderNodeMath"); stem_wrap_mul_ang.operation = 'MULTIPLY'; stem_wrap_mul_ang.inputs[1].default_value = math.pi * 2.0
    links.new(stem_sep.outputs['X'], stem_wrap_add_x.inputs[0]); links.new(stem_wrap_add_x.outputs[0], stem_wrap_mul_ang.inputs[0])

    stem_wrap_sin = nodes.new("ShaderNodeMath"); stem_wrap_sin.operation = 'SINE'; stem_wrap_mul_posx = nodes.new("ShaderNodeMath"); stem_wrap_mul_posx.operation = 'MULTIPLY'
    links.new(stem_wrap_mul_ang.outputs[0], stem_wrap_sin.inputs[0]); links.new(stem_wrap_sin.outputs[0], stem_wrap_mul_posx.inputs[0]); links.new(group_input.outputs["Stem Thickness"], stem_wrap_mul_posx.inputs[1])

    stem_wrap_cos = nodes.new("ShaderNodeMath"); stem_wrap_cos.operation = 'COSINE'; stem_wrap_mul_posy = nodes.new("ShaderNodeMath"); stem_wrap_mul_posy.operation = 'MULTIPLY'
    links.new(stem_wrap_mul_ang.outputs[0], stem_wrap_cos.inputs[0]); links.new(stem_wrap_cos.outputs[0], stem_wrap_mul_posy.inputs[0]); links.new(group_input.outputs["Stem Thickness"], stem_wrap_mul_posy.inputs[1])

    stem_wrap_div_len = nodes.new("ShaderNodeMath"); stem_wrap_div_len.operation = 'DIVIDE'; stem_wrap_div_len.inputs[1].default_value = 2.0
    stem_wrap_sub_z = nodes.new("ShaderNodeMath"); stem_wrap_sub_z.operation = 'SUBTRACT'
    links.new(group_input.outputs["Stem Length"], stem_wrap_div_len.inputs[0]); links.new(stem_sep.outputs['Y'], stem_wrap_sub_z.inputs[0]); links.new(stem_wrap_div_len.outputs[0], stem_wrap_sub_z.inputs[1])

    stem_wrap_comb = nodes.new("ShaderNodeCombineXYZ"); links.new(stem_wrap_mul_posx.outputs[0], stem_wrap_comb.inputs[0]); links.new(stem_wrap_mul_posy.outputs[0], stem_wrap_comb.inputs[1]); links.new(stem_wrap_sub_z.outputs[0], stem_wrap_comb.inputs[2])

    stem_set_pos = nodes.new("GeometryNodeSetPosition"); links.new(store_stem_uv.outputs[0], stem_set_pos.inputs["Geometry"]); links.new(stem_wrap_comb.outputs[0], stem_set_pos.inputs["Position"])
    stem_merge = nodes.new("GeometryNodeMergeByDistance"); stem_merge.inputs["Distance"].default_value = 0.001; links.new(stem_set_pos.outputs[0], stem_merge.inputs["Geometry"])

    stem_flip = nodes.new("GeometryNodeFlipFaces"); links.new(stem_merge.outputs[0], stem_flip.inputs[0])
    store_stem_col = nodes.new("GeometryNodeStoreNamedAttribute"); store_stem_col.data_type = 'FLOAT_COLOR'; store_stem_col.domain = 'CORNER'; store_stem_col.inputs["Name"].default_value = "ColorMask"
    links.new(stem_flip.outputs[0], store_stem_col.inputs["Geometry"]); links.new(group_input.outputs["Stem Color"], store_stem_col.inputs["Value"])

    stem_trans = nodes.new("GeometryNodeTransform"); links.new(store_stem_col.outputs[0], stem_trans.inputs[0]); links.new(trans_sphere_vec.outputs[0], stem_trans.inputs[1])

    join_geo = nodes.new("GeometryNodeJoinGeometry")
    set_smooth = nodes.new("GeometryNodeSetShadeSmooth"); links.new(group_input.outputs["Smooth Shading"], set_smooth.inputs[2]) 
    
    vec_ground_shift = nodes.new("ShaderNodeCombineXYZ")
    trans_to_ground = nodes.new("GeometryNodeTransform")
    
    links.new(realize_inst.outputs[0], join_geo.inputs[0]) 
    links.new(trans_sphere.outputs[0], join_geo.inputs[0]) 
    links.new(stem_trans.outputs[0], join_geo.inputs[0]) 
    links.new(join_geo.outputs[0], set_smooth.inputs[0])
    
    pivot_math = nodes.new("ShaderNodeMath"); pivot_math.operation = 'SUBTRACT'
    links.new(group_input.outputs["Stem Length"], pivot_math.inputs[0])
    links.new(sphere_z_math.outputs[0], pivot_math.inputs[1])
    links.new(pivot_math.outputs[0], vec_ground_shift.inputs[2])
    
    links.new(vec_ground_shift.outputs[0], trans_to_ground.inputs[1])
    links.new(set_smooth.outputs[0], trans_to_ground.inputs[0])

    points = nodes.new("GeometryNodePoints")
    seed_offset_1 = nodes.new("ShaderNodeMath"); seed_offset_1.operation = 'ADD'; seed_offset_1.inputs[1].default_value = 1337; seed_offset_2 = nodes.new("ShaderNodeMath"); seed_offset_2.operation = 'ADD'; seed_offset_2.inputs[1].default_value = 99; seed_offset_3 = nodes.new("ShaderNodeMath"); seed_offset_3.operation = 'ADD'; seed_offset_3.inputs[1].default_value = 7
    rand_angle = nodes.new("FunctionNodeRandomValue"); rand_angle.data_type = 'FLOAT'; rand_angle.inputs["Min"].default_value = 0.0; rand_angle.inputs["Max"].default_value = math.pi * 2.0
    rand_radius = nodes.new("FunctionNodeRandomValue"); rand_radius.data_type = 'FLOAT'; rand_radius.inputs["Min"].default_value = 0.0; rand_radius.inputs["Max"].default_value = 1.0
    math_sqrt = nodes.new("ShaderNodeMath"); math_sqrt.operation = 'POWER'; math_sqrt.inputs[1].default_value = 0.5; math_mult_rad = nodes.new("ShaderNodeMath"); math_mult_rad.operation = 'MULTIPLY'; math_cos = nodes.new("ShaderNodeMath"); math_cos.operation = 'COSINE'; math_sin = nodes.new("ShaderNodeMath"); math_sin.operation = 'SINE'; math_pos_x = nodes.new("ShaderNodeMath"); math_pos_x.operation = 'MULTIPLY'; math_pos_y = nodes.new("ShaderNodeMath"); math_pos_y.operation = 'MULTIPLY'; vec_pos = nodes.new("ShaderNodeCombineXYZ"); set_point_pos = nodes.new("GeometryNodeSetPosition")
    rand_rot = nodes.new("FunctionNodeRandomValue"); rand_rot.data_type = 'FLOAT_VECTOR'; rand_rot.inputs["Min"].default_value = (0.0, 0.0, -math.pi); rand_rot.inputs["Max"].default_value = (0.0, 0.0, math.pi)
    rand_scale = nodes.new("FunctionNodeRandomValue"); rand_scale.data_type = 'FLOAT'
    inst_field = nodes.new("GeometryNodeInstanceOnPoints"); realize_field = nodes.new("GeometryNodeRealizeInstances"); set_mat = nodes.new("GeometryNodeSetMaterial")
    
    index_node = nodes.new("GeometryNodeInputIndex")
    store_fractal = nodes.new("GeometryNodeStoreNamedAttribute"); store_fractal.data_type = 'INT'; store_fractal.domain = 'INSTANCE'; store_fractal.inputs["Name"].default_value = "fractal_id"
    
    links.new(group_input.outputs["Count"], points.inputs["Count"])
    links.new(group_input.outputs["Seed"], rand_angle.inputs["Seed"]); links.new(group_input.outputs["Seed"], seed_offset_1.inputs[0]); links.new(seed_offset_1.outputs[0], rand_radius.inputs["Seed"]); links.new(group_input.outputs["Seed"], seed_offset_2.inputs[0]); links.new(seed_offset_2.outputs[0], rand_rot.inputs["Seed"]); links.new(group_input.outputs["Seed"], seed_offset_3.inputs[0]); links.new(seed_offset_3.outputs[0], rand_scale.inputs["Seed"])
    links.new(rand_radius.outputs["Value"], math_sqrt.inputs[0]); links.new(math_sqrt.outputs[0], math_mult_rad.inputs[0]); links.new(group_input.outputs["Patch Radius"], math_mult_rad.inputs[1]); links.new(rand_angle.outputs["Value"], math_cos.inputs[0]); links.new(rand_angle.outputs["Value"], math_sin.inputs[0]); links.new(math_cos.outputs[0], math_pos_x.inputs[0]); links.new(math_mult_rad.outputs[0], math_pos_x.inputs[1]); links.new(math_sin.outputs[0], math_pos_y.inputs[0]); links.new(math_mult_rad.outputs[0], math_pos_y.inputs[1]); links.new(math_pos_x.outputs[0], vec_pos.inputs[0]); links.new(math_pos_y.outputs[0], vec_pos.inputs[1]); links.new(points.outputs["Points"], set_point_pos.inputs["Geometry"]); links.new(vec_pos.outputs[0], set_point_pos.inputs["Position"])
    links.new(group_input.outputs["Min Scale"], rand_scale.inputs["Min"]); links.new(group_input.outputs["Max Scale"], rand_scale.inputs["Max"])
    links.new(set_point_pos.outputs["Geometry"], inst_field.inputs["Points"]); links.new(trans_to_ground.outputs[0], inst_field.inputs["Instance"]); links.new(rand_rot.outputs["Value"], inst_field.inputs["Rotation"]); links.new(rand_scale.outputs["Value"], inst_field.inputs["Scale"])
    
    links.new(inst_field.outputs["Instances"], store_fractal.inputs["Geometry"])
    links.new(index_node.outputs["Index"], store_fractal.inputs["Value"])
    links.new(store_fractal.outputs[0], realize_field.inputs["Geometry"])
    
    links.new(realize_field.outputs["Geometry"], set_mat.inputs["Geometry"]); links.new(group_input.outputs["Material"], set_mat.inputs["Material"]); links.new(set_mat.outputs["Geometry"], group_output.inputs["Geometry"])

    def arrange_and_frame(node_list, frame_label, start_x, start_y, color, cols=6):
        frame = nodes.new("NodeFrame")
        frame.label = frame_label
        frame.use_custom_color = True
        frame.color = color
        for i, n in enumerate(node_list):
            n.location = (start_x + (i % cols) * 200, start_y - (i // cols) * 220)
            n.parent = frame

    arrange_and_frame([step_sub, step_div, step_floor, step_mul, step_add], "Auto-Odd Resolution", -3200, 400, (0.3, 0.2, 0.2))
    arrange_and_frame([pt_grid, pt_pos, pt_sep, math_abs_x, math_sign, math_pow, math_mul_sign, math_pi, math_sine, math_x_scale, math_abs, math_sqrt_1, math_cleavage, math_sqr, math_sub, math_max, math_sqrt_2, math_top_y, math_bot_y, map_range, math_delta, math_mul_fac, math_new_y, pt_uv_map_x, pt_uv_map_y, pt_uv_comb, store_petal_uv, store_petal_col, abs_x, abs_y, falloff_x, falloff_y, calc_vert, calc_horiz_base, mask_edges, z_final, comb_xyz, pt_set_pos], "Leaf Generation Math & Planar UV", -3200, -100, (0.2, 0.3, 0.2), 8)
    arrange_and_frame([transform_petal, mesh_circle, circle_pos, align_euler, scale_xyz, inst_on_pts, realize_inst], "Petal Instancing", -1400, 0, (0.2, 0.2, 0.3), 4)
    arrange_and_frame([icosphere, cen_uv_pos, cen_uv_sep, cen_uv_map_x, cen_uv_map_y, cen_uv_comb, store_center_uv, store_center_col, sphere_z_math, trans_sphere_vec, trans_sphere], "Center Generation", -1400, -800, (0.3, 0.3, 0.2), 4)
    arrange_and_frame([stem_res_add, stem_grid, stem_pos, stem_sep, stem_uv_map_x, stem_uv_div_y, stem_uv_map_y, stem_uv_comb, store_stem_uv, stem_wrap_add_x, stem_wrap_mul_ang, stem_wrap_sin, stem_wrap_mul_posx, stem_wrap_cos, stem_wrap_mul_posy, stem_wrap_div_len, stem_wrap_sub_z, stem_wrap_comb, stem_set_pos, stem_merge, stem_flip, store_stem_col, stem_trans], "Stem Generation", -3200, -1400, (0.2, 0.3, 0.3), 8)
    arrange_and_frame([join_geo, set_smooth, pivot_math, vec_ground_shift, trans_to_ground], "Flower Assembly & Z-Pivot", -200, 0, (0.3, 0.2, 0.3), 2)
    arrange_and_frame([points, seed_offset_1, seed_offset_2, seed_offset_3, rand_angle, rand_radius, math_sqrt, math_mult_rad, math_cos, math_sin, math_pos_x, math_pos_y, vec_pos, set_point_pos, rand_rot, rand_scale, inst_field, index_node, store_fractal, realize_field, set_mat], "Field Distribution & Butcher ID", 600, 0, (0.4, 0.2, 0.2), 6)

    return nt