import bpy
import mathutils
import os
import typing


def ff_grass_nodes_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize FF Grass Nodes node group"""
    ff_grass_nodes_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="FF Grass Nodes")

    ff_grass_nodes_1.color_tag = 'GEOMETRY'
    ff_grass_nodes_1.description = ""
    ff_grass_nodes_1.default_group_node_width = 140
    ff_grass_nodes_1.is_modifier = True
    ff_grass_nodes_1.show_modifier_manage_panel = True

    # ff_grass_nodes_1 interface

    # Socket Geometry
    geometry_socket = ff_grass_nodes_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Panel Placement
    placement_panel = ff_grass_nodes_1.interface.new_panel("Placement")
    # Socket Seed
    seed_socket = ff_grass_nodes_1.interface.new_socket(name="Seed", in_out='INPUT', socket_type='NodeSocketInt', parent = placement_panel)
    seed_socket.default_value = 0
    seed_socket.min_value = -2147483648
    seed_socket.max_value = 2147483647
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'

    # Socket Count
    count_socket = ff_grass_nodes_1.interface.new_socket(name="Count", in_out='INPUT', socket_type='NodeSocketInt', parent = placement_panel)
    count_socket.default_value = 10
    count_socket.min_value = -2147483648
    count_socket.max_value = 2147483647
    count_socket.subtype = 'NONE'
    count_socket.attribute_domain = 'POINT'
    count_socket.default_input = 'VALUE'
    count_socket.structure_type = 'AUTO'

    # Socket Patch Radius
    patch_radius_socket = ff_grass_nodes_1.interface.new_socket(name="Patch Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent = placement_panel)
    patch_radius_socket.default_value = 0.12999999523162842
    patch_radius_socket.min_value = -3.4028234663852886e+38
    patch_radius_socket.max_value = 3.4028234663852886e+38
    patch_radius_socket.subtype = 'NONE'
    patch_radius_socket.attribute_domain = 'POINT'
    patch_radius_socket.default_input = 'VALUE'
    patch_radius_socket.structure_type = 'AUTO'

    # Socket Min Scale
    min_scale_socket = ff_grass_nodes_1.interface.new_socket(name="Min Scale", in_out='INPUT', socket_type='NodeSocketFloat', parent = placement_panel)
    min_scale_socket.default_value = 0.800000011920929
    min_scale_socket.min_value = -3.4028234663852886e+38
    min_scale_socket.max_value = 3.4028234663852886e+38
    min_scale_socket.subtype = 'NONE'
    min_scale_socket.attribute_domain = 'POINT'
    min_scale_socket.default_input = 'VALUE'
    min_scale_socket.structure_type = 'AUTO'

    # Socket Max Scale
    max_scale_socket = ff_grass_nodes_1.interface.new_socket(name="Max Scale", in_out='INPUT', socket_type='NodeSocketFloat', parent = placement_panel)
    max_scale_socket.default_value = 1.0
    max_scale_socket.min_value = -3.4028234663852886e+38
    max_scale_socket.max_value = 3.4028234663852886e+38
    max_scale_socket.subtype = 'NONE'
    max_scale_socket.attribute_domain = 'POINT'
    max_scale_socket.default_input = 'VALUE'
    max_scale_socket.structure_type = 'AUTO'


    # Panel Blade Shape
    blade_shape_panel = ff_grass_nodes_1.interface.new_panel("Blade Shape")
    # Socket Resolution X
    resolution_x_socket = ff_grass_nodes_1.interface.new_socket(name="Resolution X", in_out='INPUT', socket_type='NodeSocketInt', parent = blade_shape_panel)
    resolution_x_socket.default_value = 2
    resolution_x_socket.min_value = 2
    resolution_x_socket.max_value = 2147483647
    resolution_x_socket.subtype = 'NONE'
    resolution_x_socket.attribute_domain = 'POINT'
    resolution_x_socket.default_input = 'VALUE'
    resolution_x_socket.structure_type = 'AUTO'

    # Socket Resolution Y
    resolution_y_socket = ff_grass_nodes_1.interface.new_socket(name="Resolution Y", in_out='INPUT', socket_type='NodeSocketInt', parent = blade_shape_panel)
    resolution_y_socket.default_value = 2
    resolution_y_socket.min_value = 2
    resolution_y_socket.max_value = 2147483647
    resolution_y_socket.subtype = 'NONE'
    resolution_y_socket.attribute_domain = 'POINT'
    resolution_y_socket.default_input = 'VALUE'
    resolution_y_socket.structure_type = 'AUTO'

    # Socket Height
    height_socket = ff_grass_nodes_1.interface.new_socket(name="Height", in_out='INPUT', socket_type='NodeSocketFloat', parent = blade_shape_panel)
    height_socket.default_value = 1.0
    height_socket.min_value = -3.4028234663852886e+38
    height_socket.max_value = 3.4028234663852886e+38
    height_socket.subtype = 'NONE'
    height_socket.attribute_domain = 'POINT'
    height_socket.default_input = 'VALUE'
    height_socket.structure_type = 'AUTO'

    # Socket Width
    width_socket = ff_grass_nodes_1.interface.new_socket(name="Width", in_out='INPUT', socket_type='NodeSocketFloat', parent = blade_shape_panel)
    width_socket.default_value = 0.10000000149011612
    width_socket.min_value = -3.4028234663852886e+38
    width_socket.max_value = 3.4028234663852886e+38
    width_socket.subtype = 'NONE'
    width_socket.attribute_domain = 'POINT'
    width_socket.default_input = 'VALUE'
    width_socket.structure_type = 'AUTO'

    # Socket Bend Strength
    bend_strength_socket = ff_grass_nodes_1.interface.new_socket(name="Bend Strength", in_out='INPUT', socket_type='NodeSocketFloat', parent = blade_shape_panel)
    bend_strength_socket.default_value = 0.07999999821186066
    bend_strength_socket.min_value = -3.4028234663852886e+38
    bend_strength_socket.max_value = 3.4028234663852886e+38
    bend_strength_socket.subtype = 'NONE'
    bend_strength_socket.attribute_domain = 'POINT'
    bend_strength_socket.default_input = 'VALUE'
    bend_strength_socket.structure_type = 'AUTO'


    # Panel Detail
    detail_panel = ff_grass_nodes_1.interface.new_panel("Detail")
    # Socket Material
    material_socket = ff_grass_nodes_1.interface.new_socket(name="Material", in_out='INPUT', socket_type='NodeSocketMaterial', parent = detail_panel)
    material_socket.attribute_domain = 'POINT'
    material_socket.default_input = 'VALUE'
    material_socket.structure_type = 'AUTO'

    # Socket Smooth Shading
    smooth_shading_socket = ff_grass_nodes_1.interface.new_socket(name="Smooth Shading", in_out='INPUT', socket_type='NodeSocketBool', parent = detail_panel)
    smooth_shading_socket.default_value = True
    smooth_shading_socket.attribute_domain = 'POINT'
    smooth_shading_socket.default_input = 'VALUE'
    smooth_shading_socket.structure_type = 'AUTO'

    # Socket Stylized Normals
    stylized_normals_socket = ff_grass_nodes_1.interface.new_socket(name="Stylized Normals", in_out='INPUT', socket_type='NodeSocketFloat', parent = detail_panel)
    stylized_normals_socket.default_value = 0.8500000238418579
    stylized_normals_socket.min_value = 0.0
    stylized_normals_socket.max_value = 1.0
    stylized_normals_socket.subtype = 'NONE'
    stylized_normals_socket.attribute_domain = 'POINT'
    stylized_normals_socket.default_input = 'VALUE'
    stylized_normals_socket.structure_type = 'AUTO'

    # Socket Grass Color
    grass_color_socket = ff_grass_nodes_1.interface.new_socket(name="Grass Color", in_out='INPUT', socket_type='NodeSocketColor', parent = detail_panel)
    grass_color_socket.default_value = (0.0, 1.0, 0.0, 1.0)
    grass_color_socket.attribute_domain = 'POINT'
    grass_color_socket.default_input = 'VALUE'
    grass_color_socket.structure_type = 'AUTO'


    # Initialize ff_grass_nodes_1 nodes

    # Node Group Input
    group_input = ff_grass_nodes_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Output
    group_output = ff_grass_nodes_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Grid
    grid = ff_grass_nodes_1.nodes.new("GeometryNodeMeshGrid")
    grid.name = "Grid"
    grid.show_options = True
    # Size X
    grid.inputs[0].default_value = 2.0
    # Size Y
    grid.inputs[1].default_value = 2.0

    # Node Position
    position = ff_grass_nodes_1.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    position.show_options = True

    # Node Separate XYZ
    separate_xyz = ff_grass_nodes_1.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz.show_options = True

    # Node Map Range
    map_range = ff_grass_nodes_1.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.show_options = True
    map_range.clamp = True
    map_range.data_type = 'FLOAT'
    map_range.interpolation_type = 'LINEAR'
    # From Min
    map_range.inputs[1].default_value = -1.0
    # From Max
    map_range.inputs[2].default_value = 1.0
    # To Min
    map_range.inputs[3].default_value = 0.0
    # To Max
    map_range.inputs[4].default_value = 1.0

    # Node Math
    math = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'SUBTRACT'
    math.use_clamp = False
    # Value
    math.inputs[0].default_value = 1.0

    # Node Math.001
    math_001 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.show_options = True
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = False

    # Node Map Range.001
    map_range_001 = ff_grass_nodes_1.nodes.new("ShaderNodeMapRange")
    map_range_001.name = "Map Range.001"
    map_range_001.show_options = True
    map_range_001.clamp = True
    map_range_001.data_type = 'FLOAT'
    map_range_001.interpolation_type = 'LINEAR'
    # From Min
    map_range_001.inputs[1].default_value = -1.0
    # From Max
    map_range_001.inputs[2].default_value = 1.0
    # To Min
    map_range_001.inputs[3].default_value = 0.0
    # To Max
    map_range_001.inputs[4].default_value = 1.0

    # Node Combine XYZ
    combine_xyz = ff_grass_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz.show_options = True
    # Z
    combine_xyz.inputs[2].default_value = 0.0

    # Node Store Named Attribute
    store_named_attribute = ff_grass_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'FLOAT2'
    store_named_attribute.domain = 'CORNER'
    # Selection
    store_named_attribute.inputs[1].default_value = True
    # Name
    store_named_attribute.inputs[2].default_value = "UVMap"

    # Node Store Named Attribute.001
    store_named_attribute_001 = ff_grass_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.show_options = True
    store_named_attribute_001.data_type = 'FLOAT_COLOR'
    store_named_attribute_001.domain = 'CORNER'
    # Selection
    store_named_attribute_001.inputs[1].default_value = True
    # Name
    store_named_attribute_001.inputs[2].default_value = "ColorMask"

    # Node Math.002
    math_002 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.show_options = True
    math_002.operation = 'MULTIPLY'
    math_002.use_clamp = False

    # Node Math.003
    math_003 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.show_options = True
    math_003.operation = 'ADD'
    math_003.use_clamp = False
    # Value_001
    math_003.inputs[1].default_value = 9.999999747378752e-05

    # Node Math.004
    math_004 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.show_options = True
    math_004.operation = 'DIVIDE'
    math_004.use_clamp = False

    # Node Math.005
    math_005 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.show_options = True
    math_005.operation = 'MULTIPLY'
    math_005.use_clamp = False

    # Node Math.006
    math_006 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.show_options = True
    math_006.operation = 'SINE'
    math_006.use_clamp = False

    # Node Math.007
    math_007 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.show_options = True
    math_007.operation = 'COSINE'
    math_007.use_clamp = False

    # Node Math.008
    math_008 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.show_options = True
    math_008.operation = 'MULTIPLY'
    math_008.use_clamp = False

    # Node Math.009
    math_009 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.show_options = True
    math_009.operation = 'SUBTRACT'
    math_009.use_clamp = False
    # Value
    math_009.inputs[0].default_value = 1.0

    # Node Math.010
    math_010 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.show_options = True
    math_010.operation = 'MULTIPLY'
    math_010.use_clamp = False

    # Node Math.011
    math_011 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_011.name = "Math.011"
    math_011.show_options = True
    math_011.operation = 'MULTIPLY'
    math_011.use_clamp = False
    # Value_001
    math_011.inputs[1].default_value = -1.0

    # Node Combine XYZ.001
    combine_xyz_001 = ff_grass_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    combine_xyz_001.show_options = True

    # Node Set Position
    set_position = ff_grass_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.show_options = True
    # Selection
    set_position.inputs[1].default_value = True
    # Offset
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Merge by Distance
    merge_by_distance = ff_grass_nodes_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.show_options = True
    # Selection
    merge_by_distance.inputs[1].default_value = True
    # Mode
    merge_by_distance.inputs[2].default_value = 'All'
    # Distance
    merge_by_distance.inputs[3].default_value = 0.0010000000474974513

    # Node Set Shade Smooth
    set_shade_smooth = ff_grass_nodes_1.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.show_options = True
    set_shade_smooth.domain = 'FACE'
    # Selection
    set_shade_smooth.inputs[1].default_value = True

    # Node Points
    points = ff_grass_nodes_1.nodes.new("GeometryNodePoints")
    points.name = "Points"
    points.show_options = True
    # Position
    points.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Radius
    points.inputs[2].default_value = 0.10000000149011612

    # Node Math.012
    math_012 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_012.name = "Math.012"
    math_012.show_options = True
    math_012.operation = 'ADD'
    math_012.use_clamp = False
    # Value_001
    math_012.inputs[1].default_value = 1337.0

    # Node Math.013
    math_013 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_013.name = "Math.013"
    math_013.show_options = True
    math_013.operation = 'ADD'
    math_013.use_clamp = False
    # Value_001
    math_013.inputs[1].default_value = 99.0

    # Node Math.014
    math_014 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_014.name = "Math.014"
    math_014.show_options = True
    math_014.operation = 'ADD'
    math_014.use_clamp = False
    # Value_001
    math_014.inputs[1].default_value = 7.0

    # Node Random Value
    random_value = ff_grass_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value.name = "Random Value"
    random_value.show_options = True
    random_value.data_type = 'FLOAT'
    # Min
    random_value.inputs[0].default_value = 0.0
    # Max
    random_value.inputs[1].default_value = 6.2831854820251465
    # ID
    random_value.inputs[2].default_value = 0

    # Node Random Value.001
    random_value_001 = ff_grass_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value_001.name = "Random Value.001"
    random_value_001.show_options = True
    random_value_001.data_type = 'FLOAT'
    # Min
    random_value_001.inputs[0].default_value = 0.0
    # Max
    random_value_001.inputs[1].default_value = 1.0
    # ID
    random_value_001.inputs[2].default_value = 0

    # Node Math.015
    math_015 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_015.name = "Math.015"
    math_015.show_options = True
    math_015.operation = 'POWER'
    math_015.use_clamp = False
    # Value_001
    math_015.inputs[1].default_value = 0.5

    # Node Math.016
    math_016 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_016.name = "Math.016"
    math_016.show_options = True
    math_016.operation = 'MULTIPLY'
    math_016.use_clamp = False

    # Node Math.017
    math_017 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_017.name = "Math.017"
    math_017.show_options = True
    math_017.operation = 'COSINE'
    math_017.use_clamp = False

    # Node Math.018
    math_018 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_018.name = "Math.018"
    math_018.show_options = True
    math_018.operation = 'SINE'
    math_018.use_clamp = False

    # Node Math.019
    math_019 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_019.name = "Math.019"
    math_019.show_options = True
    math_019.operation = 'MULTIPLY'
    math_019.use_clamp = False

    # Node Math.020
    math_020 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_020.name = "Math.020"
    math_020.show_options = True
    math_020.operation = 'MULTIPLY'
    math_020.use_clamp = False

    # Node Combine XYZ.002
    combine_xyz_002 = ff_grass_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    combine_xyz_002.show_options = True
    # Z
    combine_xyz_002.inputs[2].default_value = 0.0

    # Node Set Position.001
    set_position_001 = ff_grass_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    set_position_001.show_options = True
    # Selection
    set_position_001.inputs[1].default_value = True
    # Offset
    set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Random Value.002
    random_value_002 = ff_grass_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value_002.name = "Random Value.002"
    random_value_002.show_options = True
    random_value_002.data_type = 'FLOAT_VECTOR'
    # Min
    random_value_002.inputs[0].default_value = (0.0, 0.0, -3.1415927410125732)
    # Max
    random_value_002.inputs[1].default_value = (0.0, 0.0, 3.1415927410125732)
    # ID
    random_value_002.inputs[2].default_value = 0

    # Node Random Value.003
    random_value_003 = ff_grass_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value_003.name = "Random Value.003"
    random_value_003.show_options = True
    random_value_003.data_type = 'FLOAT'
    # ID
    random_value_003.inputs[2].default_value = 0

    # Node Instance on Points
    instance_on_points = ff_grass_nodes_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    instance_on_points.show_options = True
    # Selection
    instance_on_points.inputs[1].default_value = True
    # Pick Instance
    instance_on_points.inputs[3].default_value = False
    # Instance Index
    instance_on_points.inputs[4].default_value = 0

    # Node Index
    index = ff_grass_nodes_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Store Named Attribute.002
    store_named_attribute_002 = ff_grass_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_002.name = "Store Named Attribute.002"
    store_named_attribute_002.show_options = True
    store_named_attribute_002.data_type = 'INT'
    store_named_attribute_002.domain = 'INSTANCE'
    # Selection
    store_named_attribute_002.inputs[1].default_value = True
    # Name
    store_named_attribute_002.inputs[2].default_value = "fractal_id"

    # Node Realize Instances
    realize_instances = ff_grass_nodes_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    realize_instances.show_options = True
    realize_instances.realize_to_point_domain = False
    # Selection
    realize_instances.inputs[1].default_value = True
    # Realize All
    realize_instances.inputs[2].default_value = True
    # Depth
    realize_instances.inputs[3].default_value = 0

    # Node Set Material
    set_material = ff_grass_nodes_1.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.show_options = True
    # Selection
    set_material.inputs[1].default_value = True

    # Node Normal
    normal = ff_grass_nodes_1.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"
    normal.show_options = True
    normal.legacy_corner_normals = False

    # Node Convex Hull
    convex_hull = ff_grass_nodes_1.nodes.new("GeometryNodeConvexHull")
    convex_hull.name = "Convex Hull"
    convex_hull.show_options = True

    # Node Set Shade Smooth.001
    set_shade_smooth_001 = ff_grass_nodes_1.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth_001.name = "Set Shade Smooth.001"
    set_shade_smooth_001.show_options = True
    set_shade_smooth_001.domain = 'FACE'
    # Selection
    set_shade_smooth_001.inputs[1].default_value = True
    # Shade Smooth
    set_shade_smooth_001.inputs[2].default_value = True

    # Node Sample Nearest Surface
    sample_nearest_surface = ff_grass_nodes_1.nodes.new("GeometryNodeSampleNearestSurface")
    sample_nearest_surface.name = "Sample Nearest Surface"
    sample_nearest_surface.show_options = True
    sample_nearest_surface.data_type = 'FLOAT_VECTOR'
    # Group ID
    sample_nearest_surface.inputs[2].default_value = 0
    # Sample Position
    sample_nearest_surface.inputs[3].default_value = (0.0, 0.0, 0.0)
    # Sample Group ID
    sample_nearest_surface.inputs[4].default_value = 0

    # Node Math.021
    math_021 = ff_grass_nodes_1.nodes.new("ShaderNodeMath")
    math_021.name = "Math.021"
    math_021.show_options = True
    math_021.operation = 'SUBTRACT'
    math_021.use_clamp = False
    # Value
    math_021.inputs[0].default_value = 1.0

    # Node Vector Math
    vector_math = ff_grass_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.show_options = True
    vector_math.operation = 'SCALE'

    # Node Vector Math.001
    vector_math_001 = ff_grass_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.show_options = True
    vector_math_001.operation = 'SCALE'

    # Node Vector Math.002
    vector_math_002 = ff_grass_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.show_options = True
    vector_math_002.operation = 'ADD'

    # Node Vector Math.003
    vector_math_003 = ff_grass_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.show_options = True
    vector_math_003.operation = 'NORMALIZE'

    # Node Set Mesh Normal
    set_mesh_normal = ff_grass_nodes_1.nodes.new("GeometryNodeSetMeshNormal")
    set_mesh_normal.name = "Set Mesh Normal"
    set_mesh_normal.show_options = True
    set_mesh_normal.domain = 'CORNER'
    set_mesh_normal.mode = 'FREE'

    # Node Frame.001
    frame_001 = ff_grass_nodes_1.nodes.new("NodeFrame")
    frame_001.label = "Base Logic"
    frame_001.name = "Frame.001"
    frame_001.use_custom_color = True
    frame_001.color = (0.20000000298023224, 0.30000001192092896, 0.20000000298023224)
    frame_001.show_options = True
    frame_001.label_size = 20
    frame_001.shrink = True

    # Node Frame.002
    frame_002 = ff_grass_nodes_1.nodes.new("NodeFrame")
    frame_002.label = "UV & ColorMask"
    frame_002.name = "Frame.002"
    frame_002.use_custom_color = True
    frame_002.color = (0.30000001192092896, 0.30000001192092896, 0.20000000298023224)
    frame_002.show_options = True
    frame_002.label_size = 20
    frame_002.shrink = True

    # Node Frame.003
    frame_003 = ff_grass_nodes_1.nodes.new("NodeFrame")
    frame_003.label = "Zero-Stretch Bend Math"
    frame_003.name = "Frame.003"
    frame_003.use_custom_color = True
    frame_003.color = (0.20000000298023224, 0.20000000298023224, 0.30000001192092896)
    frame_003.show_options = True
    frame_003.label_size = 20
    frame_003.shrink = True

    # Node Frame.004
    frame_004 = ff_grass_nodes_1.nodes.new("NodeFrame")
    frame_004.label = "Distribution Logic"
    frame_004.name = "Frame.004"
    frame_004.use_custom_color = True
    frame_004.color = (0.30000001192092896, 0.20000000298023224, 0.20000000298023224)
    frame_004.show_options = True
    frame_004.label_size = 20
    frame_004.shrink = True

    # Node Frame.005
    frame_005 = ff_grass_nodes_1.nodes.new("NodeFrame")
    frame_005.label = "Instancing & Stylized Normals"
    frame_005.name = "Frame.005"
    frame_005.use_custom_color = True
    frame_005.color = (0.4000000059604645, 0.20000000298023224, 0.20000000298023224)
    frame_005.show_options = True
    frame_005.label_size = 20
    frame_005.shrink = True

    # Node Group Input.001
    group_input_001 = ff_grass_nodes_1.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.show_options = True

    # Node Group Input.002
    group_input_002 = ff_grass_nodes_1.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.show_options = True

    # Node Group Input.003
    group_input_003 = ff_grass_nodes_1.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.show_options = True

    # Node Group Input.004
    group_input_004 = ff_grass_nodes_1.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.show_options = True

    # Node Group Input.005
    group_input_005 = ff_grass_nodes_1.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.show_options = True

    # Node Reroute
    reroute = ff_grass_nodes_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketGeometry"
    # Node Reroute.001
    reroute_001 = ff_grass_nodes_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketVector"
    # Node Group Input.006
    group_input_006 = ff_grass_nodes_1.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.show_options = True

    # Node Normal.001
    normal_001 = ff_grass_nodes_1.nodes.new("GeometryNodeInputNormal")
    normal_001.name = "Normal.001"
    normal_001.show_options = True
    normal_001.legacy_corner_normals = False

    # Node Group Input.007
    group_input_007 = ff_grass_nodes_1.nodes.new("NodeGroupInput")
    group_input_007.name = "Group Input.007"
    group_input_007.show_options = True

    # Set parents
    ff_grass_nodes_1.nodes["Group Input"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Grid"].parent = ff_grass_nodes_1.nodes["Frame.001"]
    ff_grass_nodes_1.nodes["Position"].parent = ff_grass_nodes_1.nodes["Frame.001"]
    ff_grass_nodes_1.nodes["Separate XYZ"].parent = ff_grass_nodes_1.nodes["Frame.001"]
    ff_grass_nodes_1.nodes["Map Range"].parent = ff_grass_nodes_1.nodes["Frame.001"]
    ff_grass_nodes_1.nodes["Math"].parent = ff_grass_nodes_1.nodes["Frame.001"]
    ff_grass_nodes_1.nodes["Math.001"].parent = ff_grass_nodes_1.nodes["Frame.001"]
    ff_grass_nodes_1.nodes["Map Range.001"].parent = ff_grass_nodes_1.nodes["Frame.002"]
    ff_grass_nodes_1.nodes["Combine XYZ"].parent = ff_grass_nodes_1.nodes["Frame.002"]
    ff_grass_nodes_1.nodes["Store Named Attribute"].parent = ff_grass_nodes_1.nodes["Frame.002"]
    ff_grass_nodes_1.nodes["Store Named Attribute.001"].parent = ff_grass_nodes_1.nodes["Frame.002"]
    ff_grass_nodes_1.nodes["Math.002"].parent = ff_grass_nodes_1.nodes["Frame.003"]
    ff_grass_nodes_1.nodes["Math.003"].parent = ff_grass_nodes_1.nodes["Frame.003"]
    ff_grass_nodes_1.nodes["Math.004"].parent = ff_grass_nodes_1.nodes["Frame.003"]
    ff_grass_nodes_1.nodes["Math.005"].parent = ff_grass_nodes_1.nodes["Frame.003"]
    ff_grass_nodes_1.nodes["Math.006"].parent = ff_grass_nodes_1.nodes["Frame.003"]
    ff_grass_nodes_1.nodes["Math.007"].parent = ff_grass_nodes_1.nodes["Frame.003"]
    ff_grass_nodes_1.nodes["Math.008"].parent = ff_grass_nodes_1.nodes["Frame.003"]
    ff_grass_nodes_1.nodes["Math.009"].parent = ff_grass_nodes_1.nodes["Frame.003"]
    ff_grass_nodes_1.nodes["Math.010"].parent = ff_grass_nodes_1.nodes["Frame.003"]
    ff_grass_nodes_1.nodes["Math.011"].parent = ff_grass_nodes_1.nodes["Frame.003"]
    ff_grass_nodes_1.nodes["Combine XYZ.001"].parent = ff_grass_nodes_1.nodes["Frame.003"]
    ff_grass_nodes_1.nodes["Set Position"].parent = ff_grass_nodes_1.nodes["Frame.003"]
    ff_grass_nodes_1.nodes["Merge by Distance"].parent = ff_grass_nodes_1.nodes["Frame.003"]
    ff_grass_nodes_1.nodes["Set Shade Smooth"].parent = ff_grass_nodes_1.nodes["Frame.003"]
    ff_grass_nodes_1.nodes["Points"].parent = ff_grass_nodes_1.nodes["Frame.004"]
    ff_grass_nodes_1.nodes["Math.012"].parent = ff_grass_nodes_1.nodes["Frame.004"]
    ff_grass_nodes_1.nodes["Math.013"].parent = ff_grass_nodes_1.nodes["Frame.004"]
    ff_grass_nodes_1.nodes["Math.014"].parent = ff_grass_nodes_1.nodes["Frame.004"]
    ff_grass_nodes_1.nodes["Random Value"].parent = ff_grass_nodes_1.nodes["Frame.004"]
    ff_grass_nodes_1.nodes["Random Value.001"].parent = ff_grass_nodes_1.nodes["Frame.004"]
    ff_grass_nodes_1.nodes["Math.015"].parent = ff_grass_nodes_1.nodes["Frame.004"]
    ff_grass_nodes_1.nodes["Math.016"].parent = ff_grass_nodes_1.nodes["Frame.004"]
    ff_grass_nodes_1.nodes["Math.017"].parent = ff_grass_nodes_1.nodes["Frame.004"]
    ff_grass_nodes_1.nodes["Math.018"].parent = ff_grass_nodes_1.nodes["Frame.004"]
    ff_grass_nodes_1.nodes["Math.019"].parent = ff_grass_nodes_1.nodes["Frame.004"]
    ff_grass_nodes_1.nodes["Math.020"].parent = ff_grass_nodes_1.nodes["Frame.004"]
    ff_grass_nodes_1.nodes["Combine XYZ.002"].parent = ff_grass_nodes_1.nodes["Frame.004"]
    ff_grass_nodes_1.nodes["Set Position.001"].parent = ff_grass_nodes_1.nodes["Frame.004"]
    ff_grass_nodes_1.nodes["Random Value.002"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Random Value.003"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Instance on Points"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Index"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Store Named Attribute.002"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Realize Instances"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Set Material"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Normal"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Convex Hull"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Set Shade Smooth.001"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Sample Nearest Surface"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Math.021"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Vector Math"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Vector Math.001"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Vector Math.002"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Vector Math.003"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Set Mesh Normal"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Group Input.001"].parent = ff_grass_nodes_1.nodes["Frame.002"]
    ff_grass_nodes_1.nodes["Group Input.002"].parent = ff_grass_nodes_1.nodes["Frame.001"]
    ff_grass_nodes_1.nodes["Group Input.003"].parent = ff_grass_nodes_1.nodes["Frame.004"]
    ff_grass_nodes_1.nodes["Group Input.004"].parent = ff_grass_nodes_1.nodes["Frame.003"]
    ff_grass_nodes_1.nodes["Group Input.005"].parent = ff_grass_nodes_1.nodes["Frame.003"]
    ff_grass_nodes_1.nodes["Reroute"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Reroute.001"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Group Input.006"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Normal.001"].parent = ff_grass_nodes_1.nodes["Frame.005"]
    ff_grass_nodes_1.nodes["Group Input.007"].parent = ff_grass_nodes_1.nodes["Frame.005"]

    # Set locations
    ff_grass_nodes_1.nodes["Group Input"].location = (280.9466552734375, -770.9505615234375)
    ff_grass_nodes_1.nodes["Group Output"].location = (898.1419067382812, 8.915528297424316)
    ff_grass_nodes_1.nodes["Grid"].location = (202.91357421875, -55.0946044921875)
    ff_grass_nodes_1.nodes["Position"].location = (30.899658203125, -454.57330322265625)
    ff_grass_nodes_1.nodes["Separate XYZ"].location = (192.352783203125, -386.62213134765625)
    ff_grass_nodes_1.nodes["Map Range"].location = (390.05908203125, -111.73007202148438)
    ff_grass_nodes_1.nodes["Math"].location = (592.95703125, -170.31048583984375)
    ff_grass_nodes_1.nodes["Math.001"].location = (588.777099609375, -391.3256530761719)
    ff_grass_nodes_1.nodes["Map Range.001"].location = (29.615478515625, -199.87237548828125)
    ff_grass_nodes_1.nodes["Combine XYZ"].location = (206.907470703125, -96.58447265625)
    ff_grass_nodes_1.nodes["Store Named Attribute"].location = (379.7783203125, -37.0552978515625)
    ff_grass_nodes_1.nodes["Store Named Attribute.001"].location = (559.7685546875, -36.44317626953125)
    ff_grass_nodes_1.nodes["Math.002"].location = (1126.65087890625, -116.22754669189453)
    ff_grass_nodes_1.nodes["Math.003"].location = (224.67919921875, -603.8206787109375)
    ff_grass_nodes_1.nodes["Math.004"].location = (603.5185546875, -505.5360107421875)
    ff_grass_nodes_1.nodes["Math.005"].location = (403.5751953125, -791.1155395507812)
    ff_grass_nodes_1.nodes["Math.006"].location = (925.9736328125, -714.4425048828125)
    ff_grass_nodes_1.nodes["Math.007"].location = (611.84912109375, -688.2737426757812)
    ff_grass_nodes_1.nodes["Math.008"].location = (1120.31787109375, -428.7880554199219)
    ff_grass_nodes_1.nodes["Math.009"].location = (770.51171875, -591.6185302734375)
    ff_grass_nodes_1.nodes["Math.010"].location = (956.170166015625, -342.7718811035156)
    ff_grass_nodes_1.nodes["Math.011"].location = (1124.47119140625, -270.73236083984375)
    ff_grass_nodes_1.nodes["Combine XYZ.001"].location = (1308.03857421875, -111.06278228759766)
    ff_grass_nodes_1.nodes["Set Position"].location = (1480.95751953125, -68.21485900878906)
    ff_grass_nodes_1.nodes["Merge by Distance"].location = (1646.255859375, -70.15734100341797)
    ff_grass_nodes_1.nodes["Set Shade Smooth"].location = (1811.9266357421875, -43.968116760253906)
    ff_grass_nodes_1.nodes["Points"].location = (211.272216796875, -366.2401123046875)
    ff_grass_nodes_1.nodes["Math.012"].location = (212.55615234375, -711.7274169921875)
    ff_grass_nodes_1.nodes["Math.013"].location = (213.638916015625, -555.6929931640625)
    ff_grass_nodes_1.nodes["Math.014"].location = (216.56591796875, -36.1934814453125)
    ff_grass_nodes_1.nodes["Random Value"].location = (214.4169921875, -191.9842529296875)
    ff_grass_nodes_1.nodes["Random Value.001"].location = (374.098388671875, -595.7347412109375)
    ff_grass_nodes_1.nodes["Math.015"].location = (538.725341796875, -521.9844970703125)
    ff_grass_nodes_1.nodes["Math.016"].location = (727.45458984375, -328.5389404296875)
    ff_grass_nodes_1.nodes["Math.017"].location = (379.324951171875, -119.3431396484375)
    ff_grass_nodes_1.nodes["Math.018"].location = (377.119873046875, -251.7342529296875)
    ff_grass_nodes_1.nodes["Math.019"].location = (905.505126953125, -44.9022216796875)
    ff_grass_nodes_1.nodes["Math.020"].location = (902.2314453125, -182.277099609375)
    ff_grass_nodes_1.nodes["Combine XYZ.002"].location = (1077.597900390625, -83.2679443359375)
    ff_grass_nodes_1.nodes["Set Position.001"].location = (1281.4287109375, -365.9395751953125)
    ff_grass_nodes_1.nodes["Random Value.002"].location = (29.8043212890625, -1397.96826171875)
    ff_grass_nodes_1.nodes["Random Value.003"].location = (500.4110107421875, -1004.9638671875)
    ff_grass_nodes_1.nodes["Instance on Points"].location = (821.3866577148438, -96.9264907836914)
    ff_grass_nodes_1.nodes["Index"].location = (818.0962524414062, -35.58280944824219)
    ff_grass_nodes_1.nodes["Store Named Attribute.002"].location = (1009.8995361328125, -45.459720611572266)
    ff_grass_nodes_1.nodes["Realize Instances"].location = (1175.143798828125, -96.2083511352539)
    ff_grass_nodes_1.nodes["Set Material"].location = (2268.50927734375, -95.45822143554688)
    ff_grass_nodes_1.nodes["Normal"].location = (1170.4444580078125, -470.6741027832031)
    ff_grass_nodes_1.nodes["Convex Hull"].location = (1170.7891845703125, -243.670166015625)
    ff_grass_nodes_1.nodes["Set Shade Smooth.001"].location = (1170.2528076171875, -344.8916015625)
    ff_grass_nodes_1.nodes["Sample Nearest Surface"].location = (1431.2354736328125, -301.3208312988281)
    ff_grass_nodes_1.nodes["Math.021"].location = (1438.890869140625, -600.01123046875)
    ff_grass_nodes_1.nodes["Vector Math"].location = (1603.6396484375, -474.6690979003906)
    ff_grass_nodes_1.nodes["Vector Math.001"].location = (1620.1611328125, -248.34286499023438)
    ff_grass_nodes_1.nodes["Vector Math.002"].location = (1783.8956298828125, -177.92959594726562)
    ff_grass_nodes_1.nodes["Vector Math.003"].location = (1947.9764404296875, -128.51385498046875)
    ff_grass_nodes_1.nodes["Set Mesh Normal"].location = (2106.34228515625, -43.78035354614258)
    ff_grass_nodes_1.nodes["Frame.001"].location = (-3742.0, 593.0)
    ff_grass_nodes_1.nodes["Frame.002"].location = (-2953.0, 622.0)
    ff_grass_nodes_1.nodes["Frame.003"].location = (-3562.0, 5.0)
    ff_grass_nodes_1.nodes["Frame.004"].location = (-3034.0, -976.0)
    ff_grass_nodes_1.nodes["Frame.005"].location = (-1556.0, 104.0)
    ff_grass_nodes_1.nodes["Group Input.001"].location = (203.398681640625, -222.52621459960938)
    ff_grass_nodes_1.nodes["Group Input.002"].location = (29.997314453125, -36.22076416015625)
    ff_grass_nodes_1.nodes["Group Input.003"].location = (30.270263671875, -369.4742431640625)
    ff_grass_nodes_1.nodes["Group Input.004"].location = (1649.888916015625, -194.8697509765625)
    ff_grass_nodes_1.nodes["Group Input.005"].location = (29.5458984375, -36.18121337890625)
    ff_grass_nodes_1.nodes["Reroute"].location = (139.629150390625, -159.7470703125)
    ff_grass_nodes_1.nodes["Reroute.001"].location = (297.5174560546875, -271.53076171875)
    ff_grass_nodes_1.nodes["Group Input.006"].location = (1012.58935546875, -416.8717956542969)
    ff_grass_nodes_1.nodes["Normal.001"].location = (1433.072509765625, -522.8953857421875)
    ff_grass_nodes_1.nodes["Group Input.007"].location = (2104.390869140625, -172.4481201171875)

    # Set dimensions
    ff_grass_nodes_1.nodes["Group Input"].width  = 140.0
    ff_grass_nodes_1.nodes["Group Input"].height = 100.0

    ff_grass_nodes_1.nodes["Group Output"].width  = 140.0
    ff_grass_nodes_1.nodes["Group Output"].height = 100.0

    ff_grass_nodes_1.nodes["Grid"].width  = 140.0
    ff_grass_nodes_1.nodes["Grid"].height = 100.0

    ff_grass_nodes_1.nodes["Position"].width  = 140.0
    ff_grass_nodes_1.nodes["Position"].height = 100.0

    ff_grass_nodes_1.nodes["Separate XYZ"].width  = 140.0
    ff_grass_nodes_1.nodes["Separate XYZ"].height = 100.0

    ff_grass_nodes_1.nodes["Map Range"].width  = 140.0
    ff_grass_nodes_1.nodes["Map Range"].height = 100.0

    ff_grass_nodes_1.nodes["Math"].width  = 140.0
    ff_grass_nodes_1.nodes["Math"].height = 100.0

    ff_grass_nodes_1.nodes["Math.001"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.001"].height = 100.0

    ff_grass_nodes_1.nodes["Map Range.001"].width  = 140.0
    ff_grass_nodes_1.nodes["Map Range.001"].height = 100.0

    ff_grass_nodes_1.nodes["Combine XYZ"].width  = 140.0
    ff_grass_nodes_1.nodes["Combine XYZ"].height = 100.0

    ff_grass_nodes_1.nodes["Store Named Attribute"].width  = 140.0
    ff_grass_nodes_1.nodes["Store Named Attribute"].height = 100.0

    ff_grass_nodes_1.nodes["Store Named Attribute.001"].width  = 140.0
    ff_grass_nodes_1.nodes["Store Named Attribute.001"].height = 100.0

    ff_grass_nodes_1.nodes["Math.002"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.002"].height = 100.0

    ff_grass_nodes_1.nodes["Math.003"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.003"].height = 100.0

    ff_grass_nodes_1.nodes["Math.004"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.004"].height = 100.0

    ff_grass_nodes_1.nodes["Math.005"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.005"].height = 100.0

    ff_grass_nodes_1.nodes["Math.006"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.006"].height = 100.0

    ff_grass_nodes_1.nodes["Math.007"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.007"].height = 100.0

    ff_grass_nodes_1.nodes["Math.008"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.008"].height = 100.0

    ff_grass_nodes_1.nodes["Math.009"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.009"].height = 100.0

    ff_grass_nodes_1.nodes["Math.010"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.010"].height = 100.0

    ff_grass_nodes_1.nodes["Math.011"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.011"].height = 100.0

    ff_grass_nodes_1.nodes["Combine XYZ.001"].width  = 140.0
    ff_grass_nodes_1.nodes["Combine XYZ.001"].height = 100.0

    ff_grass_nodes_1.nodes["Set Position"].width  = 140.0
    ff_grass_nodes_1.nodes["Set Position"].height = 100.0

    ff_grass_nodes_1.nodes["Merge by Distance"].width  = 140.0
    ff_grass_nodes_1.nodes["Merge by Distance"].height = 100.0

    ff_grass_nodes_1.nodes["Set Shade Smooth"].width  = 140.0
    ff_grass_nodes_1.nodes["Set Shade Smooth"].height = 100.0

    ff_grass_nodes_1.nodes["Points"].width  = 140.0
    ff_grass_nodes_1.nodes["Points"].height = 100.0

    ff_grass_nodes_1.nodes["Math.012"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.012"].height = 100.0

    ff_grass_nodes_1.nodes["Math.013"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.013"].height = 100.0

    ff_grass_nodes_1.nodes["Math.014"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.014"].height = 100.0

    ff_grass_nodes_1.nodes["Random Value"].width  = 140.0
    ff_grass_nodes_1.nodes["Random Value"].height = 100.0

    ff_grass_nodes_1.nodes["Random Value.001"].width  = 140.0
    ff_grass_nodes_1.nodes["Random Value.001"].height = 100.0

    ff_grass_nodes_1.nodes["Math.015"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.015"].height = 100.0

    ff_grass_nodes_1.nodes["Math.016"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.016"].height = 100.0

    ff_grass_nodes_1.nodes["Math.017"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.017"].height = 100.0

    ff_grass_nodes_1.nodes["Math.018"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.018"].height = 100.0

    ff_grass_nodes_1.nodes["Math.019"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.019"].height = 100.0

    ff_grass_nodes_1.nodes["Math.020"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.020"].height = 100.0

    ff_grass_nodes_1.nodes["Combine XYZ.002"].width  = 140.0
    ff_grass_nodes_1.nodes["Combine XYZ.002"].height = 100.0

    ff_grass_nodes_1.nodes["Set Position.001"].width  = 140.0
    ff_grass_nodes_1.nodes["Set Position.001"].height = 100.0

    ff_grass_nodes_1.nodes["Random Value.002"].width  = 140.0
    ff_grass_nodes_1.nodes["Random Value.002"].height = 100.0

    ff_grass_nodes_1.nodes["Random Value.003"].width  = 140.0
    ff_grass_nodes_1.nodes["Random Value.003"].height = 100.0

    ff_grass_nodes_1.nodes["Instance on Points"].width  = 140.0
    ff_grass_nodes_1.nodes["Instance on Points"].height = 100.0

    ff_grass_nodes_1.nodes["Index"].width  = 140.0
    ff_grass_nodes_1.nodes["Index"].height = 100.0

    ff_grass_nodes_1.nodes["Store Named Attribute.002"].width  = 140.0
    ff_grass_nodes_1.nodes["Store Named Attribute.002"].height = 100.0

    ff_grass_nodes_1.nodes["Realize Instances"].width  = 140.0
    ff_grass_nodes_1.nodes["Realize Instances"].height = 100.0

    ff_grass_nodes_1.nodes["Set Material"].width  = 140.0
    ff_grass_nodes_1.nodes["Set Material"].height = 100.0

    ff_grass_nodes_1.nodes["Normal"].width  = 140.0
    ff_grass_nodes_1.nodes["Normal"].height = 100.0

    ff_grass_nodes_1.nodes["Convex Hull"].width  = 140.0
    ff_grass_nodes_1.nodes["Convex Hull"].height = 100.0

    ff_grass_nodes_1.nodes["Set Shade Smooth.001"].width  = 140.0
    ff_grass_nodes_1.nodes["Set Shade Smooth.001"].height = 100.0

    ff_grass_nodes_1.nodes["Sample Nearest Surface"].width  = 150.0
    ff_grass_nodes_1.nodes["Sample Nearest Surface"].height = 100.0

    ff_grass_nodes_1.nodes["Math.021"].width  = 140.0
    ff_grass_nodes_1.nodes["Math.021"].height = 100.0

    ff_grass_nodes_1.nodes["Vector Math"].width  = 140.0
    ff_grass_nodes_1.nodes["Vector Math"].height = 100.0

    ff_grass_nodes_1.nodes["Vector Math.001"].width  = 140.0
    ff_grass_nodes_1.nodes["Vector Math.001"].height = 100.0

    ff_grass_nodes_1.nodes["Vector Math.002"].width  = 140.0
    ff_grass_nodes_1.nodes["Vector Math.002"].height = 100.0

    ff_grass_nodes_1.nodes["Vector Math.003"].width  = 140.0
    ff_grass_nodes_1.nodes["Vector Math.003"].height = 100.0

    ff_grass_nodes_1.nodes["Set Mesh Normal"].width  = 140.0
    ff_grass_nodes_1.nodes["Set Mesh Normal"].height = 100.0

    ff_grass_nodes_1.nodes["Frame.001"].width  = 763.0
    ff_grass_nodes_1.nodes["Frame.001"].height = 569.0

    ff_grass_nodes_1.nodes["Frame.002"].width  = 730.0
    ff_grass_nodes_1.nodes["Frame.002"].height = 611.0

    ff_grass_nodes_1.nodes["Frame.003"].width  = 1982.0
    ff_grass_nodes_1.nodes["Frame.003"].height = 969.0

    ff_grass_nodes_1.nodes["Frame.004"].width  = 1451.0
    ff_grass_nodes_1.nodes["Frame.004"].height = 890.0

    ff_grass_nodes_1.nodes["Frame.005"].width  = 2439.0
    ff_grass_nodes_1.nodes["Frame.005"].height = 1717.0

    ff_grass_nodes_1.nodes["Group Input.001"].width  = 140.0
    ff_grass_nodes_1.nodes["Group Input.001"].height = 100.0

    ff_grass_nodes_1.nodes["Group Input.002"].width  = 140.0
    ff_grass_nodes_1.nodes["Group Input.002"].height = 100.0

    ff_grass_nodes_1.nodes["Group Input.003"].width  = 140.0
    ff_grass_nodes_1.nodes["Group Input.003"].height = 100.0

    ff_grass_nodes_1.nodes["Group Input.004"].width  = 140.0
    ff_grass_nodes_1.nodes["Group Input.004"].height = 100.0

    ff_grass_nodes_1.nodes["Group Input.005"].width  = 140.0
    ff_grass_nodes_1.nodes["Group Input.005"].height = 100.0

    ff_grass_nodes_1.nodes["Reroute"].width  = 10.0
    ff_grass_nodes_1.nodes["Reroute"].height = 100.0

    ff_grass_nodes_1.nodes["Reroute.001"].width  = 10.0
    ff_grass_nodes_1.nodes["Reroute.001"].height = 100.0

    ff_grass_nodes_1.nodes["Group Input.006"].width  = 140.0
    ff_grass_nodes_1.nodes["Group Input.006"].height = 100.0

    ff_grass_nodes_1.nodes["Normal.001"].width  = 140.0
    ff_grass_nodes_1.nodes["Normal.001"].height = 100.0

    ff_grass_nodes_1.nodes["Group Input.007"].width  = 140.0
    ff_grass_nodes_1.nodes["Group Input.007"].height = 100.0


    # Initialize ff_grass_nodes_1 links

    # position.Position -> separate_xyz.Vector
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Position"].outputs[0],
        ff_grass_nodes_1.nodes["Separate XYZ"].inputs[0]
    )
    # separate_xyz.Y -> map_range.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Separate XYZ"].outputs[1],
        ff_grass_nodes_1.nodes["Map Range"].inputs[0]
    )
    # map_range.Result -> math.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Map Range"].outputs[0],
        ff_grass_nodes_1.nodes["Math"].inputs[1]
    )
    # separate_xyz.X -> math_001.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Separate XYZ"].outputs[0],
        ff_grass_nodes_1.nodes["Math.001"].inputs[0]
    )
    # math.Value -> math_001.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math"].outputs[0],
        ff_grass_nodes_1.nodes["Math.001"].inputs[1]
    )
    # math_001.Value -> map_range_001.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.001"].outputs[0],
        ff_grass_nodes_1.nodes["Map Range.001"].inputs[0]
    )
    # map_range_001.Result -> combine_xyz.X
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Map Range.001"].outputs[0],
        ff_grass_nodes_1.nodes["Combine XYZ"].inputs[0]
    )
    # map_range.Result -> combine_xyz.Y
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Map Range"].outputs[0],
        ff_grass_nodes_1.nodes["Combine XYZ"].inputs[1]
    )
    # grid.Mesh -> store_named_attribute.Geometry
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Grid"].outputs[0],
        ff_grass_nodes_1.nodes["Store Named Attribute"].inputs[0]
    )
    # combine_xyz.Vector -> store_named_attribute.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Combine XYZ"].outputs[0],
        ff_grass_nodes_1.nodes["Store Named Attribute"].inputs[3]
    )
    # store_named_attribute.Geometry -> store_named_attribute_001.Geometry
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Store Named Attribute"].outputs[0],
        ff_grass_nodes_1.nodes["Store Named Attribute.001"].inputs[0]
    )
    # math_003.Value -> math_004.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.003"].outputs[0],
        ff_grass_nodes_1.nodes["Math.004"].inputs[1]
    )
    # math_003.Value -> math_005.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.003"].outputs[0],
        ff_grass_nodes_1.nodes["Math.005"].inputs[1]
    )
    # math_005.Value -> math_006.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.005"].outputs[0],
        ff_grass_nodes_1.nodes["Math.006"].inputs[0]
    )
    # math_005.Value -> math_007.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.005"].outputs[0],
        ff_grass_nodes_1.nodes["Math.007"].inputs[0]
    )
    # math_004.Value -> math_008.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.004"].outputs[0],
        ff_grass_nodes_1.nodes["Math.008"].inputs[0]
    )
    # math_006.Value -> math_008.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.006"].outputs[0],
        ff_grass_nodes_1.nodes["Math.008"].inputs[1]
    )
    # math_007.Value -> math_009.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.007"].outputs[0],
        ff_grass_nodes_1.nodes["Math.009"].inputs[1]
    )
    # math_004.Value -> math_010.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.004"].outputs[0],
        ff_grass_nodes_1.nodes["Math.010"].inputs[0]
    )
    # math_009.Value -> math_010.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.009"].outputs[0],
        ff_grass_nodes_1.nodes["Math.010"].inputs[1]
    )
    # math_010.Value -> math_011.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.010"].outputs[0],
        ff_grass_nodes_1.nodes["Math.011"].inputs[0]
    )
    # math_002.Value -> combine_xyz_001.X
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.002"].outputs[0],
        ff_grass_nodes_1.nodes["Combine XYZ.001"].inputs[0]
    )
    # math_011.Value -> combine_xyz_001.Y
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.011"].outputs[0],
        ff_grass_nodes_1.nodes["Combine XYZ.001"].inputs[1]
    )
    # math_008.Value -> combine_xyz_001.Z
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.008"].outputs[0],
        ff_grass_nodes_1.nodes["Combine XYZ.001"].inputs[2]
    )
    # store_named_attribute_001.Geometry -> set_position.Geometry
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Store Named Attribute.001"].outputs[0],
        ff_grass_nodes_1.nodes["Set Position"].inputs[0]
    )
    # combine_xyz_001.Vector -> set_position.Position
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Combine XYZ.001"].outputs[0],
        ff_grass_nodes_1.nodes["Set Position"].inputs[2]
    )
    # set_position.Geometry -> merge_by_distance.Geometry
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Set Position"].outputs[0],
        ff_grass_nodes_1.nodes["Merge by Distance"].inputs[0]
    )
    # merge_by_distance.Geometry -> set_shade_smooth.Mesh
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Merge by Distance"].outputs[0],
        ff_grass_nodes_1.nodes["Set Shade Smooth"].inputs[0]
    )
    # math_012.Value -> random_value_001.Seed
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.012"].outputs[0],
        ff_grass_nodes_1.nodes["Random Value.001"].inputs[3]
    )
    # random_value_001.Value -> math_015.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Random Value.001"].outputs[0],
        ff_grass_nodes_1.nodes["Math.015"].inputs[0]
    )
    # math_015.Value -> math_016.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.015"].outputs[0],
        ff_grass_nodes_1.nodes["Math.016"].inputs[0]
    )
    # random_value.Value -> math_017.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Random Value"].outputs[0],
        ff_grass_nodes_1.nodes["Math.017"].inputs[0]
    )
    # random_value.Value -> math_018.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Random Value"].outputs[0],
        ff_grass_nodes_1.nodes["Math.018"].inputs[0]
    )
    # math_017.Value -> math_019.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.017"].outputs[0],
        ff_grass_nodes_1.nodes["Math.019"].inputs[0]
    )
    # math_016.Value -> math_019.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.016"].outputs[0],
        ff_grass_nodes_1.nodes["Math.019"].inputs[1]
    )
    # math_018.Value -> math_020.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.018"].outputs[0],
        ff_grass_nodes_1.nodes["Math.020"].inputs[0]
    )
    # math_016.Value -> math_020.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.016"].outputs[0],
        ff_grass_nodes_1.nodes["Math.020"].inputs[1]
    )
    # math_019.Value -> combine_xyz_002.X
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.019"].outputs[0],
        ff_grass_nodes_1.nodes["Combine XYZ.002"].inputs[0]
    )
    # math_020.Value -> combine_xyz_002.Y
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.020"].outputs[0],
        ff_grass_nodes_1.nodes["Combine XYZ.002"].inputs[1]
    )
    # points.Points -> set_position_001.Geometry
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Points"].outputs[0],
        ff_grass_nodes_1.nodes["Set Position.001"].inputs[0]
    )
    # combine_xyz_002.Vector -> set_position_001.Position
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Combine XYZ.002"].outputs[0],
        ff_grass_nodes_1.nodes["Set Position.001"].inputs[2]
    )
    # math_013.Value -> random_value_002.Seed
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.013"].outputs[0],
        ff_grass_nodes_1.nodes["Random Value.002"].inputs[3]
    )
    # math_014.Value -> random_value_003.Seed
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.014"].outputs[0],
        ff_grass_nodes_1.nodes["Random Value.003"].inputs[3]
    )
    # reroute.Output -> instance_on_points.Points
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Reroute"].outputs[0],
        ff_grass_nodes_1.nodes["Instance on Points"].inputs[0]
    )
    # set_shade_smooth.Mesh -> instance_on_points.Instance
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Set Shade Smooth"].outputs[0],
        ff_grass_nodes_1.nodes["Instance on Points"].inputs[2]
    )
    # reroute_001.Output -> instance_on_points.Rotation
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Reroute.001"].outputs[0],
        ff_grass_nodes_1.nodes["Instance on Points"].inputs[5]
    )
    # random_value_003.Value -> instance_on_points.Scale
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Random Value.003"].outputs[0],
        ff_grass_nodes_1.nodes["Instance on Points"].inputs[6]
    )
    # instance_on_points.Instances -> store_named_attribute_002.Geometry
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Instance on Points"].outputs[0],
        ff_grass_nodes_1.nodes["Store Named Attribute.002"].inputs[0]
    )
    # index.Index -> store_named_attribute_002.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Index"].outputs[0],
        ff_grass_nodes_1.nodes["Store Named Attribute.002"].inputs[3]
    )
    # store_named_attribute_002.Geometry -> realize_instances.Geometry
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Store Named Attribute.002"].outputs[0],
        ff_grass_nodes_1.nodes["Realize Instances"].inputs[0]
    )
    # realize_instances.Geometry -> convex_hull.Geometry
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Realize Instances"].outputs[0],
        ff_grass_nodes_1.nodes["Convex Hull"].inputs[0]
    )
    # convex_hull.Convex Hull -> set_shade_smooth_001.Mesh
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Convex Hull"].outputs[0],
        ff_grass_nodes_1.nodes["Set Shade Smooth.001"].inputs[0]
    )
    # set_shade_smooth_001.Mesh -> sample_nearest_surface.Mesh
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Set Shade Smooth.001"].outputs[0],
        ff_grass_nodes_1.nodes["Sample Nearest Surface"].inputs[0]
    )
    # normal.Normal -> sample_nearest_surface.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Normal"].outputs[0],
        ff_grass_nodes_1.nodes["Sample Nearest Surface"].inputs[1]
    )
    # math_021.Value -> vector_math.Scale
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.021"].outputs[0],
        ff_grass_nodes_1.nodes["Vector Math"].inputs[3]
    )
    # sample_nearest_surface.Value -> vector_math_001.Vector
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Sample Nearest Surface"].outputs[0],
        ff_grass_nodes_1.nodes["Vector Math.001"].inputs[0]
    )
    # vector_math.Vector -> vector_math_002.Vector
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Vector Math"].outputs[0],
        ff_grass_nodes_1.nodes["Vector Math.002"].inputs[0]
    )
    # vector_math_001.Vector -> vector_math_002.Vector
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Vector Math.001"].outputs[0],
        ff_grass_nodes_1.nodes["Vector Math.002"].inputs[1]
    )
    # vector_math_002.Vector -> vector_math_003.Vector
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Vector Math.002"].outputs[0],
        ff_grass_nodes_1.nodes["Vector Math.003"].inputs[0]
    )
    # realize_instances.Geometry -> set_mesh_normal.Mesh
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Realize Instances"].outputs[0],
        ff_grass_nodes_1.nodes["Set Mesh Normal"].inputs[0]
    )
    # vector_math_003.Vector -> set_mesh_normal.Custom Normal
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Vector Math.003"].outputs[0],
        ff_grass_nodes_1.nodes["Set Mesh Normal"].inputs[1]
    )
    # set_mesh_normal.Mesh -> set_material.Geometry
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Set Mesh Normal"].outputs[0],
        ff_grass_nodes_1.nodes["Set Material"].inputs[0]
    )
    # set_material.Geometry -> group_output.Geometry
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Set Material"].outputs[0],
        ff_grass_nodes_1.nodes["Group Output"].inputs[0]
    )
    # group_input_001.Grass Color -> store_named_attribute_001.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input.001"].outputs[13],
        ff_grass_nodes_1.nodes["Store Named Attribute.001"].inputs[3]
    )
    # group_input_002.Resolution X -> grid.Vertices X
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input.002"].outputs[5],
        ff_grass_nodes_1.nodes["Grid"].inputs[2]
    )
    # group_input_002.Resolution Y -> grid.Vertices Y
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input.002"].outputs[6],
        ff_grass_nodes_1.nodes["Grid"].inputs[3]
    )
    # group_input_003.Seed -> random_value.Seed
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input.003"].outputs[0],
        ff_grass_nodes_1.nodes["Random Value"].inputs[3]
    )
    # group_input_003.Seed -> math_012.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input.003"].outputs[0],
        ff_grass_nodes_1.nodes["Math.012"].inputs[0]
    )
    # group_input_003.Seed -> math_013.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input.003"].outputs[0],
        ff_grass_nodes_1.nodes["Math.013"].inputs[0]
    )
    # group_input_003.Seed -> math_014.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input.003"].outputs[0],
        ff_grass_nodes_1.nodes["Math.014"].inputs[0]
    )
    # group_input_003.Count -> points.Count
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input.003"].outputs[1],
        ff_grass_nodes_1.nodes["Points"].inputs[0]
    )
    # group_input_003.Patch Radius -> math_016.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input.003"].outputs[2],
        ff_grass_nodes_1.nodes["Math.016"].inputs[1]
    )
    # math_001.Value -> math_002.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Math.001"].outputs[0],
        ff_grass_nodes_1.nodes["Math.002"].inputs[0]
    )
    # map_range.Result -> math_005.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Map Range"].outputs[0],
        ff_grass_nodes_1.nodes["Math.005"].inputs[0]
    )
    # group_input_004.Smooth Shading -> set_shade_smooth.Shade Smooth
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input.004"].outputs[11],
        ff_grass_nodes_1.nodes["Set Shade Smooth"].inputs[2]
    )
    # group_input_005.Width -> math_002.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input.005"].outputs[8],
        ff_grass_nodes_1.nodes["Math.002"].inputs[1]
    )
    # group_input_005.Height -> math_004.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input.005"].outputs[7],
        ff_grass_nodes_1.nodes["Math.004"].inputs[0]
    )
    # group_input_005.Bend Strength -> math_003.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input.005"].outputs[9],
        ff_grass_nodes_1.nodes["Math.003"].inputs[0]
    )
    # group_input.Min Scale -> random_value_003.Min
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input"].outputs[3],
        ff_grass_nodes_1.nodes["Random Value.003"].inputs[0]
    )
    # group_input.Max Scale -> random_value_003.Max
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input"].outputs[4],
        ff_grass_nodes_1.nodes["Random Value.003"].inputs[1]
    )
    # set_position_001.Geometry -> reroute.Input
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Set Position.001"].outputs[0],
        ff_grass_nodes_1.nodes["Reroute"].inputs[0]
    )
    # random_value_002.Value -> reroute_001.Input
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Random Value.002"].outputs[0],
        ff_grass_nodes_1.nodes["Reroute.001"].inputs[0]
    )
    # group_input_006.Stylized Normals -> math_021.Value
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input.006"].outputs[12],
        ff_grass_nodes_1.nodes["Math.021"].inputs[1]
    )
    # group_input_006.Stylized Normals -> vector_math_001.Scale
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input.006"].outputs[12],
        ff_grass_nodes_1.nodes["Vector Math.001"].inputs[3]
    )
    # normal_001.Normal -> vector_math.Vector
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Normal.001"].outputs[0],
        ff_grass_nodes_1.nodes["Vector Math"].inputs[0]
    )
    # group_input_007.Material -> set_material.Material
    ff_grass_nodes_1.links.new(
        ff_grass_nodes_1.nodes["Group Input.007"].outputs[10],
        ff_grass_nodes_1.nodes["Set Material"].inputs[2]
    )

    return ff_grass_nodes_1


if __name__ == "__main__":
    # Maps node tree creation functions to the node tree 
    # name, such that we don't recreate node trees unnecessarily
    node_tree_names : dict[typing.Callable, str] = {}

    ff_grass_nodes = ff_grass_nodes_1_node_group(node_tree_names)
    node_tree_names[ff_grass_nodes_1_node_group] = ff_grass_nodes.name


# ============================================================================
#  FF BRIDGE 
# ============================================================================

from . import bridge

GROUP_NAME = "FF Grass Nodes"
MAT_NAME = "M_Grass"
MAT_HEX = "00FF00"


def create_node_group():
    return bridge.get_or_create_node_group(ff_grass_nodes_1_node_group, GROUP_NAME)


def get_or_create_material():
    return bridge.get_or_create_colormask_material(MAT_NAME, MAT_HEX)