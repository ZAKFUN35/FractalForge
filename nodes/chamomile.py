import bpy
import mathutils
import os
import typing


def ff_chamomile_nodes_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize FF Chamomile Nodes node group"""
    ff_chamomile_nodes_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="FF Chamomile Nodes")

    ff_chamomile_nodes_1.color_tag = 'GEOMETRY'
    ff_chamomile_nodes_1.description = ""
    ff_chamomile_nodes_1.default_group_node_width = 140
    ff_chamomile_nodes_1.is_modifier = True
    ff_chamomile_nodes_1.show_modifier_manage_panel = True

    # ff_chamomile_nodes_1 interface

    # Socket Geometry
    geometry_socket = ff_chamomile_nodes_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Panel Placement
    placement_panel = ff_chamomile_nodes_1.interface.new_panel("Placement")
    # Socket Seed
    seed_socket = ff_chamomile_nodes_1.interface.new_socket(name="Seed", in_out='INPUT', socket_type='NodeSocketInt', parent = placement_panel)
    seed_socket.default_value = 0
    seed_socket.min_value = -2147483648
    seed_socket.max_value = 2147483647
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'

    # Socket Count
    count_socket = ff_chamomile_nodes_1.interface.new_socket(name="Count", in_out='INPUT', socket_type='NodeSocketInt', parent = placement_panel)
    count_socket.default_value = 3
    count_socket.min_value = -2147483648
    count_socket.max_value = 2147483647
    count_socket.subtype = 'NONE'
    count_socket.attribute_domain = 'POINT'
    count_socket.default_input = 'VALUE'
    count_socket.structure_type = 'AUTO'

    # Socket Patch Radius
    patch_radius_socket = ff_chamomile_nodes_1.interface.new_socket(name="Patch Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent = placement_panel)
    patch_radius_socket.default_value = 0.14000000059604645
    patch_radius_socket.min_value = -3.4028234663852886e+38
    patch_radius_socket.max_value = 3.4028234663852886e+38
    patch_radius_socket.subtype = 'NONE'
    patch_radius_socket.attribute_domain = 'POINT'
    patch_radius_socket.default_input = 'VALUE'
    patch_radius_socket.structure_type = 'AUTO'

    # Socket Min Scale
    min_scale_socket = ff_chamomile_nodes_1.interface.new_socket(name="Min Scale", in_out='INPUT', socket_type='NodeSocketFloat', parent = placement_panel)
    min_scale_socket.default_value = 0.05000000074505806
    min_scale_socket.min_value = -3.4028234663852886e+38
    min_scale_socket.max_value = 3.4028234663852886e+38
    min_scale_socket.subtype = 'NONE'
    min_scale_socket.attribute_domain = 'POINT'
    min_scale_socket.default_input = 'VALUE'
    min_scale_socket.structure_type = 'AUTO'

    # Socket Max Scale
    max_scale_socket = ff_chamomile_nodes_1.interface.new_socket(name="Max Scale", in_out='INPUT', socket_type='NodeSocketFloat', parent = placement_panel)
    max_scale_socket.default_value = 0.11999999731779099
    max_scale_socket.min_value = -3.4028234663852886e+38
    max_scale_socket.max_value = 3.4028234663852886e+38
    max_scale_socket.subtype = 'NONE'
    max_scale_socket.attribute_domain = 'POINT'
    max_scale_socket.default_input = 'VALUE'
    max_scale_socket.structure_type = 'AUTO'


    # Panel Structure
    structure_panel = ff_chamomile_nodes_1.interface.new_panel("Structure")
    # Socket Petals Count
    petals_count_socket = ff_chamomile_nodes_1.interface.new_socket(name="Petals Count", in_out='INPUT', socket_type='NodeSocketInt', parent = structure_panel)
    petals_count_socket.default_value = 5
    petals_count_socket.min_value = -2147483648
    petals_count_socket.max_value = 2147483647
    petals_count_socket.subtype = 'NONE'
    petals_count_socket.attribute_domain = 'POINT'
    petals_count_socket.default_input = 'VALUE'
    petals_count_socket.structure_type = 'AUTO'

    # Socket Center Radius
    center_radius_socket = ff_chamomile_nodes_1.interface.new_socket(name="Center Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent = structure_panel)
    center_radius_socket.default_value = 0.2800000011920929
    center_radius_socket.min_value = -3.4028234663852886e+38
    center_radius_socket.max_value = 3.4028234663852886e+38
    center_radius_socket.subtype = 'NONE'
    center_radius_socket.attribute_domain = 'POINT'
    center_radius_socket.default_input = 'VALUE'
    center_radius_socket.structure_type = 'AUTO'

    # Socket Petal Scale
    petal_scale_socket = ff_chamomile_nodes_1.interface.new_socket(name="Petal Scale", in_out='INPUT', socket_type='NodeSocketFloat', parent = structure_panel)
    petal_scale_socket.default_value = 0.5
    petal_scale_socket.min_value = -3.4028234663852886e+38
    petal_scale_socket.max_value = 3.4028234663852886e+38
    petal_scale_socket.subtype = 'NONE'
    petal_scale_socket.attribute_domain = 'POINT'
    petal_scale_socket.default_input = 'VALUE'
    petal_scale_socket.structure_type = 'AUTO'


    # Panel Center Sphere
    center_sphere_panel = ff_chamomile_nodes_1.interface.new_panel("Center Sphere")
    # Socket Scale
    scale_socket = ff_chamomile_nodes_1.interface.new_socket(name="Scale", in_out='INPUT', socket_type='NodeSocketVector', parent = center_sphere_panel)
    scale_socket.default_value = (0.3700000047683716, 0.3700000047683716, 0.07999999821186066)
    scale_socket.min_value = -3.4028234663852886e+38
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    # Socket Subdivisions
    subdivisions_socket = ff_chamomile_nodes_1.interface.new_socket(name="Subdivisions", in_out='INPUT', socket_type='NodeSocketInt', parent = center_sphere_panel)
    subdivisions_socket.default_value = 1
    subdivisions_socket.min_value = -2147483648
    subdivisions_socket.max_value = 2147483647
    subdivisions_socket.subtype = 'NONE'
    subdivisions_socket.attribute_domain = 'POINT'
    subdivisions_socket.default_input = 'VALUE'
    subdivisions_socket.structure_type = 'AUTO'


    # Panel Stem
    stem_panel = ff_chamomile_nodes_1.interface.new_panel("Stem")
    # Socket Length
    length_socket = ff_chamomile_nodes_1.interface.new_socket(name="Length", in_out='INPUT', socket_type='NodeSocketFloat', parent = stem_panel)
    length_socket.default_value = 2.5
    length_socket.min_value = -3.4028234663852886e+38
    length_socket.max_value = 3.4028234663852886e+38
    length_socket.subtype = 'NONE'
    length_socket.attribute_domain = 'POINT'
    length_socket.default_input = 'VALUE'
    length_socket.structure_type = 'AUTO'

    # Socket Thickness
    thickness_socket = ff_chamomile_nodes_1.interface.new_socket(name="Thickness", in_out='INPUT', socket_type='NodeSocketFloat', parent = stem_panel)
    thickness_socket.default_value = 0.029999999329447746
    thickness_socket.min_value = -3.4028234663852886e+38
    thickness_socket.max_value = 3.4028234663852886e+38
    thickness_socket.subtype = 'NONE'
    thickness_socket.attribute_domain = 'POINT'
    thickness_socket.default_input = 'VALUE'
    thickness_socket.structure_type = 'AUTO'

    # Socket Resolution
    resolution_socket = ff_chamomile_nodes_1.interface.new_socket(name="Resolution", in_out='INPUT', socket_type='NodeSocketInt', parent = stem_panel)
    resolution_socket.default_value = 3
    resolution_socket.min_value = 3
    resolution_socket.max_value = 2147483647
    resolution_socket.subtype = 'NONE'
    resolution_socket.attribute_domain = 'POINT'
    resolution_socket.default_input = 'VALUE'
    resolution_socket.structure_type = 'AUTO'


    # Panel Petal Shape
    petal_shape_panel = ff_chamomile_nodes_1.interface.new_panel("Petal Shape")
    # Socket Resolution X
    resolution_x_socket = ff_chamomile_nodes_1.interface.new_socket(name="Resolution X", in_out='INPUT', socket_type='NodeSocketInt', parent = petal_shape_panel)
    resolution_x_socket.default_value = 7
    resolution_x_socket.min_value = 3
    resolution_x_socket.max_value = 2147483647
    resolution_x_socket.subtype = 'NONE'
    resolution_x_socket.attribute_domain = 'POINT'
    resolution_x_socket.default_input = 'VALUE'
    resolution_x_socket.structure_type = 'AUTO'

    # Socket Resolution Y
    resolution_y_socket = ff_chamomile_nodes_1.interface.new_socket(name="Resolution Y", in_out='INPUT', socket_type='NodeSocketInt', parent = petal_shape_panel)
    resolution_y_socket.default_value = 4
    resolution_y_socket.min_value = 2
    resolution_y_socket.max_value = 2147483647
    resolution_y_socket.subtype = 'NONE'
    resolution_y_socket.attribute_domain = 'POINT'
    resolution_y_socket.default_input = 'VALUE'
    resolution_y_socket.structure_type = 'AUTO'

    # Socket Gutter Strength
    gutter_strength_socket = ff_chamomile_nodes_1.interface.new_socket(name="Gutter Strength", in_out='INPUT', socket_type='NodeSocketFloat', parent = petal_shape_panel)
    gutter_strength_socket.default_value = 0.25
    gutter_strength_socket.min_value = -3.4028234663852886e+38
    gutter_strength_socket.max_value = 3.4028234663852886e+38
    gutter_strength_socket.subtype = 'NONE'
    gutter_strength_socket.attribute_domain = 'POINT'
    gutter_strength_socket.default_input = 'VALUE'
    gutter_strength_socket.structure_type = 'AUTO'

    # Socket Arch Strength
    arch_strength_socket = ff_chamomile_nodes_1.interface.new_socket(name="Arch Strength", in_out='INPUT', socket_type='NodeSocketFloat', parent = petal_shape_panel)
    arch_strength_socket.default_value = 0.20000000298023224
    arch_strength_socket.min_value = -3.4028234663852886e+38
    arch_strength_socket.max_value = 3.4028234663852886e+38
    arch_strength_socket.subtype = 'NONE'
    arch_strength_socket.attribute_domain = 'POINT'
    arch_strength_socket.default_input = 'VALUE'
    arch_strength_socket.structure_type = 'AUTO'


    # Panel Detail
    detail_panel = ff_chamomile_nodes_1.interface.new_panel("Detail")
    # Socket Material
    material_socket = ff_chamomile_nodes_1.interface.new_socket(name="Material", in_out='INPUT', socket_type='NodeSocketMaterial', parent = detail_panel)
    material_socket.attribute_domain = 'POINT'
    material_socket.default_input = 'VALUE'
    material_socket.structure_type = 'AUTO'

    # Socket Smooth Shading
    smooth_shading_socket = ff_chamomile_nodes_1.interface.new_socket(name="Smooth Shading", in_out='INPUT', socket_type='NodeSocketBool', parent = detail_panel)
    smooth_shading_socket.default_value = True
    smooth_shading_socket.attribute_domain = 'POINT'
    smooth_shading_socket.default_input = 'VALUE'
    smooth_shading_socket.structure_type = 'AUTO'

    # Socket Stylized Normals
    stylized_normals_socket = ff_chamomile_nodes_1.interface.new_socket(name="Stylized Normals", in_out='INPUT', socket_type='NodeSocketFloat', parent = detail_panel)
    stylized_normals_socket.default_value = 0.8500000238418579
    stylized_normals_socket.min_value = 0.0
    stylized_normals_socket.max_value = 1.0
    stylized_normals_socket.subtype = 'NONE'
    stylized_normals_socket.attribute_domain = 'POINT'
    stylized_normals_socket.default_input = 'VALUE'
    stylized_normals_socket.structure_type = 'AUTO'

    # Socket Petal Color
    petal_color_socket = ff_chamomile_nodes_1.interface.new_socket(name="Petal Color", in_out='INPUT', socket_type='NodeSocketColor', parent = detail_panel)
    petal_color_socket.default_value = (0.0, 0.0, 1.0, 1.0)
    petal_color_socket.attribute_domain = 'POINT'
    petal_color_socket.default_input = 'VALUE'
    petal_color_socket.structure_type = 'AUTO'

    # Socket Center Color
    center_color_socket = ff_chamomile_nodes_1.interface.new_socket(name="Center Color", in_out='INPUT', socket_type='NodeSocketColor', parent = detail_panel)
    center_color_socket.default_value = (1.0, 0.0, 0.0, 1.0)
    center_color_socket.attribute_domain = 'POINT'
    center_color_socket.default_input = 'VALUE'
    center_color_socket.structure_type = 'AUTO'

    # Socket Stem Color
    stem_color_socket = ff_chamomile_nodes_1.interface.new_socket(name="Stem Color", in_out='INPUT', socket_type='NodeSocketColor', parent = detail_panel)
    stem_color_socket.default_value = (0.0, 1.0, 0.0, 1.0)
    stem_color_socket.attribute_domain = 'POINT'
    stem_color_socket.default_input = 'VALUE'
    stem_color_socket.structure_type = 'AUTO'


    # Initialize ff_chamomile_nodes_1 nodes

    # Node Group Input
    group_input = ff_chamomile_nodes_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Output
    group_output = ff_chamomile_nodes_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Math
    math = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'SUBTRACT'
    math.use_clamp = False
    # Value_001
    math.inputs[1].default_value = 1.0

    # Node Math.001
    math_001 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.show_options = True
    math_001.operation = 'DIVIDE'
    math_001.use_clamp = False
    # Value_001
    math_001.inputs[1].default_value = 2.0

    # Node Math.002
    math_002 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.show_options = True
    math_002.operation = 'FLOOR'
    math_002.use_clamp = False

    # Node Math.003
    math_003 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.show_options = True
    math_003.operation = 'MULTIPLY'
    math_003.use_clamp = False
    # Value_001
    math_003.inputs[1].default_value = 2.0

    # Node Math.004
    math_004 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.show_options = True
    math_004.operation = 'ADD'
    math_004.use_clamp = False
    # Value_001
    math_004.inputs[1].default_value = 1.0

    # Node Grid
    grid = ff_chamomile_nodes_1.nodes.new("GeometryNodeMeshGrid")
    grid.name = "Grid"
    grid.show_options = True
    # Size X
    grid.inputs[0].default_value = 2.0
    # Size Y
    grid.inputs[1].default_value = 2.0

    # Node Position
    position = ff_chamomile_nodes_1.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    position.show_options = True

    # Node Separate XYZ
    separate_xyz = ff_chamomile_nodes_1.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz.show_options = True

    # Node Map Range
    map_range = ff_chamomile_nodes_1.nodes.new("ShaderNodeMapRange")
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

    # Node Float Curve
    float_curve = ff_chamomile_nodes_1.nodes.new("ShaderNodeFloatCurve")
    float_curve.name = "Float Curve"
    float_curve.show_options = True
    # Mapping settings
    float_curve.mapping.extend = 'EXTRAPOLATED'
    float_curve.mapping.tone = 'STANDARD'
    float_curve.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve.mapping.clip_min_x = 0.0
    float_curve.mapping.clip_min_y = 0.0
    float_curve.mapping.clip_max_x = 1.0
    float_curve.mapping.clip_max_y = 1.0
    float_curve.mapping.use_clip = True
    # Curve 0
    float_curve_curve_0 = float_curve.mapping.curves[0]
    float_curve_curve_0_point_0 = float_curve_curve_0.points[0]
    float_curve_curve_0_point_0.location = (0.0, 0.3499999940395355)
    float_curve_curve_0_point_0.handle_type = 'AUTO'
    float_curve_curve_0_point_1 = float_curve_curve_0.points[1]
    float_curve_curve_0_point_1.location = (0.5, 0.5)
    float_curve_curve_0_point_1.handle_type = 'AUTO'
    float_curve_curve_0_point_2 = float_curve_curve_0.points.new(1.0, 0.3499999940395355)
    float_curve_curve_0_point_2.handle_type = 'AUTO'
    # Update curve after changes
    float_curve.mapping.update()
    # Factor
    float_curve.inputs[0].default_value = 1.0

    # Node Math.005
    math_005 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.show_options = True
    math_005.operation = 'MULTIPLY'
    math_005.use_clamp = False

    # Node Map Range.001
    map_range_001 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMapRange")
    map_range_001.name = "Map Range.001"
    map_range_001.show_options = True
    map_range_001.clamp = True
    map_range_001.data_type = 'FLOAT'
    map_range_001.interpolation_type = 'LINEAR'
    # From Min
    map_range_001.inputs[1].default_value = 0.0
    # From Max
    map_range_001.inputs[2].default_value = 1.0
    # To Min
    map_range_001.inputs[3].default_value = 1.0
    # To Max
    map_range_001.inputs[4].default_value = 3.5

    # Node Math.006
    math_006 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.show_options = True
    math_006.operation = 'POWER'
    math_006.use_clamp = False
    # Value_001
    math_006.inputs[1].default_value = 2.0

    # Node Math.007
    math_007 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.show_options = True
    math_007.operation = 'SUBTRACT'
    math_007.use_clamp = False
    # Value
    math_007.inputs[0].default_value = 1.0

    # Node Math.008
    math_008 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.show_options = True
    math_008.operation = 'MULTIPLY'
    math_008.use_clamp = False

    # Node Math.009
    math_009 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.show_options = True
    math_009.operation = 'MULTIPLY'
    math_009.use_clamp = False
    # Value_001
    math_009.inputs[1].default_value = 0.800000011920929

    # Node Math.010
    math_010 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.show_options = True
    math_010.operation = 'ADD'
    math_010.use_clamp = False

    # Node Math.011
    math_011 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_011.name = "Math.011"
    math_011.show_options = True
    math_011.operation = 'SINE'
    math_011.use_clamp = False

    # Node Math.012
    math_012 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_012.name = "Math.012"
    math_012.show_options = True
    math_012.operation = 'MULTIPLY'
    math_012.use_clamp = False

    # Node Math.013
    math_013 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_013.name = "Math.013"
    math_013.show_options = True
    math_013.operation = 'COSINE'
    math_013.use_clamp = False

    # Node Math.014
    math_014 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_014.name = "Math.014"
    math_014.show_options = True
    math_014.operation = 'MULTIPLY'
    math_014.use_clamp = False

    # Node Math.015
    math_015 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_015.name = "Math.015"
    math_015.show_options = True
    math_015.operation = 'SUBTRACT'
    math_015.use_clamp = False
    # Value_001
    math_015.inputs[1].default_value = 1.0

    # Node Map Range.002
    map_range_002 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMapRange")
    map_range_002.name = "Map Range.002"
    map_range_002.show_options = True
    map_range_002.clamp = True
    map_range_002.data_type = 'FLOAT'
    map_range_002.interpolation_type = 'LINEAR'
    # From Min
    map_range_002.inputs[1].default_value = -2.0999999046325684
    # From Max
    map_range_002.inputs[2].default_value = 2.0999999046325684
    # To Min
    map_range_002.inputs[3].default_value = 0.0
    # To Max
    map_range_002.inputs[4].default_value = 0.5

    # Node Map Range.003
    map_range_003 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMapRange")
    map_range_003.name = "Map Range.003"
    map_range_003.show_options = True
    map_range_003.clamp = True
    map_range_003.data_type = 'FLOAT'
    map_range_003.interpolation_type = 'LINEAR'
    # From Min
    map_range_003.inputs[1].default_value = -0.5
    # From Max
    map_range_003.inputs[2].default_value = 3.5
    # To Min
    map_range_003.inputs[3].default_value = 0.5
    # To Max
    map_range_003.inputs[4].default_value = 1.0

    # Node Combine XYZ
    combine_xyz = ff_chamomile_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz.show_options = True
    # Z
    combine_xyz.inputs[2].default_value = 0.0

    # Node Store Named Attribute
    store_named_attribute = ff_chamomile_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'FLOAT2'
    store_named_attribute.domain = 'CORNER'
    # Selection
    store_named_attribute.inputs[1].default_value = True
    # Name
    store_named_attribute.inputs[2].default_value = "UVMap"

    # Node Store Named Attribute.001
    store_named_attribute_001 = ff_chamomile_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.show_options = True
    store_named_attribute_001.data_type = 'FLOAT_COLOR'
    store_named_attribute_001.domain = 'CORNER'
    # Selection
    store_named_attribute_001.inputs[1].default_value = True
    # Name
    store_named_attribute_001.inputs[2].default_value = "ColorMask"

    # Node Math.016
    math_016 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_016.name = "Math.016"
    math_016.show_options = True
    math_016.operation = 'ABSOLUTE'
    math_016.use_clamp = False

    # Node Float Curve.001
    float_curve_001 = ff_chamomile_nodes_1.nodes.new("ShaderNodeFloatCurve")
    float_curve_001.name = "Float Curve.001"
    float_curve_001.show_options = True
    # Mapping settings
    float_curve_001.mapping.extend = 'EXTRAPOLATED'
    float_curve_001.mapping.tone = 'STANDARD'
    float_curve_001.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_001.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_001.mapping.clip_min_x = 0.0
    float_curve_001.mapping.clip_min_y = 0.0
    float_curve_001.mapping.clip_max_x = 1.0
    float_curve_001.mapping.clip_max_y = 1.0
    float_curve_001.mapping.use_clip = True
    # Curve 0
    float_curve_001_curve_0 = float_curve_001.mapping.curves[0]
    float_curve_001_curve_0_point_0 = float_curve_001_curve_0.points[0]
    float_curve_001_curve_0_point_0.location = (0.0, 0.0)
    float_curve_001_curve_0_point_0.handle_type = 'AUTO'
    float_curve_001_curve_0_point_1 = float_curve_001_curve_0.points[1]
    float_curve_001_curve_0_point_1.location = (0.30000001192092896, 0.10000000149011612)
    float_curve_001_curve_0_point_1.handle_type = 'AUTO'
    float_curve_001_curve_0_point_2 = float_curve_001_curve_0.points.new(1.0, 1.0)
    float_curve_001_curve_0_point_2.handle_type = 'AUTO'
    # Update curve after changes
    float_curve_001.mapping.update()
    # Factor
    float_curve_001.inputs[0].default_value = 1.0

    # Node Math.017
    math_017 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_017.name = "Math.017"
    math_017.show_options = True
    math_017.operation = 'MULTIPLY'
    math_017.use_clamp = False

    # Node Float Curve.002
    float_curve_002 = ff_chamomile_nodes_1.nodes.new("ShaderNodeFloatCurve")
    float_curve_002.name = "Float Curve.002"
    float_curve_002.show_options = True
    # Mapping settings
    float_curve_002.mapping.extend = 'EXTRAPOLATED'
    float_curve_002.mapping.tone = 'STANDARD'
    float_curve_002.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_002.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_002.mapping.clip_min_x = 0.0
    float_curve_002.mapping.clip_min_y = 0.0
    float_curve_002.mapping.clip_max_x = 1.0
    float_curve_002.mapping.clip_max_y = 1.0
    float_curve_002.mapping.use_clip = True
    # Curve 0
    float_curve_002_curve_0 = float_curve_002.mapping.curves[0]
    float_curve_002_curve_0_point_0 = float_curve_002_curve_0.points[0]
    float_curve_002_curve_0_point_0.location = (0.0, 0.0)
    float_curve_002_curve_0_point_0.handle_type = 'AUTO'
    float_curve_002_curve_0_point_1 = float_curve_002_curve_0.points[1]
    float_curve_002_curve_0_point_1.location = (0.5, 0.05000000074505806)
    float_curve_002_curve_0_point_1.handle_type = 'AUTO'
    float_curve_002_curve_0_point_2 = float_curve_002_curve_0.points.new(1.0, 1.0)
    float_curve_002_curve_0_point_2.handle_type = 'AUTO'
    # Update curve after changes
    float_curve_002.mapping.update()
    # Factor
    float_curve_002.inputs[0].default_value = 1.0

    # Node Math.018
    math_018 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_018.name = "Math.018"
    math_018.show_options = True
    math_018.operation = 'MULTIPLY'
    math_018.use_clamp = False

    # Node Float Curve.003
    float_curve_003 = ff_chamomile_nodes_1.nodes.new("ShaderNodeFloatCurve")
    float_curve_003.name = "Float Curve.003"
    float_curve_003.show_options = True
    # Mapping settings
    float_curve_003.mapping.extend = 'EXTRAPOLATED'
    float_curve_003.mapping.tone = 'STANDARD'
    float_curve_003.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_003.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_003.mapping.clip_min_x = 0.0
    float_curve_003.mapping.clip_min_y = 0.0
    float_curve_003.mapping.clip_max_x = 1.0
    float_curve_003.mapping.clip_max_y = 1.0
    float_curve_003.mapping.use_clip = True
    # Curve 0
    float_curve_003_curve_0 = float_curve_003.mapping.curves[0]
    float_curve_003_curve_0_point_0 = float_curve_003_curve_0.points[0]
    float_curve_003_curve_0_point_0.location = (0.0, 0.0)
    float_curve_003_curve_0_point_0.handle_type = 'AUTO'
    float_curve_003_curve_0_point_1 = float_curve_003_curve_0.points[1]
    float_curve_003_curve_0_point_1.location = (0.5, 1.0)
    float_curve_003_curve_0_point_1.handle_type = 'AUTO'
    float_curve_003_curve_0_point_2 = float_curve_003_curve_0.points.new(1.0, 0.0)
    float_curve_003_curve_0_point_2.handle_type = 'AUTO'
    # Update curve after changes
    float_curve_003.mapping.update()
    # Factor
    float_curve_003.inputs[0].default_value = 1.0

    # Node Math.019
    math_019 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_019.name = "Math.019"
    math_019.show_options = True
    math_019.operation = 'MULTIPLY'
    math_019.use_clamp = False

    # Node Math.020
    math_020 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_020.name = "Math.020"
    math_020.show_options = True
    math_020.operation = 'ADD'
    math_020.use_clamp = False

    # Node Combine XYZ.001
    combine_xyz_001 = ff_chamomile_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    combine_xyz_001.show_options = True

    # Node Set Position
    set_position = ff_chamomile_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.show_options = True
    # Selection
    set_position.inputs[1].default_value = True
    # Offset
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Transform Geometry
    transform_geometry = ff_chamomile_nodes_1.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.show_options = True
    # Mode
    transform_geometry.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry.inputs[3].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry.inputs[4].default_value = (1.0, 1.0, 1.0)

    # Node Mesh Circle
    mesh_circle = ff_chamomile_nodes_1.nodes.new("GeometryNodeMeshCircle")
    mesh_circle.name = "Mesh Circle"
    mesh_circle.show_options = True
    mesh_circle.fill_type = 'NONE'

    # Node Position.001
    position_001 = ff_chamomile_nodes_1.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"
    position_001.show_options = True

    # Node Align Euler to Vector
    align_euler_to_vector = ff_chamomile_nodes_1.nodes.new("FunctionNodeAlignEulerToVector")
    align_euler_to_vector.name = "Align Euler to Vector"
    align_euler_to_vector.show_options = True
    align_euler_to_vector.axis = 'Y'
    align_euler_to_vector.pivot_axis = 'Z'
    # Rotation
    align_euler_to_vector.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Factor
    align_euler_to_vector.inputs[1].default_value = 1.0

    # Node Combine XYZ.002
    combine_xyz_002 = ff_chamomile_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    combine_xyz_002.show_options = True

    # Node Instance on Points
    instance_on_points = ff_chamomile_nodes_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    instance_on_points.show_options = True
    # Selection
    instance_on_points.inputs[1].default_value = True
    # Pick Instance
    instance_on_points.inputs[3].default_value = False
    # Instance Index
    instance_on_points.inputs[4].default_value = 0

    # Node Realize Instances
    realize_instances = ff_chamomile_nodes_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    realize_instances.show_options = True
    realize_instances.realize_to_point_domain = False
    # Selection
    realize_instances.inputs[1].default_value = True
    # Realize All
    realize_instances.inputs[2].default_value = True
    # Depth
    realize_instances.inputs[3].default_value = 0

    # Node Ico Sphere
    ico_sphere = ff_chamomile_nodes_1.nodes.new("GeometryNodeMeshIcoSphere")
    ico_sphere.name = "Ico Sphere"
    ico_sphere.show_options = True
    # Radius
    ico_sphere.inputs[0].default_value = 1.0

    # Node Position.002
    position_002 = ff_chamomile_nodes_1.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"
    position_002.show_options = True

    # Node Separate XYZ.001
    separate_xyz_001 = ff_chamomile_nodes_1.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"
    separate_xyz_001.show_options = True

    # Node Map Range.004
    map_range_004 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMapRange")
    map_range_004.name = "Map Range.004"
    map_range_004.show_options = True
    map_range_004.clamp = True
    map_range_004.data_type = 'FLOAT'
    map_range_004.interpolation_type = 'LINEAR'
    # From Min
    map_range_004.inputs[1].default_value = -1.0
    # From Max
    map_range_004.inputs[2].default_value = 1.0
    # To Min
    map_range_004.inputs[3].default_value = 0.0
    # To Max
    map_range_004.inputs[4].default_value = 0.5

    # Node Map Range.005
    map_range_005 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMapRange")
    map_range_005.name = "Map Range.005"
    map_range_005.show_options = True
    map_range_005.clamp = True
    map_range_005.data_type = 'FLOAT'
    map_range_005.interpolation_type = 'LINEAR'
    # From Min
    map_range_005.inputs[1].default_value = -1.0
    # From Max
    map_range_005.inputs[2].default_value = 1.0
    # To Min
    map_range_005.inputs[3].default_value = 0.0
    # To Max
    map_range_005.inputs[4].default_value = 0.5

    # Node Combine XYZ.003
    combine_xyz_003 = ff_chamomile_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003.name = "Combine XYZ.003"
    combine_xyz_003.show_options = True
    # Z
    combine_xyz_003.inputs[2].default_value = 0.0

    # Node Store Named Attribute.002
    store_named_attribute_002 = ff_chamomile_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_002.name = "Store Named Attribute.002"
    store_named_attribute_002.show_options = True
    store_named_attribute_002.data_type = 'FLOAT2'
    store_named_attribute_002.domain = 'CORNER'
    # Selection
    store_named_attribute_002.inputs[1].default_value = True
    # Name
    store_named_attribute_002.inputs[2].default_value = "UVMap"

    # Node Store Named Attribute.003
    store_named_attribute_003 = ff_chamomile_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_003.name = "Store Named Attribute.003"
    store_named_attribute_003.show_options = True
    store_named_attribute_003.data_type = 'FLOAT_COLOR'
    store_named_attribute_003.domain = 'CORNER'
    # Selection
    store_named_attribute_003.inputs[1].default_value = True
    # Name
    store_named_attribute_003.inputs[2].default_value = "ColorMask"

    # Node Transform Geometry.001
    transform_geometry_001 = ff_chamomile_nodes_1.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.show_options = True
    # Mode
    transform_geometry_001.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Grid.001
    grid_001 = ff_chamomile_nodes_1.nodes.new("GeometryNodeMeshGrid")
    grid_001.name = "Grid.001"
    grid_001.show_options = True
    # Size X
    grid_001.inputs[0].default_value = 1.0
    # Vertices Y
    grid_001.inputs[3].default_value = 2

    # Node Math.021
    math_021 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_021.name = "Math.021"
    math_021.show_options = True
    math_021.operation = 'ADD'
    math_021.use_clamp = False
    # Value_001
    math_021.inputs[1].default_value = 1.0

    # Node Position.003
    position_003 = ff_chamomile_nodes_1.nodes.new("GeometryNodeInputPosition")
    position_003.name = "Position.003"
    position_003.show_options = True

    # Node Separate XYZ.002
    separate_xyz_002 = ff_chamomile_nodes_1.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_002.name = "Separate XYZ.002"
    separate_xyz_002.show_options = True

    # Node Map Range.006
    map_range_006 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMapRange")
    map_range_006.name = "Map Range.006"
    map_range_006.show_options = True
    map_range_006.clamp = True
    map_range_006.data_type = 'FLOAT'
    map_range_006.interpolation_type = 'LINEAR'
    # From Min
    map_range_006.inputs[1].default_value = -0.5
    # From Max
    map_range_006.inputs[2].default_value = 0.5
    # To Min
    map_range_006.inputs[3].default_value = 0.8999999761581421
    # To Max
    map_range_006.inputs[4].default_value = 1.0

    # Node Math.022
    math_022 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_022.name = "Math.022"
    math_022.show_options = True
    math_022.operation = 'DIVIDE'
    math_022.use_clamp = False

    # Node Map Range.007
    map_range_007 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMapRange")
    map_range_007.name = "Map Range.007"
    map_range_007.show_options = True
    map_range_007.clamp = True
    map_range_007.data_type = 'FLOAT'
    map_range_007.interpolation_type = 'LINEAR'
    # From Min
    map_range_007.inputs[1].default_value = -0.5
    # From Max
    map_range_007.inputs[2].default_value = 0.5
    # To Min
    map_range_007.inputs[3].default_value = 0.0
    # To Max
    map_range_007.inputs[4].default_value = 1.0

    # Node Combine XYZ.004
    combine_xyz_004 = ff_chamomile_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_004.name = "Combine XYZ.004"
    combine_xyz_004.show_options = True
    # Z
    combine_xyz_004.inputs[2].default_value = 0.0

    # Node Store Named Attribute.004
    store_named_attribute_004 = ff_chamomile_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_004.name = "Store Named Attribute.004"
    store_named_attribute_004.show_options = True
    store_named_attribute_004.data_type = 'FLOAT2'
    store_named_attribute_004.domain = 'CORNER'
    # Selection
    store_named_attribute_004.inputs[1].default_value = True
    # Name
    store_named_attribute_004.inputs[2].default_value = "UVMap"

    # Node Math.023
    math_023 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_023.name = "Math.023"
    math_023.show_options = True
    math_023.operation = 'ADD'
    math_023.use_clamp = False
    # Value_001
    math_023.inputs[1].default_value = 0.5

    # Node Math.024
    math_024 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_024.name = "Math.024"
    math_024.show_options = True
    math_024.operation = 'MULTIPLY'
    math_024.use_clamp = False
    # Value_001
    math_024.inputs[1].default_value = 6.2831854820251465

    # Node Math.025
    math_025 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_025.name = "Math.025"
    math_025.show_options = True
    math_025.operation = 'SINE'
    math_025.use_clamp = False

    # Node Math.026
    math_026 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_026.name = "Math.026"
    math_026.show_options = True
    math_026.operation = 'MULTIPLY'
    math_026.use_clamp = False

    # Node Math.027
    math_027 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_027.name = "Math.027"
    math_027.show_options = True
    math_027.operation = 'COSINE'
    math_027.use_clamp = False

    # Node Math.028
    math_028 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_028.name = "Math.028"
    math_028.show_options = True
    math_028.operation = 'MULTIPLY'
    math_028.use_clamp = False

    # Node Math.029
    math_029 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_029.name = "Math.029"
    math_029.show_options = True
    math_029.operation = 'DIVIDE'
    math_029.use_clamp = False
    # Value_001
    math_029.inputs[1].default_value = 2.0

    # Node Math.030
    math_030 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_030.name = "Math.030"
    math_030.show_options = True
    math_030.operation = 'SUBTRACT'
    math_030.use_clamp = False

    # Node Combine XYZ.005
    combine_xyz_005 = ff_chamomile_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_005.name = "Combine XYZ.005"
    combine_xyz_005.show_options = True

    # Node Set Position.001
    set_position_001 = ff_chamomile_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    set_position_001.show_options = True
    # Selection
    set_position_001.inputs[1].default_value = True
    # Offset
    set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Merge by Distance
    merge_by_distance = ff_chamomile_nodes_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.show_options = True
    # Selection
    merge_by_distance.inputs[1].default_value = True
    # Mode
    merge_by_distance.inputs[2].default_value = 'All'
    # Distance
    merge_by_distance.inputs[3].default_value = 0.0010000000474974513

    # Node Flip Faces
    flip_faces = ff_chamomile_nodes_1.nodes.new("GeometryNodeFlipFaces")
    flip_faces.name = "Flip Faces"
    flip_faces.show_options = True
    # Selection
    flip_faces.inputs[1].default_value = True

    # Node Store Named Attribute.005
    store_named_attribute_005 = ff_chamomile_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_005.name = "Store Named Attribute.005"
    store_named_attribute_005.show_options = True
    store_named_attribute_005.data_type = 'FLOAT_COLOR'
    store_named_attribute_005.domain = 'CORNER'
    # Selection
    store_named_attribute_005.inputs[1].default_value = True
    # Name
    store_named_attribute_005.inputs[2].default_value = "ColorMask"

    # Node Join Geometry
    join_geometry = ff_chamomile_nodes_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Set Shade Smooth
    set_shade_smooth = ff_chamomile_nodes_1.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.show_options = True
    set_shade_smooth.domain = 'FACE'
    # Selection
    set_shade_smooth.inputs[1].default_value = True

    # Node Combine XYZ.006
    combine_xyz_006 = ff_chamomile_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_006.name = "Combine XYZ.006"
    combine_xyz_006.show_options = True
    # X
    combine_xyz_006.inputs[0].default_value = 0.0
    # Y
    combine_xyz_006.inputs[1].default_value = 0.0

    # Node Transform Geometry.002
    transform_geometry_002 = ff_chamomile_nodes_1.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    transform_geometry_002.show_options = True
    # Mode
    transform_geometry_002.inputs[1].default_value = 'Components'
    # Rotation
    transform_geometry_002.inputs[3].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_002.inputs[4].default_value = (1.0, 1.0, 1.0)

    # Node Points
    points = ff_chamomile_nodes_1.nodes.new("GeometryNodePoints")
    points.name = "Points"
    points.show_options = True
    # Position
    points.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Radius
    points.inputs[2].default_value = 0.10000000149011612

    # Node Math.031
    math_031 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_031.name = "Math.031"
    math_031.show_options = True
    math_031.operation = 'ADD'
    math_031.use_clamp = False
    # Value_001
    math_031.inputs[1].default_value = 1337.0

    # Node Math.032
    math_032 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_032.name = "Math.032"
    math_032.show_options = True
    math_032.operation = 'ADD'
    math_032.use_clamp = False
    # Value_001
    math_032.inputs[1].default_value = 99.0

    # Node Math.033
    math_033 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_033.name = "Math.033"
    math_033.show_options = True
    math_033.operation = 'ADD'
    math_033.use_clamp = False
    # Value_001
    math_033.inputs[1].default_value = 7.0

    # Node Random Value
    random_value = ff_chamomile_nodes_1.nodes.new("FunctionNodeRandomValue")
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
    random_value_001 = ff_chamomile_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value_001.name = "Random Value.001"
    random_value_001.show_options = True
    random_value_001.data_type = 'FLOAT'
    # Min
    random_value_001.inputs[0].default_value = 0.0
    # Max
    random_value_001.inputs[1].default_value = 1.0
    # ID
    random_value_001.inputs[2].default_value = 0

    # Node Math.034
    math_034 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_034.name = "Math.034"
    math_034.show_options = True
    math_034.operation = 'POWER'
    math_034.use_clamp = False
    # Value_001
    math_034.inputs[1].default_value = 0.5

    # Node Math.035
    math_035 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_035.name = "Math.035"
    math_035.show_options = True
    math_035.operation = 'MULTIPLY'
    math_035.use_clamp = False

    # Node Math.036
    math_036 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_036.name = "Math.036"
    math_036.show_options = True
    math_036.operation = 'COSINE'
    math_036.use_clamp = False

    # Node Math.037
    math_037 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_037.name = "Math.037"
    math_037.show_options = True
    math_037.operation = 'SINE'
    math_037.use_clamp = False

    # Node Math.038
    math_038 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_038.name = "Math.038"
    math_038.show_options = True
    math_038.operation = 'MULTIPLY'
    math_038.use_clamp = False

    # Node Math.039
    math_039 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_039.name = "Math.039"
    math_039.show_options = True
    math_039.operation = 'MULTIPLY'
    math_039.use_clamp = False

    # Node Combine XYZ.007
    combine_xyz_007 = ff_chamomile_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_007.name = "Combine XYZ.007"
    combine_xyz_007.show_options = True
    # Z
    combine_xyz_007.inputs[2].default_value = 0.0

    # Node Set Position.002
    set_position_002 = ff_chamomile_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position_002.name = "Set Position.002"
    set_position_002.show_options = True
    # Selection
    set_position_002.inputs[1].default_value = True
    # Offset
    set_position_002.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Random Value.002
    random_value_002 = ff_chamomile_nodes_1.nodes.new("FunctionNodeRandomValue")
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
    random_value_003 = ff_chamomile_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value_003.name = "Random Value.003"
    random_value_003.show_options = True
    random_value_003.data_type = 'FLOAT'
    # ID
    random_value_003.inputs[2].default_value = 0

    # Node Instance on Points.001
    instance_on_points_001 = ff_chamomile_nodes_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_001.name = "Instance on Points.001"
    instance_on_points_001.show_options = True
    # Selection
    instance_on_points_001.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_001.inputs[3].default_value = False
    # Instance Index
    instance_on_points_001.inputs[4].default_value = 0

    # Node Realize Instances.001
    realize_instances_001 = ff_chamomile_nodes_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_001.name = "Realize Instances.001"
    realize_instances_001.show_options = True
    realize_instances_001.realize_to_point_domain = False
    # Selection
    realize_instances_001.inputs[1].default_value = True
    # Realize All
    realize_instances_001.inputs[2].default_value = True
    # Depth
    realize_instances_001.inputs[3].default_value = 0

    # Node Set Material
    set_material = ff_chamomile_nodes_1.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.show_options = True
    # Selection
    set_material.inputs[1].default_value = True

    # Node Index
    index = ff_chamomile_nodes_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Store Named Attribute.006
    store_named_attribute_006 = ff_chamomile_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_006.name = "Store Named Attribute.006"
    store_named_attribute_006.show_options = True
    store_named_attribute_006.data_type = 'INT'
    store_named_attribute_006.domain = 'INSTANCE'
    # Selection
    store_named_attribute_006.inputs[1].default_value = True
    # Name
    store_named_attribute_006.inputs[2].default_value = "fractal_id"

    # Node Convex Hull
    convex_hull = ff_chamomile_nodes_1.nodes.new("GeometryNodeConvexHull")
    convex_hull.name = "Convex Hull"
    convex_hull.show_options = True

    # Node Set Shade Smooth.001
    set_shade_smooth_001 = ff_chamomile_nodes_1.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth_001.name = "Set Shade Smooth.001"
    set_shade_smooth_001.show_options = True
    set_shade_smooth_001.domain = 'FACE'
    # Selection
    set_shade_smooth_001.inputs[1].default_value = True
    # Shade Smooth
    set_shade_smooth_001.inputs[2].default_value = True

    # Node Sample Nearest Surface
    sample_nearest_surface = ff_chamomile_nodes_1.nodes.new("GeometryNodeSampleNearestSurface")
    sample_nearest_surface.name = "Sample Nearest Surface"
    sample_nearest_surface.show_options = True
    sample_nearest_surface.data_type = 'FLOAT_VECTOR'
    # Group ID
    sample_nearest_surface.inputs[2].default_value = 0
    # Sample Position
    sample_nearest_surface.inputs[3].default_value = (0.0, 0.0, 0.0)
    # Sample Group ID
    sample_nearest_surface.inputs[4].default_value = 0

    # Node Normal
    normal = ff_chamomile_nodes_1.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"
    normal.show_options = True
    normal.legacy_corner_normals = False

    # Node Math.040
    math_040 = ff_chamomile_nodes_1.nodes.new("ShaderNodeMath")
    math_040.name = "Math.040"
    math_040.show_options = True
    math_040.operation = 'SUBTRACT'
    math_040.use_clamp = False
    # Value
    math_040.inputs[0].default_value = 1.0

    # Node Vector Math
    vector_math = ff_chamomile_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.show_options = True
    vector_math.operation = 'SCALE'

    # Node Vector Math.001
    vector_math_001 = ff_chamomile_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.show_options = True
    vector_math_001.operation = 'SCALE'

    # Node Vector Math.002
    vector_math_002 = ff_chamomile_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.show_options = True
    vector_math_002.operation = 'ADD'

    # Node Vector Math.003
    vector_math_003 = ff_chamomile_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.show_options = True
    vector_math_003.operation = 'NORMALIZE'

    # Node Set Mesh Normal
    set_mesh_normal = ff_chamomile_nodes_1.nodes.new("GeometryNodeSetMeshNormal")
    set_mesh_normal.name = "Set Mesh Normal"
    set_mesh_normal.show_options = True
    set_mesh_normal.domain = 'CORNER'
    set_mesh_normal.mode = 'FREE'

    # Node Frame
    frame = ff_chamomile_nodes_1.nodes.new("NodeFrame")
    frame.label = "Auto-Odd Resolution"
    frame.name = "Frame"
    frame.use_custom_color = True
    frame.color = (0.30000001192092896, 0.20000000298023224, 0.20000000298023224)
    frame.show_options = True
    frame.label_size = 20
    frame.shrink = True

    # Node Frame.001
    frame_001 = ff_chamomile_nodes_1.nodes.new("NodeFrame")
    frame_001.label = "Petal Gen & Planar UV"
    frame_001.name = "Frame.001"
    frame_001.use_custom_color = True
    frame_001.color = (0.20000000298023224, 0.30000001192092896, 0.20000000298023224)
    frame_001.show_options = True
    frame_001.label_size = 20
    frame_001.shrink = True

    # Node Frame.002
    frame_002 = ff_chamomile_nodes_1.nodes.new("NodeFrame")
    frame_002.label = "Petal Instancing"
    frame_002.name = "Frame.002"
    frame_002.use_custom_color = True
    frame_002.color = (0.20000000298023224, 0.20000000298023224, 0.30000001192092896)
    frame_002.show_options = True
    frame_002.label_size = 20
    frame_002.shrink = True

    # Node Frame.003
    frame_003 = ff_chamomile_nodes_1.nodes.new("NodeFrame")
    frame_003.label = "Center Generation"
    frame_003.name = "Frame.003"
    frame_003.use_custom_color = True
    frame_003.color = (0.30000001192092896, 0.30000001192092896, 0.20000000298023224)
    frame_003.show_options = True
    frame_003.label_size = 20
    frame_003.shrink = True

    # Node Frame.004
    frame_004 = ff_chamomile_nodes_1.nodes.new("NodeFrame")
    frame_004.label = "Stem Generation"
    frame_004.name = "Frame.004"
    frame_004.use_custom_color = True
    frame_004.color = (0.20000000298023224, 0.30000001192092896, 0.30000001192092896)
    frame_004.show_options = True
    frame_004.label_size = 20
    frame_004.shrink = True

    # Node Frame.005
    frame_005 = ff_chamomile_nodes_1.nodes.new("NodeFrame")
    frame_005.label = "Flower Assembly & Z-Pivot"
    frame_005.name = "Frame.005"
    frame_005.use_custom_color = True
    frame_005.color = (0.30000001192092896, 0.20000000298023224, 0.30000001192092896)
    frame_005.show_options = True
    frame_005.label_size = 20
    frame_005.shrink = True

    # Node Frame.006
    frame_006 = ff_chamomile_nodes_1.nodes.new("NodeFrame")
    frame_006.label = "Field Distribution & Butcher ID"
    frame_006.name = "Frame.006"
    frame_006.use_custom_color = True
    frame_006.color = (0.4000000059604645, 0.20000000298023224, 0.20000000298023224)
    frame_006.show_options = True
    frame_006.label_size = 20
    frame_006.shrink = True

    # Node Frame.007
    frame_007 = ff_chamomile_nodes_1.nodes.new("NodeFrame")
    frame_007.label = "Stylized Normals Logic"
    frame_007.name = "Frame.007"
    frame_007.use_custom_color = True
    frame_007.color = (0.30000001192092896, 0.4000000059604645, 0.30000001192092896)
    frame_007.show_options = True
    frame_007.label_size = 20
    frame_007.shrink = True

    # Node Group Input.001
    group_input_001 = ff_chamomile_nodes_1.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.show_options = True

    # Node Group Input.002
    group_input_002 = ff_chamomile_nodes_1.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.show_options = True

    # Node Group Input.003
    group_input_003 = ff_chamomile_nodes_1.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.show_options = True

    # Node Reroute
    reroute = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketFloat"
    # Node Reroute.001
    reroute_001 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketFloat"
    # Node Group Input.004
    group_input_004 = ff_chamomile_nodes_1.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.show_options = True

    # Node Reroute.002
    reroute_002 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketFloat"
    # Node Reroute.003
    reroute_003 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketInt"
    # Node Group Input.005
    group_input_005 = ff_chamomile_nodes_1.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.show_options = True

    # Node Reroute.004
    reroute_004 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    reroute_004.socket_idname = "NodeSocketFloat"
    # Node Reroute.005
    reroute_005 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.show_options = True
    reroute_005.socket_idname = "NodeSocketFloat"
    # Node Reroute.006
    reroute_006 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.show_options = True
    reroute_006.socket_idname = "NodeSocketFloat"
    # Node Reroute.007
    reroute_007 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.show_options = True
    reroute_007.socket_idname = "NodeSocketFloat"
    # Node Reroute.008
    reroute_008 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.show_options = True
    reroute_008.socket_idname = "NodeSocketFloat"
    # Node Reroute.009
    reroute_009 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.show_options = True
    reroute_009.socket_idname = "NodeSocketFloat"
    # Node Group Input.006
    group_input_006 = ff_chamomile_nodes_1.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.show_options = True

    # Node Reroute.010
    reroute_010 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.show_options = True
    reroute_010.socket_idname = "NodeSocketColor"
    # Node Group Input.007
    group_input_007 = ff_chamomile_nodes_1.nodes.new("NodeGroupInput")
    group_input_007.name = "Group Input.007"
    group_input_007.show_options = True

    # Node Group Input.008
    group_input_008 = ff_chamomile_nodes_1.nodes.new("NodeGroupInput")
    group_input_008.name = "Group Input.008"
    group_input_008.show_options = True

    # Node Reroute.011
    reroute_011 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"
    reroute_011.show_options = True
    reroute_011.socket_idname = "NodeSocketInt"
    # Node Reroute.012
    reroute_012 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    reroute_012.show_options = True
    reroute_012.socket_idname = "NodeSocketInt"
    # Node Reroute.013
    reroute_013 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    reroute_013.show_options = True
    reroute_013.socket_idname = "NodeSocketVector"
    # Node Reroute.014
    reroute_014 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_014.name = "Reroute.014"
    reroute_014.show_options = True
    reroute_014.socket_idname = "NodeSocketVector"
    # Node Reroute.015
    reroute_015 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_015.name = "Reroute.015"
    reroute_015.show_options = True
    reroute_015.socket_idname = "NodeSocketColor"
    # Node Reroute.016
    reroute_016 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_016.name = "Reroute.016"
    reroute_016.show_options = True
    reroute_016.socket_idname = "NodeSocketColor"
    # Node Group Input.009
    group_input_009 = ff_chamomile_nodes_1.nodes.new("NodeGroupInput")
    group_input_009.name = "Group Input.009"
    group_input_009.show_options = True

    # Node Group Input.010
    group_input_010 = ff_chamomile_nodes_1.nodes.new("NodeGroupInput")
    group_input_010.name = "Group Input.010"
    group_input_010.show_options = True

    # Node Normal.001
    normal_001 = ff_chamomile_nodes_1.nodes.new("GeometryNodeInputNormal")
    normal_001.name = "Normal.001"
    normal_001.show_options = True
    normal_001.legacy_corner_normals = False

    # Node Reroute.017
    reroute_017 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_017.name = "Reroute.017"
    reroute_017.show_options = True
    reroute_017.socket_idname = "NodeSocketMaterial"
    # Node Reroute.018
    reroute_018 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_018.name = "Reroute.018"
    reroute_018.show_options = True
    reroute_018.socket_idname = "NodeSocketGeometry"
    # Node Reroute.019
    reroute_019 = ff_chamomile_nodes_1.nodes.new("NodeReroute")
    reroute_019.name = "Reroute.019"
    reroute_019.show_options = True
    reroute_019.socket_idname = "NodeSocketGeometry"
    # Set parents
    ff_chamomile_nodes_1.nodes["Group Input"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Math"].parent = ff_chamomile_nodes_1.nodes["Frame"]
    ff_chamomile_nodes_1.nodes["Math.001"].parent = ff_chamomile_nodes_1.nodes["Frame"]
    ff_chamomile_nodes_1.nodes["Math.002"].parent = ff_chamomile_nodes_1.nodes["Frame"]
    ff_chamomile_nodes_1.nodes["Math.003"].parent = ff_chamomile_nodes_1.nodes["Frame"]
    ff_chamomile_nodes_1.nodes["Math.004"].parent = ff_chamomile_nodes_1.nodes["Frame"]
    ff_chamomile_nodes_1.nodes["Grid"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Position"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Separate XYZ"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Map Range"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Float Curve"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Math.005"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Map Range.001"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Math.006"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Math.007"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Math.008"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Math.009"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Math.010"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Math.011"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Math.012"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Math.013"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Math.014"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Math.015"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Map Range.002"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Map Range.003"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Combine XYZ"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Store Named Attribute"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Store Named Attribute.001"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Math.016"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Float Curve.001"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Math.017"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Float Curve.002"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Math.018"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Float Curve.003"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Math.019"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Math.020"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Combine XYZ.001"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Set Position"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Transform Geometry"].parent = ff_chamomile_nodes_1.nodes["Frame.002"]
    ff_chamomile_nodes_1.nodes["Mesh Circle"].parent = ff_chamomile_nodes_1.nodes["Frame.002"]
    ff_chamomile_nodes_1.nodes["Position.001"].parent = ff_chamomile_nodes_1.nodes["Frame.002"]
    ff_chamomile_nodes_1.nodes["Align Euler to Vector"].parent = ff_chamomile_nodes_1.nodes["Frame.002"]
    ff_chamomile_nodes_1.nodes["Combine XYZ.002"].parent = ff_chamomile_nodes_1.nodes["Frame.002"]
    ff_chamomile_nodes_1.nodes["Instance on Points"].parent = ff_chamomile_nodes_1.nodes["Frame.002"]
    ff_chamomile_nodes_1.nodes["Realize Instances"].parent = ff_chamomile_nodes_1.nodes["Frame.002"]
    ff_chamomile_nodes_1.nodes["Ico Sphere"].parent = ff_chamomile_nodes_1.nodes["Frame.003"]
    ff_chamomile_nodes_1.nodes["Position.002"].parent = ff_chamomile_nodes_1.nodes["Frame.003"]
    ff_chamomile_nodes_1.nodes["Separate XYZ.001"].parent = ff_chamomile_nodes_1.nodes["Frame.003"]
    ff_chamomile_nodes_1.nodes["Map Range.004"].parent = ff_chamomile_nodes_1.nodes["Frame.003"]
    ff_chamomile_nodes_1.nodes["Map Range.005"].parent = ff_chamomile_nodes_1.nodes["Frame.003"]
    ff_chamomile_nodes_1.nodes["Combine XYZ.003"].parent = ff_chamomile_nodes_1.nodes["Frame.003"]
    ff_chamomile_nodes_1.nodes["Store Named Attribute.002"].parent = ff_chamomile_nodes_1.nodes["Frame.003"]
    ff_chamomile_nodes_1.nodes["Store Named Attribute.003"].parent = ff_chamomile_nodes_1.nodes["Frame.003"]
    ff_chamomile_nodes_1.nodes["Transform Geometry.001"].parent = ff_chamomile_nodes_1.nodes["Frame.003"]
    ff_chamomile_nodes_1.nodes["Grid.001"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Math.021"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Position.003"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Separate XYZ.002"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Map Range.006"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Math.022"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Map Range.007"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Combine XYZ.004"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Store Named Attribute.004"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Math.023"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Math.024"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Math.025"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Math.026"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Math.027"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Math.028"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Math.029"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Math.030"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Combine XYZ.005"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Set Position.001"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Merge by Distance"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Flip Faces"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Store Named Attribute.005"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Join Geometry"].parent = ff_chamomile_nodes_1.nodes["Frame.005"]
    ff_chamomile_nodes_1.nodes["Set Shade Smooth"].parent = ff_chamomile_nodes_1.nodes["Frame.005"]
    ff_chamomile_nodes_1.nodes["Combine XYZ.006"].parent = ff_chamomile_nodes_1.nodes["Frame.005"]
    ff_chamomile_nodes_1.nodes["Transform Geometry.002"].parent = ff_chamomile_nodes_1.nodes["Frame.005"]
    ff_chamomile_nodes_1.nodes["Points"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Math.031"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Math.032"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Math.033"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Random Value"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Random Value.001"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Math.034"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Math.035"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Math.036"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Math.037"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Math.038"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Math.039"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Combine XYZ.007"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Set Position.002"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Random Value.002"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Random Value.003"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Instance on Points.001"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Realize Instances.001"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Set Material"].parent = ff_chamomile_nodes_1.nodes["Frame.007"]
    ff_chamomile_nodes_1.nodes["Index"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Store Named Attribute.006"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Convex Hull"].parent = ff_chamomile_nodes_1.nodes["Frame.007"]
    ff_chamomile_nodes_1.nodes["Set Shade Smooth.001"].parent = ff_chamomile_nodes_1.nodes["Frame.007"]
    ff_chamomile_nodes_1.nodes["Sample Nearest Surface"].parent = ff_chamomile_nodes_1.nodes["Frame.007"]
    ff_chamomile_nodes_1.nodes["Normal"].parent = ff_chamomile_nodes_1.nodes["Frame.007"]
    ff_chamomile_nodes_1.nodes["Math.040"].parent = ff_chamomile_nodes_1.nodes["Frame.007"]
    ff_chamomile_nodes_1.nodes["Vector Math"].parent = ff_chamomile_nodes_1.nodes["Frame.007"]
    ff_chamomile_nodes_1.nodes["Vector Math.001"].parent = ff_chamomile_nodes_1.nodes["Frame.007"]
    ff_chamomile_nodes_1.nodes["Vector Math.002"].parent = ff_chamomile_nodes_1.nodes["Frame.007"]
    ff_chamomile_nodes_1.nodes["Vector Math.003"].parent = ff_chamomile_nodes_1.nodes["Frame.007"]
    ff_chamomile_nodes_1.nodes["Set Mesh Normal"].parent = ff_chamomile_nodes_1.nodes["Frame.007"]
    ff_chamomile_nodes_1.nodes["Group Input.001"].parent = ff_chamomile_nodes_1.nodes["Frame"]
    ff_chamomile_nodes_1.nodes["Group Input.002"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Group Input.003"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Reroute"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Reroute.001"].parent = ff_chamomile_nodes_1.nodes["Frame.001"]
    ff_chamomile_nodes_1.nodes["Group Input.004"].parent = ff_chamomile_nodes_1.nodes["Frame.002"]
    ff_chamomile_nodes_1.nodes["Reroute.002"].parent = ff_chamomile_nodes_1.nodes["Frame.002"]
    ff_chamomile_nodes_1.nodes["Reroute.003"].parent = ff_chamomile_nodes_1.nodes["Frame.002"]
    ff_chamomile_nodes_1.nodes["Group Input.005"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Reroute.004"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Reroute.005"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Reroute.006"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Reroute.007"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Reroute.008"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Reroute.009"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Group Input.006"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Reroute.010"].parent = ff_chamomile_nodes_1.nodes["Frame.004"]
    ff_chamomile_nodes_1.nodes["Group Input.007"].parent = ff_chamomile_nodes_1.nodes["Frame.003"]
    ff_chamomile_nodes_1.nodes["Group Input.008"].parent = ff_chamomile_nodes_1.nodes["Frame.005"]
    ff_chamomile_nodes_1.nodes["Reroute.011"].parent = ff_chamomile_nodes_1.nodes["Frame.003"]
    ff_chamomile_nodes_1.nodes["Reroute.012"].parent = ff_chamomile_nodes_1.nodes["Frame.003"]
    ff_chamomile_nodes_1.nodes["Reroute.013"].parent = ff_chamomile_nodes_1.nodes["Frame.003"]
    ff_chamomile_nodes_1.nodes["Reroute.014"].parent = ff_chamomile_nodes_1.nodes["Frame.003"]
    ff_chamomile_nodes_1.nodes["Reroute.015"].parent = ff_chamomile_nodes_1.nodes["Frame.003"]
    ff_chamomile_nodes_1.nodes["Reroute.016"].parent = ff_chamomile_nodes_1.nodes["Frame.003"]
    ff_chamomile_nodes_1.nodes["Group Input.009"].parent = ff_chamomile_nodes_1.nodes["Frame.007"]
    ff_chamomile_nodes_1.nodes["Group Input.010"].parent = ff_chamomile_nodes_1.nodes["Frame.006"]
    ff_chamomile_nodes_1.nodes["Normal.001"].parent = ff_chamomile_nodes_1.nodes["Frame.007"]
    ff_chamomile_nodes_1.nodes["Reroute.017"].parent = ff_chamomile_nodes_1.nodes["Frame.007"]
    ff_chamomile_nodes_1.nodes["Reroute.018"].parent = ff_chamomile_nodes_1.nodes["Frame.007"]
    ff_chamomile_nodes_1.nodes["Reroute.019"].parent = ff_chamomile_nodes_1.nodes["Frame.007"]

    # Set locations
    ff_chamomile_nodes_1.nodes["Group Input"].location = (683.3284301757812, -642.1710205078125)
    ff_chamomile_nodes_1.nodes["Group Output"].location = (3245.453857421875, -764.76953125)
    ff_chamomile_nodes_1.nodes["Math"].location = (195.5732421875, -333.5994567871094)
    ff_chamomile_nodes_1.nodes["Math.001"].location = (356.14453125, -258.18212890625)
    ff_chamomile_nodes_1.nodes["Math.002"].location = (518.791015625, -184.84039306640625)
    ff_chamomile_nodes_1.nodes["Math.003"].location = (679.3623046875, -111.49835205078125)
    ff_chamomile_nodes_1.nodes["Math.004"].location = (841.74853515625, -36.36444091796875)
    ff_chamomile_nodes_1.nodes["Grid"].location = (1784.591064453125, -305.30706787109375)
    ff_chamomile_nodes_1.nodes["Position"].location = (31.07373046875, -1097.369384765625)
    ff_chamomile_nodes_1.nodes["Separate XYZ"].location = (29.69482421875, -971.841552734375)
    ff_chamomile_nodes_1.nodes["Map Range"].location = (353.91162109375, -760.5775756835938)
    ff_chamomile_nodes_1.nodes["Float Curve"].location = (513.00341796875, -1015.8116455078125)
    ff_chamomile_nodes_1.nodes["Math.005"].location = (957.115234375, -899.3009033203125)
    ff_chamomile_nodes_1.nodes["Map Range.001"].location = (960.34033203125, -652.718994140625)
    ff_chamomile_nodes_1.nodes["Math.006"].location = (194.09912109375, -699.5013427734375)
    ff_chamomile_nodes_1.nodes["Math.007"].location = (356.13525390625, -604.321044921875)
    ff_chamomile_nodes_1.nodes["Math.008"].location = (807.00390625, -527.9920654296875)
    ff_chamomile_nodes_1.nodes["Math.009"].location = (964.4892578125, -453.7134704589844)
    ff_chamomile_nodes_1.nodes["Math.010"].location = (1138.247802734375, -579.0774536132812)
    ff_chamomile_nodes_1.nodes["Math.011"].location = (1136.2119140625, -737.4537353515625)
    ff_chamomile_nodes_1.nodes["Math.012"].location = (1304.00390625, -602.9369506835938)
    ff_chamomile_nodes_1.nodes["Math.013"].location = (1145.369140625, -918.0924682617188)
    ff_chamomile_nodes_1.nodes["Math.014"].location = (1305.13232421875, -823.2689819335938)
    ff_chamomile_nodes_1.nodes["Math.015"].location = (1462.342529296875, -749.4677734375)
    ff_chamomile_nodes_1.nodes["Map Range.002"].location = (1464.63232421875, -502.34033203125)
    ff_chamomile_nodes_1.nodes["Map Range.003"].location = (1617.41064453125, -549.7914428710938)
    ff_chamomile_nodes_1.nodes["Combine XYZ"].location = (1781.252685546875, -476.33221435546875)
    ff_chamomile_nodes_1.nodes["Store Named Attribute"].location = (1959.8642578125, -255.01976013183594)
    ff_chamomile_nodes_1.nodes["Store Named Attribute.001"].location = (2120.800048828125, -254.5054473876953)
    ff_chamomile_nodes_1.nodes["Math.016"].location = (291.244140625, -1618.700439453125)
    ff_chamomile_nodes_1.nodes["Float Curve.001"].location = (453.4580078125, -1357.194091796875)
    ff_chamomile_nodes_1.nodes["Math.017"].location = (793.61083984375, -1132.3250732421875)
    ff_chamomile_nodes_1.nodes["Float Curve.002"].location = (795.9814453125, -1286.883544921875)
    ff_chamomile_nodes_1.nodes["Math.018"].location = (1146.819580078125, -1058.264892578125)
    ff_chamomile_nodes_1.nodes["Float Curve.003"].location = (799.81396484375, -1609.4947509765625)
    ff_chamomile_nodes_1.nodes["Math.019"].location = (1145.922607421875, -1216.0574951171875)
    ff_chamomile_nodes_1.nodes["Math.020"].location = (1471.18701171875, -983.4398193359375)
    ff_chamomile_nodes_1.nodes["Combine XYZ.001"].location = (1636.561279296875, -913.892822265625)
    ff_chamomile_nodes_1.nodes["Set Position"].location = (2289.796142578125, -306.3153076171875)
    ff_chamomile_nodes_1.nodes["Transform Geometry"].location = (207.671875, -194.62599182128906)
    ff_chamomile_nodes_1.nodes["Mesh Circle"].location = (378.380859375, -35.86833190917969)
    ff_chamomile_nodes_1.nodes["Position.001"].location = (207.29541015625, -725.2239990234375)
    ff_chamomile_nodes_1.nodes["Align Euler to Vector"].location = (209.1181640625, -541.3270263671875)
    ff_chamomile_nodes_1.nodes["Combine XYZ.002"].location = (208.57373046875, -789.2216796875)
    ff_chamomile_nodes_1.nodes["Instance on Points"].location = (541.770751953125, -122.61550903320312)
    ff_chamomile_nodes_1.nodes["Realize Instances"].location = (699.521240234375, -122.88189697265625)
    ff_chamomile_nodes_1.nodes["Ico Sphere"].location = (571.9495849609375, -166.01992797851562)
    ff_chamomile_nodes_1.nodes["Position.002"].location = (207.96337890625, -305.0627136230469)
    ff_chamomile_nodes_1.nodes["Separate XYZ.001"].location = (208.97705078125, -180.28945922851562)
    ff_chamomile_nodes_1.nodes["Map Range.004"].location = (391.6717529296875, -79.7161865234375)
    ff_chamomile_nodes_1.nodes["Map Range.005"].location = (390.990478515625, -338.1849060058594)
    ff_chamomile_nodes_1.nodes["Combine XYZ.003"].location = (570.408203125, -290.3843688964844)
    ff_chamomile_nodes_1.nodes["Store Named Attribute.002"].location = (732.8946533203125, -115.7177734375)
    ff_chamomile_nodes_1.nodes["Store Named Attribute.003"].location = (889.43017578125, -115.7177734375)
    ff_chamomile_nodes_1.nodes["Transform Geometry.001"].location = (1045.3326416015625, -168.43258666992188)
    ff_chamomile_nodes_1.nodes["Grid.001"].location = (788.9276123046875, -178.9661865234375)
    ff_chamomile_nodes_1.nodes["Math.021"].location = (618.34228515625, -123.8685302734375)
    ff_chamomile_nodes_1.nodes["Position.003"].location = (30.29833984375, -859.2117919921875)
    ff_chamomile_nodes_1.nodes["Separate XYZ.002"].location = (31.69482421875, -730.0711669921875)
    ff_chamomile_nodes_1.nodes["Map Range.006"].location = (603.9423828125, -528.5159912109375)
    ff_chamomile_nodes_1.nodes["Math.022"].location = (444.64697265625, -1059.853759765625)
    ff_chamomile_nodes_1.nodes["Map Range.007"].location = (601.275390625, -961.2093505859375)
    ff_chamomile_nodes_1.nodes["Combine XYZ.004"].location = (782.7135009765625, -503.9085693359375)
    ff_chamomile_nodes_1.nodes["Store Named Attribute.004"].location = (945.8997802734375, -129.7864990234375)
    ff_chamomile_nodes_1.nodes["Math.023"].location = (206.244140625, -620.2635498046875)
    ff_chamomile_nodes_1.nodes["Math.024"].location = (369.90380859375, -545.1893310546875)
    ff_chamomile_nodes_1.nodes["Math.025"].location = (606.39404296875, -376.2640380859375)
    ff_chamomile_nodes_1.nodes["Math.026"].location = (785.2471923828125, -348.3514404296875)
    ff_chamomile_nodes_1.nodes["Math.027"].location = (601.455078125, -802.1898193359375)
    ff_chamomile_nodes_1.nodes["Math.028"].location = (780.7943115234375, -784.4822998046875)
    ff_chamomile_nodes_1.nodes["Math.029"].location = (605.2880859375, -1208.686767578125)
    ff_chamomile_nodes_1.nodes["Math.030"].location = (781.6844482421875, -628.3792724609375)
    ff_chamomile_nodes_1.nodes["Combine XYZ.005"].location = (945.0255126953125, -322.3211669921875)
    ff_chamomile_nodes_1.nodes["Set Position.001"].location = (1103.4459228515625, -180.8978271484375)
    ff_chamomile_nodes_1.nodes["Merge by Distance"].location = (1263.7569580078125, -180.8973388671875)
    ff_chamomile_nodes_1.nodes["Flip Faces"].location = (1422.1776123046875, -181.8416748046875)
    ff_chamomile_nodes_1.nodes["Store Named Attribute.005"].location = (1588.0970458984375, -131.0443115234375)
    ff_chamomile_nodes_1.nodes["Join Geometry"].location = (32.48443603515625, -59.4708251953125)
    ff_chamomile_nodes_1.nodes["Set Shade Smooth"].location = (203.12164306640625, -36.25732421875)
    ff_chamomile_nodes_1.nodes["Combine XYZ.006"].location = (201.60504150390625, -164.62646484375)
    ff_chamomile_nodes_1.nodes["Transform Geometry.002"].location = (365.6318359375, -62.2158203125)
    ff_chamomile_nodes_1.nodes["Points"].location = (990.6073608398438, -407.6341552734375)
    ff_chamomile_nodes_1.nodes["Math.031"].location = (201.6865692138672, -445.572021484375)
    ff_chamomile_nodes_1.nodes["Math.032"].location = (1007.3724975585938, -946.0313720703125)
    ff_chamomile_nodes_1.nodes["Math.033"].location = (847.3890991210938, -774.3387451171875)
    ff_chamomile_nodes_1.nodes["Random Value"].location = (523.6610717773438, -79.9345703125)
    ff_chamomile_nodes_1.nodes["Random Value.001"].location = (362.97113037109375, -329.405517578125)
    ff_chamomile_nodes_1.nodes["Math.034"].location = (527.0391235351562, -256.82373046875)
    ff_chamomile_nodes_1.nodes["Math.035"].location = (685.9688110351562, -182.8133544921875)
    ff_chamomile_nodes_1.nodes["Math.036"].location = (685.3003540039062, -44.5213623046875)
    ff_chamomile_nodes_1.nodes["Math.037"].location = (679.6159057617188, -339.674072265625)
    ff_chamomile_nodes_1.nodes["Math.038"].location = (848.7843627929688, -86.439697265625)
    ff_chamomile_nodes_1.nodes["Math.039"].location = (846.6830444335938, -239.986328125)
    ff_chamomile_nodes_1.nodes["Combine XYZ.007"].location = (1018.6677856445312, -61.685791015625)
    ff_chamomile_nodes_1.nodes["Set Position.002"].location = (1154.635009765625, -409.8353271484375)
    ff_chamomile_nodes_1.nodes["Random Value.002"].location = (1163.888916015625, -706.735595703125)
    ff_chamomile_nodes_1.nodes["Random Value.003"].location = (1010.7815551757812, -660.2452392578125)
    ff_chamomile_nodes_1.nodes["Instance on Points.001"].location = (1320.04052734375, -504.001953125)
    ff_chamomile_nodes_1.nodes["Realize Instances.001"].location = (1637.59716796875, -366.58941650390625)
    ff_chamomile_nodes_1.nodes["Set Material"].location = (1464.708740234375, -762.6322631835938)
    ff_chamomile_nodes_1.nodes["Index"].location = (1315.85107421875, -432.873779296875)
    ff_chamomile_nodes_1.nodes["Store Named Attribute.006"].location = (1472.431640625, -314.5599365234375)
    ff_chamomile_nodes_1.nodes["Convex Hull"].location = (29.654541015625, -674.0294189453125)
    ff_chamomile_nodes_1.nodes["Set Shade Smooth.001"].location = (210.86181640625, -650.89599609375)
    ff_chamomile_nodes_1.nodes["Sample Nearest Surface"].location = (399.909423828125, -604.498046875)
    ff_chamomile_nodes_1.nodes["Normal"].location = (210.0263671875, -775.4783935546875)
    ff_chamomile_nodes_1.nodes["Math.040"].location = (634.564453125, -235.06503295898438)
    ff_chamomile_nodes_1.nodes["Vector Math"].location = (791.042724609375, -163.37667846679688)
    ff_chamomile_nodes_1.nodes["Vector Math.001"].location = (627.5634765625, -386.8337097167969)
    ff_chamomile_nodes_1.nodes["Vector Math.002"].location = (956.0341796875, -314.9386291503906)
    ff_chamomile_nodes_1.nodes["Vector Math.003"].location = (1116.5400390625, -266.32965087890625)
    ff_chamomile_nodes_1.nodes["Set Mesh Normal"].location = (1303.316650390625, -710.9303588867188)
    ff_chamomile_nodes_1.nodes["Frame"].location = (-4680.0, 794.0)
    ff_chamomile_nodes_1.nodes["Frame.001"].location = (-5222.0, 76.0)
    ff_chamomile_nodes_1.nodes["Frame.002"].location = (-1853.0, -39.0)
    ff_chamomile_nodes_1.nodes["Frame.003"].location = (-2200.0, 614.0)
    ff_chamomile_nodes_1.nodes["Frame.004"].location = (-2743.0, -988.0)
    ff_chamomile_nodes_1.nodes["Frame.005"].location = (-887.0, -1112.0)
    ff_chamomile_nodes_1.nodes["Frame.006"].location = (-323.0, -603.0)
    ff_chamomile_nodes_1.nodes["Frame.007"].location = (1585.0, -2.0)
    ff_chamomile_nodes_1.nodes["Group Input.001"].location = (29.6357421875, -121.974609375)
    ff_chamomile_nodes_1.nodes["Group Input.002"].location = (1302.88916015625, -36.248046875)
    ff_chamomile_nodes_1.nodes["Group Input.003"].location = (550.1748046875, -1682.2454833984375)
    ff_chamomile_nodes_1.nodes["Reroute"].location = (1034.62841796875, -2067.394775390625)
    ff_chamomile_nodes_1.nodes["Reroute.001"].location = (740.5302734375, -796.3060913085938)
    ff_chamomile_nodes_1.nodes["Group Input.004"].location = (29.54931640625, -351.0084228515625)
    ff_chamomile_nodes_1.nodes["Reroute.002"].location = (207.1572265625, -143.4286651611328)
    ff_chamomile_nodes_1.nodes["Reroute.003"].location = (192.675048828125, -120.25218200683594)
    ff_chamomile_nodes_1.nodes["Group Input.005"].location = (35.42919921875, -937.1595458984375)
    ff_chamomile_nodes_1.nodes["Reroute.004"].location = (739.3785400390625, -783.0355224609375)
    ff_chamomile_nodes_1.nodes["Reroute.005"].location = (618.18896484375, -783.8343505859375)
    ff_chamomile_nodes_1.nodes["Reroute.006"].location = (735.5882568359375, -941.2669677734375)
    ff_chamomile_nodes_1.nodes["Reroute.007"].location = (276.880859375, -945.5814208984375)
    ff_chamomile_nodes_1.nodes["Reroute.008"].location = (735.9158935546875, -516.3538818359375)
    ff_chamomile_nodes_1.nodes["Reroute.009"].location = (610.357421875, -517.7952880859375)
    ff_chamomile_nodes_1.nodes["Group Input.006"].location = (208.7890625, -35.8763427734375)
    ff_chamomile_nodes_1.nodes["Reroute.010"].location = (1421.8165283203125, -1453.483154296875)
    ff_chamomile_nodes_1.nodes["Group Input.007"].location = (29.655029296875, -35.9237060546875)
    ff_chamomile_nodes_1.nodes["Group Input.008"].location = (30.3787841796875, -127.010498046875)
    ff_chamomile_nodes_1.nodes["Reroute.011"].location = (217.000732421875, -66.1998291015625)
    ff_chamomile_nodes_1.nodes["Reroute.012"].location = (529.1322021484375, -66.6624755859375)
    ff_chamomile_nodes_1.nodes["Reroute.013"].location = (857.2335205078125, -599.5540161132812)
    ff_chamomile_nodes_1.nodes["Reroute.014"].location = (222.529052734375, -600.3551025390625)
    ff_chamomile_nodes_1.nodes["Reroute.015"].location = (266.319091796875, -586.9317626953125)
    ff_chamomile_nodes_1.nodes["Reroute.016"].location = (833.600341796875, -586.9383544921875)
    ff_chamomile_nodes_1.nodes["Group Input.009"].location = (398.83203125, -35.76483917236328)
    ff_chamomile_nodes_1.nodes["Group Input.010"].location = (29.72076416015625, -35.78936767578125)
    ff_chamomile_nodes_1.nodes["Normal.001"].location = (633.925048828125, -156.00070190429688)
    ff_chamomile_nodes_1.nodes["Reroute.017"].location = (677.87939453125, -845.4035034179688)
    ff_chamomile_nodes_1.nodes["Reroute.018"].location = (50.6099853515625, -874.7075805664062)
    ff_chamomile_nodes_1.nodes["Reroute.019"].location = (1246.7685546875, -868.5105590820312)

    # Set dimensions
    ff_chamomile_nodes_1.nodes["Group Input"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Group Input"].height = 100.0

    ff_chamomile_nodes_1.nodes["Group Output"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Group Output"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.001"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.002"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.002"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.003"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.003"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.004"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.004"].height = 100.0

    ff_chamomile_nodes_1.nodes["Grid"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Grid"].height = 100.0

    ff_chamomile_nodes_1.nodes["Position"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Position"].height = 100.0

    ff_chamomile_nodes_1.nodes["Separate XYZ"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Separate XYZ"].height = 100.0

    ff_chamomile_nodes_1.nodes["Map Range"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Map Range"].height = 100.0

    ff_chamomile_nodes_1.nodes["Float Curve"].width  = 240.0
    ff_chamomile_nodes_1.nodes["Float Curve"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.005"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.005"].height = 100.0

    ff_chamomile_nodes_1.nodes["Map Range.001"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Map Range.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.006"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.006"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.007"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.007"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.008"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.008"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.009"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.009"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.010"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.010"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.011"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.011"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.012"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.012"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.013"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.013"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.014"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.014"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.015"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.015"].height = 100.0

    ff_chamomile_nodes_1.nodes["Map Range.002"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Map Range.002"].height = 100.0

    ff_chamomile_nodes_1.nodes["Map Range.003"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Map Range.003"].height = 100.0

    ff_chamomile_nodes_1.nodes["Combine XYZ"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Combine XYZ"].height = 100.0

    ff_chamomile_nodes_1.nodes["Store Named Attribute"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Store Named Attribute"].height = 100.0

    ff_chamomile_nodes_1.nodes["Store Named Attribute.001"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Store Named Attribute.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.016"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.016"].height = 100.0

    ff_chamomile_nodes_1.nodes["Float Curve.001"].width  = 240.0
    ff_chamomile_nodes_1.nodes["Float Curve.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.017"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.017"].height = 100.0

    ff_chamomile_nodes_1.nodes["Float Curve.002"].width  = 240.0
    ff_chamomile_nodes_1.nodes["Float Curve.002"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.018"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.018"].height = 100.0

    ff_chamomile_nodes_1.nodes["Float Curve.003"].width  = 240.0
    ff_chamomile_nodes_1.nodes["Float Curve.003"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.019"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.019"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.020"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.020"].height = 100.0

    ff_chamomile_nodes_1.nodes["Combine XYZ.001"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Combine XYZ.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Set Position"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Set Position"].height = 100.0

    ff_chamomile_nodes_1.nodes["Transform Geometry"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Transform Geometry"].height = 100.0

    ff_chamomile_nodes_1.nodes["Mesh Circle"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Mesh Circle"].height = 100.0

    ff_chamomile_nodes_1.nodes["Position.001"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Position.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Align Euler to Vector"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Align Euler to Vector"].height = 100.0

    ff_chamomile_nodes_1.nodes["Combine XYZ.002"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Combine XYZ.002"].height = 100.0

    ff_chamomile_nodes_1.nodes["Instance on Points"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Instance on Points"].height = 100.0

    ff_chamomile_nodes_1.nodes["Realize Instances"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Realize Instances"].height = 100.0

    ff_chamomile_nodes_1.nodes["Ico Sphere"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Ico Sphere"].height = 100.0

    ff_chamomile_nodes_1.nodes["Position.002"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Position.002"].height = 100.0

    ff_chamomile_nodes_1.nodes["Separate XYZ.001"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Separate XYZ.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Map Range.004"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Map Range.004"].height = 100.0

    ff_chamomile_nodes_1.nodes["Map Range.005"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Map Range.005"].height = 100.0

    ff_chamomile_nodes_1.nodes["Combine XYZ.003"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Combine XYZ.003"].height = 100.0

    ff_chamomile_nodes_1.nodes["Store Named Attribute.002"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Store Named Attribute.002"].height = 100.0

    ff_chamomile_nodes_1.nodes["Store Named Attribute.003"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Store Named Attribute.003"].height = 100.0

    ff_chamomile_nodes_1.nodes["Transform Geometry.001"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Transform Geometry.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Grid.001"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Grid.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.021"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.021"].height = 100.0

    ff_chamomile_nodes_1.nodes["Position.003"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Position.003"].height = 100.0

    ff_chamomile_nodes_1.nodes["Separate XYZ.002"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Separate XYZ.002"].height = 100.0

    ff_chamomile_nodes_1.nodes["Map Range.006"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Map Range.006"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.022"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.022"].height = 100.0

    ff_chamomile_nodes_1.nodes["Map Range.007"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Map Range.007"].height = 100.0

    ff_chamomile_nodes_1.nodes["Combine XYZ.004"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Combine XYZ.004"].height = 100.0

    ff_chamomile_nodes_1.nodes["Store Named Attribute.004"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Store Named Attribute.004"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.023"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.023"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.024"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.024"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.025"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.025"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.026"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.026"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.027"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.027"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.028"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.028"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.029"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.029"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.030"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.030"].height = 100.0

    ff_chamomile_nodes_1.nodes["Combine XYZ.005"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Combine XYZ.005"].height = 100.0

    ff_chamomile_nodes_1.nodes["Set Position.001"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Set Position.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Merge by Distance"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Merge by Distance"].height = 100.0

    ff_chamomile_nodes_1.nodes["Flip Faces"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Flip Faces"].height = 100.0

    ff_chamomile_nodes_1.nodes["Store Named Attribute.005"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Store Named Attribute.005"].height = 100.0

    ff_chamomile_nodes_1.nodes["Join Geometry"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Join Geometry"].height = 100.0

    ff_chamomile_nodes_1.nodes["Set Shade Smooth"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Set Shade Smooth"].height = 100.0

    ff_chamomile_nodes_1.nodes["Combine XYZ.006"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Combine XYZ.006"].height = 100.0

    ff_chamomile_nodes_1.nodes["Transform Geometry.002"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Transform Geometry.002"].height = 100.0

    ff_chamomile_nodes_1.nodes["Points"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Points"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.031"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.031"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.032"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.032"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.033"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.033"].height = 100.0

    ff_chamomile_nodes_1.nodes["Random Value"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Random Value"].height = 100.0

    ff_chamomile_nodes_1.nodes["Random Value.001"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Random Value.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.034"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.034"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.035"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.035"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.036"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.036"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.037"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.037"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.038"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.038"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.039"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.039"].height = 100.0

    ff_chamomile_nodes_1.nodes["Combine XYZ.007"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Combine XYZ.007"].height = 100.0

    ff_chamomile_nodes_1.nodes["Set Position.002"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Set Position.002"].height = 100.0

    ff_chamomile_nodes_1.nodes["Random Value.002"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Random Value.002"].height = 100.0

    ff_chamomile_nodes_1.nodes["Random Value.003"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Random Value.003"].height = 100.0

    ff_chamomile_nodes_1.nodes["Instance on Points.001"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Instance on Points.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Realize Instances.001"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Realize Instances.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Set Material"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Set Material"].height = 100.0

    ff_chamomile_nodes_1.nodes["Index"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Index"].height = 100.0

    ff_chamomile_nodes_1.nodes["Store Named Attribute.006"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Store Named Attribute.006"].height = 100.0

    ff_chamomile_nodes_1.nodes["Convex Hull"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Convex Hull"].height = 100.0

    ff_chamomile_nodes_1.nodes["Set Shade Smooth.001"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Set Shade Smooth.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Sample Nearest Surface"].width  = 150.0
    ff_chamomile_nodes_1.nodes["Sample Nearest Surface"].height = 100.0

    ff_chamomile_nodes_1.nodes["Normal"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Normal"].height = 100.0

    ff_chamomile_nodes_1.nodes["Math.040"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Math.040"].height = 100.0

    ff_chamomile_nodes_1.nodes["Vector Math"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Vector Math"].height = 100.0

    ff_chamomile_nodes_1.nodes["Vector Math.001"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Vector Math.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Vector Math.002"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Vector Math.002"].height = 100.0

    ff_chamomile_nodes_1.nodes["Vector Math.003"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Vector Math.003"].height = 100.0

    ff_chamomile_nodes_1.nodes["Set Mesh Normal"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Set Mesh Normal"].height = 100.0

    ff_chamomile_nodes_1.nodes["Frame"].width  = 1012.0
    ff_chamomile_nodes_1.nodes["Frame"].height = 708.0

    ff_chamomile_nodes_1.nodes["Frame.001"].width  = 2460.0
    ff_chamomile_nodes_1.nodes["Frame.001"].height = 2268.0

    ff_chamomile_nodes_1.nodes["Frame.002"].width  = 870.0
    ff_chamomile_nodes_1.nodes["Frame.002"].height = 938.0

    ff_chamomile_nodes_1.nodes["Frame.003"].width  = 1215.0
    ff_chamomile_nodes_1.nodes["Frame.003"].height = 635.3551025390625

    ff_chamomile_nodes_1.nodes["Frame.004"].width  = 1758.0
    ff_chamomile_nodes_1.nodes["Frame.004"].height = 1523.0

    ff_chamomile_nodes_1.nodes["Frame.005"].width  = 536.0
    ff_chamomile_nodes_1.nodes["Frame.005"].height = 713.0

    ff_chamomile_nodes_1.nodes["Frame.006"].width  = 1808.0
    ff_chamomile_nodes_1.nodes["Frame.006"].height = 1228.0

    ff_chamomile_nodes_1.nodes["Frame.007"].width  = 1635.0
    ff_chamomile_nodes_1.nodes["Frame.007"].height = 909.7075805664062

    ff_chamomile_nodes_1.nodes["Group Input.001"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Group Input.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Group Input.002"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Group Input.002"].height = 100.0

    ff_chamomile_nodes_1.nodes["Group Input.003"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Group Input.003"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.001"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Group Input.004"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Group Input.004"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.002"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.002"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.003"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.003"].height = 100.0

    ff_chamomile_nodes_1.nodes["Group Input.005"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Group Input.005"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.004"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.004"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.005"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.005"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.006"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.006"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.007"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.007"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.008"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.008"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.009"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.009"].height = 100.0

    ff_chamomile_nodes_1.nodes["Group Input.006"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Group Input.006"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.010"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.010"].height = 100.0

    ff_chamomile_nodes_1.nodes["Group Input.007"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Group Input.007"].height = 100.0

    ff_chamomile_nodes_1.nodes["Group Input.008"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Group Input.008"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.011"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.011"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.012"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.012"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.013"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.013"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.014"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.014"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.015"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.015"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.016"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.016"].height = 100.0

    ff_chamomile_nodes_1.nodes["Group Input.009"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Group Input.009"].height = 100.0

    ff_chamomile_nodes_1.nodes["Group Input.010"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Group Input.010"].height = 100.0

    ff_chamomile_nodes_1.nodes["Normal.001"].width  = 140.0
    ff_chamomile_nodes_1.nodes["Normal.001"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.017"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.017"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.018"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.018"].height = 100.0

    ff_chamomile_nodes_1.nodes["Reroute.019"].width  = 10.0
    ff_chamomile_nodes_1.nodes["Reroute.019"].height = 100.0


    # Initialize ff_chamomile_nodes_1 links

    # math.Value -> math_001.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.001"].inputs[0]
    )
    # math_001.Value -> math_002.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.002"].inputs[0]
    )
    # math_002.Value -> math_003.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.002"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.003"].inputs[0]
    )
    # math_003.Value -> math_004.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.003"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.004"].inputs[0]
    )
    # math_004.Value -> grid.Vertices X
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.004"].outputs[0],
        ff_chamomile_nodes_1.nodes["Grid"].inputs[2]
    )
    # position.Position -> separate_xyz.Vector
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Position"].outputs[0],
        ff_chamomile_nodes_1.nodes["Separate XYZ"].inputs[0]
    )
    # separate_xyz.Y -> map_range.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Separate XYZ"].outputs[1],
        ff_chamomile_nodes_1.nodes["Map Range"].inputs[0]
    )
    # map_range.Result -> float_curve.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Map Range"].outputs[0],
        ff_chamomile_nodes_1.nodes["Float Curve"].inputs[1]
    )
    # separate_xyz.X -> math_005.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Separate XYZ"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.005"].inputs[0]
    )
    # float_curve.Value -> math_005.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Float Curve"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.005"].inputs[1]
    )
    # separate_xyz.X -> math_006.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Separate XYZ"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.006"].inputs[0]
    )
    # math_006.Value -> math_007.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.006"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.007"].inputs[1]
    )
    # math_007.Value -> math_008.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.007"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.008"].inputs[0]
    )
    # math_008.Value -> math_009.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.008"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.009"].inputs[0]
    )
    # map_range_001.Result -> math_010.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Map Range.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.010"].inputs[0]
    )
    # math_009.Value -> math_010.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.009"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.010"].inputs[1]
    )
    # math_005.Value -> math_011.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.005"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.011"].inputs[0]
    )
    # math_010.Value -> math_012.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.010"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.012"].inputs[0]
    )
    # math_011.Value -> math_012.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.011"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.012"].inputs[1]
    )
    # math_005.Value -> math_013.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.005"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.013"].inputs[0]
    )
    # math_010.Value -> math_014.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.010"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.014"].inputs[0]
    )
    # math_013.Value -> math_014.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.013"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.014"].inputs[1]
    )
    # math_014.Value -> math_015.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.014"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.015"].inputs[0]
    )
    # math_012.Value -> map_range_002.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.012"].outputs[0],
        ff_chamomile_nodes_1.nodes["Map Range.002"].inputs[0]
    )
    # math_015.Value -> map_range_003.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.015"].outputs[0],
        ff_chamomile_nodes_1.nodes["Map Range.003"].inputs[0]
    )
    # map_range_002.Result -> combine_xyz.X
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Map Range.002"].outputs[0],
        ff_chamomile_nodes_1.nodes["Combine XYZ"].inputs[0]
    )
    # map_range_003.Result -> combine_xyz.Y
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Map Range.003"].outputs[0],
        ff_chamomile_nodes_1.nodes["Combine XYZ"].inputs[1]
    )
    # grid.Mesh -> store_named_attribute.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Grid"].outputs[0],
        ff_chamomile_nodes_1.nodes["Store Named Attribute"].inputs[0]
    )
    # combine_xyz.Vector -> store_named_attribute.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Combine XYZ"].outputs[0],
        ff_chamomile_nodes_1.nodes["Store Named Attribute"].inputs[3]
    )
    # store_named_attribute.Geometry -> store_named_attribute_001.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Store Named Attribute"].outputs[0],
        ff_chamomile_nodes_1.nodes["Store Named Attribute.001"].inputs[0]
    )
    # separate_xyz.X -> math_016.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Separate XYZ"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.016"].inputs[0]
    )
    # math_016.Value -> float_curve_001.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.016"].outputs[0],
        ff_chamomile_nodes_1.nodes["Float Curve.001"].inputs[1]
    )
    # float_curve_001.Value -> math_017.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Float Curve.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.017"].inputs[0]
    )
    # reroute_001.Output -> float_curve_002.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Float Curve.002"].inputs[1]
    )
    # math_017.Value -> math_018.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.017"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.018"].inputs[0]
    )
    # float_curve_002.Value -> math_018.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Float Curve.002"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.018"].inputs[1]
    )
    # reroute_001.Output -> float_curve_003.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Float Curve.003"].inputs[1]
    )
    # float_curve_003.Value -> math_019.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Float Curve.003"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.019"].inputs[0]
    )
    # math_018.Value -> math_020.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.018"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.020"].inputs[0]
    )
    # math_019.Value -> math_020.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.019"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.020"].inputs[1]
    )
    # math_012.Value -> combine_xyz_001.X
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.012"].outputs[0],
        ff_chamomile_nodes_1.nodes["Combine XYZ.001"].inputs[0]
    )
    # math_015.Value -> combine_xyz_001.Y
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.015"].outputs[0],
        ff_chamomile_nodes_1.nodes["Combine XYZ.001"].inputs[1]
    )
    # math_020.Value -> combine_xyz_001.Z
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.020"].outputs[0],
        ff_chamomile_nodes_1.nodes["Combine XYZ.001"].inputs[2]
    )
    # store_named_attribute_001.Geometry -> set_position.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Store Named Attribute.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Set Position"].inputs[0]
    )
    # combine_xyz_001.Vector -> set_position.Position
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Combine XYZ.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Set Position"].inputs[2]
    )
    # set_position.Geometry -> transform_geometry.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Set Position"].outputs[0],
        ff_chamomile_nodes_1.nodes["Transform Geometry"].inputs[0]
    )
    # position_001.Position -> align_euler_to_vector.Vector
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Position.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Align Euler to Vector"].inputs[2]
    )
    # mesh_circle.Mesh -> instance_on_points.Points
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Mesh Circle"].outputs[0],
        ff_chamomile_nodes_1.nodes["Instance on Points"].inputs[0]
    )
    # transform_geometry.Geometry -> instance_on_points.Instance
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Transform Geometry"].outputs[0],
        ff_chamomile_nodes_1.nodes["Instance on Points"].inputs[2]
    )
    # align_euler_to_vector.Rotation -> instance_on_points.Rotation
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Align Euler to Vector"].outputs[0],
        ff_chamomile_nodes_1.nodes["Instance on Points"].inputs[5]
    )
    # combine_xyz_002.Vector -> instance_on_points.Scale
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Combine XYZ.002"].outputs[0],
        ff_chamomile_nodes_1.nodes["Instance on Points"].inputs[6]
    )
    # instance_on_points.Instances -> realize_instances.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Instance on Points"].outputs[0],
        ff_chamomile_nodes_1.nodes["Realize Instances"].inputs[0]
    )
    # position_002.Position -> separate_xyz_001.Vector
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Position.002"].outputs[0],
        ff_chamomile_nodes_1.nodes["Separate XYZ.001"].inputs[0]
    )
    # separate_xyz_001.X -> map_range_004.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Separate XYZ.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Map Range.004"].inputs[0]
    )
    # separate_xyz_001.Y -> map_range_005.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Separate XYZ.001"].outputs[1],
        ff_chamomile_nodes_1.nodes["Map Range.005"].inputs[0]
    )
    # map_range_004.Result -> combine_xyz_003.X
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Map Range.004"].outputs[0],
        ff_chamomile_nodes_1.nodes["Combine XYZ.003"].inputs[0]
    )
    # map_range_005.Result -> combine_xyz_003.Y
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Map Range.005"].outputs[0],
        ff_chamomile_nodes_1.nodes["Combine XYZ.003"].inputs[1]
    )
    # ico_sphere.Mesh -> store_named_attribute_002.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Ico Sphere"].outputs[0],
        ff_chamomile_nodes_1.nodes["Store Named Attribute.002"].inputs[0]
    )
    # combine_xyz_003.Vector -> store_named_attribute_002.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Combine XYZ.003"].outputs[0],
        ff_chamomile_nodes_1.nodes["Store Named Attribute.002"].inputs[3]
    )
    # store_named_attribute_002.Geometry -> store_named_attribute_003.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Store Named Attribute.002"].outputs[0],
        ff_chamomile_nodes_1.nodes["Store Named Attribute.003"].inputs[0]
    )
    # store_named_attribute_003.Geometry -> transform_geometry_001.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Store Named Attribute.003"].outputs[0],
        ff_chamomile_nodes_1.nodes["Transform Geometry.001"].inputs[0]
    )
    # math_021.Value -> grid_001.Vertices X
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.021"].outputs[0],
        ff_chamomile_nodes_1.nodes["Grid.001"].inputs[2]
    )
    # position_003.Position -> separate_xyz_002.Vector
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Position.003"].outputs[0],
        ff_chamomile_nodes_1.nodes["Separate XYZ.002"].inputs[0]
    )
    # separate_xyz_002.Y -> math_022.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Separate XYZ.002"].outputs[1],
        ff_chamomile_nodes_1.nodes["Math.022"].inputs[0]
    )
    # separate_xyz_002.X -> map_range_006.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Separate XYZ.002"].outputs[0],
        ff_chamomile_nodes_1.nodes["Map Range.006"].inputs[0]
    )
    # math_022.Value -> map_range_007.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.022"].outputs[0],
        ff_chamomile_nodes_1.nodes["Map Range.007"].inputs[0]
    )
    # map_range_006.Result -> combine_xyz_004.X
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Map Range.006"].outputs[0],
        ff_chamomile_nodes_1.nodes["Combine XYZ.004"].inputs[0]
    )
    # map_range_007.Result -> combine_xyz_004.Y
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Map Range.007"].outputs[0],
        ff_chamomile_nodes_1.nodes["Combine XYZ.004"].inputs[1]
    )
    # grid_001.Mesh -> store_named_attribute_004.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Grid.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Store Named Attribute.004"].inputs[0]
    )
    # combine_xyz_004.Vector -> store_named_attribute_004.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Combine XYZ.004"].outputs[0],
        ff_chamomile_nodes_1.nodes["Store Named Attribute.004"].inputs[3]
    )
    # separate_xyz_002.X -> math_023.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Separate XYZ.002"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.023"].inputs[0]
    )
    # math_023.Value -> math_024.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.023"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.024"].inputs[0]
    )
    # math_024.Value -> math_025.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.024"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.025"].inputs[0]
    )
    # math_025.Value -> math_026.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.025"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.026"].inputs[0]
    )
    # math_024.Value -> math_027.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.024"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.027"].inputs[0]
    )
    # math_027.Value -> math_028.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.027"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.028"].inputs[0]
    )
    # reroute_004.Output -> math_030.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.004"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.030"].inputs[0]
    )
    # math_029.Value -> math_030.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.029"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.030"].inputs[1]
    )
    # math_026.Value -> combine_xyz_005.X
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.026"].outputs[0],
        ff_chamomile_nodes_1.nodes["Combine XYZ.005"].inputs[0]
    )
    # math_028.Value -> combine_xyz_005.Y
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.028"].outputs[0],
        ff_chamomile_nodes_1.nodes["Combine XYZ.005"].inputs[1]
    )
    # math_030.Value -> combine_xyz_005.Z
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.030"].outputs[0],
        ff_chamomile_nodes_1.nodes["Combine XYZ.005"].inputs[2]
    )
    # store_named_attribute_004.Geometry -> set_position_001.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Store Named Attribute.004"].outputs[0],
        ff_chamomile_nodes_1.nodes["Set Position.001"].inputs[0]
    )
    # combine_xyz_005.Vector -> set_position_001.Position
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Combine XYZ.005"].outputs[0],
        ff_chamomile_nodes_1.nodes["Set Position.001"].inputs[2]
    )
    # set_position_001.Geometry -> merge_by_distance.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Set Position.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Merge by Distance"].inputs[0]
    )
    # merge_by_distance.Geometry -> flip_faces.Mesh
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Merge by Distance"].outputs[0],
        ff_chamomile_nodes_1.nodes["Flip Faces"].inputs[0]
    )
    # flip_faces.Mesh -> store_named_attribute_005.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Flip Faces"].outputs[0],
        ff_chamomile_nodes_1.nodes["Store Named Attribute.005"].inputs[0]
    )
    # realize_instances.Geometry -> join_geometry.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Realize Instances"].outputs[0],
        ff_chamomile_nodes_1.nodes["Join Geometry"].inputs[0]
    )
    # join_geometry.Geometry -> set_shade_smooth.Mesh
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Join Geometry"].outputs[0],
        ff_chamomile_nodes_1.nodes["Set Shade Smooth"].inputs[0]
    )
    # combine_xyz_006.Vector -> transform_geometry_002.Translation
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Combine XYZ.006"].outputs[0],
        ff_chamomile_nodes_1.nodes["Transform Geometry.002"].inputs[2]
    )
    # set_shade_smooth.Mesh -> transform_geometry_002.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Set Shade Smooth"].outputs[0],
        ff_chamomile_nodes_1.nodes["Transform Geometry.002"].inputs[0]
    )
    # math_031.Value -> random_value_001.Seed
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.031"].outputs[0],
        ff_chamomile_nodes_1.nodes["Random Value.001"].inputs[3]
    )
    # group_input.Seed -> math_032.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.032"].inputs[0]
    )
    # math_032.Value -> random_value_002.Seed
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.032"].outputs[0],
        ff_chamomile_nodes_1.nodes["Random Value.002"].inputs[3]
    )
    # group_input.Seed -> math_033.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.033"].inputs[0]
    )
    # math_033.Value -> random_value_003.Seed
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.033"].outputs[0],
        ff_chamomile_nodes_1.nodes["Random Value.003"].inputs[3]
    )
    # random_value_001.Value -> math_034.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Random Value.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.034"].inputs[0]
    )
    # math_034.Value -> math_035.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.034"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.035"].inputs[0]
    )
    # random_value.Value -> math_036.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Random Value"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.036"].inputs[0]
    )
    # random_value.Value -> math_037.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Random Value"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.037"].inputs[0]
    )
    # math_036.Value -> math_038.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.036"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.038"].inputs[0]
    )
    # math_035.Value -> math_038.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.035"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.038"].inputs[1]
    )
    # math_037.Value -> math_039.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.037"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.039"].inputs[0]
    )
    # math_035.Value -> math_039.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.035"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.039"].inputs[1]
    )
    # math_038.Value -> combine_xyz_007.X
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.038"].outputs[0],
        ff_chamomile_nodes_1.nodes["Combine XYZ.007"].inputs[0]
    )
    # math_039.Value -> combine_xyz_007.Y
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.039"].outputs[0],
        ff_chamomile_nodes_1.nodes["Combine XYZ.007"].inputs[1]
    )
    # points.Points -> set_position_002.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Points"].outputs[0],
        ff_chamomile_nodes_1.nodes["Set Position.002"].inputs[0]
    )
    # combine_xyz_007.Vector -> set_position_002.Position
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Combine XYZ.007"].outputs[0],
        ff_chamomile_nodes_1.nodes["Set Position.002"].inputs[2]
    )
    # group_input.Min Scale -> random_value_003.Min
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input"].outputs[3],
        ff_chamomile_nodes_1.nodes["Random Value.003"].inputs[0]
    )
    # group_input.Max Scale -> random_value_003.Max
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input"].outputs[4],
        ff_chamomile_nodes_1.nodes["Random Value.003"].inputs[1]
    )
    # set_position_002.Geometry -> instance_on_points_001.Points
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Set Position.002"].outputs[0],
        ff_chamomile_nodes_1.nodes["Instance on Points.001"].inputs[0]
    )
    # transform_geometry_002.Geometry -> instance_on_points_001.Instance
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Transform Geometry.002"].outputs[0],
        ff_chamomile_nodes_1.nodes["Instance on Points.001"].inputs[2]
    )
    # random_value_002.Value -> instance_on_points_001.Rotation
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Random Value.002"].outputs[0],
        ff_chamomile_nodes_1.nodes["Instance on Points.001"].inputs[5]
    )
    # random_value_003.Value -> instance_on_points_001.Scale
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Random Value.003"].outputs[0],
        ff_chamomile_nodes_1.nodes["Instance on Points.001"].inputs[6]
    )
    # instance_on_points_001.Instances -> store_named_attribute_006.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Instance on Points.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Store Named Attribute.006"].inputs[0]
    )
    # index.Index -> store_named_attribute_006.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Index"].outputs[0],
        ff_chamomile_nodes_1.nodes["Store Named Attribute.006"].inputs[3]
    )
    # store_named_attribute_006.Geometry -> realize_instances_001.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Store Named Attribute.006"].outputs[0],
        ff_chamomile_nodes_1.nodes["Realize Instances.001"].inputs[0]
    )
    # math_040.Value -> vector_math.Scale
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Math.040"].outputs[0],
        ff_chamomile_nodes_1.nodes["Vector Math"].inputs[3]
    )
    # normal.Normal -> sample_nearest_surface.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Normal"].outputs[0],
        ff_chamomile_nodes_1.nodes["Sample Nearest Surface"].inputs[1]
    )
    # realize_instances_001.Geometry -> convex_hull.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Realize Instances.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Convex Hull"].inputs[0]
    )
    # convex_hull.Convex Hull -> set_shade_smooth_001.Mesh
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Convex Hull"].outputs[0],
        ff_chamomile_nodes_1.nodes["Set Shade Smooth.001"].inputs[0]
    )
    # set_shade_smooth_001.Mesh -> sample_nearest_surface.Mesh
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Set Shade Smooth.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Sample Nearest Surface"].inputs[0]
    )
    # sample_nearest_surface.Value -> vector_math_001.Vector
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Sample Nearest Surface"].outputs[0],
        ff_chamomile_nodes_1.nodes["Vector Math.001"].inputs[0]
    )
    # vector_math.Vector -> vector_math_002.Vector
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Vector Math"].outputs[0],
        ff_chamomile_nodes_1.nodes["Vector Math.002"].inputs[0]
    )
    # vector_math_001.Vector -> vector_math_002.Vector
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Vector Math.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Vector Math.002"].inputs[1]
    )
    # vector_math_002.Vector -> vector_math_003.Vector
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Vector Math.002"].outputs[0],
        ff_chamomile_nodes_1.nodes["Vector Math.003"].inputs[0]
    )
    # vector_math_003.Vector -> set_mesh_normal.Custom Normal
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Vector Math.003"].outputs[0],
        ff_chamomile_nodes_1.nodes["Set Mesh Normal"].inputs[1]
    )
    # reroute_019.Output -> set_mesh_normal.Mesh
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.019"].outputs[0],
        ff_chamomile_nodes_1.nodes["Set Mesh Normal"].inputs[0]
    )
    # set_mesh_normal.Mesh -> set_material.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Set Mesh Normal"].outputs[0],
        ff_chamomile_nodes_1.nodes["Set Material"].inputs[0]
    )
    # set_material.Geometry -> group_output.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Set Material"].outputs[0],
        ff_chamomile_nodes_1.nodes["Group Output"].inputs[0]
    )
    # group_input_001.Resolution X -> math.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.001"].outputs[13],
        ff_chamomile_nodes_1.nodes["Math"].inputs[0]
    )
    # group_input_002.Resolution Y -> grid.Vertices Y
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.002"].outputs[14],
        ff_chamomile_nodes_1.nodes["Grid"].inputs[3]
    )
    # reroute.Output -> math_019.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.019"].inputs[1]
    )
    # group_input_003.Gutter Strength -> math_017.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.003"].outputs[15],
        ff_chamomile_nodes_1.nodes["Math.017"].inputs[1]
    )
    # group_input_003.Arch Strength -> reroute.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.003"].outputs[16],
        ff_chamomile_nodes_1.nodes["Reroute"].inputs[0]
    )
    # group_input_002.Petal Color -> store_named_attribute_001.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.002"].outputs[20],
        ff_chamomile_nodes_1.nodes["Store Named Attribute.001"].inputs[3]
    )
    # map_range.Result -> reroute_001.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Map Range"].outputs[0],
        ff_chamomile_nodes_1.nodes["Reroute.001"].inputs[0]
    )
    # reroute_001.Output -> math_008.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.008"].inputs[1]
    )
    # reroute_001.Output -> map_range_001.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Map Range.001"].inputs[0]
    )
    # reroute_003.Output -> mesh_circle.Vertices
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.003"].outputs[0],
        ff_chamomile_nodes_1.nodes["Mesh Circle"].inputs[0]
    )
    # reroute_002.Output -> mesh_circle.Radius
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.002"].outputs[0],
        ff_chamomile_nodes_1.nodes["Mesh Circle"].inputs[1]
    )
    # group_input_004.Petal Scale -> combine_xyz_002.X
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.004"].outputs[7],
        ff_chamomile_nodes_1.nodes["Combine XYZ.002"].inputs[0]
    )
    # group_input_004.Petal Scale -> combine_xyz_002.Y
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.004"].outputs[7],
        ff_chamomile_nodes_1.nodes["Combine XYZ.002"].inputs[1]
    )
    # group_input_004.Petal Scale -> combine_xyz_002.Z
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.004"].outputs[7],
        ff_chamomile_nodes_1.nodes["Combine XYZ.002"].inputs[2]
    )
    # group_input_004.Center Radius -> reroute_002.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.004"].outputs[6],
        ff_chamomile_nodes_1.nodes["Reroute.002"].inputs[0]
    )
    # group_input_004.Petals Count -> reroute_003.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.004"].outputs[5],
        ff_chamomile_nodes_1.nodes["Reroute.003"].inputs[0]
    )
    # reroute_008.Output -> math_026.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.008"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.026"].inputs[1]
    )
    # reroute_006.Output -> math_028.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.006"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.028"].inputs[1]
    )
    # reroute_010.Output -> store_named_attribute_005.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.010"].outputs[0],
        ff_chamomile_nodes_1.nodes["Store Named Attribute.005"].inputs[3]
    )
    # reroute_005.Output -> reroute_004.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.005"].outputs[0],
        ff_chamomile_nodes_1.nodes["Reroute.004"].inputs[0]
    )
    # separate_xyz_002.Y -> reroute_005.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Separate XYZ.002"].outputs[1],
        ff_chamomile_nodes_1.nodes["Reroute.005"].inputs[0]
    )
    # reroute_007.Output -> reroute_006.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.007"].outputs[0],
        ff_chamomile_nodes_1.nodes["Reroute.006"].inputs[0]
    )
    # group_input_005.Thickness -> reroute_007.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.005"].outputs[11],
        ff_chamomile_nodes_1.nodes["Reroute.007"].inputs[0]
    )
    # reroute_009.Output -> reroute_008.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.009"].outputs[0],
        ff_chamomile_nodes_1.nodes["Reroute.008"].inputs[0]
    )
    # group_input_005.Length -> math_022.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.005"].outputs[10],
        ff_chamomile_nodes_1.nodes["Math.022"].inputs[1]
    )
    # group_input_005.Length -> math_029.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.005"].outputs[10],
        ff_chamomile_nodes_1.nodes["Math.029"].inputs[0]
    )
    # group_input_006.Length -> grid_001.Size Y
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.006"].outputs[10],
        ff_chamomile_nodes_1.nodes["Grid.001"].inputs[1]
    )
    # group_input_006.Resolution -> math_021.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.006"].outputs[12],
        ff_chamomile_nodes_1.nodes["Math.021"].inputs[0]
    )
    # group_input_006.Thickness -> reroute_009.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.006"].outputs[11],
        ff_chamomile_nodes_1.nodes["Reroute.009"].inputs[0]
    )
    # group_input_005.Stem Color -> reroute_010.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.005"].outputs[22],
        ff_chamomile_nodes_1.nodes["Reroute.010"].inputs[0]
    )
    # reroute_013.Output -> transform_geometry_001.Scale
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.013"].outputs[0],
        ff_chamomile_nodes_1.nodes["Transform Geometry.001"].inputs[4]
    )
    # reroute_012.Output -> ico_sphere.Subdivisions
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.012"].outputs[0],
        ff_chamomile_nodes_1.nodes["Ico Sphere"].inputs[1]
    )
    # reroute_016.Output -> store_named_attribute_003.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.016"].outputs[0],
        ff_chamomile_nodes_1.nodes["Store Named Attribute.003"].inputs[3]
    )
    # group_input_008.Length -> combine_xyz_006.Z
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.008"].outputs[10],
        ff_chamomile_nodes_1.nodes["Combine XYZ.006"].inputs[2]
    )
    # group_input_008.Smooth Shading -> set_shade_smooth.Shade Smooth
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.008"].outputs[18],
        ff_chamomile_nodes_1.nodes["Set Shade Smooth"].inputs[2]
    )
    # group_input_007.Subdivisions -> reroute_011.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.007"].outputs[9],
        ff_chamomile_nodes_1.nodes["Reroute.011"].inputs[0]
    )
    # reroute_011.Output -> reroute_012.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.011"].outputs[0],
        ff_chamomile_nodes_1.nodes["Reroute.012"].inputs[0]
    )
    # reroute_014.Output -> reroute_013.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.014"].outputs[0],
        ff_chamomile_nodes_1.nodes["Reroute.013"].inputs[0]
    )
    # group_input_007.Scale -> reroute_014.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.007"].outputs[8],
        ff_chamomile_nodes_1.nodes["Reroute.014"].inputs[0]
    )
    # group_input_007.Center Color -> reroute_015.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.007"].outputs[21],
        ff_chamomile_nodes_1.nodes["Reroute.015"].inputs[0]
    )
    # reroute_015.Output -> reroute_016.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.015"].outputs[0],
        ff_chamomile_nodes_1.nodes["Reroute.016"].inputs[0]
    )
    # reroute_017.Output -> set_material.Material
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.017"].outputs[0],
        ff_chamomile_nodes_1.nodes["Set Material"].inputs[2]
    )
    # group_input_009.Stylized Normals -> math_040.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.009"].outputs[19],
        ff_chamomile_nodes_1.nodes["Math.040"].inputs[1]
    )
    # group_input_009.Stylized Normals -> vector_math_001.Scale
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.009"].outputs[19],
        ff_chamomile_nodes_1.nodes["Vector Math.001"].inputs[3]
    )
    # group_input_010.Seed -> random_value.Seed
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.010"].outputs[0],
        ff_chamomile_nodes_1.nodes["Random Value"].inputs[3]
    )
    # group_input_010.Seed -> math_031.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.010"].outputs[0],
        ff_chamomile_nodes_1.nodes["Math.031"].inputs[0]
    )
    # group_input_010.Count -> points.Count
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.010"].outputs[1],
        ff_chamomile_nodes_1.nodes["Points"].inputs[0]
    )
    # group_input_010.Patch Radius -> math_035.Value
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.010"].outputs[2],
        ff_chamomile_nodes_1.nodes["Math.035"].inputs[1]
    )
    # normal_001.Normal -> vector_math.Vector
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Normal.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Vector Math"].inputs[0]
    )
    # group_input_009.Material -> reroute_017.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Group Input.009"].outputs[17],
        ff_chamomile_nodes_1.nodes["Reroute.017"].inputs[0]
    )
    # realize_instances_001.Geometry -> reroute_018.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Realize Instances.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Reroute.018"].inputs[0]
    )
    # reroute_018.Output -> reroute_019.Input
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Reroute.018"].outputs[0],
        ff_chamomile_nodes_1.nodes["Reroute.019"].inputs[0]
    )
    # transform_geometry_001.Geometry -> join_geometry.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Transform Geometry.001"].outputs[0],
        ff_chamomile_nodes_1.nodes["Join Geometry"].inputs[0]
    )
    # store_named_attribute_005.Geometry -> join_geometry.Geometry
    ff_chamomile_nodes_1.links.new(
        ff_chamomile_nodes_1.nodes["Store Named Attribute.005"].outputs[0],
        ff_chamomile_nodes_1.nodes["Join Geometry"].inputs[0]
    )

    return ff_chamomile_nodes_1


if __name__ == "__main__":
    # Maps node tree creation functions to the node tree 
    # name, such that we don't recreate node trees unnecessarily
    node_tree_names : dict[typing.Callable, str] = {}

    ff_chamomile_nodes = ff_chamomile_nodes_1_node_group(node_tree_names)
    node_tree_names[ff_chamomile_nodes_1_node_group] = ff_chamomile_nodes.name


# ============================================================================
#  FF BRIDGE 
# ============================================================================

from . import bridge

GROUP_NAME = "FF Chamomile Nodes"
MAT_NAME = "M_Chamomile"
MAT_HEX = "00FF00"


def create_node_group():
    return bridge.get_or_create_node_group(ff_chamomile_nodes_1_node_group, GROUP_NAME)


def get_or_create_material():
    return bridge.get_or_create_colormask_material(MAT_NAME, MAT_HEX)