import bpy
import mathutils
import os
import typing


def ff_macadam_nodes_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize FF Macadam Nodes node group"""
    ff_macadam_nodes_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="FF Macadam Nodes")

    ff_macadam_nodes_1.color_tag = 'GEOMETRY'
    ff_macadam_nodes_1.description = ""
    ff_macadam_nodes_1.default_group_node_width = 140
    ff_macadam_nodes_1.is_modifier = True
    ff_macadam_nodes_1.show_modifier_manage_panel = True

    # ff_macadam_nodes_1 interface

    # Socket Geometry
    geometry_socket = ff_macadam_nodes_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Panel Placement
    placement_panel = ff_macadam_nodes_1.interface.new_panel("Placement")
    # Socket Seed
    seed_socket = ff_macadam_nodes_1.interface.new_socket(name="Seed", in_out='INPUT', socket_type='NodeSocketInt', parent = placement_panel)
    seed_socket.default_value = 0
    seed_socket.min_value = -2147483648
    seed_socket.max_value = 2147483647
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'

    # Socket Count
    count_socket = ff_macadam_nodes_1.interface.new_socket(name="Count", in_out='INPUT', socket_type='NodeSocketInt', parent = placement_panel)
    count_socket.default_value = 15
    count_socket.min_value = -2147483648
    count_socket.max_value = 2147483647
    count_socket.subtype = 'NONE'
    count_socket.attribute_domain = 'POINT'
    count_socket.default_input = 'VALUE'
    count_socket.structure_type = 'AUTO'

    # Socket Patch Radius
    patch_radius_socket = ff_macadam_nodes_1.interface.new_socket(name="Patch Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent = placement_panel)
    patch_radius_socket.default_value = 0.75
    patch_radius_socket.min_value = -3.4028234663852886e+38
    patch_radius_socket.max_value = 3.4028234663852886e+38
    patch_radius_socket.subtype = 'NONE'
    patch_radius_socket.attribute_domain = 'POINT'
    patch_radius_socket.default_input = 'VALUE'
    patch_radius_socket.structure_type = 'AUTO'

    # Socket Min Scale
    min_scale_socket = ff_macadam_nodes_1.interface.new_socket(name="Min Scale", in_out='INPUT', socket_type='NodeSocketFloat', parent = placement_panel)
    min_scale_socket.default_value = 0.029999999329447746
    min_scale_socket.min_value = -3.4028234663852886e+38
    min_scale_socket.max_value = 3.4028234663852886e+38
    min_scale_socket.subtype = 'NONE'
    min_scale_socket.attribute_domain = 'POINT'
    min_scale_socket.default_input = 'VALUE'
    min_scale_socket.structure_type = 'AUTO'

    # Socket Max Scale
    max_scale_socket = ff_macadam_nodes_1.interface.new_socket(name="Max Scale", in_out='INPUT', socket_type='NodeSocketFloat', parent = placement_panel)
    max_scale_socket.default_value = 0.11999999731779099
    max_scale_socket.min_value = -3.4028234663852886e+38
    max_scale_socket.max_value = 3.4028234663852886e+38
    max_scale_socket.subtype = 'NONE'
    max_scale_socket.attribute_domain = 'POINT'
    max_scale_socket.default_input = 'VALUE'
    max_scale_socket.structure_type = 'AUTO'


    # Panel Rock Shape
    rock_shape_panel = ff_macadam_nodes_1.interface.new_panel("Rock Shape")
    # Socket Shape Seed
    shape_seed_socket = ff_macadam_nodes_1.interface.new_socket(name="Shape Seed", in_out='INPUT', socket_type='NodeSocketInt', parent = rock_shape_panel)
    shape_seed_socket.default_value = 2
    shape_seed_socket.min_value = -2147483648
    shape_seed_socket.max_value = 2147483647
    shape_seed_socket.subtype = 'NONE'
    shape_seed_socket.attribute_domain = 'POINT'
    shape_seed_socket.force_non_field = True
    shape_seed_socket.default_input = 'VALUE'
    shape_seed_socket.structure_type = 'SINGLE'

    # Socket Detail
    detail_socket = ff_macadam_nodes_1.interface.new_socket(name="Detail", in_out='INPUT', socket_type='NodeSocketInt', parent = rock_shape_panel)
    detail_socket.default_value = 1
    detail_socket.min_value = -2147483648
    detail_socket.max_value = 2147483647
    detail_socket.subtype = 'NONE'
    detail_socket.attribute_domain = 'POINT'
    detail_socket.force_non_field = True
    detail_socket.default_input = 'VALUE'
    detail_socket.structure_type = 'SINGLE'

    # Socket Base Radius
    base_radius_socket = ff_macadam_nodes_1.interface.new_socket(name="Base Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent = rock_shape_panel)
    base_radius_socket.default_value = 2.869999885559082
    base_radius_socket.min_value = -3.4028234663852886e+38
    base_radius_socket.max_value = 3.4028234663852886e+38
    base_radius_socket.subtype = 'NONE'
    base_radius_socket.attribute_domain = 'POINT'
    base_radius_socket.force_non_field = True
    base_radius_socket.default_input = 'VALUE'
    base_radius_socket.structure_type = 'SINGLE'

    # Socket Roundness
    roundness_socket = ff_macadam_nodes_1.interface.new_socket(name="Roundness", in_out='INPUT', socket_type='NodeSocketVector', parent = rock_shape_panel)
    roundness_socket.default_value = (0.7200000286102295, 0.05000000074505806, 0.14000000059604645)
    roundness_socket.min_value = -3.4028234663852886e+38
    roundness_socket.max_value = 3.4028234663852886e+38
    roundness_socket.subtype = 'NONE'
    roundness_socket.attribute_domain = 'POINT'
    roundness_socket.force_non_field = True
    roundness_socket.default_input = 'VALUE'
    roundness_socket.structure_type = 'SINGLE'


    # Panel Detail
    detail_panel = ff_macadam_nodes_1.interface.new_panel("Detail")
    # Socket Material
    material_socket = ff_macadam_nodes_1.interface.new_socket(name="Material", in_out='INPUT', socket_type='NodeSocketMaterial', parent = detail_panel)
    material_socket.attribute_domain = 'POINT'
    material_socket.default_input = 'VALUE'
    material_socket.structure_type = 'AUTO'
    material_socket.optional_label = True

    # Socket Smooth Shading
    smooth_shading_socket = ff_macadam_nodes_1.interface.new_socket(name="Smooth Shading", in_out='INPUT', socket_type='NodeSocketBool', parent = detail_panel)
    smooth_shading_socket.default_value = False
    smooth_shading_socket.attribute_domain = 'POINT'
    smooth_shading_socket.default_input = 'VALUE'
    smooth_shading_socket.structure_type = 'AUTO'

    # Socket Stylized Normals
    stylized_normals_socket = ff_macadam_nodes_1.interface.new_socket(name="Stylized Normals", in_out='INPUT', socket_type='NodeSocketFloat', parent = detail_panel)
    stylized_normals_socket.default_value = 0.0
    stylized_normals_socket.min_value = 0.0
    stylized_normals_socket.max_value = 1.0
    stylized_normals_socket.subtype = 'NONE'
    stylized_normals_socket.attribute_domain = 'POINT'
    stylized_normals_socket.default_input = 'VALUE'
    stylized_normals_socket.structure_type = 'AUTO'

    # Socket Rocks Color
    rocks_color_socket = ff_macadam_nodes_1.interface.new_socket(name="Rocks Color", in_out='INPUT', socket_type='NodeSocketColor', parent = detail_panel)
    rocks_color_socket.default_value = (0.0, 1.0, 0.0, 1.0)
    rocks_color_socket.attribute_domain = 'POINT'
    rocks_color_socket.default_input = 'VALUE'
    rocks_color_socket.structure_type = 'AUTO'


    # Initialize ff_macadam_nodes_1 nodes

    # Node Group Input
    group_input = ff_macadam_nodes_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Input.001
    group_input_001 = ff_macadam_nodes_1.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.show_options = True

    # Node Group Input.002
    group_input_002 = ff_macadam_nodes_1.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.show_options = True

    # Node Group Input.003
    group_input_003 = ff_macadam_nodes_1.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.show_options = True

    # Node Group Output
    group_output = ff_macadam_nodes_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Mesh Line
    mesh_line = ff_macadam_nodes_1.nodes.new("GeometryNodeMeshLine")
    mesh_line.name = "Mesh Line"
    mesh_line.show_options = True
    mesh_line.count_mode = 'TOTAL'
    mesh_line.mode = 'OFFSET'
    # Start Location
    mesh_line.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Offset
    mesh_line.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Ico Sphere
    ico_sphere = ff_macadam_nodes_1.nodes.new("GeometryNodeMeshIcoSphere")
    ico_sphere.name = "Ico Sphere"
    ico_sphere.show_options = True
    # Subdivisions
    ico_sphere.inputs[1].default_value = 1

    # Node Math
    math = ff_macadam_nodes_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'ADD'
    math.use_clamp = False
    # Value_001
    math.inputs[1].default_value = 1.0

    # Node Random Value
    random_value = ff_macadam_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value.name = "Random Value"
    random_value.show_options = True
    random_value.data_type = 'FLOAT_VECTOR'
    # Min
    random_value.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Max
    random_value.inputs[1].default_value = (6.2831854820251465, 6.2831854820251465, 6.2831854820251465)
    # ID
    random_value.inputs[2].default_value = 0

    # Node Random Value.001
    random_value_001 = ff_macadam_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value_001.name = "Random Value.001"
    random_value_001.show_options = True
    random_value_001.data_type = 'FLOAT_VECTOR'
    # Max
    random_value_001.inputs[1].default_value = (1.0, 1.0, 1.0)
    # ID
    random_value_001.inputs[2].default_value = 0

    # Node Instance on Points
    instance_on_points = ff_macadam_nodes_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    instance_on_points.show_options = True
    # Selection
    instance_on_points.inputs[1].default_value = True
    # Pick Instance
    instance_on_points.inputs[3].default_value = False
    # Instance Index
    instance_on_points.inputs[4].default_value = 0

    # Node Mesh Boolean
    mesh_boolean = ff_macadam_nodes_1.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.name = "Mesh Boolean"
    mesh_boolean.show_options = True
    mesh_boolean.operation = 'INTERSECT'
    mesh_boolean.solver = 'EXACT'
    # Self Intersection
    mesh_boolean.inputs[2].default_value = False
    # Hole Tolerant
    mesh_boolean.inputs[3].default_value = False

    # Node Edge Angle
    edge_angle = ff_macadam_nodes_1.nodes.new("GeometryNodeInputMeshEdgeAngle")
    edge_angle.name = "Edge Angle"
    edge_angle.show_options = True

    # Node Compare
    compare = ff_macadam_nodes_1.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.show_options = True
    compare.data_type = 'FLOAT'
    compare.mode = 'ELEMENT'
    compare.operation = 'GREATER_THAN'
    # B
    compare.inputs[1].default_value = 0.5

    # Node UV Unwrap
    uv_unwrap = ff_macadam_nodes_1.nodes.new("GeometryNodeUVUnwrap")
    uv_unwrap.name = "UV Unwrap"
    uv_unwrap.show_options = True
    # Selection
    uv_unwrap.inputs[0].default_value = True
    # Margin
    uv_unwrap.inputs[2].default_value = 0.019999999552965164
    # Fill Holes
    uv_unwrap.inputs[3].default_value = True
    # Method
    uv_unwrap.inputs[4].default_value = 'Angle Based'
    # Iterations
    uv_unwrap.inputs[5].default_value = 10
    # No Flip
    uv_unwrap.inputs[6].default_value = False

    # Node Store Named Attribute
    store_named_attribute = ff_macadam_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'FLOAT2'
    store_named_attribute.domain = 'CORNER'
    # Selection
    store_named_attribute.inputs[1].default_value = True
    # Name
    store_named_attribute.inputs[2].default_value = "UVMap"

    # Node Set Shade Smooth
    set_shade_smooth = ff_macadam_nodes_1.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.show_options = True
    set_shade_smooth.domain = 'FACE'
    # Selection
    set_shade_smooth.inputs[1].default_value = True

    # Node Points
    points = ff_macadam_nodes_1.nodes.new("GeometryNodePoints")
    points.name = "Points"
    points.show_options = True
    # Position
    points.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Radius
    points.inputs[2].default_value = 0.10000000149011612

    # Node Math.001
    math_001 = ff_macadam_nodes_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.show_options = True
    math_001.operation = 'ADD'
    math_001.use_clamp = False
    # Value_001
    math_001.inputs[1].default_value = 1337.0

    # Node Random Value.002
    random_value_002 = ff_macadam_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value_002.name = "Random Value.002"
    random_value_002.show_options = True
    random_value_002.data_type = 'FLOAT'
    # Min
    random_value_002.inputs[0].default_value = 0.0
    # Max
    random_value_002.inputs[1].default_value = 6.2831854820251465
    # ID
    random_value_002.inputs[2].default_value = 0

    # Node Random Value.003
    random_value_003 = ff_macadam_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value_003.name = "Random Value.003"
    random_value_003.show_options = True
    random_value_003.data_type = 'FLOAT'
    # Min
    random_value_003.inputs[0].default_value = 0.0
    # Max
    random_value_003.inputs[1].default_value = 1.0
    # ID
    random_value_003.inputs[2].default_value = 0

    # Node Math.002
    math_002 = ff_macadam_nodes_1.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.show_options = True
    math_002.operation = 'POWER'
    math_002.use_clamp = False
    # Value_001
    math_002.inputs[1].default_value = 0.5

    # Node Math.003
    math_003 = ff_macadam_nodes_1.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.show_options = True
    math_003.operation = 'MULTIPLY'
    math_003.use_clamp = False

    # Node Math.004
    math_004 = ff_macadam_nodes_1.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.show_options = True
    math_004.operation = 'COSINE'
    math_004.use_clamp = False

    # Node Math.005
    math_005 = ff_macadam_nodes_1.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.show_options = True
    math_005.operation = 'SINE'
    math_005.use_clamp = False

    # Node Math.006
    math_006 = ff_macadam_nodes_1.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.show_options = True
    math_006.operation = 'MULTIPLY'
    math_006.use_clamp = False

    # Node Math.007
    math_007 = ff_macadam_nodes_1.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.show_options = True
    math_007.operation = 'MULTIPLY'
    math_007.use_clamp = False

    # Node Combine XYZ
    combine_xyz = ff_macadam_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz.show_options = True
    # Z
    combine_xyz.inputs[2].default_value = 0.0

    # Node Set Position
    set_position = ff_macadam_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.show_options = True
    # Selection
    set_position.inputs[1].default_value = True
    # Offset
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Math.008
    math_008 = ff_macadam_nodes_1.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.show_options = True
    math_008.operation = 'ADD'
    math_008.use_clamp = False
    # Value_001
    math_008.inputs[1].default_value = 99.0

    # Node Math.009
    math_009 = ff_macadam_nodes_1.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.show_options = True
    math_009.operation = 'ADD'
    math_009.use_clamp = False
    # Value_001
    math_009.inputs[1].default_value = 7.0

    # Node Random Value.004
    random_value_004 = ff_macadam_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value_004.name = "Random Value.004"
    random_value_004.show_options = True
    random_value_004.data_type = 'FLOAT_VECTOR'
    # Min
    random_value_004.inputs[0].default_value = (-3.1415927410125732, -3.1415927410125732, -3.1415927410125732)
    # Max
    random_value_004.inputs[1].default_value = (3.1415927410125732, 3.1415927410125732, 3.1415927410125732)
    # ID
    random_value_004.inputs[2].default_value = 0

    # Node Random Value.005
    random_value_005 = ff_macadam_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value_005.name = "Random Value.005"
    random_value_005.show_options = True
    random_value_005.data_type = 'FLOAT'
    # ID
    random_value_005.inputs[2].default_value = 0

    # Node Instance on Points.001
    instance_on_points_001 = ff_macadam_nodes_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_001.name = "Instance on Points.001"
    instance_on_points_001.show_options = True
    # Selection
    instance_on_points_001.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_001.inputs[3].default_value = False
    # Instance Index
    instance_on_points_001.inputs[4].default_value = 0

    # Node Index
    index = ff_macadam_nodes_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Store Named Attribute.001
    store_named_attribute_001 = ff_macadam_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.show_options = True
    store_named_attribute_001.data_type = 'INT'
    store_named_attribute_001.domain = 'INSTANCE'
    # Selection
    store_named_attribute_001.inputs[1].default_value = True
    # Name
    store_named_attribute_001.inputs[2].default_value = "fractal_id"

    # Node Realize Instances
    realize_instances = ff_macadam_nodes_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    realize_instances.show_options = True
    realize_instances.realize_to_point_domain = False
    # Selection
    realize_instances.inputs[1].default_value = True
    # Realize All
    realize_instances.inputs[2].default_value = True
    # Depth
    realize_instances.inputs[3].default_value = 0

    # Node Group Input.004
    group_input_004 = ff_macadam_nodes_1.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.show_options = True

    # Node Normal
    normal = ff_macadam_nodes_1.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"
    normal.show_options = True
    normal.legacy_corner_normals = False

    # Node Convex Hull
    convex_hull = ff_macadam_nodes_1.nodes.new("GeometryNodeConvexHull")
    convex_hull.name = "Convex Hull"
    convex_hull.show_options = True

    # Node Set Shade Smooth.001
    set_shade_smooth_001 = ff_macadam_nodes_1.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth_001.name = "Set Shade Smooth.001"
    set_shade_smooth_001.show_options = True
    set_shade_smooth_001.domain = 'FACE'
    # Selection
    set_shade_smooth_001.inputs[1].default_value = True
    # Shade Smooth
    set_shade_smooth_001.inputs[2].default_value = True

    # Node Sample Nearest Surface
    sample_nearest_surface = ff_macadam_nodes_1.nodes.new("GeometryNodeSampleNearestSurface")
    sample_nearest_surface.name = "Sample Nearest Surface"
    sample_nearest_surface.show_options = True
    sample_nearest_surface.data_type = 'FLOAT_VECTOR'
    # Group ID
    sample_nearest_surface.inputs[2].default_value = 0
    # Sample Position
    sample_nearest_surface.inputs[3].default_value = (0.0, 0.0, 0.0)
    # Sample Group ID
    sample_nearest_surface.inputs[4].default_value = 0

    # Node Math.010
    math_010 = ff_macadam_nodes_1.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.show_options = True
    math_010.operation = 'SUBTRACT'
    math_010.use_clamp = False
    # Value
    math_010.inputs[0].default_value = 1.0

    # Node Vector Math
    vector_math = ff_macadam_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.show_options = True
    vector_math.operation = 'SCALE'

    # Node Vector Math.001
    vector_math_001 = ff_macadam_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.show_options = True
    vector_math_001.operation = 'SCALE'

    # Node Vector Math.002
    vector_math_002 = ff_macadam_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.show_options = True
    vector_math_002.operation = 'ADD'

    # Node Vector Math.003
    vector_math_003 = ff_macadam_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.show_options = True
    vector_math_003.operation = 'NORMALIZE'

    # Node Set Mesh Normal
    set_mesh_normal = ff_macadam_nodes_1.nodes.new("GeometryNodeSetMeshNormal")
    set_mesh_normal.name = "Set Mesh Normal"
    set_mesh_normal.show_options = True
    set_mesh_normal.domain = 'CORNER'
    set_mesh_normal.mode = 'FREE'

    # Node Frame
    frame = ff_macadam_nodes_1.nodes.new("NodeFrame")
    frame.label = "Boolean Rock Generator"
    frame.name = "Frame"
    frame.use_custom_color = True
    frame.color = (0.20000000298023224, 0.30000001192092896, 0.30000001192092896)
    frame.show_options = True
    frame.label_size = 20
    frame.shrink = True

    # Node Frame.001
    frame_001 = ff_macadam_nodes_1.nodes.new("NodeFrame")
    frame_001.label = "Smart UV Project & Attributes"
    frame_001.name = "Frame.001"
    frame_001.use_custom_color = True
    frame_001.color = (0.30000001192092896, 0.30000001192092896, 0.20000000298023224)
    frame_001.show_options = True
    frame_001.label_size = 20
    frame_001.shrink = True

    # Node Frame.002
    frame_002 = ff_macadam_nodes_1.nodes.new("NodeFrame")
    frame_002.label = "Distribution Logic"
    frame_002.name = "Frame.002"
    frame_002.use_custom_color = True
    frame_002.color = (0.30000001192092896, 0.20000000298023224, 0.20000000298023224)
    frame_002.show_options = True
    frame_002.label_size = 20
    frame_002.shrink = True

    # Node Frame.003
    frame_003 = ff_macadam_nodes_1.nodes.new("NodeFrame")
    frame_003.label = "Instancing"
    frame_003.name = "Frame.003"
    frame_003.use_custom_color = True
    frame_003.color = (0.4000000059604645, 0.20000000298023224, 0.20000000298023224)
    frame_003.show_options = True
    frame_003.label_size = 20
    frame_003.shrink = True

    # Node Frame.004
    frame_004 = ff_macadam_nodes_1.nodes.new("NodeFrame")
    frame_004.label = "Stylized Normals & Output"
    frame_004.name = "Frame.004"
    frame_004.use_custom_color = True
    frame_004.color = (0.4000000059604645, 0.20000000298023224, 0.4000000059604645)
    frame_004.show_options = True
    frame_004.label_size = 20
    frame_004.shrink = True

    # Node Reroute
    reroute = ff_macadam_nodes_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketFloat"
    # Node Reroute.001
    reroute_001 = ff_macadam_nodes_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketFloat"
    # Node Reroute.002
    reroute_002 = ff_macadam_nodes_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketFloat"
    # Node Reroute.003
    reroute_003 = ff_macadam_nodes_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketGeometry"
    # Node Normal.001
    normal_001 = ff_macadam_nodes_1.nodes.new("GeometryNodeInputNormal")
    normal_001.name = "Normal.001"
    normal_001.show_options = True
    normal_001.legacy_corner_normals = False

    # Node Group Input.005
    group_input_005 = ff_macadam_nodes_1.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.show_options = True

    # Node Reroute.004
    reroute_004 = ff_macadam_nodes_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    reroute_004.socket_idname = "NodeSocketGeometry"
    # Node Store ColorMask (Injected)
    store_colormask__injected_ = ff_macadam_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_colormask__injected_.name = "Store ColorMask (Injected)"
    store_colormask__injected_.show_options = True
    store_colormask__injected_.data_type = 'FLOAT_COLOR'
    store_colormask__injected_.domain = 'INSTANCE'
    # Selection
    store_colormask__injected_.inputs[1].default_value = True
    # Name
    store_colormask__injected_.inputs[2].default_value = "ColorMask"

    # Node Group Input.006
    group_input_006 = ff_macadam_nodes_1.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.show_options = True

    # Node Set Material
    set_material = ff_macadam_nodes_1.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.show_options = True
    # Selection
    set_material.inputs[1].default_value = True

    # Node Random Value.007
    random_value_007 = ff_macadam_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value_007.name = "Random Value.007"
    random_value_007.show_options = True
    random_value_007.data_type = 'FLOAT_VECTOR'
    # Min
    random_value_007.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Max
    random_value_007.inputs[1].default_value = (1.0, 1.0, 1.0)
    # ID
    random_value_007.inputs[2].default_value = 0

    # Node Color To Seed
    color_to_seed = ff_macadam_nodes_1.nodes.new("ShaderNodeVectorMath")
    color_to_seed.name = "Color To Seed"
    color_to_seed.show_options = True
    color_to_seed.operation = 'DOT_PRODUCT'
    # Vector_001
    color_to_seed.inputs[1].default_value = (137.5399932861328, 452.19000244140625, 874.02001953125)

    # Node Group Input.007
    group_input_007 = ff_macadam_nodes_1.nodes.new("NodeGroupInput")
    group_input_007.name = "Group Input.007"
    group_input_007.show_options = True

    # Set parents
    ff_macadam_nodes_1.nodes["Group Input"].parent = ff_macadam_nodes_1.nodes["Frame"]
    ff_macadam_nodes_1.nodes["Group Input.001"].parent = ff_macadam_nodes_1.nodes["Frame.001"]
    ff_macadam_nodes_1.nodes["Group Input.002"].parent = ff_macadam_nodes_1.nodes["Frame.002"]
    ff_macadam_nodes_1.nodes["Group Input.003"].parent = ff_macadam_nodes_1.nodes["Frame.003"]
    ff_macadam_nodes_1.nodes["Mesh Line"].parent = ff_macadam_nodes_1.nodes["Frame"]
    ff_macadam_nodes_1.nodes["Ico Sphere"].parent = ff_macadam_nodes_1.nodes["Frame"]
    ff_macadam_nodes_1.nodes["Math"].parent = ff_macadam_nodes_1.nodes["Frame"]
    ff_macadam_nodes_1.nodes["Random Value"].parent = ff_macadam_nodes_1.nodes["Frame"]
    ff_macadam_nodes_1.nodes["Random Value.001"].parent = ff_macadam_nodes_1.nodes["Frame"]
    ff_macadam_nodes_1.nodes["Instance on Points"].parent = ff_macadam_nodes_1.nodes["Frame"]
    ff_macadam_nodes_1.nodes["Mesh Boolean"].parent = ff_macadam_nodes_1.nodes["Frame"]
    ff_macadam_nodes_1.nodes["Edge Angle"].parent = ff_macadam_nodes_1.nodes["Frame.001"]
    ff_macadam_nodes_1.nodes["Compare"].parent = ff_macadam_nodes_1.nodes["Frame.001"]
    ff_macadam_nodes_1.nodes["UV Unwrap"].parent = ff_macadam_nodes_1.nodes["Frame.001"]
    ff_macadam_nodes_1.nodes["Store Named Attribute"].parent = ff_macadam_nodes_1.nodes["Frame.001"]
    ff_macadam_nodes_1.nodes["Set Shade Smooth"].parent = ff_macadam_nodes_1.nodes["Frame.001"]
    ff_macadam_nodes_1.nodes["Points"].parent = ff_macadam_nodes_1.nodes["Frame.002"]
    ff_macadam_nodes_1.nodes["Math.001"].parent = ff_macadam_nodes_1.nodes["Frame.002"]
    ff_macadam_nodes_1.nodes["Random Value.002"].parent = ff_macadam_nodes_1.nodes["Frame.002"]
    ff_macadam_nodes_1.nodes["Random Value.003"].parent = ff_macadam_nodes_1.nodes["Frame.002"]
    ff_macadam_nodes_1.nodes["Math.002"].parent = ff_macadam_nodes_1.nodes["Frame.002"]
    ff_macadam_nodes_1.nodes["Math.003"].parent = ff_macadam_nodes_1.nodes["Frame.002"]
    ff_macadam_nodes_1.nodes["Math.004"].parent = ff_macadam_nodes_1.nodes["Frame.002"]
    ff_macadam_nodes_1.nodes["Math.005"].parent = ff_macadam_nodes_1.nodes["Frame.002"]
    ff_macadam_nodes_1.nodes["Math.006"].parent = ff_macadam_nodes_1.nodes["Frame.002"]
    ff_macadam_nodes_1.nodes["Math.007"].parent = ff_macadam_nodes_1.nodes["Frame.002"]
    ff_macadam_nodes_1.nodes["Combine XYZ"].parent = ff_macadam_nodes_1.nodes["Frame.002"]
    ff_macadam_nodes_1.nodes["Set Position"].parent = ff_macadam_nodes_1.nodes["Frame.002"]
    ff_macadam_nodes_1.nodes["Math.008"].parent = ff_macadam_nodes_1.nodes["Frame.003"]
    ff_macadam_nodes_1.nodes["Math.009"].parent = ff_macadam_nodes_1.nodes["Frame.003"]
    ff_macadam_nodes_1.nodes["Random Value.004"].parent = ff_macadam_nodes_1.nodes["Frame.003"]
    ff_macadam_nodes_1.nodes["Random Value.005"].parent = ff_macadam_nodes_1.nodes["Frame.003"]
    ff_macadam_nodes_1.nodes["Instance on Points.001"].parent = ff_macadam_nodes_1.nodes["Frame.003"]
    ff_macadam_nodes_1.nodes["Index"].parent = ff_macadam_nodes_1.nodes["Frame.003"]
    ff_macadam_nodes_1.nodes["Store Named Attribute.001"].parent = ff_macadam_nodes_1.nodes["Frame.003"]
    ff_macadam_nodes_1.nodes["Realize Instances"].parent = ff_macadam_nodes_1.nodes["Frame.003"]
    ff_macadam_nodes_1.nodes["Group Input.004"].parent = ff_macadam_nodes_1.nodes["Frame.004"]
    ff_macadam_nodes_1.nodes["Normal"].parent = ff_macadam_nodes_1.nodes["Frame.004"]
    ff_macadam_nodes_1.nodes["Convex Hull"].parent = ff_macadam_nodes_1.nodes["Frame.004"]
    ff_macadam_nodes_1.nodes["Set Shade Smooth.001"].parent = ff_macadam_nodes_1.nodes["Frame.004"]
    ff_macadam_nodes_1.nodes["Sample Nearest Surface"].parent = ff_macadam_nodes_1.nodes["Frame.004"]
    ff_macadam_nodes_1.nodes["Math.010"].parent = ff_macadam_nodes_1.nodes["Frame.004"]
    ff_macadam_nodes_1.nodes["Vector Math"].parent = ff_macadam_nodes_1.nodes["Frame.004"]
    ff_macadam_nodes_1.nodes["Vector Math.001"].parent = ff_macadam_nodes_1.nodes["Frame.004"]
    ff_macadam_nodes_1.nodes["Vector Math.002"].parent = ff_macadam_nodes_1.nodes["Frame.004"]
    ff_macadam_nodes_1.nodes["Vector Math.003"].parent = ff_macadam_nodes_1.nodes["Frame.004"]
    ff_macadam_nodes_1.nodes["Set Mesh Normal"].parent = ff_macadam_nodes_1.nodes["Frame.004"]
    ff_macadam_nodes_1.nodes["Reroute"].parent = ff_macadam_nodes_1.nodes["Frame.002"]
    ff_macadam_nodes_1.nodes["Reroute.001"].parent = ff_macadam_nodes_1.nodes["Frame.002"]
    ff_macadam_nodes_1.nodes["Reroute.002"].parent = ff_macadam_nodes_1.nodes["Frame.002"]
    ff_macadam_nodes_1.nodes["Reroute.003"].parent = ff_macadam_nodes_1.nodes["Frame.003"]
    ff_macadam_nodes_1.nodes["Normal.001"].parent = ff_macadam_nodes_1.nodes["Frame.004"]
    ff_macadam_nodes_1.nodes["Group Input.005"].parent = ff_macadam_nodes_1.nodes["Frame.004"]
    ff_macadam_nodes_1.nodes["Reroute.004"].parent = ff_macadam_nodes_1.nodes["Frame.004"]
    ff_macadam_nodes_1.nodes["Store ColorMask (Injected)"].parent = ff_macadam_nodes_1.nodes["Frame.003"]
    ff_macadam_nodes_1.nodes["Group Input.006"].parent = ff_macadam_nodes_1.nodes["Frame.004"]
    ff_macadam_nodes_1.nodes["Set Material"].parent = ff_macadam_nodes_1.nodes["Frame.004"]
    ff_macadam_nodes_1.nodes["Random Value.007"].parent = ff_macadam_nodes_1.nodes["Frame.003"]
    ff_macadam_nodes_1.nodes["Color To Seed"].parent = ff_macadam_nodes_1.nodes["Frame.003"]
    ff_macadam_nodes_1.nodes["Group Input.007"].parent = ff_macadam_nodes_1.nodes["Frame.003"]

    # Set locations
    ff_macadam_nodes_1.nodes["Group Input"].location = (29.535888671875, -322.58935546875)
    ff_macadam_nodes_1.nodes["Group Input.001"].location = (506.11614990234375, -211.4599609375)
    ff_macadam_nodes_1.nodes["Group Input.002"].location = (29.6571044921875, -40.1685791015625)
    ff_macadam_nodes_1.nodes["Group Input.003"].location = (30.40838623046875, -532.9530029296875)
    ff_macadam_nodes_1.nodes["Group Output"].location = (2903.882080078125, 1961.0848388671875)
    ff_macadam_nodes_1.nodes["Mesh Line"].location = (440.3167724609375, -156.02197265625)
    ff_macadam_nodes_1.nodes["Ico Sphere"].location = (441.7183837890625, -430.775390625)
    ff_macadam_nodes_1.nodes["Math"].location = (283.678955078125, -1029.3828125)
    ff_macadam_nodes_1.nodes["Random Value"].location = (443.51220703125, -553.6748046875)
    ff_macadam_nodes_1.nodes["Random Value.001"].location = (441.827880859375, -852.76318359375)
    ff_macadam_nodes_1.nodes["Instance on Points"].location = (622.392333984375, -131.4918212890625)
    ff_macadam_nodes_1.nodes["Mesh Boolean"].location = (781.2349853515625, -35.758056640625)
    ff_macadam_nodes_1.nodes["Edge Angle"].location = (30.32421875, -273.421630859375)
    ff_macadam_nodes_1.nodes["Compare"].location = (190.02734375, -198.2093505859375)
    ff_macadam_nodes_1.nodes["UV Unwrap"].location = (353.64239501953125, -151.462158203125)
    ff_macadam_nodes_1.nodes["Store Named Attribute"].location = (510.32391357421875, -35.924560546875)
    ff_macadam_nodes_1.nodes["Set Shade Smooth"].location = (681.0617065429688, -60.219970703125)
    ff_macadam_nodes_1.nodes["Points"].location = (1202.0765380859375, -36.0992431640625)
    ff_macadam_nodes_1.nodes["Math.001"].location = (224.2457275390625, -679.0408935546875)
    ff_macadam_nodes_1.nodes["Random Value.002"].location = (381.588134765625, -211.88519287109375)
    ff_macadam_nodes_1.nodes["Random Value.003"].location = (381.4925537109375, -563.6213989257812)
    ff_macadam_nodes_1.nodes["Math.002"].location = (534.8129272460938, -488.10858154296875)
    ff_macadam_nodes_1.nodes["Math.003"].location = (692.420166015625, -413.98699951171875)
    ff_macadam_nodes_1.nodes["Math.004"].location = (538.3834228515625, -212.37225341796875)
    ff_macadam_nodes_1.nodes["Math.005"].location = (537.3704833984375, -342.87872314453125)
    ff_macadam_nodes_1.nodes["Math.006"].location = (1037.5928955078125, -136.19146728515625)
    ff_macadam_nodes_1.nodes["Math.007"].location = (857.3956909179688, -270.69769287109375)
    ff_macadam_nodes_1.nodes["Combine XYZ"].location = (1201.4019775390625, -223.29833984375)
    ff_macadam_nodes_1.nodes["Set Position"].location = (1364.290283203125, -37.12060546875)
    ff_macadam_nodes_1.nodes["Math.008"].location = (202.3260498046875, -460.325927734375)
    ff_macadam_nodes_1.nodes["Math.009"].location = (195.21197509765625, -661.785888671875)
    ff_macadam_nodes_1.nodes["Random Value.004"].location = (396.3427734375, -220.9542236328125)
    ff_macadam_nodes_1.nodes["Random Value.005"].location = (394.8470458984375, -522.6871337890625)
    ff_macadam_nodes_1.nodes["Instance on Points.001"].location = (563.6744995117188, -85.800048828125)
    ff_macadam_nodes_1.nodes["Index"].location = (726.3834228515625, -211.016845703125)
    ff_macadam_nodes_1.nodes["Store Named Attribute.001"].location = (728.294677734375, -36.214599609375)
    ff_macadam_nodes_1.nodes["Realize Instances"].location = (1052.4671630859375, -85.8533935546875)
    ff_macadam_nodes_1.nodes["Group Input.004"].location = (186.2926025390625, -523.9542236328125)
    ff_macadam_nodes_1.nodes["Normal"].location = (186.2860107421875, -446.4471435546875)
    ff_macadam_nodes_1.nodes["Convex Hull"].location = (30.39404296875, -345.8834228515625)
    ff_macadam_nodes_1.nodes["Set Shade Smooth.001"].location = (188.380126953125, -321.627685546875)
    ff_macadam_nodes_1.nodes["Sample Nearest Surface"].location = (346.179443359375, -275.2667236328125)
    ff_macadam_nodes_1.nodes["Math.010"].location = (350.82763671875, -492.0528564453125)
    ff_macadam_nodes_1.nodes["Vector Math"].location = (525.667724609375, -353.7667236328125)
    ff_macadam_nodes_1.nodes["Vector Math.001"].location = (528.0703125, -227.5452880859375)
    ff_macadam_nodes_1.nodes["Vector Math.002"].location = (698.25048828125, -156.3233642578125)
    ff_macadam_nodes_1.nodes["Vector Math.003"].location = (855.822998046875, -108.307861328125)
    ff_macadam_nodes_1.nodes["Set Mesh Normal"].location = (1021.44091796875, -35.833251953125)
    ff_macadam_nodes_1.nodes["Frame"].location = (-2229.0, 1635.0)
    ff_macadam_nodes_1.nodes["Frame.001"].location = (-1262.0, 1686.0)
    ff_macadam_nodes_1.nodes["Frame.002"].location = (-1260.0, 1137.0)
    ff_macadam_nodes_1.nodes["Frame.003"].location = (291.0, 1760.0)
    ff_macadam_nodes_1.nodes["Frame.004"].location = (1531.0, 2046.0)
    ff_macadam_nodes_1.nodes["Reroute"].location = (666.9492797851562, -476.78228759765625)
    ff_macadam_nodes_1.nodes["Reroute.001"].location = (539.432373046875, -478.401123046875)
    ff_macadam_nodes_1.nodes["Reroute.002"].location = (1000.274658203125, -447.645751953125)
    ff_macadam_nodes_1.nodes["Reroute.003"].location = (39.055633544921875, -146.7783203125)
    ff_macadam_nodes_1.nodes["Normal.001"].location = (523.4677734375, -486.1920166015625)
    ff_macadam_nodes_1.nodes["Group Input.005"].location = (350.025390625, -648.8990478515625)
    ff_macadam_nodes_1.nodes["Reroute.004"].location = (41.0806884765625, -123.98291015625)
    ff_macadam_nodes_1.nodes["Store ColorMask (Injected)"].location = (893.6680908203125, -35.9774169921875)
    ff_macadam_nodes_1.nodes["Group Input.006"].location = (1018.06591796875, -166.417236328125)
    ff_macadam_nodes_1.nodes["Set Material"].location = (1178.088623046875, -85.690185546875)
    ff_macadam_nodes_1.nodes["Random Value.007"].location = (727.3980712890625, -274.4736328125)
    ff_macadam_nodes_1.nodes["Color To Seed"].location = (721.9230346679688, -578.978515625)
    ff_macadam_nodes_1.nodes["Group Input.007"].location = (566.2164306640625, -629.0882568359375)

    # Set dimensions
    ff_macadam_nodes_1.nodes["Group Input"].width  = 140.0
    ff_macadam_nodes_1.nodes["Group Input"].height = 100.0

    ff_macadam_nodes_1.nodes["Group Input.001"].width  = 140.0
    ff_macadam_nodes_1.nodes["Group Input.001"].height = 100.0

    ff_macadam_nodes_1.nodes["Group Input.002"].width  = 140.0
    ff_macadam_nodes_1.nodes["Group Input.002"].height = 100.0

    ff_macadam_nodes_1.nodes["Group Input.003"].width  = 140.0
    ff_macadam_nodes_1.nodes["Group Input.003"].height = 100.0

    ff_macadam_nodes_1.nodes["Group Output"].width  = 140.0
    ff_macadam_nodes_1.nodes["Group Output"].height = 100.0

    ff_macadam_nodes_1.nodes["Mesh Line"].width  = 140.0
    ff_macadam_nodes_1.nodes["Mesh Line"].height = 100.0

    ff_macadam_nodes_1.nodes["Ico Sphere"].width  = 140.0
    ff_macadam_nodes_1.nodes["Ico Sphere"].height = 100.0

    ff_macadam_nodes_1.nodes["Math"].width  = 140.0
    ff_macadam_nodes_1.nodes["Math"].height = 100.0

    ff_macadam_nodes_1.nodes["Random Value"].width  = 140.0
    ff_macadam_nodes_1.nodes["Random Value"].height = 100.0

    ff_macadam_nodes_1.nodes["Random Value.001"].width  = 140.0
    ff_macadam_nodes_1.nodes["Random Value.001"].height = 100.0

    ff_macadam_nodes_1.nodes["Instance on Points"].width  = 140.0
    ff_macadam_nodes_1.nodes["Instance on Points"].height = 100.0

    ff_macadam_nodes_1.nodes["Mesh Boolean"].width  = 140.0
    ff_macadam_nodes_1.nodes["Mesh Boolean"].height = 100.0

    ff_macadam_nodes_1.nodes["Edge Angle"].width  = 140.0
    ff_macadam_nodes_1.nodes["Edge Angle"].height = 100.0

    ff_macadam_nodes_1.nodes["Compare"].width  = 140.0
    ff_macadam_nodes_1.nodes["Compare"].height = 100.0

    ff_macadam_nodes_1.nodes["UV Unwrap"].width  = 140.0
    ff_macadam_nodes_1.nodes["UV Unwrap"].height = 100.0

    ff_macadam_nodes_1.nodes["Store Named Attribute"].width  = 140.0
    ff_macadam_nodes_1.nodes["Store Named Attribute"].height = 100.0

    ff_macadam_nodes_1.nodes["Set Shade Smooth"].width  = 140.0
    ff_macadam_nodes_1.nodes["Set Shade Smooth"].height = 100.0

    ff_macadam_nodes_1.nodes["Points"].width  = 140.0
    ff_macadam_nodes_1.nodes["Points"].height = 100.0

    ff_macadam_nodes_1.nodes["Math.001"].width  = 140.0
    ff_macadam_nodes_1.nodes["Math.001"].height = 100.0

    ff_macadam_nodes_1.nodes["Random Value.002"].width  = 140.0
    ff_macadam_nodes_1.nodes["Random Value.002"].height = 100.0

    ff_macadam_nodes_1.nodes["Random Value.003"].width  = 140.0
    ff_macadam_nodes_1.nodes["Random Value.003"].height = 100.0

    ff_macadam_nodes_1.nodes["Math.002"].width  = 140.0
    ff_macadam_nodes_1.nodes["Math.002"].height = 100.0

    ff_macadam_nodes_1.nodes["Math.003"].width  = 140.0
    ff_macadam_nodes_1.nodes["Math.003"].height = 100.0

    ff_macadam_nodes_1.nodes["Math.004"].width  = 140.0
    ff_macadam_nodes_1.nodes["Math.004"].height = 100.0

    ff_macadam_nodes_1.nodes["Math.005"].width  = 140.0
    ff_macadam_nodes_1.nodes["Math.005"].height = 100.0

    ff_macadam_nodes_1.nodes["Math.006"].width  = 140.0
    ff_macadam_nodes_1.nodes["Math.006"].height = 100.0

    ff_macadam_nodes_1.nodes["Math.007"].width  = 140.0
    ff_macadam_nodes_1.nodes["Math.007"].height = 100.0

    ff_macadam_nodes_1.nodes["Combine XYZ"].width  = 140.0
    ff_macadam_nodes_1.nodes["Combine XYZ"].height = 100.0

    ff_macadam_nodes_1.nodes["Set Position"].width  = 140.0
    ff_macadam_nodes_1.nodes["Set Position"].height = 100.0

    ff_macadam_nodes_1.nodes["Math.008"].width  = 140.0
    ff_macadam_nodes_1.nodes["Math.008"].height = 100.0

    ff_macadam_nodes_1.nodes["Math.009"].width  = 140.0
    ff_macadam_nodes_1.nodes["Math.009"].height = 100.0

    ff_macadam_nodes_1.nodes["Random Value.004"].width  = 140.0
    ff_macadam_nodes_1.nodes["Random Value.004"].height = 100.0

    ff_macadam_nodes_1.nodes["Random Value.005"].width  = 140.0
    ff_macadam_nodes_1.nodes["Random Value.005"].height = 100.0

    ff_macadam_nodes_1.nodes["Instance on Points.001"].width  = 140.0
    ff_macadam_nodes_1.nodes["Instance on Points.001"].height = 100.0

    ff_macadam_nodes_1.nodes["Index"].width  = 140.0
    ff_macadam_nodes_1.nodes["Index"].height = 100.0

    ff_macadam_nodes_1.nodes["Store Named Attribute.001"].width  = 140.0
    ff_macadam_nodes_1.nodes["Store Named Attribute.001"].height = 100.0

    ff_macadam_nodes_1.nodes["Realize Instances"].width  = 140.0
    ff_macadam_nodes_1.nodes["Realize Instances"].height = 100.0

    ff_macadam_nodes_1.nodes["Group Input.004"].width  = 140.0
    ff_macadam_nodes_1.nodes["Group Input.004"].height = 100.0

    ff_macadam_nodes_1.nodes["Normal"].width  = 140.0
    ff_macadam_nodes_1.nodes["Normal"].height = 100.0

    ff_macadam_nodes_1.nodes["Convex Hull"].width  = 140.0
    ff_macadam_nodes_1.nodes["Convex Hull"].height = 100.0

    ff_macadam_nodes_1.nodes["Set Shade Smooth.001"].width  = 140.0
    ff_macadam_nodes_1.nodes["Set Shade Smooth.001"].height = 100.0

    ff_macadam_nodes_1.nodes["Sample Nearest Surface"].width  = 150.0
    ff_macadam_nodes_1.nodes["Sample Nearest Surface"].height = 100.0

    ff_macadam_nodes_1.nodes["Math.010"].width  = 140.0
    ff_macadam_nodes_1.nodes["Math.010"].height = 100.0

    ff_macadam_nodes_1.nodes["Vector Math"].width  = 140.0
    ff_macadam_nodes_1.nodes["Vector Math"].height = 100.0

    ff_macadam_nodes_1.nodes["Vector Math.001"].width  = 140.0
    ff_macadam_nodes_1.nodes["Vector Math.001"].height = 100.0

    ff_macadam_nodes_1.nodes["Vector Math.002"].width  = 140.0
    ff_macadam_nodes_1.nodes["Vector Math.002"].height = 100.0

    ff_macadam_nodes_1.nodes["Vector Math.003"].width  = 140.0
    ff_macadam_nodes_1.nodes["Vector Math.003"].height = 100.0

    ff_macadam_nodes_1.nodes["Set Mesh Normal"].width  = 140.0
    ff_macadam_nodes_1.nodes["Set Mesh Normal"].height = 100.0

    ff_macadam_nodes_1.nodes["Frame"].width  = 951.0
    ff_macadam_nodes_1.nodes["Frame"].height = 1207.0

    ff_macadam_nodes_1.nodes["Frame.001"].width  = 851.0
    ff_macadam_nodes_1.nodes["Frame.001"].height = 577.0

    ff_macadam_nodes_1.nodes["Frame.002"].width  = 1534.0
    ff_macadam_nodes_1.nodes["Frame.002"].height = 857.0

    ff_macadam_nodes_1.nodes["Frame.003"].width  = 1222.0
    ff_macadam_nodes_1.nodes["Frame.003"].height = 995.0

    ff_macadam_nodes_1.nodes["Frame.004"].width  = 1348.0
    ff_macadam_nodes_1.nodes["Frame.004"].height = 1015.0

    ff_macadam_nodes_1.nodes["Reroute"].width  = 10.0
    ff_macadam_nodes_1.nodes["Reroute"].height = 100.0

    ff_macadam_nodes_1.nodes["Reroute.001"].width  = 10.0
    ff_macadam_nodes_1.nodes["Reroute.001"].height = 100.0

    ff_macadam_nodes_1.nodes["Reroute.002"].width  = 10.0
    ff_macadam_nodes_1.nodes["Reroute.002"].height = 100.0

    ff_macadam_nodes_1.nodes["Reroute.003"].width  = 10.0
    ff_macadam_nodes_1.nodes["Reroute.003"].height = 100.0

    ff_macadam_nodes_1.nodes["Normal.001"].width  = 140.0
    ff_macadam_nodes_1.nodes["Normal.001"].height = 100.0

    ff_macadam_nodes_1.nodes["Group Input.005"].width  = 140.0
    ff_macadam_nodes_1.nodes["Group Input.005"].height = 100.0

    ff_macadam_nodes_1.nodes["Reroute.004"].width  = 10.0
    ff_macadam_nodes_1.nodes["Reroute.004"].height = 100.0

    ff_macadam_nodes_1.nodes["Store ColorMask (Injected)"].width  = 140.0
    ff_macadam_nodes_1.nodes["Store ColorMask (Injected)"].height = 100.0

    ff_macadam_nodes_1.nodes["Group Input.006"].width  = 140.0
    ff_macadam_nodes_1.nodes["Group Input.006"].height = 100.0

    ff_macadam_nodes_1.nodes["Set Material"].width  = 140.0
    ff_macadam_nodes_1.nodes["Set Material"].height = 100.0

    ff_macadam_nodes_1.nodes["Random Value.007"].width  = 140.0
    ff_macadam_nodes_1.nodes["Random Value.007"].height = 100.0

    ff_macadam_nodes_1.nodes["Color To Seed"].width  = 140.0
    ff_macadam_nodes_1.nodes["Color To Seed"].height = 100.0

    ff_macadam_nodes_1.nodes["Group Input.007"].width  = 140.0
    ff_macadam_nodes_1.nodes["Group Input.007"].height = 100.0


    # Initialize ff_macadam_nodes_1 links

    # group_input.Detail -> mesh_line.Count
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input"].outputs[6],
        ff_macadam_nodes_1.nodes["Mesh Line"].inputs[0]
    )
    # group_input.Base Radius -> ico_sphere.Radius
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input"].outputs[7],
        ff_macadam_nodes_1.nodes["Ico Sphere"].inputs[0]
    )
    # group_input.Shape Seed -> math.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input"].outputs[5],
        ff_macadam_nodes_1.nodes["Math"].inputs[0]
    )
    # group_input.Shape Seed -> random_value.Seed
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input"].outputs[5],
        ff_macadam_nodes_1.nodes["Random Value"].inputs[3]
    )
    # math.Value -> random_value_001.Seed
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Math"].outputs[0],
        ff_macadam_nodes_1.nodes["Random Value.001"].inputs[3]
    )
    # group_input.Roundness -> random_value_001.Min
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input"].outputs[8],
        ff_macadam_nodes_1.nodes["Random Value.001"].inputs[0]
    )
    # mesh_line.Mesh -> instance_on_points.Points
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Mesh Line"].outputs[0],
        ff_macadam_nodes_1.nodes["Instance on Points"].inputs[0]
    )
    # ico_sphere.Mesh -> instance_on_points.Instance
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Ico Sphere"].outputs[0],
        ff_macadam_nodes_1.nodes["Instance on Points"].inputs[2]
    )
    # random_value.Value -> instance_on_points.Rotation
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Random Value"].outputs[0],
        ff_macadam_nodes_1.nodes["Instance on Points"].inputs[5]
    )
    # random_value_001.Value -> instance_on_points.Scale
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Random Value.001"].outputs[0],
        ff_macadam_nodes_1.nodes["Instance on Points"].inputs[6]
    )
    # instance_on_points.Instances -> mesh_boolean.Mesh
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Instance on Points"].outputs[0],
        ff_macadam_nodes_1.nodes["Mesh Boolean"].inputs[1]
    )
    # edge_angle.Unsigned Angle -> compare.A
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Edge Angle"].outputs[0],
        ff_macadam_nodes_1.nodes["Compare"].inputs[0]
    )
    # compare.Result -> uv_unwrap.Seam
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Compare"].outputs[0],
        ff_macadam_nodes_1.nodes["UV Unwrap"].inputs[1]
    )
    # mesh_boolean.Mesh -> store_named_attribute.Geometry
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Mesh Boolean"].outputs[0],
        ff_macadam_nodes_1.nodes["Store Named Attribute"].inputs[0]
    )
    # uv_unwrap.UV -> store_named_attribute.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["UV Unwrap"].outputs[0],
        ff_macadam_nodes_1.nodes["Store Named Attribute"].inputs[3]
    )
    # store_named_attribute.Geometry -> set_shade_smooth.Mesh
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Store Named Attribute"].outputs[0],
        ff_macadam_nodes_1.nodes["Set Shade Smooth"].inputs[0]
    )
    # group_input_001.Smooth Shading -> set_shade_smooth.Shade Smooth
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input.001"].outputs[10],
        ff_macadam_nodes_1.nodes["Set Shade Smooth"].inputs[2]
    )
    # group_input_002.Count -> points.Count
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input.002"].outputs[1],
        ff_macadam_nodes_1.nodes["Points"].inputs[0]
    )
    # group_input_002.Seed -> random_value_002.Seed
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input.002"].outputs[0],
        ff_macadam_nodes_1.nodes["Random Value.002"].inputs[3]
    )
    # group_input_002.Seed -> math_001.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input.002"].outputs[0],
        ff_macadam_nodes_1.nodes["Math.001"].inputs[0]
    )
    # math_001.Value -> random_value_003.Seed
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Math.001"].outputs[0],
        ff_macadam_nodes_1.nodes["Random Value.003"].inputs[3]
    )
    # random_value_003.Value -> math_002.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Random Value.003"].outputs[0],
        ff_macadam_nodes_1.nodes["Math.002"].inputs[0]
    )
    # math_002.Value -> math_003.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Math.002"].outputs[0],
        ff_macadam_nodes_1.nodes["Math.003"].inputs[0]
    )
    # reroute.Output -> math_003.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Reroute"].outputs[0],
        ff_macadam_nodes_1.nodes["Math.003"].inputs[1]
    )
    # random_value_002.Value -> math_004.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Random Value.002"].outputs[0],
        ff_macadam_nodes_1.nodes["Math.004"].inputs[0]
    )
    # random_value_002.Value -> math_005.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Random Value.002"].outputs[0],
        ff_macadam_nodes_1.nodes["Math.005"].inputs[0]
    )
    # math_004.Value -> math_006.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Math.004"].outputs[0],
        ff_macadam_nodes_1.nodes["Math.006"].inputs[0]
    )
    # reroute_002.Output -> math_006.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Reroute.002"].outputs[0],
        ff_macadam_nodes_1.nodes["Math.006"].inputs[1]
    )
    # math_005.Value -> math_007.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Math.005"].outputs[0],
        ff_macadam_nodes_1.nodes["Math.007"].inputs[0]
    )
    # math_003.Value -> math_007.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Math.003"].outputs[0],
        ff_macadam_nodes_1.nodes["Math.007"].inputs[1]
    )
    # math_006.Value -> combine_xyz.X
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Math.006"].outputs[0],
        ff_macadam_nodes_1.nodes["Combine XYZ"].inputs[0]
    )
    # math_007.Value -> combine_xyz.Y
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Math.007"].outputs[0],
        ff_macadam_nodes_1.nodes["Combine XYZ"].inputs[1]
    )
    # points.Points -> set_position.Geometry
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Points"].outputs[0],
        ff_macadam_nodes_1.nodes["Set Position"].inputs[0]
    )
    # combine_xyz.Vector -> set_position.Position
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Combine XYZ"].outputs[0],
        ff_macadam_nodes_1.nodes["Set Position"].inputs[2]
    )
    # group_input_003.Seed -> math_008.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input.003"].outputs[0],
        ff_macadam_nodes_1.nodes["Math.008"].inputs[0]
    )
    # math_008.Value -> random_value_004.Seed
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Math.008"].outputs[0],
        ff_macadam_nodes_1.nodes["Random Value.004"].inputs[3]
    )
    # group_input_003.Seed -> math_009.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input.003"].outputs[0],
        ff_macadam_nodes_1.nodes["Math.009"].inputs[0]
    )
    # math_009.Value -> random_value_005.Seed
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Math.009"].outputs[0],
        ff_macadam_nodes_1.nodes["Random Value.005"].inputs[3]
    )
    # group_input_003.Min Scale -> random_value_005.Min
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input.003"].outputs[3],
        ff_macadam_nodes_1.nodes["Random Value.005"].inputs[0]
    )
    # group_input_003.Max Scale -> random_value_005.Max
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input.003"].outputs[4],
        ff_macadam_nodes_1.nodes["Random Value.005"].inputs[1]
    )
    # reroute_003.Output -> instance_on_points_001.Points
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Reroute.003"].outputs[0],
        ff_macadam_nodes_1.nodes["Instance on Points.001"].inputs[0]
    )
    # set_shade_smooth.Mesh -> instance_on_points_001.Instance
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Set Shade Smooth"].outputs[0],
        ff_macadam_nodes_1.nodes["Instance on Points.001"].inputs[2]
    )
    # random_value_004.Value -> instance_on_points_001.Rotation
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Random Value.004"].outputs[0],
        ff_macadam_nodes_1.nodes["Instance on Points.001"].inputs[5]
    )
    # random_value_005.Value -> instance_on_points_001.Scale
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Random Value.005"].outputs[0],
        ff_macadam_nodes_1.nodes["Instance on Points.001"].inputs[6]
    )
    # instance_on_points_001.Instances -> store_named_attribute_001.Geometry
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Instance on Points.001"].outputs[0],
        ff_macadam_nodes_1.nodes["Store Named Attribute.001"].inputs[0]
    )
    # index.Index -> store_named_attribute_001.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Index"].outputs[0],
        ff_macadam_nodes_1.nodes["Store Named Attribute.001"].inputs[3]
    )
    # reroute_004.Output -> set_mesh_normal.Mesh
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Reroute.004"].outputs[0],
        ff_macadam_nodes_1.nodes["Set Mesh Normal"].inputs[0]
    )
    # realize_instances.Geometry -> convex_hull.Geometry
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Realize Instances"].outputs[0],
        ff_macadam_nodes_1.nodes["Convex Hull"].inputs[0]
    )
    # convex_hull.Convex Hull -> set_shade_smooth_001.Mesh
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Convex Hull"].outputs[0],
        ff_macadam_nodes_1.nodes["Set Shade Smooth.001"].inputs[0]
    )
    # set_shade_smooth_001.Mesh -> sample_nearest_surface.Mesh
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Set Shade Smooth.001"].outputs[0],
        ff_macadam_nodes_1.nodes["Sample Nearest Surface"].inputs[0]
    )
    # normal.Normal -> sample_nearest_surface.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Normal"].outputs[0],
        ff_macadam_nodes_1.nodes["Sample Nearest Surface"].inputs[1]
    )
    # group_input_004.Stylized Normals -> math_010.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input.004"].outputs[11],
        ff_macadam_nodes_1.nodes["Math.010"].inputs[1]
    )
    # math_010.Value -> vector_math.Scale
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Math.010"].outputs[0],
        ff_macadam_nodes_1.nodes["Vector Math"].inputs[3]
    )
    # sample_nearest_surface.Value -> vector_math_001.Vector
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Sample Nearest Surface"].outputs[0],
        ff_macadam_nodes_1.nodes["Vector Math.001"].inputs[0]
    )
    # vector_math.Vector -> vector_math_002.Vector
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Vector Math"].outputs[0],
        ff_macadam_nodes_1.nodes["Vector Math.002"].inputs[0]
    )
    # vector_math_001.Vector -> vector_math_002.Vector
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Vector Math.001"].outputs[0],
        ff_macadam_nodes_1.nodes["Vector Math.002"].inputs[1]
    )
    # vector_math_002.Vector -> vector_math_003.Vector
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Vector Math.002"].outputs[0],
        ff_macadam_nodes_1.nodes["Vector Math.003"].inputs[0]
    )
    # vector_math_003.Vector -> set_mesh_normal.Custom Normal
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Vector Math.003"].outputs[0],
        ff_macadam_nodes_1.nodes["Set Mesh Normal"].inputs[1]
    )
    # reroute_001.Output -> reroute.Input
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Reroute.001"].outputs[0],
        ff_macadam_nodes_1.nodes["Reroute"].inputs[0]
    )
    # group_input_002.Patch Radius -> reroute_001.Input
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input.002"].outputs[2],
        ff_macadam_nodes_1.nodes["Reroute.001"].inputs[0]
    )
    # math_003.Value -> reroute_002.Input
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Math.003"].outputs[0],
        ff_macadam_nodes_1.nodes["Reroute.002"].inputs[0]
    )
    # set_position.Geometry -> reroute_003.Input
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Set Position"].outputs[0],
        ff_macadam_nodes_1.nodes["Reroute.003"].inputs[0]
    )
    # normal_001.Normal -> vector_math.Vector
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Normal.001"].outputs[0],
        ff_macadam_nodes_1.nodes["Vector Math"].inputs[0]
    )
    # group_input_005.Stylized Normals -> vector_math_001.Scale
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input.005"].outputs[11],
        ff_macadam_nodes_1.nodes["Vector Math.001"].inputs[3]
    )
    # realize_instances.Geometry -> reroute_004.Input
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Realize Instances"].outputs[0],
        ff_macadam_nodes_1.nodes["Reroute.004"].inputs[0]
    )
    # store_named_attribute_001.Geometry -> store_colormask__injected_.Geometry
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Store Named Attribute.001"].outputs[0],
        ff_macadam_nodes_1.nodes["Store ColorMask (Injected)"].inputs[0]
    )
    # store_colormask__injected_.Geometry -> realize_instances.Geometry
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Store ColorMask (Injected)"].outputs[0],
        ff_macadam_nodes_1.nodes["Realize Instances"].inputs[0]
    )
    # group_input_006.Material -> set_material.Material
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input.006"].outputs[9],
        ff_macadam_nodes_1.nodes["Set Material"].inputs[2]
    )
    # set_mesh_normal.Mesh -> set_material.Geometry
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Set Mesh Normal"].outputs[0],
        ff_macadam_nodes_1.nodes["Set Material"].inputs[0]
    )
    # set_material.Geometry -> group_output.Geometry
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Set Material"].outputs[0],
        ff_macadam_nodes_1.nodes["Group Output"].inputs[0]
    )
    # color_to_seed.Value -> random_value_007.Seed
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Color To Seed"].outputs[1],
        ff_macadam_nodes_1.nodes["Random Value.007"].inputs[3]
    )
    # random_value_007.Value -> store_colormask__injected_.Value
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Random Value.007"].outputs[0],
        ff_macadam_nodes_1.nodes["Store ColorMask (Injected)"].inputs[3]
    )
    # group_input_007.Rocks Color -> color_to_seed.Vector
    ff_macadam_nodes_1.links.new(
        ff_macadam_nodes_1.nodes["Group Input.007"].outputs[12],
        ff_macadam_nodes_1.nodes["Color To Seed"].inputs[0]
    )

    return ff_macadam_nodes_1


if __name__ == "__main__":
    # Maps node tree creation functions to the node tree 
    # name, such that we don't recreate node trees unnecessarily
    node_tree_names : dict[typing.Callable, str] = {}

    ff_macadam_nodes = ff_macadam_nodes_1_node_group(node_tree_names)
    node_tree_names[ff_macadam_nodes_1_node_group] = ff_macadam_nodes.name


# ============================================================================
#  FF BRIDGE 
# ============================================================================

from . import bridge

GROUP_NAME = "FF Macadam Nodes"
MAT_NAME = "M_Rocks"
MAT_HEX = "00FF00"


def create_node_group():
    return bridge.get_or_create_node_group(ff_macadam_nodes_1_node_group, GROUP_NAME)


def get_or_create_material():
    return bridge.get_or_create_colormask_material(MAT_NAME, MAT_HEX)