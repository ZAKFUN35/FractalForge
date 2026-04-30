import bpy

def get_or_create_material():
    mat_name = "M_Blob"
    if mat_name in bpy.data.materials:
        return bpy.data.materials[mat_name]

    m_blob = bpy.data.materials.new(name=mat_name)
    m_blob.use_nodes = True
    m_blob.blend_method = 'HASHED'
    m_blob.show_transparent_back = True
    m_blob.use_backface_culling_lightprobe_volume = True

    shader_nodetree = m_blob.node_tree
    for node in shader_nodetree.nodes:
        shader_nodetree.nodes.remove(node)

    material_output = shader_nodetree.nodes.new("ShaderNodeOutputMaterial")
    material_output.location = (331, 288)

    color_ramp = shader_nodetree.nodes.new("ShaderNodeValToRGB")
    color_ramp.color_ramp.interpolation = 'CONSTANT'
    color_ramp.color_ramp.elements.remove(color_ramp.color_ramp.elements[0])
    cr_0 = color_ramp.color_ramp.elements[0]
    cr_0.position, cr_0.color = 0.0, (0.0395, 0.0998, 0.0722, 1.0)
    cr_1 = color_ramp.color_ramp.elements.new(0.082)
    cr_1.color = (0.0703, 0.2663, 0.1094, 1.0)
    cr_2 = color_ramp.color_ramp.elements.new(0.198)
    cr_2.color = (0.1559, 0.5775, 0.1980, 1.0)
    cr_3 = color_ramp.color_ramp.elements.new(0.263)
    cr_3.color = (0.3467, 0.8148, 0.1589, 1.0)
    color_ramp.location = (-197, 271)

    shader_to_rgb = shader_nodetree.nodes.new("ShaderNodeShaderToRGB")
    shader_to_rgb.location = (-550, -107)

    diffuse_bsdf = shader_nodetree.nodes.new("ShaderNodeBsdfDiffuse")
    diffuse_bsdf.inputs[0].default_value = (0.8, 0.8, 0.8, 1.0)
    diffuse_bsdf.location = (-751, -179)

    texture_coordinate = shader_nodetree.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.location = (-743, 63)

    separate_xyz = shader_nodetree.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.location = (-586, 114)

    mix = shader_nodetree.nodes.new("ShaderNodeMix")
    mix.blend_type = 'MULTIPLY'
    mix.clamp_factor = True
    mix.data_type = 'RGBA'
    mix.inputs[0].default_value = 0.192
    mix.location = (-376, 114)

    hue_saturation_value = shader_nodetree.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value.location = (136, 375)

    object_info = shader_nodetree.nodes.new("ShaderNodeObjectInfo")
    object_info.location = (-421, 510)

    color_ramp_001 = shader_nodetree.nodes.new("ShaderNodeValToRGB")
    color_ramp_001.color_ramp.elements.remove(color_ramp_001.color_ramp.elements[0])
    cr_001_0 = color_ramp_001.color_ramp.elements[0]
    cr_001_0.position, cr_001_0.color = 0.0, (0.467, 0.467, 0.467, 1.0)
    cr_001_1 = color_ramp_001.color_ramp.elements.new(1.0)
    cr_001_1.color = (0.527, 0.527, 0.527, 1.0)
    color_ramp_001.location = (-197, 710)

    color_ramp_002 = shader_nodetree.nodes.new("ShaderNodeValToRGB")
    color_ramp_002.color_ramp.elements.remove(color_ramp_002.color_ramp.elements[0])
    cr_002_0 = color_ramp_002.color_ramp.elements[0]
    cr_002_0.position, cr_002_0.color = 0.0, (1.0, 1.0, 1.0, 1.0)
    cr_002_1 = color_ramp_002.color_ramp.elements.new(1.0)
    cr_002_1.color = (1.1, 1.1, 1.1, 1.0)
    color_ramp_002.location = (-200, 490)

    sl = shader_nodetree.links.new
    sl(hue_saturation_value.outputs[0], material_output.inputs[0])
    sl(diffuse_bsdf.outputs[0], shader_to_rgb.inputs[0])
    sl(texture_coordinate.outputs[1], separate_xyz.inputs[0])
    sl(separate_xyz.outputs[2], mix.inputs[7]) 
    sl(shader_to_rgb.outputs[0], mix.inputs[6]) 
    sl(mix.outputs[2], color_ramp.inputs[0])
    sl(color_ramp.outputs[0], hue_saturation_value.inputs[4])
    sl(object_info.outputs[5], color_ramp_001.inputs[0])
    sl(object_info.outputs[5], color_ramp_002.inputs[0])
    sl(color_ramp_002.outputs[0], hue_saturation_value.inputs[1])
    sl(color_ramp_001.outputs[0], hue_saturation_value.inputs[0])

    return m_blob

