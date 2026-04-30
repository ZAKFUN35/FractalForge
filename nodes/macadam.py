import bpy
import math

def create_node_group():
    group_name = "FF Rocks Nodes"
    

    if group_name in bpy.data.node_groups:
        return bpy.data.node_groups[group_name]
        
    nt = bpy.data.node_groups.new(type='GeometryNodeTree', name=group_name)
    nt.color_tag = 'GEOMETRY'
    
    if hasattr(nt, "interface"):
        nt.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
        panel_field = nt.interface.new_panel("Placement")
        panel_main = nt.interface.new_panel("Rock Shape")
        panel_detail = nt.interface.new_panel("Detail")
        
        seed_val = nt.interface.new_socket(name="Seed", in_out='INPUT', socket_type='NodeSocketInt', parent=panel_field)
        count_val = nt.interface.new_socket(name="Count", in_out='INPUT', socket_type='NodeSocketInt', parent=panel_field)
        patch_rad = nt.interface.new_socket(name="Patch Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent=panel_field)
        min_scale = nt.interface.new_socket(name="Min Scale", in_out='INPUT', socket_type='NodeSocketFloat', parent=panel_field)
        max_scale = nt.interface.new_socket(name="Max Scale", in_out='INPUT', socket_type='NodeSocketFloat', parent=panel_field)
        
        shape_seed = nt.interface.new_socket(name="Shape Seed", in_out='INPUT', socket_type='NodeSocketInt', parent=panel_main)
        if hasattr(shape_seed, "force_non_field"): shape_seed.force_non_field = True
        
        detail_val = nt.interface.new_socket(name="Detail", in_out='INPUT', socket_type='NodeSocketInt', parent=panel_main)
        if hasattr(detail_val, "force_non_field"): detail_val.force_non_field = True 
        
        base_rad = nt.interface.new_socket(name="Base Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent=panel_main)
        if hasattr(base_rad, "force_non_field"): base_rad.force_non_field = True
        
        roundness = nt.interface.new_socket(name="Roundness", in_out='INPUT', socket_type='NodeSocketVector', parent=panel_main)
        if hasattr(roundness, "force_non_field"): roundness.force_non_field = True
        
        shade_smooth = nt.interface.new_socket(name="Smooth Shading", in_out='INPUT', socket_type='NodeSocketBool', parent=panel_detail)
    else:
        nt.outputs.new('NodeSocketGeometry', "Geometry")
        seed_val = nt.inputs.new('NodeSocketInt', "Seed"); count_val = nt.inputs.new('NodeSocketInt', "Count")
        patch_rad = nt.inputs.new('NodeSocketFloat', "Patch Radius"); min_scale = nt.inputs.new('NodeSocketFloat', "Min Scale"); max_scale = nt.inputs.new('NodeSocketFloat', "Max Scale")
        shape_seed = nt.inputs.new('NodeSocketInt', "Shape Seed")
        detail_val = nt.inputs.new('NodeSocketInt', "Detail"); base_rad = nt.inputs.new('NodeSocketFloat', "Base Radius")
        roundness = nt.inputs.new('NodeSocketVector', "Roundness")
        shade_smooth = nt.inputs.new('NodeSocketBool', "Smooth Shading")

    seed_val.default_value = 0
    count_val.default_value = 15
    patch_rad.default_value = 0.750
    min_scale.default_value = 0.030
    max_scale.default_value = 0.120
    shape_seed.default_value = 2
    detail_val.default_value = 1
    base_rad.default_value = 2.870
    roundness.default_value = (0.720, 0.050, 0.140)
    shade_smooth.default_value = False

    nodes = nt.nodes; links = nt.links

    gi_rock = nodes.new("NodeGroupInput"); gi_rock.location = (-2200, 800)
    gi_uv   = nodes.new("NodeGroupInput"); gi_uv.location = (-650, 850)
    gi_dist = nodes.new("NodeGroupInput"); gi_dist.location = (-2200, -50)
    gi_inst = nodes.new("NodeGroupInput"); gi_inst.location = (-800, -100)
    
    group_output = nodes.new("NodeGroupOutput")
    group_output.is_active_output = True
    group_output.location = (800, 300)

    n_line = nodes.new('GeometryNodeMeshLine'); n_line.location = (-2000, 900)
    n_line.inputs['Offset'].default_value = (0.0, 0.0, 0.0)
    
    n_ico = nodes.new('GeometryNodeMeshIcoSphere'); n_ico.location = (-2000, 750)
    n_ico.inputs['Subdivisions'].default_value = 1
    
    seed_offset = nodes.new('ShaderNodeMath'); seed_offset.location = (-2000, 550)
    seed_offset.operation = 'ADD'; seed_offset.inputs[1].default_value = 1.0
    
    n_rand_rot = nodes.new('FunctionNodeRandomValue'); n_rand_rot.location = (-2000, 400)
    n_rand_rot.data_type = 'FLOAT_VECTOR'
    n_rand_rot.inputs['Min'].default_value = (0.0, 0.0, 0.0)
    n_rand_rot.inputs['Max'].default_value = (math.pi*2, math.pi*2, math.pi*2)
    
    n_rand_scale = nodes.new('FunctionNodeRandomValue'); n_rand_scale.location = (-1800, 400)
    n_rand_scale.data_type = 'FLOAT_VECTOR'; n_rand_scale.inputs['Max'].default_value = (1.0, 1.0, 1.0)
    
    n_inst_rock = nodes.new('GeometryNodeInstanceOnPoints'); n_inst_rock.location = (-1600, 900)
    n_bool = nodes.new('GeometryNodeMeshBoolean'); n_bool.location = (-1400, 900)
    n_bool.operation = 'INTERSECT'; n_bool.solver = 'EXACT'

    links.new(gi_rock.outputs["Detail"], n_line.inputs['Count'])
    links.new(gi_rock.outputs["Base Radius"], n_ico.inputs['Radius'])
    links.new(gi_rock.outputs["Shape Seed"], seed_offset.inputs[0])
    links.new(gi_rock.outputs["Shape Seed"], n_rand_rot.inputs['Seed'])
    links.new(seed_offset.outputs[0], n_rand_scale.inputs['Seed'])
    links.new(gi_rock.outputs["Roundness"], n_rand_scale.inputs['Min'])
    
    links.new(n_line.outputs['Mesh'], n_inst_rock.inputs['Points'])
    links.new(n_ico.outputs['Mesh'], n_inst_rock.inputs['Instance'])
    links.new(n_rand_rot.outputs['Value'], n_inst_rock.inputs['Rotation'])
    links.new(n_rand_scale.outputs['Value'], n_inst_rock.inputs['Scale'])
    if 'Mesh' in n_bool.inputs: links.new(n_inst_rock.outputs['Instances'], n_bool.inputs['Mesh'])
    else: links.new(n_inst_rock.outputs['Instances'], n_bool.inputs[0])

    edge_angle = nodes.new("GeometryNodeInputMeshEdgeAngle"); edge_angle.location = (-1150, 900)
    
    compare_angle = nodes.new("FunctionNodeCompare"); compare_angle.location = (-950, 900)
    compare_angle.data_type = 'FLOAT'; compare_angle.operation = 'GREATER_THAN'
    compare_angle.inputs[1].default_value = 0.5 
    
    uv_unwrap = nodes.new("GeometryNodeUVUnwrap"); uv_unwrap.location = (-750, 900)
    uv_unwrap.inputs["Margin"].default_value = 0.02
    
    store_uv = nodes.new("GeometryNodeStoreNamedAttribute"); store_uv.location = (-550, 900)
    store_uv.data_type = 'FLOAT2'; store_uv.domain = 'CORNER'; store_uv.inputs["Name"].default_value = "UVMap"
    
    set_smooth = nodes.new("GeometryNodeSetShadeSmooth"); set_smooth.location = (-350, 900)

    links.new(edge_angle.outputs["Unsigned Angle"], compare_angle.inputs[0])
    links.new(compare_angle.outputs[0], uv_unwrap.inputs["Seam"])
    links.new(n_bool.outputs[0], store_uv.inputs["Geometry"])
    links.new(uv_unwrap.outputs["UV"], store_uv.inputs["Value"])
    links.new(store_uv.outputs[0], set_smooth.inputs[0])
    links.new(gi_uv.outputs["Smooth Shading"], set_smooth.inputs[2])

    points = nodes.new("GeometryNodePoints"); points.location = (-2000, -50)
    
    seed_off_pos = nodes.new("ShaderNodeMath"); seed_off_pos.location = (-2000, -200)
    seed_off_pos.operation = 'ADD'; seed_off_pos.inputs[1].default_value = 1337
    
    rand_angle = nodes.new("FunctionNodeRandomValue"); rand_angle.location = (-1800, -50)
    rand_angle.data_type = 'FLOAT'; rand_angle.inputs["Min"].default_value = 0.0; rand_angle.inputs["Max"].default_value = math.pi * 2.0
    
    rand_radius = nodes.new("FunctionNodeRandomValue"); rand_radius.location = (-1800, -250)
    rand_radius.data_type = 'FLOAT'; rand_radius.inputs["Min"].default_value = 0.0; rand_radius.inputs["Max"].default_value = 1.0
    
    math_sqrt = nodes.new("ShaderNodeMath"); math_sqrt.location = (-1600, -250); math_sqrt.operation = 'POWER'; math_sqrt.inputs[1].default_value = 0.5
    math_mult_rad = nodes.new("ShaderNodeMath"); math_mult_rad.location = (-1400, -250); math_mult_rad.operation = 'MULTIPLY'
    
    math_cos = nodes.new("ShaderNodeMath"); math_cos.location = (-1600, -50); math_cos.operation = 'COSINE'
    math_sin = nodes.new("ShaderNodeMath"); math_sin.location = (-1600, -180); math_sin.operation = 'SINE'
    
    math_pos_x = nodes.new("ShaderNodeMath"); math_pos_x.location = (-1400, -50); math_pos_x.operation = 'MULTIPLY'
    math_pos_y = nodes.new("ShaderNodeMath"); math_pos_y.location = (-1400, -180); math_pos_y.operation = 'MULTIPLY'
    
    vec_pos = nodes.new("ShaderNodeCombineXYZ"); vec_pos.location = (-1200, -100)
    set_point_pos = nodes.new("GeometryNodeSetPosition"); set_point_pos.location = (-1000, -50)

    links.new(gi_dist.outputs["Count"], points.inputs["Count"])
    links.new(gi_dist.outputs["Seed"], rand_angle.inputs["Seed"])
    links.new(gi_dist.outputs["Seed"], seed_off_pos.inputs[0])
    links.new(seed_off_pos.outputs[0], rand_radius.inputs["Seed"])
    
    links.new(rand_radius.outputs["Value"], math_sqrt.inputs[0])
    links.new(math_sqrt.outputs[0], math_mult_rad.inputs[0])
    links.new(gi_dist.outputs["Patch Radius"], math_mult_rad.inputs[1])
    
    links.new(rand_angle.outputs["Value"], math_cos.inputs[0])
    links.new(rand_angle.outputs["Value"], math_sin.inputs[0])
    links.new(math_cos.outputs[0], math_pos_x.inputs[0])
    links.new(math_mult_rad.outputs[0], math_pos_x.inputs[1])
    links.new(math_sin.outputs[0], math_pos_y.inputs[0])
    links.new(math_mult_rad.outputs[0], math_pos_y.inputs[1])
    
    links.new(math_pos_x.outputs[0], vec_pos.inputs[0])
    links.new(math_pos_y.outputs[0], vec_pos.inputs[1])
    links.new(points.outputs["Points"], set_point_pos.inputs["Geometry"])
    links.new(vec_pos.outputs[0], set_point_pos.inputs["Position"])

    seed_off_rot = nodes.new("ShaderNodeMath"); seed_off_rot.location = (-600, -100)
    seed_off_rot.operation = 'ADD'; seed_off_rot.inputs[1].default_value = 99
    
    seed_off_scl = nodes.new("ShaderNodeMath"); seed_off_scl.location = (-600, -250)
    seed_off_scl.operation = 'ADD'; seed_off_scl.inputs[1].default_value = 7
    
    rand_rot_field = nodes.new("FunctionNodeRandomValue"); rand_rot_field.location = (-400, -100)
    rand_rot_field.data_type = 'FLOAT_VECTOR'
    rand_rot_field.inputs["Min"].default_value = (-math.pi, -math.pi, -math.pi)
    rand_rot_field.inputs["Max"].default_value = (math.pi, math.pi, math.pi) 
    
    rand_scale_field = nodes.new("FunctionNodeRandomValue"); rand_scale_field.location = (-400, -300)
    rand_scale_field.data_type = 'FLOAT'
    
    links.new(gi_inst.outputs["Seed"], seed_off_rot.inputs[0])
    links.new(seed_off_rot.outputs[0], rand_rot_field.inputs["Seed"])
    links.new(gi_inst.outputs["Seed"], seed_off_scl.inputs[0])
    links.new(seed_off_scl.outputs[0], rand_scale_field.inputs["Seed"])
    links.new(gi_inst.outputs["Min Scale"], rand_scale_field.inputs["Min"])
    links.new(gi_inst.outputs["Max Scale"], rand_scale_field.inputs["Max"])

    inst_field = nodes.new("GeometryNodeInstanceOnPoints"); inst_field.location = (150, 300)
    index_node = nodes.new("GeometryNodeInputIndex"); index_node.location = (150, 100)
    
    store_fractal = nodes.new("GeometryNodeStoreNamedAttribute"); store_fractal.location = (350, 300)
    store_fractal.data_type = 'INT'; store_fractal.domain = 'INSTANCE'; store_fractal.inputs["Name"].default_value = "fractal_id"
    
    realize_field = nodes.new("GeometryNodeRealizeInstances"); realize_field.location = (550, 300)

    links.new(set_point_pos.outputs["Geometry"], inst_field.inputs["Points"])
    links.new(set_smooth.outputs[0], inst_field.inputs["Instance"])
    
    links.new(rand_rot_field.outputs["Value"], inst_field.inputs["Rotation"])
    links.new(rand_scale_field.outputs["Value"], inst_field.inputs["Scale"])

    links.new(inst_field.outputs["Instances"], store_fractal.inputs["Geometry"])
    links.new(index_node.outputs["Index"], store_fractal.inputs["Value"])
    links.new(store_fractal.outputs[0], realize_field.inputs["Geometry"])
    links.new(realize_field.outputs["Geometry"], group_output.inputs["Geometry"])

    def frame_nodes(node_list, frame_label, color):
        frame = nodes.new("NodeFrame")
        frame.label = frame_label
        frame.use_custom_color = True
        frame.color = color
        for n in node_list: n.parent = frame

    frame_nodes([gi_rock, n_line, n_ico, seed_offset, n_rand_rot, n_rand_scale, n_inst_rock, n_bool], "Boolean Rock Generator", (0.2, 0.3, 0.3))
    frame_nodes([gi_uv, edge_angle, compare_angle, uv_unwrap, store_uv, set_smooth], "Smart UV Project & Attributes", (0.3, 0.3, 0.2))
    frame_nodes([gi_dist, points, seed_off_pos, rand_angle, rand_radius, math_sqrt, math_mult_rad, math_cos, math_sin, math_pos_x, math_pos_y, vec_pos, set_point_pos], "Distribution Logic", (0.3, 0.2, 0.2))
    frame_nodes([gi_inst, seed_off_rot, seed_off_scl, rand_rot_field, rand_scale_field, inst_field, index_node, store_fractal, realize_field], "Instancing", (0.4, 0.2, 0.2))

    return nt