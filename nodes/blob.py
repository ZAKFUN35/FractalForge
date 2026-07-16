import bpy
import mathutils
import os
import typing


def ff_blob_nodes_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize FF Blob Nodes node group"""
    ff_blob_nodes_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="FF Blob Nodes")

    ff_blob_nodes_1.color_tag = 'NONE'
    ff_blob_nodes_1.description = ""
    ff_blob_nodes_1.default_group_node_width = 140
    ff_blob_nodes_1.is_modifier = True
    ff_blob_nodes_1.show_modifier_manage_panel = True

    # ff_blob_nodes_1 interface

    # Socket Geometry
    geometry_socket = ff_blob_nodes_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket Geometry
    geometry_socket_1 = ff_blob_nodes_1.interface.new_socket(name="Geometry", in_out='INPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket ScatterBlobs
    scatterblobs_socket = ff_blob_nodes_1.interface.new_socket(name="ScatterBlobs", in_out='INPUT', socket_type='NodeSocketFloat')
    scatterblobs_socket.default_value = 8.0
    scatterblobs_socket.min_value = -3.4028234663852886e+38
    scatterblobs_socket.max_value = 3.4028234663852886e+38
    scatterblobs_socket.subtype = 'NONE'
    scatterblobs_socket.attribute_domain = 'POINT'
    scatterblobs_socket.default_input = 'VALUE'
    scatterblobs_socket.structure_type = 'AUTO'

    # Panel Scatter Directions Separately
    scatter_directions_separately_panel = ff_blob_nodes_1.interface.new_panel("Scatter Directions Separately")
    # Socket Scatter in X direction
    scatter_in_x_direction_socket = ff_blob_nodes_1.interface.new_socket(name="Scatter in X direction", in_out='INPUT', socket_type='NodeSocketFloat', parent = scatter_directions_separately_panel)
    scatter_in_x_direction_socket.default_value = 1.0
    scatter_in_x_direction_socket.min_value = -3.4028234663852886e+38
    scatter_in_x_direction_socket.max_value = 3.4028234663852886e+38
    scatter_in_x_direction_socket.subtype = 'NONE'
    scatter_in_x_direction_socket.attribute_domain = 'POINT'
    scatter_in_x_direction_socket.default_input = 'VALUE'
    scatter_in_x_direction_socket.structure_type = 'AUTO'

    # Socket Scatter in Y direction
    scatter_in_y_direction_socket = ff_blob_nodes_1.interface.new_socket(name="Scatter in Y direction", in_out='INPUT', socket_type='NodeSocketFloat', parent = scatter_directions_separately_panel)
    scatter_in_y_direction_socket.default_value = 1.0
    scatter_in_y_direction_socket.min_value = -3.4028234663852886e+38
    scatter_in_y_direction_socket.max_value = 3.4028234663852886e+38
    scatter_in_y_direction_socket.subtype = 'NONE'
    scatter_in_y_direction_socket.attribute_domain = 'POINT'
    scatter_in_y_direction_socket.default_input = 'VALUE'
    scatter_in_y_direction_socket.structure_type = 'AUTO'

    # Socket Scatter in Z direction
    scatter_in_z_direction_socket = ff_blob_nodes_1.interface.new_socket(name="Scatter in Z direction", in_out='INPUT', socket_type='NodeSocketFloat', parent = scatter_directions_separately_panel)
    scatter_in_z_direction_socket.default_value = 1.0
    scatter_in_z_direction_socket.min_value = -3.4028234663852886e+38
    scatter_in_z_direction_socket.max_value = 3.4028234663852886e+38
    scatter_in_z_direction_socket.subtype = 'NONE'
    scatter_in_z_direction_socket.attribute_domain = 'POINT'
    scatter_in_z_direction_socket.default_input = 'VALUE'
    scatter_in_z_direction_socket.structure_type = 'AUTO'


    # Panel Blob Randomization
    blob_randomization_panel = ff_blob_nodes_1.interface.new_panel("Blob Randomization")
    # Socket Amount of Blobs
    amount_of_blobs_socket = ff_blob_nodes_1.interface.new_socket(name="Amount of Blobs", in_out='INPUT', socket_type='NodeSocketFloat', parent = blob_randomization_panel)
    amount_of_blobs_socket.default_value = 100.0
    amount_of_blobs_socket.min_value = -3.4028234663852886e+38
    amount_of_blobs_socket.max_value = 3.4028234663852886e+38
    amount_of_blobs_socket.subtype = 'NONE'
    amount_of_blobs_socket.attribute_domain = 'POINT'
    amount_of_blobs_socket.default_input = 'VALUE'
    amount_of_blobs_socket.structure_type = 'AUTO'

    # Socket Blob Radius Min
    blob_radius_min_socket = ff_blob_nodes_1.interface.new_socket(name="Blob Radius Min", in_out='INPUT', socket_type='NodeSocketFloat', parent = blob_randomization_panel)
    blob_radius_min_socket.default_value = 0.20000000298023224
    blob_radius_min_socket.min_value = -3.4028234663852886e+38
    blob_radius_min_socket.max_value = 3.4028234663852886e+38
    blob_radius_min_socket.subtype = 'NONE'
    blob_radius_min_socket.attribute_domain = 'POINT'
    blob_radius_min_socket.default_input = 'VALUE'
    blob_radius_min_socket.structure_type = 'AUTO'

    # Socket Blob Radius Max
    blob_radius_max_socket = ff_blob_nodes_1.interface.new_socket(name="Blob Radius Max", in_out='INPUT', socket_type='NodeSocketFloat', parent = blob_randomization_panel)
    blob_radius_max_socket.default_value = 1.0
    blob_radius_max_socket.min_value = -3.4028234663852886e+38
    blob_radius_max_socket.max_value = 3.4028234663852886e+38
    blob_radius_max_socket.subtype = 'NONE'
    blob_radius_max_socket.attribute_domain = 'POINT'
    blob_radius_max_socket.default_input = 'VALUE'
    blob_radius_max_socket.structure_type = 'AUTO'

    # Socket Randomize Blobs Big Shape
    randomize_blobs_big_shape_socket = ff_blob_nodes_1.interface.new_socket(name="Randomize Blobs Big Shape", in_out='INPUT', socket_type='NodeSocketInt', parent = blob_randomization_panel)
    randomize_blobs_big_shape_socket.default_value = 14
    randomize_blobs_big_shape_socket.min_value = -2147483648
    randomize_blobs_big_shape_socket.max_value = 2147483647
    randomize_blobs_big_shape_socket.subtype = 'NONE'
    randomize_blobs_big_shape_socket.attribute_domain = 'POINT'
    randomize_blobs_big_shape_socket.default_input = 'VALUE'
    randomize_blobs_big_shape_socket.structure_type = 'AUTO'

    # Socket Randomize Blobs Random Seed
    randomize_blobs_random_seed_socket = ff_blob_nodes_1.interface.new_socket(name="Randomize Blobs Random Seed", in_out='INPUT', socket_type='NodeSocketInt', parent = blob_randomization_panel)
    randomize_blobs_random_seed_socket.default_value = 27
    randomize_blobs_random_seed_socket.min_value = -2147483648
    randomize_blobs_random_seed_socket.max_value = 2147483647
    randomize_blobs_random_seed_socket.subtype = 'NONE'
    randomize_blobs_random_seed_socket.attribute_domain = 'POINT'
    randomize_blobs_random_seed_socket.default_input = 'VALUE'
    randomize_blobs_random_seed_socket.structure_type = 'AUTO'

    # Socket Roundness
    roundness_socket = ff_blob_nodes_1.interface.new_socket(name="Roundness", in_out='INPUT', socket_type='NodeSocketInt', parent = blob_randomization_panel)
    roundness_socket.default_value = 0
    roundness_socket.min_value = -2147483648
    roundness_socket.max_value = 2147483647
    roundness_socket.subtype = 'NONE'
    roundness_socket.attribute_domain = 'POINT'
    roundness_socket.default_input = 'VALUE'
    roundness_socket.structure_type = 'AUTO'


    # Panel Details
    details_panel = ff_blob_nodes_1.interface.new_panel("Details")
    # Socket Amount of Details
    amount_of_details_socket = ff_blob_nodes_1.interface.new_socket(name="Amount of Details", in_out='INPUT', socket_type='NodeSocketFloat', parent = details_panel)
    amount_of_details_socket.default_value = 0.05000000074505806
    amount_of_details_socket.min_value = -3.4028234663852886e+38
    amount_of_details_socket.max_value = 3.4028234663852886e+38
    amount_of_details_socket.subtype = 'NONE'
    amount_of_details_socket.attribute_domain = 'POINT'
    amount_of_details_socket.default_input = 'VALUE'
    amount_of_details_socket.structure_type = 'AUTO'

    # Socket Details Coverage
    details_coverage_socket = ff_blob_nodes_1.interface.new_socket(name="Details Coverage", in_out='INPUT', socket_type='NodeSocketFloat', parent = details_panel)
    details_coverage_socket.default_value = 0.15000000596046448
    details_coverage_socket.min_value = -3.4028234663852886e+38
    details_coverage_socket.max_value = 3.4028234663852886e+38
    details_coverage_socket.subtype = 'NONE'
    details_coverage_socket.attribute_domain = 'POINT'
    details_coverage_socket.default_input = 'VALUE'
    details_coverage_socket.structure_type = 'AUTO'

    # Socket Details Randomization
    details_randomization_socket = ff_blob_nodes_1.interface.new_socket(name="Details Randomization", in_out='INPUT', socket_type='NodeSocketInt', parent = details_panel)
    details_randomization_socket.default_value = 50
    details_randomization_socket.min_value = -2147483648
    details_randomization_socket.max_value = 2147483647
    details_randomization_socket.subtype = 'NONE'
    details_randomization_socket.attribute_domain = 'POINT'
    details_randomization_socket.default_input = 'VALUE'
    details_randomization_socket.structure_type = 'AUTO'


    # Initialize ff_blob_nodes_1 nodes

    # Node Group Input
    group_input = ff_blob_nodes_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Mesh to Volume
    mesh_to_volume = ff_blob_nodes_1.nodes.new("GeometryNodeMeshToVolume")
    mesh_to_volume.name = "Mesh to Volume"
    mesh_to_volume.show_options = True
    # Density
    mesh_to_volume.inputs[1].default_value = 1.0
    # Resolution Mode
    mesh_to_volume.inputs[2].default_value = 'Amount'
    # Voxel Size
    mesh_to_volume.inputs[3].default_value = 0.30000001192092896
    # Voxel Amount
    mesh_to_volume.inputs[4].default_value = 64.0
    # Interior Band Width
    mesh_to_volume.inputs[5].default_value = 0.20000000298023224

    # Node Distribute Points in Volume
    distribute_points_in_volume = ff_blob_nodes_1.nodes.new("GeometryNodeDistributePointsInVolume")
    distribute_points_in_volume.name = "Distribute Points in Volume"
    distribute_points_in_volume.show_options = True
    # Mode
    distribute_points_in_volume.inputs[1].default_value = 'Random'
    # Spacing
    distribute_points_in_volume.inputs[4].default_value = (0.30000001192092896, 0.30000001192092896, 0.30000001192092896)
    # Threshold
    distribute_points_in_volume.inputs[5].default_value = 0.10000000149011612

    # Node Points to Volume
    points_to_volume = ff_blob_nodes_1.nodes.new("GeometryNodePointsToVolume")
    points_to_volume.name = "Points to Volume"
    points_to_volume.show_options = True
    # Density
    points_to_volume.inputs[1].default_value = 1.0
    # Resolution Mode
    points_to_volume.inputs[2].default_value = 'Size'
    # Voxel Amount
    points_to_volume.inputs[4].default_value = 64.0

    # Node Volume to Mesh
    volume_to_mesh = ff_blob_nodes_1.nodes.new("GeometryNodeVolumeToMesh")
    volume_to_mesh.name = "Volume to Mesh"
    volume_to_mesh.show_options = True
    # Resolution Mode
    volume_to_mesh.inputs[1].default_value = 'Grid'
    # Voxel Size
    volume_to_mesh.inputs[2].default_value = 0.30000001192092896
    # Voxel Amount
    volume_to_mesh.inputs[3].default_value = 64.0
    # Threshold
    volume_to_mesh.inputs[4].default_value = 0.550000011920929
    # Adaptivity
    volume_to_mesh.inputs[5].default_value = 0.0

    # Node Set Shade Smooth
    set_shade_smooth = ff_blob_nodes_1.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.show_options = True
    set_shade_smooth.domain = 'FACE'
    # Selection
    set_shade_smooth.inputs[1].default_value = True
    # Shade Smooth
    set_shade_smooth.inputs[2].default_value = True

    # Node Set Position
    set_position = ff_blob_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.show_options = True
    # Selection
    set_position.inputs[1].default_value = True
    # Position
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Noise Texture
    noise_texture = ff_blob_nodes_1.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.show_options = True
    noise_texture.show_texture = True
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    # Vector
    noise_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Scale
    noise_texture.inputs[2].default_value = 5.0
    # Detail
    noise_texture.inputs[3].default_value = 2.0
    # Roughness
    noise_texture.inputs[4].default_value = 0.5
    # Lacunarity
    noise_texture.inputs[5].default_value = 2.0
    # Distortion
    noise_texture.inputs[8].default_value = 0.0

    # Node Vector Math
    vector_math = ff_blob_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.show_options = True
    vector_math.operation = 'SUBTRACT'
    # Vector_001
    vector_math.inputs[1].default_value = (0.5, 0.5, 0.5)

    # Node Vector Math.001
    vector_math_001 = ff_blob_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.show_options = True
    vector_math_001.operation = 'SCALE'

    # Node Random Value
    random_value = ff_blob_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value.name = "Random Value"
    random_value.show_options = True
    random_value.data_type = 'FLOAT'
    # ID
    random_value.inputs[2].default_value = 0

    # Node Set Position.001
    set_position_001 = ff_blob_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    set_position_001.show_options = True
    # Position
    set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Noise Texture.001
    noise_texture_001 = ff_blob_nodes_1.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.show_options = True
    noise_texture_001.noise_dimensions = '3D'
    noise_texture_001.noise_type = 'FBM'
    noise_texture_001.normalize = True
    # Vector
    noise_texture_001.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Scale
    noise_texture_001.inputs[2].default_value = 3.0
    # Detail
    noise_texture_001.inputs[3].default_value = 5.0
    # Roughness
    noise_texture_001.inputs[4].default_value = 0.75
    # Lacunarity
    noise_texture_001.inputs[5].default_value = 1.0399999618530273
    # Distortion
    noise_texture_001.inputs[8].default_value = 1.0399999618530273

    # Node Vector Math.002
    vector_math_002 = ff_blob_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.show_options = True
    vector_math_002.operation = 'SUBTRACT'
    # Vector_001
    vector_math_002.inputs[1].default_value = (0.5, 0.5, 0.5)

    # Node Vector Math.003
    vector_math_003 = ff_blob_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.show_options = True
    vector_math_003.operation = 'SCALE'
    # Scale
    vector_math_003.inputs[3].default_value = 1.0

    # Node Random Value.001
    random_value_001 = ff_blob_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value_001.name = "Random Value.001"
    random_value_001.show_options = True
    random_value_001.data_type = 'BOOLEAN'
    # ID
    random_value_001.inputs[1].default_value = 0

    # Node Subdivision Surface
    subdivision_surface = ff_blob_nodes_1.nodes.new("GeometryNodeSubdivisionSurface")
    subdivision_surface.name = "Subdivision Surface"
    subdivision_surface.show_options = True
    # Edge Crease
    subdivision_surface.inputs[2].default_value = 0.0
    # Vertex Crease
    subdivision_surface.inputs[3].default_value = 0.0
    # Limit Surface
    subdivision_surface.inputs[4].default_value = True
    # Quality
    subdivision_surface.inputs[5].default_value = 3
    # UV Smooth
    subdivision_surface.inputs[6].default_value = 'Keep Boundaries'
    # Boundary Smooth
    subdivision_surface.inputs[7].default_value = 'All'

    # Node Group Input.001
    group_input_001 = ff_blob_nodes_1.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.show_options = True

    # Node Math
    math = ff_blob_nodes_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'ADD'
    math.use_clamp = False

    # Node Self Object
    self_object = ff_blob_nodes_1.nodes.new("GeometryNodeSelfObject")
    self_object.name = "Self Object"
    self_object.show_options = True

    # Node Object Info
    object_info = ff_blob_nodes_1.nodes.new("GeometryNodeObjectInfo")
    object_info.name = "Object Info"
    object_info.show_options = True
    object_info.transform_space = 'ORIGINAL'
    # As Instance
    object_info.inputs[1].default_value = False

    # Node Separate XYZ
    separate_xyz = ff_blob_nodes_1.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz.show_options = True

    # Node Math.001
    math_001 = ff_blob_nodes_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.show_options = True
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = True
    # Value_001
    math_001.inputs[1].default_value = 10.0

    # Node Math.002
    math_002 = ff_blob_nodes_1.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.show_options = True
    math_002.operation = 'TRUNC'
    math_002.use_clamp = False

    # Node Combine XYZ
    combine_xyz = ff_blob_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz.show_options = True

    # Node Vector Math.004
    vector_math_004 = ff_blob_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_004.name = "Vector Math.004"
    vector_math_004.show_options = True
    vector_math_004.operation = 'MULTIPLY'

    # Node Group Input.002
    group_input_002 = ff_blob_nodes_1.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.show_options = True

    # Node Group Input.004
    group_input_004 = ff_blob_nodes_1.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.show_options = True

    # Node Group Input.005
    group_input_005 = ff_blob_nodes_1.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.show_options = True

    # Node Frame
    frame = ff_blob_nodes_1.nodes.new("NodeFrame")
    frame.label = "Blob Count Math"
    frame.name = "Frame"
    frame.use_custom_color = True
    frame.color = (0.30000001192092896, 0.20000000298023224, 0.20000000298023224)
    frame.show_options = True
    frame.label_size = 20
    frame.shrink = True

    # Node Frame.001
    frame_001 = ff_blob_nodes_1.nodes.new("NodeFrame")
    frame_001.label = "Details Mask"
    frame_001.name = "Frame.001"
    frame_001.use_custom_color = True
    frame_001.color = (0.30000001192092896, 0.20000000298023224, 0.30000001192092896)
    frame_001.show_options = True
    frame_001.label_size = 20
    frame_001.shrink = True

    # Node Frame.002
    frame_002 = ff_blob_nodes_1.nodes.new("NodeFrame")
    frame_002.label = "Volume Pipeline"
    frame_002.name = "Frame.002"
    frame_002.use_custom_color = True
    frame_002.color = (0.30000001192092896, 0.30000001192092896, 0.20000000298023224)
    frame_002.show_options = True
    frame_002.label_size = 20
    frame_002.shrink = True

    # Node Frame.003
    frame_003 = ff_blob_nodes_1.nodes.new("NodeFrame")
    frame_003.label = "Output Assembly"
    frame_003.name = "Frame.003"
    frame_003.use_custom_color = True
    frame_003.color = (0.4000000059604645, 0.20000000298023224, 0.20000000298023224)
    frame_003.show_options = True
    frame_003.label_size = 20
    frame_003.shrink = True

    # Node Frame.004
    frame_004 = ff_blob_nodes_1.nodes.new("NodeFrame")
    frame_004.label = "Scatter Direction Math"
    frame_004.name = "Frame.004"
    frame_004.use_custom_color = True
    frame_004.color = (0.20000000298023224, 0.30000001192092896, 0.20000000298023224)
    frame_004.show_options = True
    frame_004.label_size = 20
    frame_004.shrink = True

    # Node Frame.005
    frame_005 = ff_blob_nodes_1.nodes.new("NodeFrame")
    frame_005.label = "Radius Settings"
    frame_005.name = "Frame.005"
    frame_005.use_custom_color = True
    frame_005.color = (0.20000000298023224, 0.20000000298023224, 0.30000001192092896)
    frame_005.show_options = True
    frame_005.label_size = 20
    frame_005.shrink = True

    # Node Frame.006
    frame_006 = ff_blob_nodes_1.nodes.new("NodeFrame")
    frame_006.label = "Displacement Math"
    frame_006.name = "Frame.006"
    frame_006.use_custom_color = True
    frame_006.color = (0.20000000298023224, 0.30000001192092896, 0.30000001192092896)
    frame_006.show_options = True
    frame_006.label_size = 20
    frame_006.shrink = True

    # Node Group Input.006
    group_input_006 = ff_blob_nodes_1.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.show_options = True

    # Node Group Output.001
    group_output_001 = ff_blob_nodes_1.nodes.new("NodeGroupOutput")
    group_output_001.name = "Group Output.001"
    group_output_001.show_options = True
    group_output_001.is_active_output = True

    # Set parents
    ff_blob_nodes_1.nodes["Group Input"].parent = ff_blob_nodes_1.nodes["Frame.002"]
    ff_blob_nodes_1.nodes["Mesh to Volume"].parent = ff_blob_nodes_1.nodes["Frame.002"]
    ff_blob_nodes_1.nodes["Distribute Points in Volume"].parent = ff_blob_nodes_1.nodes["Frame.002"]
    ff_blob_nodes_1.nodes["Points to Volume"].parent = ff_blob_nodes_1.nodes["Frame.002"]
    ff_blob_nodes_1.nodes["Volume to Mesh"].parent = ff_blob_nodes_1.nodes["Frame.002"]
    ff_blob_nodes_1.nodes["Set Shade Smooth"].parent = ff_blob_nodes_1.nodes["Frame.003"]
    ff_blob_nodes_1.nodes["Set Position"].parent = ff_blob_nodes_1.nodes["Frame.002"]
    ff_blob_nodes_1.nodes["Noise Texture"].parent = ff_blob_nodes_1.nodes["Frame.004"]
    ff_blob_nodes_1.nodes["Vector Math"].parent = ff_blob_nodes_1.nodes["Frame.004"]
    ff_blob_nodes_1.nodes["Vector Math.001"].parent = ff_blob_nodes_1.nodes["Frame.004"]
    ff_blob_nodes_1.nodes["Random Value"].parent = ff_blob_nodes_1.nodes["Frame.005"]
    ff_blob_nodes_1.nodes["Set Position.001"].parent = ff_blob_nodes_1.nodes["Frame.003"]
    ff_blob_nodes_1.nodes["Noise Texture.001"].parent = ff_blob_nodes_1.nodes["Frame.006"]
    ff_blob_nodes_1.nodes["Vector Math.002"].parent = ff_blob_nodes_1.nodes["Frame.006"]
    ff_blob_nodes_1.nodes["Vector Math.003"].parent = ff_blob_nodes_1.nodes["Frame.006"]
    ff_blob_nodes_1.nodes["Random Value.001"].parent = ff_blob_nodes_1.nodes["Frame.001"]
    ff_blob_nodes_1.nodes["Subdivision Surface"].parent = ff_blob_nodes_1.nodes["Frame.002"]
    ff_blob_nodes_1.nodes["Group Input.001"].parent = ff_blob_nodes_1.nodes["Frame"]
    ff_blob_nodes_1.nodes["Math"].parent = ff_blob_nodes_1.nodes["Frame"]
    ff_blob_nodes_1.nodes["Self Object"].parent = ff_blob_nodes_1.nodes["Frame"]
    ff_blob_nodes_1.nodes["Object Info"].parent = ff_blob_nodes_1.nodes["Frame"]
    ff_blob_nodes_1.nodes["Separate XYZ"].parent = ff_blob_nodes_1.nodes["Frame"]
    ff_blob_nodes_1.nodes["Math.001"].parent = ff_blob_nodes_1.nodes["Frame"]
    ff_blob_nodes_1.nodes["Math.002"].parent = ff_blob_nodes_1.nodes["Frame"]
    ff_blob_nodes_1.nodes["Combine XYZ"].parent = ff_blob_nodes_1.nodes["Frame.004"]
    ff_blob_nodes_1.nodes["Vector Math.004"].parent = ff_blob_nodes_1.nodes["Frame.004"]
    ff_blob_nodes_1.nodes["Group Input.002"].parent = ff_blob_nodes_1.nodes["Frame.004"]
    ff_blob_nodes_1.nodes["Group Input.004"].parent = ff_blob_nodes_1.nodes["Frame.005"]
    ff_blob_nodes_1.nodes["Group Input.005"].parent = ff_blob_nodes_1.nodes["Frame.001"]
    ff_blob_nodes_1.nodes["Group Input.006"].parent = ff_blob_nodes_1.nodes["Frame.002"]

    # Set locations
    ff_blob_nodes_1.nodes["Group Input"].location = (30.07080078125, -132.12115478515625)
    ff_blob_nodes_1.nodes["Mesh to Volume"].location = (361.1396484375, -106.86566162109375)
    ff_blob_nodes_1.nodes["Distribute Points in Volume"].location = (621.3470458984375, -81.5574951171875)
    ff_blob_nodes_1.nodes["Points to Volume"].location = (1061.138916015625, -60.70709228515625)
    ff_blob_nodes_1.nodes["Volume to Mesh"].location = (1249.61279296875, -35.83154296875)
    ff_blob_nodes_1.nodes["Set Shade Smooth"].location = (191.84271240234375, -35.68011474609375)
    ff_blob_nodes_1.nodes["Set Position"].location = (833.7832641601562, -83.7476806640625)
    ff_blob_nodes_1.nodes["Noise Texture"].location = (211.50634765625, -62.915992736816406)
    ff_blob_nodes_1.nodes["Vector Math"].location = (382.7528076171875, -36.355133056640625)
    ff_blob_nodes_1.nodes["Vector Math.001"].location = (718.8397216796875, -166.41293334960938)
    ff_blob_nodes_1.nodes["Random Value"].location = (206.51934814453125, -119.48252868652344)
    ff_blob_nodes_1.nodes["Set Position.001"].location = (30.058975219726562, -61.51336669921875)
    ff_blob_nodes_1.nodes["Noise Texture.001"].location = (30.149505615234375, -111.99394226074219)
    ff_blob_nodes_1.nodes["Vector Math.002"].location = (192.27493286132812, -85.28689575195312)
    ff_blob_nodes_1.nodes["Vector Math.003"].location = (351.5905456542969, -35.621158599853516)
    ff_blob_nodes_1.nodes["Random Value.001"].location = (189.9112548828125, -238.11346435546875)
    ff_blob_nodes_1.nodes["Subdivision Surface"].location = (194.594970703125, -133.13140869140625)
    ff_blob_nodes_1.nodes["Group Input.001"].location = (662.600341796875, -242.4984130859375)
    ff_blob_nodes_1.nodes["Math"].location = (833.400146484375, -36.376953125)
    ff_blob_nodes_1.nodes["Self Object"].location = (29.65576171875, -442.30224609375)
    ff_blob_nodes_1.nodes["Object Info"].location = (181.0257568359375, -304.758056640625)
    ff_blob_nodes_1.nodes["Separate XYZ"].location = (344.4241943359375, -257.84228515625)
    ff_blob_nodes_1.nodes["Math.001"].location = (503.682373046875, -183.328857421875)
    ff_blob_nodes_1.nodes["Math.002"].location = (665.0194091796875, -109.6561279296875)
    ff_blob_nodes_1.nodes["Combine XYZ"].location = (213.5367431640625, -352.702392578125)
    ff_blob_nodes_1.nodes["Vector Math.004"].location = (558.05712890625, -117.42634582519531)
    ff_blob_nodes_1.nodes["Group Input.002"].location = (30.122314453125, -214.75779724121094)
    ff_blob_nodes_1.nodes["Group Input.004"].location = (30.23876953125, -35.7192497253418)
    ff_blob_nodes_1.nodes["Group Input.005"].location = (29.90802001953125, -36.2392578125)
    ff_blob_nodes_1.nodes["Frame"].location = (-2092.0, 1347.0)
    ff_blob_nodes_1.nodes["Frame.001"].location = (-521.0, 1153.0)
    ff_blob_nodes_1.nodes["Frame.002"].location = (-1613.0, 692.0)
    ff_blob_nodes_1.nodes["Frame.003"].location = (-137.0, 715.0)
    ff_blob_nodes_1.nodes["Frame.004"].location = (-1803.0, -23.0)
    ff_blob_nodes_1.nodes["Frame.005"].location = (-866.0, -23.0)
    ff_blob_nodes_1.nodes["Frame.006"].location = (-478.0, -23.0)
    ff_blob_nodes_1.nodes["Group Input.006"].location = (420.21923828125, -276.5929870605469)
    ff_blob_nodes_1.nodes["Group Output.001"].location = (241.00148010253906, 654.13037109375)

    # Set dimensions
    ff_blob_nodes_1.nodes["Group Input"].width  = 140.0
    ff_blob_nodes_1.nodes["Group Input"].height = 100.0

    ff_blob_nodes_1.nodes["Mesh to Volume"].width  = 200.0
    ff_blob_nodes_1.nodes["Mesh to Volume"].height = 100.0

    ff_blob_nodes_1.nodes["Distribute Points in Volume"].width  = 170.0
    ff_blob_nodes_1.nodes["Distribute Points in Volume"].height = 100.0

    ff_blob_nodes_1.nodes["Points to Volume"].width  = 170.0
    ff_blob_nodes_1.nodes["Points to Volume"].height = 100.0

    ff_blob_nodes_1.nodes["Volume to Mesh"].width  = 170.0
    ff_blob_nodes_1.nodes["Volume to Mesh"].height = 100.0

    ff_blob_nodes_1.nodes["Set Shade Smooth"].width  = 140.0
    ff_blob_nodes_1.nodes["Set Shade Smooth"].height = 100.0

    ff_blob_nodes_1.nodes["Set Position"].width  = 140.0
    ff_blob_nodes_1.nodes["Set Position"].height = 100.0

    ff_blob_nodes_1.nodes["Noise Texture"].width  = 145.0
    ff_blob_nodes_1.nodes["Noise Texture"].height = 100.0

    ff_blob_nodes_1.nodes["Vector Math"].width  = 140.0
    ff_blob_nodes_1.nodes["Vector Math"].height = 100.0

    ff_blob_nodes_1.nodes["Vector Math.001"].width  = 140.0
    ff_blob_nodes_1.nodes["Vector Math.001"].height = 100.0

    ff_blob_nodes_1.nodes["Random Value"].width  = 140.0
    ff_blob_nodes_1.nodes["Random Value"].height = 100.0

    ff_blob_nodes_1.nodes["Set Position.001"].width  = 140.0
    ff_blob_nodes_1.nodes["Set Position.001"].height = 100.0

    ff_blob_nodes_1.nodes["Noise Texture.001"].width  = 145.0
    ff_blob_nodes_1.nodes["Noise Texture.001"].height = 100.0

    ff_blob_nodes_1.nodes["Vector Math.002"].width  = 140.0
    ff_blob_nodes_1.nodes["Vector Math.002"].height = 100.0

    ff_blob_nodes_1.nodes["Vector Math.003"].width  = 140.0
    ff_blob_nodes_1.nodes["Vector Math.003"].height = 100.0

    ff_blob_nodes_1.nodes["Random Value.001"].width  = 140.0
    ff_blob_nodes_1.nodes["Random Value.001"].height = 100.0

    ff_blob_nodes_1.nodes["Subdivision Surface"].width  = 150.0
    ff_blob_nodes_1.nodes["Subdivision Surface"].height = 100.0

    ff_blob_nodes_1.nodes["Group Input.001"].width  = 140.0
    ff_blob_nodes_1.nodes["Group Input.001"].height = 100.0

    ff_blob_nodes_1.nodes["Math"].width  = 140.0
    ff_blob_nodes_1.nodes["Math"].height = 100.0

    ff_blob_nodes_1.nodes["Self Object"].width  = 140.0
    ff_blob_nodes_1.nodes["Self Object"].height = 100.0

    ff_blob_nodes_1.nodes["Object Info"].width  = 140.0
    ff_blob_nodes_1.nodes["Object Info"].height = 100.0

    ff_blob_nodes_1.nodes["Separate XYZ"].width  = 140.0
    ff_blob_nodes_1.nodes["Separate XYZ"].height = 100.0

    ff_blob_nodes_1.nodes["Math.001"].width  = 140.0
    ff_blob_nodes_1.nodes["Math.001"].height = 100.0

    ff_blob_nodes_1.nodes["Math.002"].width  = 140.0
    ff_blob_nodes_1.nodes["Math.002"].height = 100.0

    ff_blob_nodes_1.nodes["Combine XYZ"].width  = 140.0
    ff_blob_nodes_1.nodes["Combine XYZ"].height = 100.0

    ff_blob_nodes_1.nodes["Vector Math.004"].width  = 140.0
    ff_blob_nodes_1.nodes["Vector Math.004"].height = 100.0

    ff_blob_nodes_1.nodes["Group Input.002"].width  = 140.0
    ff_blob_nodes_1.nodes["Group Input.002"].height = 100.0

    ff_blob_nodes_1.nodes["Group Input.004"].width  = 140.0
    ff_blob_nodes_1.nodes["Group Input.004"].height = 100.0

    ff_blob_nodes_1.nodes["Group Input.005"].width  = 140.0
    ff_blob_nodes_1.nodes["Group Input.005"].height = 100.0

    ff_blob_nodes_1.nodes["Frame"].width  = 1003.0
    ff_blob_nodes_1.nodes["Frame"].height = 630.0

    ff_blob_nodes_1.nodes["Frame.001"].width  = 360.0
    ff_blob_nodes_1.nodes["Frame.001"].height = 424.0

    ff_blob_nodes_1.nodes["Frame.002"].width  = 1450.0
    ff_blob_nodes_1.nodes["Frame.002"].height = 665.0

    ff_blob_nodes_1.nodes["Frame.003"].width  = 362.0
    ff_blob_nodes_1.nodes["Frame.003"].height = 206.0

    ff_blob_nodes_1.nodes["Frame.004"].width  = 889.0
    ff_blob_nodes_1.nodes["Frame.004"].height = 603.0

    ff_blob_nodes_1.nodes["Frame.005"].width  = 377.0
    ff_blob_nodes_1.nodes["Frame.005"].height = 424.0

    ff_blob_nodes_1.nodes["Frame.006"].width  = 522.0
    ff_blob_nodes_1.nodes["Frame.006"].height = 423.0

    ff_blob_nodes_1.nodes["Group Input.006"].width  = 140.0
    ff_blob_nodes_1.nodes["Group Input.006"].height = 100.0

    ff_blob_nodes_1.nodes["Group Output.001"].width  = 140.0
    ff_blob_nodes_1.nodes["Group Output.001"].height = 100.0


    # Initialize ff_blob_nodes_1 links

    # mesh_to_volume.Volume -> distribute_points_in_volume.Volume
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Mesh to Volume"].outputs[0],
        ff_blob_nodes_1.nodes["Distribute Points in Volume"].inputs[0]
    )
    # points_to_volume.Volume -> volume_to_mesh.Volume
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Points to Volume"].outputs[0],
        ff_blob_nodes_1.nodes["Volume to Mesh"].inputs[0]
    )
    # distribute_points_in_volume.Points -> set_position.Geometry
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Distribute Points in Volume"].outputs[0],
        ff_blob_nodes_1.nodes["Set Position"].inputs[0]
    )
    # vector_math_001.Vector -> set_position.Offset
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Vector Math.001"].outputs[0],
        ff_blob_nodes_1.nodes["Set Position"].inputs[3]
    )
    # noise_texture.Color -> vector_math.Vector
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Noise Texture"].outputs[1],
        ff_blob_nodes_1.nodes["Vector Math"].inputs[0]
    )
    # random_value.Value -> points_to_volume.Radius
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Random Value"].outputs[0],
        ff_blob_nodes_1.nodes["Points to Volume"].inputs[5]
    )
    # volume_to_mesh.Mesh -> set_position_001.Geometry
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Volume to Mesh"].outputs[0],
        ff_blob_nodes_1.nodes["Set Position.001"].inputs[0]
    )
    # set_position_001.Geometry -> set_shade_smooth.Mesh
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Set Position.001"].outputs[0],
        ff_blob_nodes_1.nodes["Set Shade Smooth"].inputs[0]
    )
    # noise_texture_001.Color -> vector_math_002.Vector
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Noise Texture.001"].outputs[1],
        ff_blob_nodes_1.nodes["Vector Math.002"].inputs[0]
    )
    # vector_math_002.Vector -> vector_math_003.Vector
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Vector Math.002"].outputs[0],
        ff_blob_nodes_1.nodes["Vector Math.003"].inputs[0]
    )
    # vector_math_003.Vector -> set_position_001.Offset
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Vector Math.003"].outputs[0],
        ff_blob_nodes_1.nodes["Set Position.001"].inputs[3]
    )
    # random_value_001.Value -> set_position_001.Selection
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Random Value.001"].outputs[0],
        ff_blob_nodes_1.nodes["Set Position.001"].inputs[1]
    )
    # group_input.Geometry -> subdivision_surface.Mesh
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Group Input"].outputs[0],
        ff_blob_nodes_1.nodes["Subdivision Surface"].inputs[0]
    )
    # group_input.Roundness -> subdivision_surface.Level
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Group Input"].outputs[10],
        ff_blob_nodes_1.nodes["Subdivision Surface"].inputs[1]
    )
    # subdivision_surface.Mesh -> mesh_to_volume.Mesh
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Subdivision Surface"].outputs[0],
        ff_blob_nodes_1.nodes["Mesh to Volume"].inputs[0]
    )
    # set_position.Geometry -> points_to_volume.Points
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Set Position"].outputs[0],
        ff_blob_nodes_1.nodes["Points to Volume"].inputs[0]
    )
    # math.Value -> distribute_points_in_volume.Seed
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Math"].outputs[0],
        ff_blob_nodes_1.nodes["Distribute Points in Volume"].inputs[3]
    )
    # self_object.Self Object -> object_info.Object
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Self Object"].outputs[0],
        ff_blob_nodes_1.nodes["Object Info"].inputs[0]
    )
    # group_input_001.Randomize Blobs Big Shape -> math.Value
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Group Input.001"].outputs[8],
        ff_blob_nodes_1.nodes["Math"].inputs[1]
    )
    # object_info.Location -> separate_xyz.Vector
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Object Info"].outputs[1],
        ff_blob_nodes_1.nodes["Separate XYZ"].inputs[0]
    )
    # separate_xyz.X -> math_001.Value
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Separate XYZ"].outputs[0],
        ff_blob_nodes_1.nodes["Math.001"].inputs[0]
    )
    # math_001.Value -> math_002.Value
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Math.001"].outputs[0],
        ff_blob_nodes_1.nodes["Math.002"].inputs[0]
    )
    # math_002.Value -> math.Value
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Math.002"].outputs[0],
        ff_blob_nodes_1.nodes["Math"].inputs[0]
    )
    # vector_math_004.Vector -> vector_math_001.Vector
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Vector Math.004"].outputs[0],
        ff_blob_nodes_1.nodes["Vector Math.001"].inputs[0]
    )
    # vector_math.Vector -> vector_math_004.Vector
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Vector Math"].outputs[0],
        ff_blob_nodes_1.nodes["Vector Math.004"].inputs[0]
    )
    # combine_xyz.Vector -> vector_math_004.Vector
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Combine XYZ"].outputs[0],
        ff_blob_nodes_1.nodes["Vector Math.004"].inputs[1]
    )
    # group_input_002.Scatter in X direction -> combine_xyz.X
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Group Input.002"].outputs[2],
        ff_blob_nodes_1.nodes["Combine XYZ"].inputs[0]
    )
    # group_input_002.Scatter in Y direction -> combine_xyz.Y
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Group Input.002"].outputs[3],
        ff_blob_nodes_1.nodes["Combine XYZ"].inputs[1]
    )
    # group_input_002.Scatter in Z direction -> combine_xyz.Z
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Group Input.002"].outputs[4],
        ff_blob_nodes_1.nodes["Combine XYZ"].inputs[2]
    )
    # group_input_002.ScatterBlobs -> vector_math_001.Scale
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Group Input.002"].outputs[1],
        ff_blob_nodes_1.nodes["Vector Math.001"].inputs[3]
    )
    # group_input_004.Amount of Details -> points_to_volume.Voxel Size
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Group Input.004"].outputs[11],
        ff_blob_nodes_1.nodes["Points to Volume"].inputs[3]
    )
    # group_input_004.Blob Radius Min -> random_value.Min
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Group Input.004"].outputs[6],
        ff_blob_nodes_1.nodes["Random Value"].inputs[0]
    )
    # group_input_004.Blob Radius Max -> random_value.Max
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Group Input.004"].outputs[7],
        ff_blob_nodes_1.nodes["Random Value"].inputs[1]
    )
    # group_input_004.Randomize Blobs Random Seed -> random_value.Seed
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Group Input.004"].outputs[9],
        ff_blob_nodes_1.nodes["Random Value"].inputs[3]
    )
    # group_input_005.Details Coverage -> random_value_001.Probability
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Group Input.005"].outputs[12],
        ff_blob_nodes_1.nodes["Random Value.001"].inputs[0]
    )
    # group_input_005.Details Randomization -> random_value_001.Seed
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Group Input.005"].outputs[13],
        ff_blob_nodes_1.nodes["Random Value.001"].inputs[2]
    )
    # group_input_006.Amount of Blobs -> distribute_points_in_volume.Density
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Group Input.006"].outputs[5],
        ff_blob_nodes_1.nodes["Distribute Points in Volume"].inputs[2]
    )
    # set_shade_smooth.Mesh -> group_output_001.Geometry
    ff_blob_nodes_1.links.new(
        ff_blob_nodes_1.nodes["Set Shade Smooth"].outputs[0],
        ff_blob_nodes_1.nodes["Group Output.001"].inputs[0]
    )

    return ff_blob_nodes_1


if __name__ == "__main__":
    # Maps node tree creation functions to the node tree 
    # name, such that we don't recreate node trees unnecessarily
    node_tree_names : dict[typing.Callable, str] = {}

    ff_blob_nodes = ff_blob_nodes_1_node_group(node_tree_names)
    node_tree_names[ff_blob_nodes_1_node_group] = ff_blob_nodes.name


# ============================================================================
#  FF BRIDGE
# ============================================================================

from . import bridge

GROUP_NAME = "FF Blob Nodes"

# blob не спавнит пустышку - модификатор вешается на уже выделенный mesh-объект
# Материал не генерируется...
REQUIRES_OBJECT = True


def create_node_group():
    return bridge.get_or_create_node_group(ff_blob_nodes_1_node_group, GROUP_NAME)