def create_node_group():
    group_name = "FF Blob Nodes"
    
    if group_name in bpy.data.node_groups:
        return bpy.data.node_groups[group_name]

    ff_blob_nodes_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name=group_name)
    ff_blob_nodes_1.color_tag = 'NONE'
    
    if hasattr(ff_blob_nodes_1, "interface"):
        geometry_socket = ff_blob_nodes_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
        geometry_socket.attribute_domain = 'POINT'
        geometry_socket.default_input = 'VALUE'
        geometry_socket.structure_type = 'AUTO'

        geometry_socket_1 = ff_blob_nodes_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
        geometry_socket_1.attribute_domain = 'POINT'
        geometry_socket_1.default_input = 'VALUE'
        geometry_socket_1.structure_type = 'AUTO'

        scatterblobs_socket = ff_blob_nodes_1.interface.new_socket(name="ScatterBlobs", in_out='INPUT', socket_type='NodeSocketFloat')
        scatterblobs_socket.default_value = 8.0
        scatterblobs_socket.subtype = 'NONE'

        scatter_directions_separately_panel = ff_blob_nodes_1.interface.new_panel("Scatter Directions Separately")
        scatter_in_x_direction_socket = ff_blob_nodes_1.interface.new_socket(name="Scatter in X direction", in_out='INPUT', socket_type='NodeSocketFloat', parent=scatter_directions_separately_panel)
        scatter_in_x_direction_socket.default_value = 1.0

        scatter_in_y_direction_socket = ff_blob_nodes_1.interface.new_socket(name="Scatter in Y direction", in_out='INPUT', socket_type='NodeSocketFloat', parent=scatter_directions_separately_panel)
        scatter_in_y_direction_socket.default_value = 1.0

        scatter_in_z_direction_socket = ff_blob_nodes_1.interface.new_socket(name="Scatter in Z direction", in_out='INPUT', socket_type='NodeSocketFloat', parent=scatter_directions_separately_panel)
        scatter_in_z_direction_socket.default_value = 1.0

        blob_randomization_panel = ff_blob_nodes_1.interface.new_panel("Blob Randomization")
        amount_of_blobs_socket = ff_blob_nodes_1.interface.new_socket(name="Amount of Blobs", in_out='INPUT', socket_type='NodeSocketFloat', parent=blob_randomization_panel)
        amount_of_blobs_socket.default_value = 100.0
        amount_of_blobs_socket.min_value = 0.0
        amount_of_blobs_socket.max_value = 50000.0

        blob_radius_min_socket = ff_blob_nodes_1.interface.new_socket(name="Blob Radius Min", in_out='INPUT', socket_type='NodeSocketFloat', parent=blob_randomization_panel)
        blob_radius_min_socket.default_value = 0.2
        blob_radius_min_socket.min_value = 0.0

        blob_radius_max_socket = ff_blob_nodes_1.interface.new_socket(name="Blob Radius Max", in_out='INPUT', socket_type='NodeSocketFloat', parent=blob_randomization_panel)
        blob_radius_max_socket.default_value = 1.0
        blob_radius_max_socket.min_value = 0.0

        randomize_blobs_big_shape_socket = ff_blob_nodes_1.interface.new_socket(name="Randomize Blobs Big Shape", in_out='INPUT', socket_type='NodeSocketInt', parent=blob_randomization_panel)
        randomize_blobs_big_shape_socket.default_value = 14

        randomize_blobs_random_seed_socket = ff_blob_nodes_1.interface.new_socket(name="Randomize Blobs Random Seed", in_out='INPUT', socket_type='NodeSocketInt', parent=blob_randomization_panel)
        randomize_blobs_random_seed_socket.default_value = 27

        roundness_socket = ff_blob_nodes_1.interface.new_socket(name="Roundness", in_out='INPUT', socket_type='NodeSocketInt', parent=blob_randomization_panel)
        roundness_socket.default_value = 0
        roundness_socket.min_value = 0
        roundness_socket.max_value = 6

        details_panel = ff_blob_nodes_1.interface.new_panel("Details")
        amount_of_details_socket = ff_blob_nodes_1.interface.new_socket(name="Amount of Details", in_out='INPUT', socket_type='NodeSocketFloat', parent=details_panel)
        amount_of_details_socket.default_value = 0.05
        amount_of_details_socket.min_value = 0.0

        details_coverage_socket = ff_blob_nodes_1.interface.new_socket(name="Details Coverage", in_out='INPUT', socket_type='NodeSocketFloat', parent=details_panel)
        details_coverage_socket.default_value = 0.15
        details_coverage_socket.min_value = 0.0
        details_coverage_socket.max_value = 1.0

        details_randomization_socket = ff_blob_nodes_1.interface.new_socket(name="Details Randomization", in_out='INPUT', socket_type='NodeSocketInt', parent=details_panel)
        details_randomization_socket.default_value = 50

        material_socket = ff_blob_nodes_1.interface.new_socket(name="Material", in_out='INPUT', socket_type='NodeSocketMaterial', parent=details_panel)

    group_input = ff_blob_nodes_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    group_output = ff_blob_nodes_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    mesh_to_volume = ff_blob_nodes_1.nodes.new("GeometryNodeMeshToVolume")
    mesh_to_volume.name = "Mesh to Volume"
    mesh_to_volume.resolution_mode = 'VOXEL_AMOUNT'
    mesh_to_volume.inputs[1].default_value = 1.0
    mesh_to_volume.inputs[3].default_value = 64.0
    mesh_to_volume.inputs[4].default_value = 0.2

    distribute_points_in_volume = ff_blob_nodes_1.nodes.new("GeometryNodeDistributePointsInVolume")
    distribute_points_in_volume.name = "Distribute Points in Volume"
    distribute_points_in_volume.mode = 'DENSITY_RANDOM'

    points_to_volume = ff_blob_nodes_1.nodes.new("GeometryNodePointsToVolume")
    points_to_volume.name = "Points to Volume"
    points_to_volume.resolution_mode = 'VOXEL_SIZE'
    points_to_volume.inputs[1].default_value = 1.0

    volume_to_mesh = ff_blob_nodes_1.nodes.new("GeometryNodeVolumeToMesh")
    volume_to_mesh.name = "Volume to Mesh"
    volume_to_mesh.resolution_mode = 'GRID'
    volume_to_mesh.inputs[3].default_value = 0.55
    volume_to_mesh.inputs[4].default_value = 0.0

    set_shade_smooth = ff_blob_nodes_1.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = 'FACE'
    set_shade_smooth.inputs[1].default_value = True
    set_shade_smooth.inputs[2].default_value = True

    set_material = ff_blob_nodes_1.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.inputs[1].default_value = True

    set_position = ff_blob_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.inputs[1].default_value = True
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)

    noise_texture = ff_blob_nodes_1.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    noise_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
    noise_texture.inputs[2].default_value = 5.0
    noise_texture.inputs[3].default_value = 2.0
    noise_texture.inputs[4].default_value = 0.5
    noise_texture.inputs[5].default_value = 2.0
    noise_texture.inputs[8].default_value = 0.0

    vector_math = ff_blob_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'SUBTRACT'
    vector_math.inputs[1].default_value = (0.5, 0.5, 0.5)

    vector_math_001 = ff_blob_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'SCALE'

    random_value = ff_blob_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value.name = "Random Value"
    random_value.data_type = 'FLOAT'
    random_value.inputs[7].default_value = 0

    set_position_001 = ff_blob_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)

    noise_texture_001 = ff_blob_nodes_1.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = '3D'
    noise_texture_001.noise_type = 'FBM'
    noise_texture_001.normalize = True
    noise_texture_001.inputs[0].default_value = (0.0, 0.0, 0.0)
    noise_texture_001.inputs[2].default_value = 3.0
    noise_texture_001.inputs[3].default_value = 5.0
    noise_texture_001.inputs[4].default_value = 0.75
    noise_texture_001.inputs[5].default_value = 2.0
    noise_texture_001.inputs[8].default_value = 1.0399999618530273

    vector_math_002 = ff_blob_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = 'SUBTRACT'
    vector_math_002.inputs[1].default_value = (0.5, 0.5, 0.5)

    vector_math_003 = ff_blob_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.operation = 'SCALE'
    vector_math_003.inputs[3].default_value = 1.0

    random_value_001 = ff_blob_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value_001.name = "Random Value.001"
    random_value_001.data_type = 'BOOLEAN'
    random_value_001.inputs[7].default_value = 0

    subdivision_surface = ff_blob_nodes_1.nodes.new("GeometryNodeSubdivisionSurface")
    subdivision_surface.name = "Subdivision Surface"
    subdivision_surface.boundary_smooth = 'ALL'
    subdivision_surface.uv_smooth = 'PRESERVE_BOUNDARIES'
    subdivision_surface.inputs[2].default_value = 0.0
    subdivision_surface.inputs[3].default_value = 0.0
    subdivision_surface.inputs[4].default_value = True

    group_input_001 = ff_blob_nodes_1.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"

    math = ff_blob_nodes_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'ADD'
    math.use_clamp = False

    self_object = ff_blob_nodes_1.nodes.new("GeometryNodeSelfObject")
    self_object.name = "Self Object"

    object_info = ff_blob_nodes_1.nodes.new("GeometryNodeObjectInfo")
    object_info.name = "Object Info"
    object_info.transform_space = 'ORIGINAL'
    object_info.inputs[1].default_value = False

    separate_xyz = ff_blob_nodes_1.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"

    math_001 = ff_blob_nodes_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = True
    math_001.inputs[1].default_value = 10.0

    math_002 = ff_blob_nodes_1.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'TRUNC'
    math_002.use_clamp = False

    combine_xyz = ff_blob_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"

    vector_math_004 = ff_blob_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_004.name = "Vector Math.004"
    vector_math_004.operation = 'MULTIPLY'

    group_input_002 = ff_blob_nodes_1.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"

    group_input_003 = ff_blob_nodes_1.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"

    group_input_004 = ff_blob_nodes_1.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"

    group_input_005 = ff_blob_nodes_1.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"

    def arrange_and_frame(node_list, frame_label, start_x, start_y, color, cols=7):
        frame = ff_blob_nodes_1.nodes.new("NodeFrame")
        frame.label = frame_label
        frame.use_custom_color = True
        frame.color = color
        for i, n in enumerate(node_list):
            n.location = (start_x + (i % cols) * 260, start_y - (i // cols) * 300)
            n.parent = frame

    arrange_and_frame([group_input_001, self_object, object_info, separate_xyz, math_001, math_002, math], "Blob Count Math", -1800, 1400, (0.3, 0.2, 0.2))
    arrange_and_frame([group_input_005, random_value_001], "Details Mask", 1000, 1400, (0.3, 0.2, 0.3))
    
    arrange_and_frame([group_input, subdivision_surface, mesh_to_volume, distribute_points_in_volume, set_position, points_to_volume, volume_to_mesh], "Volume Pipeline", -1800, 600, (0.3, 0.3, 0.2))
    arrange_and_frame([set_position_001, set_shade_smooth, group_input_003, set_material, group_output], "Output Assembly", 1000, 600, (0.4, 0.2, 0.2))
    
    arrange_and_frame([group_input_002, noise_texture, vector_math, combine_xyz, vector_math_004, vector_math_001], "Scatter Direction Math", -1800, -300, (0.2, 0.3, 0.2))
    arrange_and_frame([group_input_004, random_value], "Radius Settings", 200, -300, (0.2, 0.2, 0.3))
    arrange_and_frame([noise_texture_001, vector_math_002, vector_math_003], "Displacement Math", 1000, -300, (0.2, 0.3, 0.3))

    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Mesh to Volume"].outputs[0], ff_blob_nodes_1.nodes["Distribute Points in Volume"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Points to Volume"].outputs[0], ff_blob_nodes_1.nodes["Volume to Mesh"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Set Shade Smooth"].outputs[0], ff_blob_nodes_1.nodes["Set Material"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Distribute Points in Volume"].outputs[0], ff_blob_nodes_1.nodes["Set Position"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Vector Math.001"].outputs[0], ff_blob_nodes_1.nodes["Set Position"].inputs[3])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Noise Texture"].outputs[1], ff_blob_nodes_1.nodes["Vector Math"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Random Value"].outputs[1], ff_blob_nodes_1.nodes["Points to Volume"].inputs[4])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Volume to Mesh"].outputs[0], ff_blob_nodes_1.nodes["Set Position.001"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Set Position.001"].outputs[0], ff_blob_nodes_1.nodes["Set Shade Smooth"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Noise Texture.001"].outputs[1], ff_blob_nodes_1.nodes["Vector Math.002"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Vector Math.002"].outputs[0], ff_blob_nodes_1.nodes["Vector Math.003"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Vector Math.003"].outputs[0], ff_blob_nodes_1.nodes["Set Position.001"].inputs[3])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Random Value.001"].outputs[3], ff_blob_nodes_1.nodes["Set Position.001"].inputs[1])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Set Material"].outputs[0], ff_blob_nodes_1.nodes["Group Output"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Group Input"].outputs[0], ff_blob_nodes_1.nodes["Subdivision Surface"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Group Input"].outputs[10], ff_blob_nodes_1.nodes["Subdivision Surface"].inputs[1])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Subdivision Surface"].outputs[0], ff_blob_nodes_1.nodes["Mesh to Volume"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Set Position"].outputs[0], ff_blob_nodes_1.nodes["Points to Volume"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Group Input.001"].outputs[5], ff_blob_nodes_1.nodes["Distribute Points in Volume"].inputs[1])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Math"].outputs[0], ff_blob_nodes_1.nodes["Distribute Points in Volume"].inputs[2])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Self Object"].outputs[0], ff_blob_nodes_1.nodes["Object Info"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Group Input.001"].outputs[8], ff_blob_nodes_1.nodes["Math"].inputs[1])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Object Info"].outputs[1], ff_blob_nodes_1.nodes["Separate XYZ"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Separate XYZ"].outputs[0], ff_blob_nodes_1.nodes["Math.001"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Math.001"].outputs[0], ff_blob_nodes_1.nodes["Math.002"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Math.002"].outputs[0], ff_blob_nodes_1.nodes["Math"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Vector Math.004"].outputs[0], ff_blob_nodes_1.nodes["Vector Math.001"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Vector Math"].outputs[0], ff_blob_nodes_1.nodes["Vector Math.004"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Combine XYZ"].outputs[0], ff_blob_nodes_1.nodes["Vector Math.004"].inputs[1])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Group Input.002"].outputs[2], ff_blob_nodes_1.nodes["Combine XYZ"].inputs[0])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Group Input.002"].outputs[3], ff_blob_nodes_1.nodes["Combine XYZ"].inputs[1])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Group Input.002"].outputs[4], ff_blob_nodes_1.nodes["Combine XYZ"].inputs[2])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Group Input.002"].outputs[1], ff_blob_nodes_1.nodes["Vector Math.001"].inputs[3])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Group Input.003"].outputs[14], ff_blob_nodes_1.nodes["Set Material"].inputs[2])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Group Input.004"].outputs[11], ff_blob_nodes_1.nodes["Points to Volume"].inputs[2])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Group Input.004"].outputs[6], ff_blob_nodes_1.nodes["Random Value"].inputs[2])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Group Input.004"].outputs[7], ff_blob_nodes_1.nodes["Random Value"].inputs[3])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Group Input.004"].outputs[9], ff_blob_nodes_1.nodes["Random Value"].inputs[8])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Group Input.005"].outputs[12], ff_blob_nodes_1.nodes["Random Value.001"].inputs[6])
    ff_blob_nodes_1.links.new(ff_blob_nodes_1.nodes["Group Input.005"].outputs[13], ff_blob_nodes_1.nodes["Random Value.001"].inputs[8])

    return ff_blob_nodes_1