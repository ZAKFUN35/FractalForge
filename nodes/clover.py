import bpy
import mathutils
import os
import typing


def ff_clover_nodes_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize FF Clover Nodes node group"""
    ff_clover_nodes_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="FF Clover Nodes")

    ff_clover_nodes_1.color_tag = 'GEOMETRY'
    ff_clover_nodes_1.description = ""
    ff_clover_nodes_1.default_group_node_width = 140
    ff_clover_nodes_1.is_modifier = True
    ff_clover_nodes_1.show_modifier_manage_panel = True

    # ff_clover_nodes_1 interface

    # Socket Geometry
    geometry_socket = ff_clover_nodes_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Panel Placement
    placement_panel = ff_clover_nodes_1.interface.new_panel("Placement")
    # Socket Seed
    seed_socket = ff_clover_nodes_1.interface.new_socket(name="Seed", in_out='INPUT', socket_type='NodeSocketInt', parent = placement_panel)
    seed_socket.default_value = 0
    seed_socket.min_value = -2147483648
    seed_socket.max_value = 2147483647
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'

    # Socket Count
    count_socket = ff_clover_nodes_1.interface.new_socket(name="Count", in_out='INPUT', socket_type='NodeSocketInt', parent = placement_panel)
    count_socket.default_value = 3
    count_socket.min_value = -2147483648
    count_socket.max_value = 2147483647
    count_socket.subtype = 'NONE'
    count_socket.attribute_domain = 'POINT'
    count_socket.default_input = 'VALUE'
    count_socket.structure_type = 'AUTO'

    # Socket Patch Radius
    patch_radius_socket = ff_clover_nodes_1.interface.new_socket(name="Patch Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent = placement_panel)
    patch_radius_socket.default_value = 0.14000000059604645
    patch_radius_socket.min_value = -3.4028234663852886e+38
    patch_radius_socket.max_value = 3.4028234663852886e+38
    patch_radius_socket.subtype = 'NONE'
    patch_radius_socket.attribute_domain = 'POINT'
    patch_radius_socket.default_input = 'VALUE'
    patch_radius_socket.structure_type = 'AUTO'

    # Socket Min Scale
    min_scale_socket = ff_clover_nodes_1.interface.new_socket(name="Min Scale", in_out='INPUT', socket_type='NodeSocketFloat', parent = placement_panel)
    min_scale_socket.default_value = 0.05000000074505806
    min_scale_socket.min_value = -3.4028234663852886e+38
    min_scale_socket.max_value = 3.4028234663852886e+38
    min_scale_socket.subtype = 'NONE'
    min_scale_socket.attribute_domain = 'POINT'
    min_scale_socket.default_input = 'VALUE'
    min_scale_socket.structure_type = 'AUTO'

    # Socket Max Scale
    max_scale_socket = ff_clover_nodes_1.interface.new_socket(name="Max Scale", in_out='INPUT', socket_type='NodeSocketFloat', parent = placement_panel)
    max_scale_socket.default_value = 0.11999999731779099
    max_scale_socket.min_value = -3.4028234663852886e+38
    max_scale_socket.max_value = 3.4028234663852886e+38
    max_scale_socket.subtype = 'NONE'
    max_scale_socket.attribute_domain = 'POINT'
    max_scale_socket.default_input = 'VALUE'
    max_scale_socket.structure_type = 'AUTO'


    # Panel Structure
    structure_panel = ff_clover_nodes_1.interface.new_panel("Structure")
    # Socket Petals Count
    petals_count_socket = ff_clover_nodes_1.interface.new_socket(name="Petals Count", in_out='INPUT', socket_type='NodeSocketInt', parent = structure_panel)
    petals_count_socket.default_value = 4
    petals_count_socket.min_value = -2147483648
    petals_count_socket.max_value = 2147483647
    petals_count_socket.subtype = 'NONE'
    petals_count_socket.attribute_domain = 'POINT'
    petals_count_socket.default_input = 'VALUE'
    petals_count_socket.structure_type = 'AUTO'

    # Socket Center Radius
    center_radius_socket = ff_clover_nodes_1.interface.new_socket(name="Center Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent = structure_panel)
    center_radius_socket.default_value = 0.05000000074505806
    center_radius_socket.min_value = -3.4028234663852886e+38
    center_radius_socket.max_value = 3.4028234663852886e+38
    center_radius_socket.subtype = 'NONE'
    center_radius_socket.attribute_domain = 'POINT'
    center_radius_socket.default_input = 'VALUE'
    center_radius_socket.structure_type = 'AUTO'

    # Socket Petal Scale
    petal_scale_socket = ff_clover_nodes_1.interface.new_socket(name="Petal Scale", in_out='INPUT', socket_type='NodeSocketFloat', parent = structure_panel)
    petal_scale_socket.default_value = 0.6000000238418579
    petal_scale_socket.min_value = -3.4028234663852886e+38
    petal_scale_socket.max_value = 3.4028234663852886e+38
    petal_scale_socket.subtype = 'NONE'
    petal_scale_socket.attribute_domain = 'POINT'
    petal_scale_socket.default_input = 'VALUE'
    petal_scale_socket.structure_type = 'AUTO'


    # Panel Center Sphere
    center_sphere_panel = ff_clover_nodes_1.interface.new_panel("Center Sphere")
    # Socket Scale
    scale_socket = ff_clover_nodes_1.interface.new_socket(name="Scale", in_out='INPUT', socket_type='NodeSocketVector', parent = center_sphere_panel)
    scale_socket.default_value = (0.07999999821186066, 0.07999999821186066, 0.03200000151991844)
    scale_socket.min_value = -3.4028234663852886e+38
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    # Socket Subdivisions
    subdivisions_socket = ff_clover_nodes_1.interface.new_socket(name="Subdivisions", in_out='INPUT', socket_type='NodeSocketInt', parent = center_sphere_panel)
    subdivisions_socket.default_value = 1
    subdivisions_socket.min_value = -2147483648
    subdivisions_socket.max_value = 2147483647
    subdivisions_socket.subtype = 'NONE'
    subdivisions_socket.attribute_domain = 'POINT'
    subdivisions_socket.default_input = 'VALUE'
    subdivisions_socket.structure_type = 'AUTO'


    # Panel Stem
    stem_panel = ff_clover_nodes_1.interface.new_panel("Stem")
    # Socket Stem Length
    stem_length_socket = ff_clover_nodes_1.interface.new_socket(name="Stem Length", in_out='INPUT', socket_type='NodeSocketFloat', parent = stem_panel)
    stem_length_socket.default_value = 2.0
    stem_length_socket.min_value = -3.4028234663852886e+38
    stem_length_socket.max_value = 3.4028234663852886e+38
    stem_length_socket.subtype = 'NONE'
    stem_length_socket.attribute_domain = 'POINT'
    stem_length_socket.default_input = 'VALUE'
    stem_length_socket.structure_type = 'AUTO'

    # Socket Stem Thickness
    stem_thickness_socket = ff_clover_nodes_1.interface.new_socket(name="Stem Thickness", in_out='INPUT', socket_type='NodeSocketFloat', parent = stem_panel)
    stem_thickness_socket.default_value = 0.02500000037252903
    stem_thickness_socket.min_value = -3.4028234663852886e+38
    stem_thickness_socket.max_value = 3.4028234663852886e+38
    stem_thickness_socket.subtype = 'NONE'
    stem_thickness_socket.attribute_domain = 'POINT'
    stem_thickness_socket.default_input = 'VALUE'
    stem_thickness_socket.structure_type = 'AUTO'

    # Socket Stem Resolution
    stem_resolution_socket = ff_clover_nodes_1.interface.new_socket(name="Stem Resolution", in_out='INPUT', socket_type='NodeSocketInt', parent = stem_panel)
    stem_resolution_socket.default_value = 3
    stem_resolution_socket.min_value = 3
    stem_resolution_socket.max_value = 2147483647
    stem_resolution_socket.subtype = 'NONE'
    stem_resolution_socket.attribute_domain = 'POINT'
    stem_resolution_socket.default_input = 'VALUE'
    stem_resolution_socket.structure_type = 'AUTO'


    # Panel Petal Shape
    petal_shape_panel = ff_clover_nodes_1.interface.new_panel("Petal Shape")
    # Socket Resolution X
    resolution_x_socket = ff_clover_nodes_1.interface.new_socket(name="Resolution X", in_out='INPUT', socket_type='NodeSocketInt', parent = petal_shape_panel)
    resolution_x_socket.default_value = 7
    resolution_x_socket.min_value = -2147483648
    resolution_x_socket.max_value = 2147483647
    resolution_x_socket.subtype = 'NONE'
    resolution_x_socket.attribute_domain = 'POINT'
    resolution_x_socket.default_input = 'VALUE'
    resolution_x_socket.structure_type = 'AUTO'

    # Socket Resolution Y
    resolution_y_socket = ff_clover_nodes_1.interface.new_socket(name="Resolution Y", in_out='INPUT', socket_type='NodeSocketInt', parent = petal_shape_panel)
    resolution_y_socket.default_value = 3
    resolution_y_socket.min_value = 2
    resolution_y_socket.max_value = 2147483647
    resolution_y_socket.subtype = 'NONE'
    resolution_y_socket.attribute_domain = 'POINT'
    resolution_y_socket.default_input = 'VALUE'
    resolution_y_socket.structure_type = 'AUTO'

    # Socket Center Density
    center_density_socket = ff_clover_nodes_1.interface.new_socket(name="Center Density", in_out='INPUT', socket_type='NodeSocketFloat', parent = petal_shape_panel)
    center_density_socket.default_value = 1.5
    center_density_socket.min_value = -3.4028234663852886e+38
    center_density_socket.max_value = 3.4028234663852886e+38
    center_density_socket.subtype = 'NONE'
    center_density_socket.attribute_domain = 'POINT'
    center_density_socket.default_input = 'VALUE'
    center_density_socket.structure_type = 'AUTO'

    # Socket Side Sharpness
    side_sharpness_socket = ff_clover_nodes_1.interface.new_socket(name="Side Sharpness", in_out='INPUT', socket_type='NodeSocketFloat', parent = petal_shape_panel)
    side_sharpness_socket.default_value = 1.0
    side_sharpness_socket.min_value = -3.4028234663852886e+38
    side_sharpness_socket.max_value = 3.4028234663852886e+38
    side_sharpness_socket.subtype = 'NONE'
    side_sharpness_socket.attribute_domain = 'POINT'
    side_sharpness_socket.default_input = 'VALUE'
    side_sharpness_socket.structure_type = 'AUTO'

    # Socket Cleavage Depth
    cleavage_depth_socket = ff_clover_nodes_1.interface.new_socket(name="Cleavage Depth", in_out='INPUT', socket_type='NodeSocketFloat', parent = petal_shape_panel)
    cleavage_depth_socket.default_value = 0.75
    cleavage_depth_socket.min_value = -3.4028234663852886e+38
    cleavage_depth_socket.max_value = 3.4028234663852886e+38
    cleavage_depth_socket.subtype = 'NONE'
    cleavage_depth_socket.attribute_domain = 'POINT'
    cleavage_depth_socket.default_input = 'VALUE'
    cleavage_depth_socket.structure_type = 'AUTO'

    # Socket Vertical Crease (X)
    vertical_crease__x__socket = ff_clover_nodes_1.interface.new_socket(name="Vertical Crease (X)", in_out='INPUT', socket_type='NodeSocketFloat', parent = petal_shape_panel)
    vertical_crease__x__socket.default_value = -0.3499999940395355
    vertical_crease__x__socket.min_value = -3.4028234663852886e+38
    vertical_crease__x__socket.max_value = 3.4028234663852886e+38
    vertical_crease__x__socket.subtype = 'NONE'
    vertical_crease__x__socket.attribute_domain = 'POINT'
    vertical_crease__x__socket.default_input = 'VALUE'
    vertical_crease__x__socket.structure_type = 'AUTO'

    # Socket Horizontal Curve (Y)
    horizontal_curve__y__socket = ff_clover_nodes_1.interface.new_socket(name="Horizontal Curve (Y)", in_out='INPUT', socket_type='NodeSocketFloat', parent = petal_shape_panel)
    horizontal_curve__y__socket.default_value = 0.20000000298023224
    horizontal_curve__y__socket.min_value = -3.4028234663852886e+38
    horizontal_curve__y__socket.max_value = 3.4028234663852886e+38
    horizontal_curve__y__socket.subtype = 'NONE'
    horizontal_curve__y__socket.attribute_domain = 'POINT'
    horizontal_curve__y__socket.default_input = 'VALUE'
    horizontal_curve__y__socket.structure_type = 'AUTO'


    # Panel Detail
    detail_panel = ff_clover_nodes_1.interface.new_panel("Detail")
    # Socket Material
    material_socket = ff_clover_nodes_1.interface.new_socket(name="Material", in_out='INPUT', socket_type='NodeSocketMaterial', parent = detail_panel)
    material_socket.attribute_domain = 'POINT'
    material_socket.default_input = 'VALUE'
    material_socket.structure_type = 'AUTO'

    # Socket Smooth Shading
    smooth_shading_socket = ff_clover_nodes_1.interface.new_socket(name="Smooth Shading", in_out='INPUT', socket_type='NodeSocketBool', parent = detail_panel)
    smooth_shading_socket.default_value = True
    smooth_shading_socket.attribute_domain = 'POINT'
    smooth_shading_socket.default_input = 'VALUE'
    smooth_shading_socket.structure_type = 'AUTO'

    # Socket Stylized Normals
    stylized_normals_socket = ff_clover_nodes_1.interface.new_socket(name="Stylized Normals", in_out='INPUT', socket_type='NodeSocketFloat', parent = detail_panel)
    stylized_normals_socket.default_value = 0.8500000238418579
    stylized_normals_socket.min_value = 0.0
    stylized_normals_socket.max_value = 1.0
    stylized_normals_socket.subtype = 'NONE'
    stylized_normals_socket.attribute_domain = 'POINT'
    stylized_normals_socket.default_input = 'VALUE'
    stylized_normals_socket.structure_type = 'AUTO'

    # Socket Petal Color
    petal_color_socket = ff_clover_nodes_1.interface.new_socket(name="Petal Color", in_out='INPUT', socket_type='NodeSocketColor', parent = detail_panel)
    petal_color_socket.default_value = (0.0, 1.0, 0.0, 1.0)
    petal_color_socket.attribute_domain = 'POINT'
    petal_color_socket.default_input = 'VALUE'
    petal_color_socket.structure_type = 'AUTO'

    # Socket Center Color
    center_color_socket = ff_clover_nodes_1.interface.new_socket(name="Center Color", in_out='INPUT', socket_type='NodeSocketColor', parent = detail_panel)
    center_color_socket.default_value = (0.0, 1.0, 0.0, 1.0)
    center_color_socket.attribute_domain = 'POINT'
    center_color_socket.default_input = 'VALUE'
    center_color_socket.structure_type = 'AUTO'

    # Socket Stem Color
    stem_color_socket = ff_clover_nodes_1.interface.new_socket(name="Stem Color", in_out='INPUT', socket_type='NodeSocketColor', parent = detail_panel)
    stem_color_socket.default_value = (0.0, 1.0, 0.0, 1.0)
    stem_color_socket.attribute_domain = 'POINT'
    stem_color_socket.default_input = 'VALUE'
    stem_color_socket.structure_type = 'AUTO'


    # Initialize ff_clover_nodes_1 nodes

    # Node Group Input
    group_input = ff_clover_nodes_1.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node Group Input.001
    group_input_001 = ff_clover_nodes_1.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.show_options = True

    # Node Group Input.002
    group_input_002 = ff_clover_nodes_1.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.show_options = True

    # Node Group Input.003
    group_input_003 = ff_clover_nodes_1.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.show_options = True

    # Node Group Input.004
    group_input_004 = ff_clover_nodes_1.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.show_options = True

    # Node Group Input.005
    group_input_005 = ff_clover_nodes_1.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.show_options = True

    # Node Group Input.006
    group_input_006 = ff_clover_nodes_1.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.show_options = True

    # Node Group Input.007
    group_input_007 = ff_clover_nodes_1.nodes.new("NodeGroupInput")
    group_input_007.name = "Group Input.007"
    group_input_007.show_options = True

    # Node Math
    math = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.show_options = True
    math.operation = 'SUBTRACT'
    math.use_clamp = False
    # Value_001
    math.inputs[1].default_value = 1.0

    # Node Math.001
    math_001 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.show_options = True
    math_001.operation = 'DIVIDE'
    math_001.use_clamp = False
    # Value_001
    math_001.inputs[1].default_value = 2.0

    # Node Math.002
    math_002 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.show_options = True
    math_002.operation = 'FLOOR'
    math_002.use_clamp = False

    # Node Math.003
    math_003 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.show_options = True
    math_003.operation = 'MULTIPLY'
    math_003.use_clamp = False
    # Value_001
    math_003.inputs[1].default_value = 2.0

    # Node Math.004
    math_004 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.show_options = True
    math_004.operation = 'ADD'
    math_004.use_clamp = False
    # Value_001
    math_004.inputs[1].default_value = 1.0

    # Node Grid
    grid = ff_clover_nodes_1.nodes.new("GeometryNodeMeshGrid")
    grid.name = "Grid"
    grid.show_options = True
    # Size X
    grid.inputs[0].default_value = 2.0
    # Size Y
    grid.inputs[1].default_value = 2.0

    # Node Position
    position = ff_clover_nodes_1.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    position.show_options = True

    # Node Separate XYZ
    separate_xyz = ff_clover_nodes_1.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz.show_options = True

    # Node Math.005
    math_005 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.show_options = True
    math_005.operation = 'ABSOLUTE'
    math_005.use_clamp = False

    # Node Math.006
    math_006 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.show_options = True
    math_006.operation = 'SIGN'
    math_006.use_clamp = False

    # Node Math.007
    math_007 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.show_options = True
    math_007.operation = 'POWER'
    math_007.use_clamp = False

    # Node Math.008
    math_008 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.show_options = True
    math_008.operation = 'MULTIPLY'
    math_008.use_clamp = False

    # Node Math.009
    math_009 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.show_options = True
    math_009.operation = 'MULTIPLY'
    math_009.use_clamp = False
    # Value_001
    math_009.inputs[1].default_value = 1.5707963705062866

    # Node Math.010
    math_010 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.show_options = True
    math_010.operation = 'SINE'
    math_010.use_clamp = False

    # Node Math.011
    math_011 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_011.name = "Math.011"
    math_011.show_options = True
    math_011.operation = 'MULTIPLY'
    math_011.use_clamp = False

    # Node Math.012
    math_012 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_012.name = "Math.012"
    math_012.show_options = True
    math_012.operation = 'ABSOLUTE'
    math_012.use_clamp = False

    # Node Math.013
    math_013 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_013.name = "Math.013"
    math_013.show_options = True
    math_013.operation = 'SQRT'
    math_013.use_clamp = False

    # Node Math.014
    math_014 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_014.name = "Math.014"
    math_014.show_options = True
    math_014.operation = 'MULTIPLY'
    math_014.use_clamp = False

    # Node Math.015
    math_015 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_015.name = "Math.015"
    math_015.show_options = True
    math_015.operation = 'MULTIPLY'
    math_015.use_clamp = False

    # Node Math.016
    math_016 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_016.name = "Math.016"
    math_016.show_options = True
    math_016.operation = 'SUBTRACT'
    math_016.use_clamp = False
    # Value
    math_016.inputs[0].default_value = 1.0

    # Node Math.017
    math_017 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_017.name = "Math.017"
    math_017.show_options = True
    math_017.operation = 'MAXIMUM'
    math_017.use_clamp = False
    # Value_001
    math_017.inputs[1].default_value = 0.0

    # Node Math.018
    math_018 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_018.name = "Math.018"
    math_018.show_options = True
    math_018.operation = 'SQRT'
    math_018.use_clamp = False

    # Node Math.019
    math_019 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_019.name = "Math.019"
    math_019.show_options = True
    math_019.operation = 'ADD'
    math_019.use_clamp = False

    # Node Math.020
    math_020 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_020.name = "Math.020"
    math_020.show_options = True
    math_020.operation = 'SUBTRACT'
    math_020.use_clamp = False

    # Node Map Range
    map_range = ff_clover_nodes_1.nodes.new("ShaderNodeMapRange")
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

    # Node Math.021
    math_021 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_021.name = "Math.021"
    math_021.show_options = True
    math_021.operation = 'SUBTRACT'
    math_021.use_clamp = False

    # Node Math.022
    math_022 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_022.name = "Math.022"
    math_022.show_options = True
    math_022.operation = 'MULTIPLY'
    math_022.use_clamp = False

    # Node Math.023
    math_023 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_023.name = "Math.023"
    math_023.show_options = True
    math_023.operation = 'ADD'
    math_023.use_clamp = False

    # Node Map Range.001
    map_range_001 = ff_clover_nodes_1.nodes.new("ShaderNodeMapRange")
    map_range_001.name = "Map Range.001"
    map_range_001.show_options = True
    map_range_001.clamp = True
    map_range_001.data_type = 'FLOAT'
    map_range_001.interpolation_type = 'LINEAR'
    # From Min
    map_range_001.inputs[1].default_value = -1.100000023841858
    # From Max
    map_range_001.inputs[2].default_value = 1.100000023841858
    # To Min
    map_range_001.inputs[3].default_value = 0.0
    # To Max
    map_range_001.inputs[4].default_value = 0.5

    # Node Map Range.002
    map_range_002 = ff_clover_nodes_1.nodes.new("ShaderNodeMapRange")
    map_range_002.name = "Map Range.002"
    map_range_002.show_options = True
    map_range_002.clamp = True
    map_range_002.data_type = 'FLOAT'
    map_range_002.interpolation_type = 'LINEAR'
    # From Min
    map_range_002.inputs[1].default_value = -1.100000023841858
    # From Max
    map_range_002.inputs[2].default_value = 1.100000023841858
    # To Min
    map_range_002.inputs[3].default_value = 0.5
    # To Max
    map_range_002.inputs[4].default_value = 1.0

    # Node Combine XYZ
    combine_xyz = ff_clover_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz.show_options = True
    # Z
    combine_xyz.inputs[2].default_value = 0.0

    # Node Store Named Attribute
    store_named_attribute = ff_clover_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.show_options = True
    store_named_attribute.data_type = 'FLOAT2'
    store_named_attribute.domain = 'CORNER'
    # Selection
    store_named_attribute.inputs[1].default_value = True
    # Name
    store_named_attribute.inputs[2].default_value = "UVMap"

    # Node Store Named Attribute.001
    store_named_attribute_001 = ff_clover_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.show_options = True
    store_named_attribute_001.data_type = 'FLOAT_COLOR'
    store_named_attribute_001.domain = 'CORNER'
    # Selection
    store_named_attribute_001.inputs[1].default_value = True
    # Name
    store_named_attribute_001.inputs[2].default_value = "ColorMask"

    # Node Math.024
    math_024 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_024.name = "Math.024"
    math_024.show_options = True
    math_024.operation = 'ABSOLUTE'
    math_024.use_clamp = False

    # Node Math.025
    math_025 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_025.name = "Math.025"
    math_025.show_options = True
    math_025.operation = 'ABSOLUTE'
    math_025.use_clamp = False

    # Node Math.026
    math_026 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_026.name = "Math.026"
    math_026.show_options = True
    math_026.operation = 'SUBTRACT'
    math_026.use_clamp = False
    # Value
    math_026.inputs[0].default_value = 1.0

    # Node Math.027
    math_027 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_027.name = "Math.027"
    math_027.show_options = True
    math_027.operation = 'SUBTRACT'
    math_027.use_clamp = False
    # Value
    math_027.inputs[0].default_value = 1.0

    # Node Math.028
    math_028 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_028.name = "Math.028"
    math_028.show_options = True
    math_028.operation = 'MULTIPLY'
    math_028.use_clamp = False

    # Node Math.029
    math_029 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_029.name = "Math.029"
    math_029.show_options = True
    math_029.operation = 'MULTIPLY'
    math_029.use_clamp = False

    # Node Math.030
    math_030 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_030.name = "Math.030"
    math_030.show_options = True
    math_030.operation = 'MULTIPLY'
    math_030.use_clamp = False

    # Node Math.031
    math_031 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_031.name = "Math.031"
    math_031.show_options = True
    math_031.operation = 'ADD'
    math_031.use_clamp = False

    # Node Combine XYZ.001
    combine_xyz_001 = ff_clover_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    combine_xyz_001.show_options = True

    # Node Set Position
    set_position = ff_clover_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.show_options = True
    # Selection
    set_position.inputs[1].default_value = True
    # Offset
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Transform Geometry
    transform_geometry = ff_clover_nodes_1.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.show_options = True
    # Mode
    transform_geometry.inputs[1].default_value = 'Components'
    # Translation
    transform_geometry.inputs[2].default_value = (0.0, 1.0, 0.0)
    # Rotation
    transform_geometry.inputs[3].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry.inputs[4].default_value = (1.2000000476837158, 1.0, 1.0)

    # Node Mesh Circle
    mesh_circle = ff_clover_nodes_1.nodes.new("GeometryNodeMeshCircle")
    mesh_circle.name = "Mesh Circle"
    mesh_circle.show_options = True
    mesh_circle.fill_type = 'NONE'

    # Node Position.001
    position_001 = ff_clover_nodes_1.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"
    position_001.show_options = True

    # Node Align Euler to Vector
    align_euler_to_vector = ff_clover_nodes_1.nodes.new("FunctionNodeAlignEulerToVector")
    align_euler_to_vector.name = "Align Euler to Vector"
    align_euler_to_vector.show_options = True
    align_euler_to_vector.axis = 'Y'
    align_euler_to_vector.pivot_axis = 'Z'
    # Rotation
    align_euler_to_vector.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Factor
    align_euler_to_vector.inputs[1].default_value = 1.0

    # Node Combine XYZ.002
    combine_xyz_002 = ff_clover_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    combine_xyz_002.show_options = True

    # Node Instance on Points
    instance_on_points = ff_clover_nodes_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    instance_on_points.show_options = True
    # Selection
    instance_on_points.inputs[1].default_value = True
    # Pick Instance
    instance_on_points.inputs[3].default_value = False
    # Instance Index
    instance_on_points.inputs[4].default_value = 0

    # Node Realize Instances
    realize_instances = ff_clover_nodes_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    realize_instances.show_options = True
    realize_instances.realize_to_point_domain = True
    # Selection
    realize_instances.inputs[1].default_value = True
    # Realize All
    realize_instances.inputs[2].default_value = True
    # Depth
    realize_instances.inputs[3].default_value = 0

    # Node Ico Sphere
    ico_sphere = ff_clover_nodes_1.nodes.new("GeometryNodeMeshIcoSphere")
    ico_sphere.name = "Ico Sphere"
    ico_sphere.show_options = True
    # Radius
    ico_sphere.inputs[0].default_value = 1.0

    # Node Position.002
    position_002 = ff_clover_nodes_1.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"
    position_002.show_options = True

    # Node Separate XYZ.001
    separate_xyz_001 = ff_clover_nodes_1.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"
    separate_xyz_001.show_options = True

    # Node Map Range.003
    map_range_003 = ff_clover_nodes_1.nodes.new("ShaderNodeMapRange")
    map_range_003.name = "Map Range.003"
    map_range_003.show_options = True
    map_range_003.clamp = True
    map_range_003.data_type = 'FLOAT'
    map_range_003.interpolation_type = 'LINEAR'
    # From Min
    map_range_003.inputs[1].default_value = -1.0
    # From Max
    map_range_003.inputs[2].default_value = 1.0
    # To Min
    map_range_003.inputs[3].default_value = 0.0
    # To Max
    map_range_003.inputs[4].default_value = 0.5

    # Node Map Range.004
    map_range_004 = ff_clover_nodes_1.nodes.new("ShaderNodeMapRange")
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

    # Node Combine XYZ.003
    combine_xyz_003 = ff_clover_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003.name = "Combine XYZ.003"
    combine_xyz_003.show_options = True
    # Z
    combine_xyz_003.inputs[2].default_value = 0.0

    # Node Store Named Attribute.002
    store_named_attribute_002 = ff_clover_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_002.name = "Store Named Attribute.002"
    store_named_attribute_002.show_options = True
    store_named_attribute_002.data_type = 'FLOAT2'
    store_named_attribute_002.domain = 'CORNER'
    # Selection
    store_named_attribute_002.inputs[1].default_value = True
    # Name
    store_named_attribute_002.inputs[2].default_value = "UVMap"

    # Node Store Named Attribute.003
    store_named_attribute_003 = ff_clover_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_003.name = "Store Named Attribute.003"
    store_named_attribute_003.show_options = True
    store_named_attribute_003.data_type = 'FLOAT_COLOR'
    store_named_attribute_003.domain = 'CORNER'
    # Selection
    store_named_attribute_003.inputs[1].default_value = True
    # Name
    store_named_attribute_003.inputs[2].default_value = "ColorMask"

    # Node Math.032
    math_032 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_032.name = "Math.032"
    math_032.show_options = True
    math_032.operation = 'MULTIPLY'
    math_032.use_clamp = False

    # Node Combine XYZ.004
    combine_xyz_004 = ff_clover_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_004.name = "Combine XYZ.004"
    combine_xyz_004.show_options = True
    # X
    combine_xyz_004.inputs[0].default_value = 0.0
    # Y
    combine_xyz_004.inputs[1].default_value = 0.0

    # Node Transform Geometry.001
    transform_geometry_001 = ff_clover_nodes_1.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.show_options = True
    # Mode
    transform_geometry_001.inputs[1].default_value = 'Components'
    # Rotation
    transform_geometry_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Grid.001
    grid_001 = ff_clover_nodes_1.nodes.new("GeometryNodeMeshGrid")
    grid_001.name = "Grid.001"
    grid_001.show_options = True
    # Size X
    grid_001.inputs[0].default_value = 1.0
    # Vertices Y
    grid_001.inputs[3].default_value = 2

    # Node Math.033
    math_033 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_033.name = "Math.033"
    math_033.show_options = True
    math_033.operation = 'ADD'
    math_033.use_clamp = False
    # Value_001
    math_033.inputs[1].default_value = 1.0

    # Node Position.003
    position_003 = ff_clover_nodes_1.nodes.new("GeometryNodeInputPosition")
    position_003.name = "Position.003"
    position_003.show_options = True

    # Node Separate XYZ.002
    separate_xyz_002 = ff_clover_nodes_1.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_002.name = "Separate XYZ.002"
    separate_xyz_002.show_options = True

    # Node Map Range.005
    map_range_005 = ff_clover_nodes_1.nodes.new("ShaderNodeMapRange")
    map_range_005.name = "Map Range.005"
    map_range_005.show_options = True
    map_range_005.clamp = True
    map_range_005.data_type = 'FLOAT'
    map_range_005.interpolation_type = 'LINEAR'
    # From Min
    map_range_005.inputs[1].default_value = -0.5
    # From Max
    map_range_005.inputs[2].default_value = 0.5
    # To Min
    map_range_005.inputs[3].default_value = 0.8999999761581421
    # To Max
    map_range_005.inputs[4].default_value = 1.0

    # Node Math.034
    math_034 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_034.name = "Math.034"
    math_034.show_options = True
    math_034.operation = 'DIVIDE'
    math_034.use_clamp = False

    # Node Map Range.006
    map_range_006 = ff_clover_nodes_1.nodes.new("ShaderNodeMapRange")
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
    map_range_006.inputs[3].default_value = 0.0
    # To Max
    map_range_006.inputs[4].default_value = 1.0

    # Node Combine XYZ.005
    combine_xyz_005 = ff_clover_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_005.name = "Combine XYZ.005"
    combine_xyz_005.show_options = True
    # Z
    combine_xyz_005.inputs[2].default_value = 0.0

    # Node Store Named Attribute.004
    store_named_attribute_004 = ff_clover_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_004.name = "Store Named Attribute.004"
    store_named_attribute_004.show_options = True
    store_named_attribute_004.data_type = 'FLOAT2'
    store_named_attribute_004.domain = 'CORNER'
    # Selection
    store_named_attribute_004.inputs[1].default_value = True
    # Name
    store_named_attribute_004.inputs[2].default_value = "UVMap"

    # Node Math.035
    math_035 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_035.name = "Math.035"
    math_035.show_options = True
    math_035.operation = 'ADD'
    math_035.use_clamp = False
    # Value_001
    math_035.inputs[1].default_value = 0.5

    # Node Math.036
    math_036 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_036.name = "Math.036"
    math_036.show_options = True
    math_036.operation = 'MULTIPLY'
    math_036.use_clamp = False
    # Value_001
    math_036.inputs[1].default_value = 6.2831854820251465

    # Node Math.037
    math_037 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_037.name = "Math.037"
    math_037.show_options = True
    math_037.operation = 'SINE'
    math_037.use_clamp = False

    # Node Math.038
    math_038 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_038.name = "Math.038"
    math_038.show_options = True
    math_038.operation = 'MULTIPLY'
    math_038.use_clamp = False

    # Node Math.039
    math_039 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_039.name = "Math.039"
    math_039.show_options = True
    math_039.operation = 'COSINE'
    math_039.use_clamp = False

    # Node Math.040
    math_040 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_040.name = "Math.040"
    math_040.show_options = True
    math_040.operation = 'MULTIPLY'
    math_040.use_clamp = False

    # Node Math.041
    math_041 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_041.name = "Math.041"
    math_041.show_options = True
    math_041.operation = 'DIVIDE'
    math_041.use_clamp = False
    # Value_001
    math_041.inputs[1].default_value = 2.0

    # Node Math.042
    math_042 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_042.name = "Math.042"
    math_042.show_options = True
    math_042.operation = 'SUBTRACT'
    math_042.use_clamp = False

    # Node Combine XYZ.006
    combine_xyz_006 = ff_clover_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_006.name = "Combine XYZ.006"
    combine_xyz_006.show_options = True

    # Node Set Position.001
    set_position_001 = ff_clover_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    set_position_001.show_options = True
    # Selection
    set_position_001.inputs[1].default_value = True
    # Offset
    set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Merge by Distance
    merge_by_distance = ff_clover_nodes_1.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.show_options = True
    # Selection
    merge_by_distance.inputs[1].default_value = True
    # Mode
    merge_by_distance.inputs[2].default_value = 'All'
    # Distance
    merge_by_distance.inputs[3].default_value = 0.0010000000474974513

    # Node Flip Faces
    flip_faces = ff_clover_nodes_1.nodes.new("GeometryNodeFlipFaces")
    flip_faces.name = "Flip Faces"
    flip_faces.show_options = True
    # Selection
    flip_faces.inputs[1].default_value = True

    # Node Store Named Attribute.005
    store_named_attribute_005 = ff_clover_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_005.name = "Store Named Attribute.005"
    store_named_attribute_005.show_options = True
    store_named_attribute_005.data_type = 'FLOAT_COLOR'
    store_named_attribute_005.domain = 'CORNER'
    # Selection
    store_named_attribute_005.inputs[1].default_value = True
    # Name
    store_named_attribute_005.inputs[2].default_value = "ColorMask"

    # Node Transform Geometry.002
    transform_geometry_002 = ff_clover_nodes_1.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    transform_geometry_002.show_options = True
    # Mode
    transform_geometry_002.inputs[1].default_value = 'Components'
    # Rotation
    transform_geometry_002.inputs[3].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_002.inputs[4].default_value = (1.0, 1.0, 1.0)

    # Node Join Geometry
    join_geometry = ff_clover_nodes_1.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    join_geometry.show_options = True

    # Node Set Shade Smooth
    set_shade_smooth = ff_clover_nodes_1.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.show_options = True
    set_shade_smooth.domain = 'FACE'
    # Selection
    set_shade_smooth.inputs[1].default_value = True

    # Node Combine XYZ.007
    combine_xyz_007 = ff_clover_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_007.name = "Combine XYZ.007"
    combine_xyz_007.show_options = True
    # X
    combine_xyz_007.inputs[0].default_value = 0.0
    # Y
    combine_xyz_007.inputs[1].default_value = 0.0

    # Node Transform Geometry.003
    transform_geometry_003 = ff_clover_nodes_1.nodes.new("GeometryNodeTransform")
    transform_geometry_003.name = "Transform Geometry.003"
    transform_geometry_003.show_options = True
    # Mode
    transform_geometry_003.inputs[1].default_value = 'Components'
    # Rotation
    transform_geometry_003.inputs[3].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_003.inputs[4].default_value = (1.0, 1.0, 1.0)

    # Node Math.043
    math_043 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_043.name = "Math.043"
    math_043.show_options = True
    math_043.operation = 'SUBTRACT'
    math_043.use_clamp = False

    # Node Points
    points = ff_clover_nodes_1.nodes.new("GeometryNodePoints")
    points.name = "Points"
    points.show_options = True
    # Position
    points.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Radius
    points.inputs[2].default_value = 0.10000000149011612

    # Node Reroute.004
    reroute_004 = ff_clover_nodes_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    reroute_004.socket_idname = "NodeSocketInt"
    # Node Math.044
    math_044 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_044.name = "Math.044"
    math_044.show_options = True
    math_044.operation = 'ADD'
    math_044.use_clamp = False
    # Value_001
    math_044.inputs[1].default_value = 1337.0

    # Node Math.045
    math_045 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_045.name = "Math.045"
    math_045.show_options = True
    math_045.operation = 'ADD'
    math_045.use_clamp = False
    # Value_001
    math_045.inputs[1].default_value = 99.0

    # Node Math.046
    math_046 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_046.name = "Math.046"
    math_046.show_options = True
    math_046.operation = 'ADD'
    math_046.use_clamp = False
    # Value_001
    math_046.inputs[1].default_value = 7.0

    # Node Random Value
    random_value = ff_clover_nodes_1.nodes.new("FunctionNodeRandomValue")
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
    random_value_001 = ff_clover_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value_001.name = "Random Value.001"
    random_value_001.show_options = True
    random_value_001.data_type = 'FLOAT'
    # Min
    random_value_001.inputs[0].default_value = 0.0
    # Max
    random_value_001.inputs[1].default_value = 1.0
    # ID
    random_value_001.inputs[2].default_value = 0

    # Node Math.047
    math_047 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_047.name = "Math.047"
    math_047.show_options = True
    math_047.operation = 'POWER'
    math_047.use_clamp = False
    # Value_001
    math_047.inputs[1].default_value = 0.5

    # Node Math.048
    math_048 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_048.name = "Math.048"
    math_048.show_options = True
    math_048.operation = 'MULTIPLY'
    math_048.use_clamp = False

    # Node Math.049
    math_049 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_049.name = "Math.049"
    math_049.show_options = True
    math_049.operation = 'COSINE'
    math_049.use_clamp = False

    # Node Math.050
    math_050 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_050.name = "Math.050"
    math_050.show_options = True
    math_050.operation = 'SINE'
    math_050.use_clamp = False

    # Node Math.051
    math_051 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_051.name = "Math.051"
    math_051.show_options = True
    math_051.operation = 'MULTIPLY'
    math_051.use_clamp = False

    # Node Math.052
    math_052 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_052.name = "Math.052"
    math_052.show_options = True
    math_052.operation = 'MULTIPLY'
    math_052.use_clamp = False

    # Node Combine XYZ.008
    combine_xyz_008 = ff_clover_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_008.name = "Combine XYZ.008"
    combine_xyz_008.show_options = True
    # Z
    combine_xyz_008.inputs[2].default_value = 0.0

    # Node Set Position.002
    set_position_002 = ff_clover_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position_002.name = "Set Position.002"
    set_position_002.show_options = True
    # Selection
    set_position_002.inputs[1].default_value = True
    # Offset
    set_position_002.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Random Value.002
    random_value_002 = ff_clover_nodes_1.nodes.new("FunctionNodeRandomValue")
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
    random_value_003 = ff_clover_nodes_1.nodes.new("FunctionNodeRandomValue")
    random_value_003.name = "Random Value.003"
    random_value_003.show_options = True
    random_value_003.data_type = 'FLOAT'
    # ID
    random_value_003.inputs[2].default_value = 0

    # Node Instance on Points.001
    instance_on_points_001 = ff_clover_nodes_1.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_001.name = "Instance on Points.001"
    instance_on_points_001.show_options = True
    # Selection
    instance_on_points_001.inputs[1].default_value = True
    # Pick Instance
    instance_on_points_001.inputs[3].default_value = False
    # Instance Index
    instance_on_points_001.inputs[4].default_value = 0

    # Node Realize Instances.001
    realize_instances_001 = ff_clover_nodes_1.nodes.new("GeometryNodeRealizeInstances")
    realize_instances_001.name = "Realize Instances.001"
    realize_instances_001.show_options = True
    realize_instances_001.realize_to_point_domain = True
    # Selection
    realize_instances_001.inputs[1].default_value = True
    # Realize All
    realize_instances_001.inputs[2].default_value = True
    # Depth
    realize_instances_001.inputs[3].default_value = 0

    # Node Index
    index = ff_clover_nodes_1.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    index.show_options = True

    # Node Store Named Attribute.006
    store_named_attribute_006 = ff_clover_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_006.name = "Store Named Attribute.006"
    store_named_attribute_006.show_options = True
    store_named_attribute_006.data_type = 'INT'
    store_named_attribute_006.domain = 'INSTANCE'
    # Selection
    store_named_attribute_006.inputs[1].default_value = True
    # Name
    store_named_attribute_006.inputs[2].default_value = "fractal_id"

    # Node Set Material
    set_material = ff_clover_nodes_1.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.show_options = True
    # Selection
    set_material.inputs[1].default_value = True

    # Node Normal
    normal = ff_clover_nodes_1.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"
    normal.show_options = True
    normal.legacy_corner_normals = False

    # Node Convex Hull
    convex_hull = ff_clover_nodes_1.nodes.new("GeometryNodeConvexHull")
    convex_hull.name = "Convex Hull"
    convex_hull.show_options = True

    # Node Set Shade Smooth.001
    set_shade_smooth_001 = ff_clover_nodes_1.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth_001.name = "Set Shade Smooth.001"
    set_shade_smooth_001.show_options = True
    set_shade_smooth_001.domain = 'FACE'
    # Selection
    set_shade_smooth_001.inputs[1].default_value = True
    # Shade Smooth
    set_shade_smooth_001.inputs[2].default_value = True

    # Node Sample Nearest Surface
    sample_nearest_surface = ff_clover_nodes_1.nodes.new("GeometryNodeSampleNearestSurface")
    sample_nearest_surface.name = "Sample Nearest Surface"
    sample_nearest_surface.show_options = True
    sample_nearest_surface.data_type = 'FLOAT_VECTOR'
    # Group ID
    sample_nearest_surface.inputs[2].default_value = 0
    # Sample Position
    sample_nearest_surface.inputs[3].default_value = (0.0, 0.0, 0.0)
    # Sample Group ID
    sample_nearest_surface.inputs[4].default_value = 0

    # Node Math.053
    math_053 = ff_clover_nodes_1.nodes.new("ShaderNodeMath")
    math_053.name = "Math.053"
    math_053.show_options = True
    math_053.operation = 'SUBTRACT'
    math_053.use_clamp = False
    # Value
    math_053.inputs[0].default_value = 1.0

    # Node Vector Math
    vector_math = ff_clover_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.show_options = True
    vector_math.operation = 'SCALE'

    # Node Vector Math.001
    vector_math_001 = ff_clover_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.show_options = True
    vector_math_001.operation = 'SCALE'

    # Node Vector Math.002
    vector_math_002 = ff_clover_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.show_options = True
    vector_math_002.operation = 'ADD'

    # Node Vector Math.003
    vector_math_003 = ff_clover_nodes_1.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.show_options = True
    vector_math_003.operation = 'NORMALIZE'

    # Node Set Mesh Normal
    set_mesh_normal = ff_clover_nodes_1.nodes.new("GeometryNodeSetMeshNormal")
    set_mesh_normal.name = "Set Mesh Normal"
    set_mesh_normal.show_options = True
    set_mesh_normal.domain = 'CORNER'
    set_mesh_normal.mode = 'FREE'

    # Node Frame
    frame = ff_clover_nodes_1.nodes.new("NodeFrame")
    frame.label = "Auto-Odd Resolution"
    frame.name = "Frame"
    frame.use_custom_color = True
    frame.color = (0.30000001192092896, 0.20000000298023224, 0.20000000298023224)
    frame.show_options = True
    frame.label_size = 20
    frame.shrink = True

    # Node Frame.001
    frame_001 = ff_clover_nodes_1.nodes.new("NodeFrame")
    frame_001.label = "Leaf Generation Math & Planar UV"
    frame_001.name = "Frame.001"
    frame_001.use_custom_color = True
    frame_001.color = (0.20000000298023224, 0.30000001192092896, 0.20000000298023224)
    frame_001.show_options = True
    frame_001.label_size = 20
    frame_001.shrink = True

    # Node Frame.002
    frame_002 = ff_clover_nodes_1.nodes.new("NodeFrame")
    frame_002.label = "Petal Instancing"
    frame_002.name = "Frame.002"
    frame_002.use_custom_color = True
    frame_002.color = (0.20000000298023224, 0.20000000298023224, 0.30000001192092896)
    frame_002.show_options = True
    frame_002.label_size = 20
    frame_002.shrink = True

    # Node Frame.003
    frame_003 = ff_clover_nodes_1.nodes.new("NodeFrame")
    frame_003.label = "Center Generation"
    frame_003.name = "Frame.003"
    frame_003.use_custom_color = True
    frame_003.color = (0.30000001192092896, 0.30000001192092896, 0.20000000298023224)
    frame_003.show_options = True
    frame_003.label_size = 20
    frame_003.shrink = True

    # Node Frame.004
    frame_004 = ff_clover_nodes_1.nodes.new("NodeFrame")
    frame_004.label = "Stem Generation"
    frame_004.name = "Frame.004"
    frame_004.use_custom_color = True
    frame_004.color = (0.20000000298023224, 0.30000001192092896, 0.30000001192092896)
    frame_004.show_options = True
    frame_004.label_size = 20
    frame_004.shrink = True

    # Node Frame.005
    frame_005 = ff_clover_nodes_1.nodes.new("NodeFrame")
    frame_005.label = "Flower Assembly & Z-Pivot"
    frame_005.name = "Frame.005"
    frame_005.use_custom_color = True
    frame_005.color = (0.30000001192092896, 0.20000000298023224, 0.30000001192092896)
    frame_005.show_options = True
    frame_005.label_size = 20
    frame_005.shrink = True

    # Node Frame.006
    frame_006 = ff_clover_nodes_1.nodes.new("NodeFrame")
    frame_006.label = "Field Distribution & Butcher ID"
    frame_006.name = "Frame.006"
    frame_006.use_custom_color = True
    frame_006.color = (0.4000000059604645, 0.20000000298023224, 0.20000000298023224)
    frame_006.show_options = True
    frame_006.label_size = 20
    frame_006.shrink = True

    # Node Frame.007
    frame_007 = ff_clover_nodes_1.nodes.new("NodeFrame")
    frame_007.label = "Stylized Normals & Output"
    frame_007.name = "Frame.007"
    frame_007.use_custom_color = True
    frame_007.color = (0.4000000059604645, 0.20000000298023224, 0.4000000059604645)
    frame_007.show_options = True
    frame_007.label_size = 20
    frame_007.shrink = True

    # Node Group Input.008
    group_input_008 = ff_clover_nodes_1.nodes.new("NodeGroupInput")
    group_input_008.name = "Group Input.008"
    group_input_008.show_options = True

    # Node Reroute
    reroute = ff_clover_nodes_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketFloat"
    # Node Reroute.006
    reroute_006 = ff_clover_nodes_1.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.show_options = True
    reroute_006.socket_idname = "NodeSocketFloat"
    # Node Reroute.007
    reroute_007 = ff_clover_nodes_1.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.show_options = True
    reroute_007.socket_idname = "NodeSocketFloat"
    # Node Reroute.001
    reroute_001 = ff_clover_nodes_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketFloat"
    # Node Reroute.008
    reroute_008 = ff_clover_nodes_1.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.show_options = True
    reroute_008.socket_idname = "NodeSocketVector"
    # Node Group Input.009
    group_input_009 = ff_clover_nodes_1.nodes.new("NodeGroupInput")
    group_input_009.name = "Group Input.009"
    group_input_009.show_options = True

    # Node Group Input.010
    group_input_010 = ff_clover_nodes_1.nodes.new("NodeGroupInput")
    group_input_010.name = "Group Input.010"
    group_input_010.show_options = True

    # Node Reroute.002
    reroute_002 = ff_clover_nodes_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketVector"
    # Node Reroute.003
    reroute_003 = ff_clover_nodes_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketFloat"
    # Node Reroute.009
    reroute_009 = ff_clover_nodes_1.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.show_options = True
    reroute_009.socket_idname = "NodeSocketFloat"
    # Node Reroute.010
    reroute_010 = ff_clover_nodes_1.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.show_options = True
    reroute_010.socket_idname = "NodeSocketVector"
    # Node Reroute.011
    reroute_011 = ff_clover_nodes_1.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"
    reroute_011.show_options = True
    reroute_011.socket_idname = "NodeSocketVector"
    # Node Group Input.011
    group_input_011 = ff_clover_nodes_1.nodes.new("NodeGroupInput")
    group_input_011.name = "Group Input.011"
    group_input_011.show_options = True

    # Node Reroute.012
    reroute_012 = ff_clover_nodes_1.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    reroute_012.show_options = True
    reroute_012.socket_idname = "NodeSocketInt"
    # Node Reroute.005
    reroute_005 = ff_clover_nodes_1.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.show_options = True
    reroute_005.socket_idname = "NodeSocketGeometry"
    # Node Reroute.013
    reroute_013 = ff_clover_nodes_1.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    reroute_013.show_options = True
    reroute_013.socket_idname = "NodeSocketFloat"
    # Node Group Output.001
    group_output_001 = ff_clover_nodes_1.nodes.new("NodeGroupOutput")
    group_output_001.name = "Group Output.001"
    group_output_001.show_options = True
    group_output_001.is_active_output = True

    # Set parents
    ff_clover_nodes_1.nodes["Group Input"].parent = ff_clover_nodes_1.nodes["Frame"]
    ff_clover_nodes_1.nodes["Group Input.001"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Group Input.002"].parent = ff_clover_nodes_1.nodes["Frame.002"]
    ff_clover_nodes_1.nodes["Group Input.003"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Group Input.004"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Group Input.005"].parent = ff_clover_nodes_1.nodes["Frame.005"]
    ff_clover_nodes_1.nodes["Group Input.006"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Group Input.007"].parent = ff_clover_nodes_1.nodes["Frame.007"]
    ff_clover_nodes_1.nodes["Math"].parent = ff_clover_nodes_1.nodes["Frame"]
    ff_clover_nodes_1.nodes["Math.001"].parent = ff_clover_nodes_1.nodes["Frame"]
    ff_clover_nodes_1.nodes["Math.002"].parent = ff_clover_nodes_1.nodes["Frame"]
    ff_clover_nodes_1.nodes["Math.003"].parent = ff_clover_nodes_1.nodes["Frame"]
    ff_clover_nodes_1.nodes["Math.004"].parent = ff_clover_nodes_1.nodes["Frame"]
    ff_clover_nodes_1.nodes["Grid"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Position"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Separate XYZ"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.005"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.006"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.007"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.008"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.009"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.010"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.011"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.012"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.013"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.014"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.015"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.016"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.017"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.018"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.019"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.020"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Map Range"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.021"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.022"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.023"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Map Range.001"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Map Range.002"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Combine XYZ"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Store Named Attribute"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Store Named Attribute.001"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.024"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.025"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.026"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.027"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.028"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.029"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.030"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Math.031"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Combine XYZ.001"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Set Position"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Transform Geometry"].parent = ff_clover_nodes_1.nodes["Frame.002"]
    ff_clover_nodes_1.nodes["Mesh Circle"].parent = ff_clover_nodes_1.nodes["Frame.002"]
    ff_clover_nodes_1.nodes["Position.001"].parent = ff_clover_nodes_1.nodes["Frame.002"]
    ff_clover_nodes_1.nodes["Align Euler to Vector"].parent = ff_clover_nodes_1.nodes["Frame.002"]
    ff_clover_nodes_1.nodes["Combine XYZ.002"].parent = ff_clover_nodes_1.nodes["Frame.002"]
    ff_clover_nodes_1.nodes["Instance on Points"].parent = ff_clover_nodes_1.nodes["Frame.002"]
    ff_clover_nodes_1.nodes["Realize Instances"].parent = ff_clover_nodes_1.nodes["Frame.002"]
    ff_clover_nodes_1.nodes["Ico Sphere"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Position.002"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Separate XYZ.001"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Map Range.003"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Map Range.004"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Combine XYZ.003"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Store Named Attribute.002"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Store Named Attribute.003"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Math.032"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Combine XYZ.004"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Transform Geometry.001"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Grid.001"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Math.033"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Position.003"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Separate XYZ.002"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Map Range.005"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Math.034"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Map Range.006"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Combine XYZ.005"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Store Named Attribute.004"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Math.035"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Math.036"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Math.037"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Math.038"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Math.039"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Math.040"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Math.041"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Math.042"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Combine XYZ.006"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Set Position.001"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Merge by Distance"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Flip Faces"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Store Named Attribute.005"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Transform Geometry.002"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Join Geometry"].parent = ff_clover_nodes_1.nodes["Frame.005"]
    ff_clover_nodes_1.nodes["Set Shade Smooth"].parent = ff_clover_nodes_1.nodes["Frame.005"]
    ff_clover_nodes_1.nodes["Combine XYZ.007"].parent = ff_clover_nodes_1.nodes["Frame.005"]
    ff_clover_nodes_1.nodes["Transform Geometry.003"].parent = ff_clover_nodes_1.nodes["Frame.005"]
    ff_clover_nodes_1.nodes["Math.043"].parent = ff_clover_nodes_1.nodes["Frame.005"]
    ff_clover_nodes_1.nodes["Points"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Reroute.004"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Math.044"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Math.045"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Math.046"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Random Value"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Random Value.001"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Math.047"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Math.048"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Math.049"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Math.050"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Math.051"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Math.052"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Combine XYZ.008"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Set Position.002"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Random Value.002"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Random Value.003"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Instance on Points.001"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Realize Instances.001"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Index"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Store Named Attribute.006"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Set Material"].parent = ff_clover_nodes_1.nodes["Frame.007"]
    ff_clover_nodes_1.nodes["Normal"].parent = ff_clover_nodes_1.nodes["Frame.007"]
    ff_clover_nodes_1.nodes["Convex Hull"].parent = ff_clover_nodes_1.nodes["Frame.007"]
    ff_clover_nodes_1.nodes["Set Shade Smooth.001"].parent = ff_clover_nodes_1.nodes["Frame.007"]
    ff_clover_nodes_1.nodes["Sample Nearest Surface"].parent = ff_clover_nodes_1.nodes["Frame.007"]
    ff_clover_nodes_1.nodes["Math.053"].parent = ff_clover_nodes_1.nodes["Frame.007"]
    ff_clover_nodes_1.nodes["Vector Math"].parent = ff_clover_nodes_1.nodes["Frame.007"]
    ff_clover_nodes_1.nodes["Vector Math.001"].parent = ff_clover_nodes_1.nodes["Frame.007"]
    ff_clover_nodes_1.nodes["Vector Math.002"].parent = ff_clover_nodes_1.nodes["Frame.007"]
    ff_clover_nodes_1.nodes["Vector Math.003"].parent = ff_clover_nodes_1.nodes["Frame.007"]
    ff_clover_nodes_1.nodes["Set Mesh Normal"].parent = ff_clover_nodes_1.nodes["Frame.007"]
    ff_clover_nodes_1.nodes["Group Input.008"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Reroute"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Reroute.006"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Reroute.007"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Reroute.001"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Reroute.008"].parent = ff_clover_nodes_1.nodes["Frame.001"]
    ff_clover_nodes_1.nodes["Group Input.009"].parent = ff_clover_nodes_1.nodes["Frame.004"]
    ff_clover_nodes_1.nodes["Group Input.010"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Reroute.002"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Reroute.003"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Reroute.009"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Reroute.010"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Reroute.011"].parent = ff_clover_nodes_1.nodes["Frame.003"]
    ff_clover_nodes_1.nodes["Group Input.011"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Reroute.012"].parent = ff_clover_nodes_1.nodes["Frame.006"]
    ff_clover_nodes_1.nodes["Reroute.005"].parent = ff_clover_nodes_1.nodes["Frame.007"]
    ff_clover_nodes_1.nodes["Reroute.013"].parent = ff_clover_nodes_1.nodes["Frame.007"]

    # Set locations
    ff_clover_nodes_1.nodes["Group Input"].location = (29.7142333984375, -119.849853515625)
    ff_clover_nodes_1.nodes["Group Input.001"].location = (29.58935546875, -1178.62939453125)
    ff_clover_nodes_1.nodes["Group Input.002"].location = (32.5074462890625, -417.6788330078125)
    ff_clover_nodes_1.nodes["Group Input.003"].location = (532.47314453125, -36.0244140625)
    ff_clover_nodes_1.nodes["Group Input.004"].location = (30.4598388671875, -109.43988037109375)
    ff_clover_nodes_1.nodes["Group Input.005"].location = (29.68896484375, -35.559326171875)
    ff_clover_nodes_1.nodes["Group Input.006"].location = (29.713134765625, -229.082275390625)
    ff_clover_nodes_1.nodes["Group Input.007"].location = (190.89306640625, -478.723876953125)
    ff_clover_nodes_1.nodes["Math"].location = (197.6434326171875, -331.73046875)
    ff_clover_nodes_1.nodes["Math.001"].location = (364.3135986328125, -257.650390625)
    ff_clover_nodes_1.nodes["Math.002"].location = (530.9910888671875, -183.848876953125)
    ff_clover_nodes_1.nodes["Math.003"].location = (698.3533935546875, -110.12841796875)
    ff_clover_nodes_1.nodes["Math.004"].location = (864.0960693359375, -35.597900390625)
    ff_clover_nodes_1.nodes["Grid"].location = (2893.465576171875, -86.1002197265625)
    ff_clover_nodes_1.nodes["Position"].location = (192.976806640625, -1391.534912109375)
    ff_clover_nodes_1.nodes["Separate XYZ"].location = (353.8876953125, -1320.3922119140625)
    ff_clover_nodes_1.nodes["Math.005"].location = (515.60205078125, -1246.419921875)
    ff_clover_nodes_1.nodes["Math.006"].location = (679.59912109375, -1331.401611328125)
    ff_clover_nodes_1.nodes["Math.007"].location = (680.749755859375, -1175.166259765625)
    ff_clover_nodes_1.nodes["Math.008"].location = (854.05029296875, -1257.1363525390625)
    ff_clover_nodes_1.nodes["Math.009"].location = (1010.968017578125, -1182.382568359375)
    ff_clover_nodes_1.nodes["Math.010"].location = (1165.071533203125, -1108.7811279296875)
    ff_clover_nodes_1.nodes["Math.011"].location = (1330.9091796875, -1035.45068359375)
    ff_clover_nodes_1.nodes["Math.012"].location = (1495.64501953125, -1116.8489990234375)
    ff_clover_nodes_1.nodes["Math.013"].location = (1654.7806396484375, -1045.2496337890625)
    ff_clover_nodes_1.nodes["Math.014"].location = (1817.483642578125, -970.019287109375)
    ff_clover_nodes_1.nodes["Math.015"].location = (1495.28955078125, -961.5584716796875)
    ff_clover_nodes_1.nodes["Math.016"].location = (1654.625244140625, -865.89013671875)
    ff_clover_nodes_1.nodes["Math.017"].location = (1810.870849609375, -790.0673828125)
    ff_clover_nodes_1.nodes["Math.018"].location = (1969.07666015625, -716.325927734375)
    ff_clover_nodes_1.nodes["Math.019"].location = (2186.85595703125, -621.320556640625)
    ff_clover_nodes_1.nodes["Math.020"].location = (2176.397705078125, -894.3524169921875)
    ff_clover_nodes_1.nodes["Map Range"].location = (2368.65380859375, -478.8831787109375)
    ff_clover_nodes_1.nodes["Math.021"].location = (2373.408203125, -741.7634887695312)
    ff_clover_nodes_1.nodes["Math.022"].location = (2543.307373046875, -482.8731689453125)
    ff_clover_nodes_1.nodes["Math.023"].location = (2709.017822265625, -608.094970703125)
    ff_clover_nodes_1.nodes["Map Range.001"].location = (2895.098876953125, -256.9085693359375)
    ff_clover_nodes_1.nodes["Map Range.002"].location = (2894.633056640625, -507.0360107421875)
    ff_clover_nodes_1.nodes["Combine XYZ"].location = (3055.297119140625, -231.5325927734375)
    ff_clover_nodes_1.nodes["Store Named Attribute"].location = (3216.206298828125, -35.9886474609375)
    ff_clover_nodes_1.nodes["Store Named Attribute.001"].location = (3389.638427734375, -36.0826416015625)
    ff_clover_nodes_1.nodes["Math.024"].location = (555.4814453125, -1742.0604248046875)
    ff_clover_nodes_1.nodes["Math.025"].location = (680.15478515625, -1465.990966796875)
    ff_clover_nodes_1.nodes["Math.026"].location = (1009.98583984375, -1643.52294921875)
    ff_clover_nodes_1.nodes["Math.027"].location = (853.558837890625, -1417.16357421875)
    ff_clover_nodes_1.nodes["Math.028"].location = (2333.875244140625, -1441.4267578125)
    ff_clover_nodes_1.nodes["Math.029"].location = (1007.62939453125, -1487.1337890625)
    ff_clover_nodes_1.nodes["Math.030"].location = (1177.3709716796875, -1411.392822265625)
    ff_clover_nodes_1.nodes["Math.031"].location = (2522.25927734375, -1303.977783203125)
    ff_clover_nodes_1.nodes["Combine XYZ.001"].location = (2888.2470703125, -990.8580322265625)
    ff_clover_nodes_1.nodes["Set Position"].location = (3555.53076171875, -86.963623046875)
    ff_clover_nodes_1.nodes["Transform Geometry"].location = (30.4793701171875, -81.1614990234375)
    ff_clover_nodes_1.nodes["Mesh Circle"].location = (259.0321044921875, -159.10955810546875)
    ff_clover_nodes_1.nodes["Position.001"].location = (256.79571533203125, -483.2847900390625)
    ff_clover_nodes_1.nodes["Align Euler to Vector"].location = (257.64569091796875, -307.21722412109375)
    ff_clover_nodes_1.nodes["Combine XYZ.002"].location = (252.7520751953125, -545.7125244140625)
    ff_clover_nodes_1.nodes["Instance on Points"].location = (476.3115234375, -35.5430908203125)
    ff_clover_nodes_1.nodes["Realize Instances"].location = (646.262451171875, -36.5650634765625)
    ff_clover_nodes_1.nodes["Ico Sphere"].location = (704.436279296875, -468.15740966796875)
    ff_clover_nodes_1.nodes["Position.002"].location = (29.6527099609375, -846.9938354492188)
    ff_clover_nodes_1.nodes["Separate XYZ.001"].location = (187.8150634765625, -776.28662109375)
    ff_clover_nodes_1.nodes["Map Range.003"].location = (363.8753662109375, -570.0799560546875)
    ff_clover_nodes_1.nodes["Map Range.004"].location = (363.7733154296875, -817.4664306640625)
    ff_clover_nodes_1.nodes["Combine XYZ.003"].location = (535.186279296875, -667.21240234375)
    ff_clover_nodes_1.nodes["Store Named Attribute.002"].location = (1044.17041015625, -419.56378173828125)
    ff_clover_nodes_1.nodes["Store Named Attribute.003"].location = (1204.2734375, -419.5537109375)
    ff_clover_nodes_1.nodes["Math.032"].location = (1069.8037109375, -796.5074462890625)
    ff_clover_nodes_1.nodes["Combine XYZ.004"].location = (1228.418212890625, -728.6139526367188)
    ff_clover_nodes_1.nodes["Transform Geometry.001"].location = (1415.202392578125, -444.52276611328125)
    ff_clover_nodes_1.nodes["Grid.001"].location = (510.641357421875, -84.70712280273438)
    ff_clover_nodes_1.nodes["Math.033"].location = (348.1212158203125, -175.94485473632812)
    ff_clover_nodes_1.nodes["Position.003"].location = (29.9947509765625, -741.9649047851562)
    ff_clover_nodes_1.nodes["Separate XYZ.002"].location = (194.0828857421875, -672.5525512695312)
    ff_clover_nodes_1.nodes["Map Range.005"].location = (353.3565673828125, -775.8152465820312)
    ff_clover_nodes_1.nodes["Math.034"].location = (356.1551513671875, -620.2051391601562)
    ff_clover_nodes_1.nodes["Map Range.006"].location = (513.789306640625, -518.2753295898438)
    ff_clover_nodes_1.nodes["Combine XYZ.005"].location = (690.917724609375, -749.3748168945312)
    ff_clover_nodes_1.nodes["Store Named Attribute.004"].location = (883.419189453125, -35.75624084472656)
    ff_clover_nodes_1.nodes["Math.035"].location = (346.2218017578125, -1028.057861328125)
    ff_clover_nodes_1.nodes["Math.036"].location = (510.375732421875, -954.99267578125)
    ff_clover_nodes_1.nodes["Math.037"].location = (689.57421875, -1010.98486328125)
    ff_clover_nodes_1.nodes["Math.038"].location = (878.0166015625, -454.98162841796875)
    ff_clover_nodes_1.nodes["Math.039"].location = (693.516357421875, -879.98388671875)
    ff_clover_nodes_1.nodes["Math.040"].location = (879.796142578125, -797.7993774414062)
    ff_clover_nodes_1.nodes["Math.041"].location = (507.019287109375, -255.17239379882812)
    ff_clover_nodes_1.nodes["Math.042"].location = (877.2392578125, -614.4285278320312)
    ff_clover_nodes_1.nodes["Combine XYZ.006"].location = (1060.142333984375, -544.6796264648438)
    ff_clover_nodes_1.nodes["Set Position.001"].location = (1262.034912109375, -89.52188110351562)
    ff_clover_nodes_1.nodes["Merge by Distance"].location = (1422.238037109375, -63.16937255859375)
    ff_clover_nodes_1.nodes["Flip Faces"].location = (1578.942626953125, -90.33059692382812)
    ff_clover_nodes_1.nodes["Store Named Attribute.005"].location = (1739.115478515625, -39.25065612792969)
    ff_clover_nodes_1.nodes["Transform Geometry.002"].location = (1906.958251953125, -65.01177978515625)
    ff_clover_nodes_1.nodes["Join Geometry"].location = (367.059814453125, -646.796142578125)
    ff_clover_nodes_1.nodes["Set Shade Smooth"].location = (550.351806640625, -622.3118896484375)
    ff_clover_nodes_1.nodes["Combine XYZ.007"].location = (541.42626953125, -115.8817138671875)
    ff_clover_nodes_1.nodes["Transform Geometry.003"].location = (714.6640625, -622.065185546875)
    ff_clover_nodes_1.nodes["Math.043"].location = (384.869384765625, -182.80224609375)
    ff_clover_nodes_1.nodes["Points"].location = (1245.40185546875, -1142.7628173828125)
    ff_clover_nodes_1.nodes["Reroute.004"].location = (304.1005859375, -1734.394775390625)
    ff_clover_nodes_1.nodes["Math.044"].location = (305.31201171875, -991.962158203125)
    ff_clover_nodes_1.nodes["Math.045"].location = (1218.16455078125, -1628.536865234375)
    ff_clover_nodes_1.nodes["Math.046"].location = (1217.63134765625, -2411.036865234375)
    ff_clover_nodes_1.nodes["Random Value"].location = (595.341796875, -111.816162109375)
    ff_clover_nodes_1.nodes["Random Value.001"].location = (469.58740234375, -875.01806640625)
    ff_clover_nodes_1.nodes["Math.047"].location = (639.90869140625, -799.913330078125)
    ff_clover_nodes_1.nodes["Math.048"].location = (830.0244140625, -726.56640625)
    ff_clover_nodes_1.nodes["Math.049"].location = (830.9404296875, -878.5574951171875)
    ff_clover_nodes_1.nodes["Math.050"].location = (760.5693359375, -36.39453125)
    ff_clover_nodes_1.nodes["Math.051"].location = (1073.42529296875, -807.16748046875)
    ff_clover_nodes_1.nodes["Math.052"].location = (1073.93701171875, -959.7786865234375)
    ff_clover_nodes_1.nodes["Combine XYZ.008"].location = (1243.25244140625, -1018.5457763671875)
    ff_clover_nodes_1.nodes["Set Position.002"].location = (1412.84814453125, -1143.6893310546875)
    ff_clover_nodes_1.nodes["Random Value.002"].location = (1414.21923828125, -1386.7022705078125)
    ff_clover_nodes_1.nodes["Random Value.003"].location = (1410.54345703125, -1685.5325927734375)
    ff_clover_nodes_1.nodes["Instance on Points.001"].location = (1586.14599609375, -1250.646484375)
    ff_clover_nodes_1.nodes["Realize Instances.001"].location = (1910.25830078125, -1250.31396484375)
    ff_clover_nodes_1.nodes["Index"].location = (1584.36669921875, -1466.1944580078125)
    ff_clover_nodes_1.nodes["Store Named Attribute.006"].location = (1748.09619140625, -1200.4820556640625)
    ff_clover_nodes_1.nodes["Set Material"].location = (1230.3359375, -394.0224609375)
    ff_clover_nodes_1.nodes["Normal"].location = (187.96337890625, -231.2606201171875)
    ff_clover_nodes_1.nodes["Convex Hull"].location = (30.4443359375, -115.746337890625)
    ff_clover_nodes_1.nodes["Set Shade Smooth.001"].location = (189.3583984375, -90.31201171875)
    ff_clover_nodes_1.nodes["Sample Nearest Surface"].location = (370.98193359375, -43.130615234375)
    ff_clover_nodes_1.nodes["Math.053"].location = (376.40625, -275.17041015625)
    ff_clover_nodes_1.nodes["Vector Math"].location = (561.55810546875, -181.1640625)
    ff_clover_nodes_1.nodes["Vector Math.001"].location = (562.96728515625, -50.944580078125)
    ff_clover_nodes_1.nodes["Vector Math.002"].location = (727.6318359375, -87.6798095703125)
    ff_clover_nodes_1.nodes["Vector Math.003"].location = (886.32958984375, -35.8427734375)
    ff_clover_nodes_1.nodes["Set Mesh Normal"].location = (1066.685546875, -344.2939453125)
    ff_clover_nodes_1.nodes["Frame"].location = (-1302.0, 1928.0)
    ff_clover_nodes_1.nodes["Frame.001"].location = (-3031.0, 1144.0)
    ff_clover_nodes_1.nodes["Frame.002"].location = (711.0, 1163.0)
    ff_clover_nodes_1.nodes["Frame.003"].location = (1540.0, 1069.0)
    ff_clover_nodes_1.nodes["Frame.004"].location = (1544.0, -198.0)
    ff_clover_nodes_1.nodes["Frame.005"].location = (3141.0, 1782.0)
    ff_clover_nodes_1.nodes["Frame.006"].location = (4045.0, 2459.0)
    ff_clover_nodes_1.nodes["Frame.007"].location = (6145.0, 1350.0)
    ff_clover_nodes_1.nodes["Group Input.008"].location = (3216.341064453125, -210.6053466796875)
    ff_clover_nodes_1.nodes["Reroute"].location = (2301.36962890625, -1672.189453125)
    ff_clover_nodes_1.nodes["Reroute.006"].location = (551.128173828125, -619.7801513671875)
    ff_clover_nodes_1.nodes["Reroute.007"].location = (2665.309814453125, -925.4188842773438)
    ff_clover_nodes_1.nodes["Reroute.001"].location = (1528.30810546875, -394.6827392578125)
    ff_clover_nodes_1.nodes["Reroute.008"].location = (3481.50341796875, -1013.9068603515625)
    ff_clover_nodes_1.nodes["Group Input.009"].location = (1579.966552734375, -168.22479248046875)
    ff_clover_nodes_1.nodes["Group Input.010"].location = (901.0400390625, -599.1280517578125)
    ff_clover_nodes_1.nodes["Reroute.002"].location = (1385.3408203125, -243.736083984375)
    ff_clover_nodes_1.nodes["Reroute.003"].location = (1237.408447265625, -878.3619384765625)
    ff_clover_nodes_1.nodes["Reroute.009"].location = (1542.509765625, -879.6018676757812)
    ff_clover_nodes_1.nodes["Reroute.010"].location = (768.500732421875, -596.5839233398438)
    ff_clover_nodes_1.nodes["Reroute.011"].location = (1023.678466796875, -593.7671508789062)
    ff_clover_nodes_1.nodes["Group Input.011"].location = (1219.48486328125, -1782.5107421875)
    ff_clover_nodes_1.nodes["Reroute.012"].location = (296.92822265625, -1215.04296875)
    ff_clover_nodes_1.nodes["Reroute.005"].location = (43.2939453125, -445.470947265625)
    ff_clover_nodes_1.nodes["Reroute.013"].location = (483.68408203125, -996.1220092773438)
    ff_clover_nodes_1.nodes["Group Output.001"].location = (7568.38330078125, 957.3430786132812)

    # Set dimensions
    ff_clover_nodes_1.nodes["Group Input"].width  = 140.0
    ff_clover_nodes_1.nodes["Group Input"].height = 100.0

    ff_clover_nodes_1.nodes["Group Input.001"].width  = 140.0
    ff_clover_nodes_1.nodes["Group Input.001"].height = 100.0

    ff_clover_nodes_1.nodes["Group Input.002"].width  = 140.0
    ff_clover_nodes_1.nodes["Group Input.002"].height = 100.0

    ff_clover_nodes_1.nodes["Group Input.003"].width  = 140.0
    ff_clover_nodes_1.nodes["Group Input.003"].height = 100.0

    ff_clover_nodes_1.nodes["Group Input.004"].width  = 140.0
    ff_clover_nodes_1.nodes["Group Input.004"].height = 100.0

    ff_clover_nodes_1.nodes["Group Input.005"].width  = 140.0
    ff_clover_nodes_1.nodes["Group Input.005"].height = 100.0

    ff_clover_nodes_1.nodes["Group Input.006"].width  = 140.0
    ff_clover_nodes_1.nodes["Group Input.006"].height = 100.0

    ff_clover_nodes_1.nodes["Group Input.007"].width  = 140.0
    ff_clover_nodes_1.nodes["Group Input.007"].height = 100.0

    ff_clover_nodes_1.nodes["Math"].width  = 140.0
    ff_clover_nodes_1.nodes["Math"].height = 100.0

    ff_clover_nodes_1.nodes["Math.001"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.001"].height = 100.0

    ff_clover_nodes_1.nodes["Math.002"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.002"].height = 100.0

    ff_clover_nodes_1.nodes["Math.003"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.003"].height = 100.0

    ff_clover_nodes_1.nodes["Math.004"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.004"].height = 100.0

    ff_clover_nodes_1.nodes["Grid"].width  = 140.0
    ff_clover_nodes_1.nodes["Grid"].height = 100.0

    ff_clover_nodes_1.nodes["Position"].width  = 140.0
    ff_clover_nodes_1.nodes["Position"].height = 100.0

    ff_clover_nodes_1.nodes["Separate XYZ"].width  = 140.0
    ff_clover_nodes_1.nodes["Separate XYZ"].height = 100.0

    ff_clover_nodes_1.nodes["Math.005"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.005"].height = 100.0

    ff_clover_nodes_1.nodes["Math.006"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.006"].height = 100.0

    ff_clover_nodes_1.nodes["Math.007"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.007"].height = 100.0

    ff_clover_nodes_1.nodes["Math.008"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.008"].height = 100.0

    ff_clover_nodes_1.nodes["Math.009"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.009"].height = 100.0

    ff_clover_nodes_1.nodes["Math.010"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.010"].height = 100.0

    ff_clover_nodes_1.nodes["Math.011"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.011"].height = 100.0

    ff_clover_nodes_1.nodes["Math.012"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.012"].height = 100.0

    ff_clover_nodes_1.nodes["Math.013"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.013"].height = 100.0

    ff_clover_nodes_1.nodes["Math.014"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.014"].height = 100.0

    ff_clover_nodes_1.nodes["Math.015"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.015"].height = 100.0

    ff_clover_nodes_1.nodes["Math.016"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.016"].height = 100.0

    ff_clover_nodes_1.nodes["Math.017"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.017"].height = 100.0

    ff_clover_nodes_1.nodes["Math.018"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.018"].height = 100.0

    ff_clover_nodes_1.nodes["Math.019"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.019"].height = 100.0

    ff_clover_nodes_1.nodes["Math.020"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.020"].height = 100.0

    ff_clover_nodes_1.nodes["Map Range"].width  = 140.0
    ff_clover_nodes_1.nodes["Map Range"].height = 100.0

    ff_clover_nodes_1.nodes["Math.021"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.021"].height = 100.0

    ff_clover_nodes_1.nodes["Math.022"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.022"].height = 100.0

    ff_clover_nodes_1.nodes["Math.023"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.023"].height = 100.0

    ff_clover_nodes_1.nodes["Map Range.001"].width  = 140.0
    ff_clover_nodes_1.nodes["Map Range.001"].height = 100.0

    ff_clover_nodes_1.nodes["Map Range.002"].width  = 140.0
    ff_clover_nodes_1.nodes["Map Range.002"].height = 100.0

    ff_clover_nodes_1.nodes["Combine XYZ"].width  = 140.0
    ff_clover_nodes_1.nodes["Combine XYZ"].height = 100.0

    ff_clover_nodes_1.nodes["Store Named Attribute"].width  = 140.0
    ff_clover_nodes_1.nodes["Store Named Attribute"].height = 100.0

    ff_clover_nodes_1.nodes["Store Named Attribute.001"].width  = 140.0
    ff_clover_nodes_1.nodes["Store Named Attribute.001"].height = 100.0

    ff_clover_nodes_1.nodes["Math.024"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.024"].height = 100.0

    ff_clover_nodes_1.nodes["Math.025"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.025"].height = 100.0

    ff_clover_nodes_1.nodes["Math.026"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.026"].height = 100.0

    ff_clover_nodes_1.nodes["Math.027"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.027"].height = 100.0

    ff_clover_nodes_1.nodes["Math.028"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.028"].height = 100.0

    ff_clover_nodes_1.nodes["Math.029"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.029"].height = 100.0

    ff_clover_nodes_1.nodes["Math.030"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.030"].height = 100.0

    ff_clover_nodes_1.nodes["Math.031"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.031"].height = 100.0

    ff_clover_nodes_1.nodes["Combine XYZ.001"].width  = 140.0
    ff_clover_nodes_1.nodes["Combine XYZ.001"].height = 100.0

    ff_clover_nodes_1.nodes["Set Position"].width  = 140.0
    ff_clover_nodes_1.nodes["Set Position"].height = 100.0

    ff_clover_nodes_1.nodes["Transform Geometry"].width  = 140.0
    ff_clover_nodes_1.nodes["Transform Geometry"].height = 100.0

    ff_clover_nodes_1.nodes["Mesh Circle"].width  = 140.0
    ff_clover_nodes_1.nodes["Mesh Circle"].height = 100.0

    ff_clover_nodes_1.nodes["Position.001"].width  = 140.0
    ff_clover_nodes_1.nodes["Position.001"].height = 100.0

    ff_clover_nodes_1.nodes["Align Euler to Vector"].width  = 140.0
    ff_clover_nodes_1.nodes["Align Euler to Vector"].height = 100.0

    ff_clover_nodes_1.nodes["Combine XYZ.002"].width  = 140.0
    ff_clover_nodes_1.nodes["Combine XYZ.002"].height = 100.0

    ff_clover_nodes_1.nodes["Instance on Points"].width  = 140.0
    ff_clover_nodes_1.nodes["Instance on Points"].height = 100.0

    ff_clover_nodes_1.nodes["Realize Instances"].width  = 140.0
    ff_clover_nodes_1.nodes["Realize Instances"].height = 100.0

    ff_clover_nodes_1.nodes["Ico Sphere"].width  = 140.0
    ff_clover_nodes_1.nodes["Ico Sphere"].height = 100.0

    ff_clover_nodes_1.nodes["Position.002"].width  = 140.0
    ff_clover_nodes_1.nodes["Position.002"].height = 100.0

    ff_clover_nodes_1.nodes["Separate XYZ.001"].width  = 140.0
    ff_clover_nodes_1.nodes["Separate XYZ.001"].height = 100.0

    ff_clover_nodes_1.nodes["Map Range.003"].width  = 140.0
    ff_clover_nodes_1.nodes["Map Range.003"].height = 100.0

    ff_clover_nodes_1.nodes["Map Range.004"].width  = 140.0
    ff_clover_nodes_1.nodes["Map Range.004"].height = 100.0

    ff_clover_nodes_1.nodes["Combine XYZ.003"].width  = 140.0
    ff_clover_nodes_1.nodes["Combine XYZ.003"].height = 100.0

    ff_clover_nodes_1.nodes["Store Named Attribute.002"].width  = 140.0
    ff_clover_nodes_1.nodes["Store Named Attribute.002"].height = 100.0

    ff_clover_nodes_1.nodes["Store Named Attribute.003"].width  = 140.0
    ff_clover_nodes_1.nodes["Store Named Attribute.003"].height = 100.0

    ff_clover_nodes_1.nodes["Math.032"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.032"].height = 100.0

    ff_clover_nodes_1.nodes["Combine XYZ.004"].width  = 140.0
    ff_clover_nodes_1.nodes["Combine XYZ.004"].height = 100.0

    ff_clover_nodes_1.nodes["Transform Geometry.001"].width  = 140.0
    ff_clover_nodes_1.nodes["Transform Geometry.001"].height = 100.0

    ff_clover_nodes_1.nodes["Grid.001"].width  = 140.0
    ff_clover_nodes_1.nodes["Grid.001"].height = 100.0

    ff_clover_nodes_1.nodes["Math.033"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.033"].height = 100.0

    ff_clover_nodes_1.nodes["Position.003"].width  = 140.0
    ff_clover_nodes_1.nodes["Position.003"].height = 100.0

    ff_clover_nodes_1.nodes["Separate XYZ.002"].width  = 140.0
    ff_clover_nodes_1.nodes["Separate XYZ.002"].height = 100.0

    ff_clover_nodes_1.nodes["Map Range.005"].width  = 140.0
    ff_clover_nodes_1.nodes["Map Range.005"].height = 100.0

    ff_clover_nodes_1.nodes["Math.034"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.034"].height = 100.0

    ff_clover_nodes_1.nodes["Map Range.006"].width  = 140.0
    ff_clover_nodes_1.nodes["Map Range.006"].height = 100.0

    ff_clover_nodes_1.nodes["Combine XYZ.005"].width  = 140.0
    ff_clover_nodes_1.nodes["Combine XYZ.005"].height = 100.0

    ff_clover_nodes_1.nodes["Store Named Attribute.004"].width  = 140.0
    ff_clover_nodes_1.nodes["Store Named Attribute.004"].height = 100.0

    ff_clover_nodes_1.nodes["Math.035"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.035"].height = 100.0

    ff_clover_nodes_1.nodes["Math.036"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.036"].height = 100.0

    ff_clover_nodes_1.nodes["Math.037"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.037"].height = 100.0

    ff_clover_nodes_1.nodes["Math.038"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.038"].height = 100.0

    ff_clover_nodes_1.nodes["Math.039"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.039"].height = 100.0

    ff_clover_nodes_1.nodes["Math.040"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.040"].height = 100.0

    ff_clover_nodes_1.nodes["Math.041"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.041"].height = 100.0

    ff_clover_nodes_1.nodes["Math.042"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.042"].height = 100.0

    ff_clover_nodes_1.nodes["Combine XYZ.006"].width  = 140.0
    ff_clover_nodes_1.nodes["Combine XYZ.006"].height = 100.0

    ff_clover_nodes_1.nodes["Set Position.001"].width  = 140.0
    ff_clover_nodes_1.nodes["Set Position.001"].height = 100.0

    ff_clover_nodes_1.nodes["Merge by Distance"].width  = 140.0
    ff_clover_nodes_1.nodes["Merge by Distance"].height = 100.0

    ff_clover_nodes_1.nodes["Flip Faces"].width  = 140.0
    ff_clover_nodes_1.nodes["Flip Faces"].height = 100.0

    ff_clover_nodes_1.nodes["Store Named Attribute.005"].width  = 140.0
    ff_clover_nodes_1.nodes["Store Named Attribute.005"].height = 100.0

    ff_clover_nodes_1.nodes["Transform Geometry.002"].width  = 140.0
    ff_clover_nodes_1.nodes["Transform Geometry.002"].height = 100.0

    ff_clover_nodes_1.nodes["Join Geometry"].width  = 140.0
    ff_clover_nodes_1.nodes["Join Geometry"].height = 100.0

    ff_clover_nodes_1.nodes["Set Shade Smooth"].width  = 140.0
    ff_clover_nodes_1.nodes["Set Shade Smooth"].height = 100.0

    ff_clover_nodes_1.nodes["Combine XYZ.007"].width  = 140.0
    ff_clover_nodes_1.nodes["Combine XYZ.007"].height = 100.0

    ff_clover_nodes_1.nodes["Transform Geometry.003"].width  = 140.0
    ff_clover_nodes_1.nodes["Transform Geometry.003"].height = 100.0

    ff_clover_nodes_1.nodes["Math.043"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.043"].height = 100.0

    ff_clover_nodes_1.nodes["Points"].width  = 140.0
    ff_clover_nodes_1.nodes["Points"].height = 100.0

    ff_clover_nodes_1.nodes["Reroute.004"].width  = 100.0
    ff_clover_nodes_1.nodes["Reroute.004"].height = 100.0

    ff_clover_nodes_1.nodes["Math.044"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.044"].height = 100.0

    ff_clover_nodes_1.nodes["Math.045"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.045"].height = 100.0

    ff_clover_nodes_1.nodes["Math.046"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.046"].height = 100.0

    ff_clover_nodes_1.nodes["Random Value"].width  = 140.0
    ff_clover_nodes_1.nodes["Random Value"].height = 100.0

    ff_clover_nodes_1.nodes["Random Value.001"].width  = 140.0
    ff_clover_nodes_1.nodes["Random Value.001"].height = 100.0

    ff_clover_nodes_1.nodes["Math.047"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.047"].height = 100.0

    ff_clover_nodes_1.nodes["Math.048"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.048"].height = 100.0

    ff_clover_nodes_1.nodes["Math.049"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.049"].height = 100.0

    ff_clover_nodes_1.nodes["Math.050"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.050"].height = 100.0

    ff_clover_nodes_1.nodes["Math.051"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.051"].height = 100.0

    ff_clover_nodes_1.nodes["Math.052"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.052"].height = 100.0

    ff_clover_nodes_1.nodes["Combine XYZ.008"].width  = 140.0
    ff_clover_nodes_1.nodes["Combine XYZ.008"].height = 100.0

    ff_clover_nodes_1.nodes["Set Position.002"].width  = 140.0
    ff_clover_nodes_1.nodes["Set Position.002"].height = 100.0

    ff_clover_nodes_1.nodes["Random Value.002"].width  = 140.0
    ff_clover_nodes_1.nodes["Random Value.002"].height = 100.0

    ff_clover_nodes_1.nodes["Random Value.003"].width  = 140.0
    ff_clover_nodes_1.nodes["Random Value.003"].height = 100.0

    ff_clover_nodes_1.nodes["Instance on Points.001"].width  = 140.0
    ff_clover_nodes_1.nodes["Instance on Points.001"].height = 100.0

    ff_clover_nodes_1.nodes["Realize Instances.001"].width  = 140.0
    ff_clover_nodes_1.nodes["Realize Instances.001"].height = 100.0

    ff_clover_nodes_1.nodes["Index"].width  = 140.0
    ff_clover_nodes_1.nodes["Index"].height = 100.0

    ff_clover_nodes_1.nodes["Store Named Attribute.006"].width  = 140.0
    ff_clover_nodes_1.nodes["Store Named Attribute.006"].height = 100.0

    ff_clover_nodes_1.nodes["Set Material"].width  = 140.0
    ff_clover_nodes_1.nodes["Set Material"].height = 100.0

    ff_clover_nodes_1.nodes["Normal"].width  = 140.0
    ff_clover_nodes_1.nodes["Normal"].height = 100.0

    ff_clover_nodes_1.nodes["Convex Hull"].width  = 140.0
    ff_clover_nodes_1.nodes["Convex Hull"].height = 100.0

    ff_clover_nodes_1.nodes["Set Shade Smooth.001"].width  = 140.0
    ff_clover_nodes_1.nodes["Set Shade Smooth.001"].height = 100.0

    ff_clover_nodes_1.nodes["Sample Nearest Surface"].width  = 150.0
    ff_clover_nodes_1.nodes["Sample Nearest Surface"].height = 100.0

    ff_clover_nodes_1.nodes["Math.053"].width  = 140.0
    ff_clover_nodes_1.nodes["Math.053"].height = 100.0

    ff_clover_nodes_1.nodes["Vector Math"].width  = 140.0
    ff_clover_nodes_1.nodes["Vector Math"].height = 100.0

    ff_clover_nodes_1.nodes["Vector Math.001"].width  = 140.0
    ff_clover_nodes_1.nodes["Vector Math.001"].height = 100.0

    ff_clover_nodes_1.nodes["Vector Math.002"].width  = 140.0
    ff_clover_nodes_1.nodes["Vector Math.002"].height = 100.0

    ff_clover_nodes_1.nodes["Vector Math.003"].width  = 140.0
    ff_clover_nodes_1.nodes["Vector Math.003"].height = 100.0

    ff_clover_nodes_1.nodes["Set Mesh Normal"].width  = 140.0
    ff_clover_nodes_1.nodes["Set Mesh Normal"].height = 100.0

    ff_clover_nodes_1.nodes["Frame"].width  = 1034.0
    ff_clover_nodes_1.nodes["Frame"].height = 772.0

    ff_clover_nodes_1.nodes["Frame.001"].width  = 3726.0
    ff_clover_nodes_1.nodes["Frame.001"].height = 1898.0

    ff_clover_nodes_1.nodes["Frame.002"].width  = 816.0
    ff_clover_nodes_1.nodes["Frame.002"].height = 1070.0

    ff_clover_nodes_1.nodes["Frame.003"].width  = 1585.0
    ff_clover_nodes_1.nodes["Frame.003"].height = 1251.0

    ff_clover_nodes_1.nodes["Frame.004"].width  = 2077.0
    ff_clover_nodes_1.nodes["Frame.004"].height = 1206.0

    ff_clover_nodes_1.nodes["Frame.005"].width  = 885.0
    ff_clover_nodes_1.nodes["Frame.005"].height = 912.0

    ff_clover_nodes_1.nodes["Frame.006"].width  = 2080.0
    ff_clover_nodes_1.nodes["Frame.006"].height = 2589.0

    ff_clover_nodes_1.nodes["Frame.007"].width  = 1400.0
    ff_clover_nodes_1.nodes["Frame.007"].height = 1131.0

    ff_clover_nodes_1.nodes["Group Input.008"].width  = 140.0
    ff_clover_nodes_1.nodes["Group Input.008"].height = 100.0

    ff_clover_nodes_1.nodes["Reroute"].width  = 100.0
    ff_clover_nodes_1.nodes["Reroute"].height = 100.0

    ff_clover_nodes_1.nodes["Reroute.006"].width  = 100.0
    ff_clover_nodes_1.nodes["Reroute.006"].height = 100.0

    ff_clover_nodes_1.nodes["Reroute.007"].width  = 100.0
    ff_clover_nodes_1.nodes["Reroute.007"].height = 100.0

    ff_clover_nodes_1.nodes["Reroute.001"].width  = 100.0
    ff_clover_nodes_1.nodes["Reroute.001"].height = 100.0

    ff_clover_nodes_1.nodes["Reroute.008"].width  = 100.0
    ff_clover_nodes_1.nodes["Reroute.008"].height = 100.0

    ff_clover_nodes_1.nodes["Group Input.009"].width  = 140.0
    ff_clover_nodes_1.nodes["Group Input.009"].height = 100.0

    ff_clover_nodes_1.nodes["Group Input.010"].width  = 140.0
    ff_clover_nodes_1.nodes["Group Input.010"].height = 100.0

    ff_clover_nodes_1.nodes["Reroute.002"].width  = 100.0
    ff_clover_nodes_1.nodes["Reroute.002"].height = 100.0

    ff_clover_nodes_1.nodes["Reroute.003"].width  = 100.0
    ff_clover_nodes_1.nodes["Reroute.003"].height = 100.0

    ff_clover_nodes_1.nodes["Reroute.009"].width  = 100.0
    ff_clover_nodes_1.nodes["Reroute.009"].height = 100.0

    ff_clover_nodes_1.nodes["Reroute.010"].width  = 100.0
    ff_clover_nodes_1.nodes["Reroute.010"].height = 100.0

    ff_clover_nodes_1.nodes["Reroute.011"].width  = 100.0
    ff_clover_nodes_1.nodes["Reroute.011"].height = 100.0

    ff_clover_nodes_1.nodes["Group Input.011"].width  = 140.0
    ff_clover_nodes_1.nodes["Group Input.011"].height = 100.0

    ff_clover_nodes_1.nodes["Reroute.012"].width  = 100.0
    ff_clover_nodes_1.nodes["Reroute.012"].height = 100.0

    ff_clover_nodes_1.nodes["Reroute.005"].width  = 100.0
    ff_clover_nodes_1.nodes["Reroute.005"].height = 100.0

    ff_clover_nodes_1.nodes["Reroute.013"].width  = 100.0
    ff_clover_nodes_1.nodes["Reroute.013"].height = 100.0

    ff_clover_nodes_1.nodes["Group Output.001"].width  = 140.0
    ff_clover_nodes_1.nodes["Group Output.001"].height = 100.0


    # Initialize ff_clover_nodes_1 links

    # group_input.Resolution X -> math.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input"].outputs[13],
        ff_clover_nodes_1.nodes["Math"].inputs[0]
    )
    # math.Value -> math_001.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math"].outputs[0],
        ff_clover_nodes_1.nodes["Math.001"].inputs[0]
    )
    # math_001.Value -> math_002.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.001"].outputs[0],
        ff_clover_nodes_1.nodes["Math.002"].inputs[0]
    )
    # math_002.Value -> math_003.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.002"].outputs[0],
        ff_clover_nodes_1.nodes["Math.003"].inputs[0]
    )
    # math_003.Value -> math_004.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.003"].outputs[0],
        ff_clover_nodes_1.nodes["Math.004"].inputs[0]
    )
    # math_004.Value -> grid.Vertices X
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.004"].outputs[0],
        ff_clover_nodes_1.nodes["Grid"].inputs[2]
    )
    # group_input.Resolution Y -> grid.Vertices Y
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input"].outputs[14],
        ff_clover_nodes_1.nodes["Grid"].inputs[3]
    )
    # position.Position -> separate_xyz.Vector
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Position"].outputs[0],
        ff_clover_nodes_1.nodes["Separate XYZ"].inputs[0]
    )
    # math_005.Value -> math_007.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.005"].outputs[0],
        ff_clover_nodes_1.nodes["Math.007"].inputs[0]
    )
    # group_input_001.Center Density -> math_007.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.001"].outputs[15],
        ff_clover_nodes_1.nodes["Math.007"].inputs[1]
    )
    # math_006.Value -> math_008.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.006"].outputs[0],
        ff_clover_nodes_1.nodes["Math.008"].inputs[0]
    )
    # math_007.Value -> math_008.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.007"].outputs[0],
        ff_clover_nodes_1.nodes["Math.008"].inputs[1]
    )
    # math_008.Value -> math_009.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.008"].outputs[0],
        ff_clover_nodes_1.nodes["Math.009"].inputs[0]
    )
    # math_009.Value -> math_010.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.009"].outputs[0],
        ff_clover_nodes_1.nodes["Math.010"].inputs[0]
    )
    # math_010.Value -> math_011.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.010"].outputs[0],
        ff_clover_nodes_1.nodes["Math.011"].inputs[0]
    )
    # group_input_001.Side Sharpness -> math_011.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.001"].outputs[16],
        ff_clover_nodes_1.nodes["Math.011"].inputs[1]
    )
    # math_011.Value -> math_012.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.011"].outputs[0],
        ff_clover_nodes_1.nodes["Math.012"].inputs[0]
    )
    # math_012.Value -> math_013.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.012"].outputs[0],
        ff_clover_nodes_1.nodes["Math.013"].inputs[0]
    )
    # math_013.Value -> math_014.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.013"].outputs[0],
        ff_clover_nodes_1.nodes["Math.014"].inputs[0]
    )
    # group_input_001.Cleavage Depth -> math_014.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.001"].outputs[17],
        ff_clover_nodes_1.nodes["Math.014"].inputs[1]
    )
    # math_011.Value -> math_015.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.011"].outputs[0],
        ff_clover_nodes_1.nodes["Math.015"].inputs[0]
    )
    # math_011.Value -> math_015.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.011"].outputs[0],
        ff_clover_nodes_1.nodes["Math.015"].inputs[1]
    )
    # math_015.Value -> math_016.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.015"].outputs[0],
        ff_clover_nodes_1.nodes["Math.016"].inputs[1]
    )
    # math_016.Value -> math_017.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.016"].outputs[0],
        ff_clover_nodes_1.nodes["Math.017"].inputs[0]
    )
    # math_017.Value -> math_018.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.017"].outputs[0],
        ff_clover_nodes_1.nodes["Math.018"].inputs[0]
    )
    # math_014.Value -> math_019.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.014"].outputs[0],
        ff_clover_nodes_1.nodes["Math.019"].inputs[0]
    )
    # math_018.Value -> math_019.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.018"].outputs[0],
        ff_clover_nodes_1.nodes["Math.019"].inputs[1]
    )
    # math_014.Value -> math_020.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.014"].outputs[0],
        ff_clover_nodes_1.nodes["Math.020"].inputs[0]
    )
    # math_018.Value -> math_020.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.018"].outputs[0],
        ff_clover_nodes_1.nodes["Math.020"].inputs[1]
    )
    # math_019.Value -> math_021.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.019"].outputs[0],
        ff_clover_nodes_1.nodes["Math.021"].inputs[0]
    )
    # math_020.Value -> math_021.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.020"].outputs[0],
        ff_clover_nodes_1.nodes["Math.021"].inputs[1]
    )
    # math_021.Value -> math_022.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.021"].outputs[0],
        ff_clover_nodes_1.nodes["Math.022"].inputs[0]
    )
    # map_range.Result -> math_022.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Map Range"].outputs[0],
        ff_clover_nodes_1.nodes["Math.022"].inputs[1]
    )
    # reroute_007.Output -> math_023.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Reroute.007"].outputs[0],
        ff_clover_nodes_1.nodes["Math.023"].inputs[0]
    )
    # math_022.Value -> math_023.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.022"].outputs[0],
        ff_clover_nodes_1.nodes["Math.023"].inputs[1]
    )
    # reroute_001.Output -> map_range_001.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Reroute.001"].outputs[0],
        ff_clover_nodes_1.nodes["Map Range.001"].inputs[0]
    )
    # math_023.Value -> map_range_002.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.023"].outputs[0],
        ff_clover_nodes_1.nodes["Map Range.002"].inputs[0]
    )
    # map_range_001.Result -> combine_xyz.X
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Map Range.001"].outputs[0],
        ff_clover_nodes_1.nodes["Combine XYZ"].inputs[0]
    )
    # map_range_002.Result -> combine_xyz.Y
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Map Range.002"].outputs[0],
        ff_clover_nodes_1.nodes["Combine XYZ"].inputs[1]
    )
    # grid.Mesh -> store_named_attribute.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Grid"].outputs[0],
        ff_clover_nodes_1.nodes["Store Named Attribute"].inputs[0]
    )
    # combine_xyz.Vector -> store_named_attribute.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Combine XYZ"].outputs[0],
        ff_clover_nodes_1.nodes["Store Named Attribute"].inputs[3]
    )
    # store_named_attribute.Geometry -> store_named_attribute_001.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Store Named Attribute"].outputs[0],
        ff_clover_nodes_1.nodes["Store Named Attribute.001"].inputs[0]
    )
    # math_024.Value -> math_026.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.024"].outputs[0],
        ff_clover_nodes_1.nodes["Math.026"].inputs[1]
    )
    # math_025.Value -> math_027.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.025"].outputs[0],
        ff_clover_nodes_1.nodes["Math.027"].inputs[1]
    )
    # reroute.Output -> math_028.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Reroute"].outputs[0],
        ff_clover_nodes_1.nodes["Math.028"].inputs[0]
    )
    # math_027.Value -> math_029.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.027"].outputs[0],
        ff_clover_nodes_1.nodes["Math.029"].inputs[0]
    )
    # group_input_001.Horizontal Curve (Y) -> math_029.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.001"].outputs[19],
        ff_clover_nodes_1.nodes["Math.029"].inputs[1]
    )
    # math_029.Value -> math_030.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.029"].outputs[0],
        ff_clover_nodes_1.nodes["Math.030"].inputs[0]
    )
    # math_026.Value -> math_030.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.026"].outputs[0],
        ff_clover_nodes_1.nodes["Math.030"].inputs[1]
    )
    # math_028.Value -> math_031.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.028"].outputs[0],
        ff_clover_nodes_1.nodes["Math.031"].inputs[0]
    )
    # math_030.Value -> math_031.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.030"].outputs[0],
        ff_clover_nodes_1.nodes["Math.031"].inputs[1]
    )
    # math_023.Value -> combine_xyz_001.Y
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.023"].outputs[0],
        ff_clover_nodes_1.nodes["Combine XYZ.001"].inputs[1]
    )
    # math_031.Value -> combine_xyz_001.Z
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.031"].outputs[0],
        ff_clover_nodes_1.nodes["Combine XYZ.001"].inputs[2]
    )
    # store_named_attribute_001.Geometry -> set_position.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Store Named Attribute.001"].outputs[0],
        ff_clover_nodes_1.nodes["Set Position"].inputs[0]
    )
    # reroute_008.Output -> set_position.Position
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Reroute.008"].outputs[0],
        ff_clover_nodes_1.nodes["Set Position"].inputs[2]
    )
    # set_position.Geometry -> transform_geometry.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Set Position"].outputs[0],
        ff_clover_nodes_1.nodes["Transform Geometry"].inputs[0]
    )
    # group_input_002.Petals Count -> mesh_circle.Vertices
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.002"].outputs[5],
        ff_clover_nodes_1.nodes["Mesh Circle"].inputs[0]
    )
    # group_input_002.Center Radius -> mesh_circle.Radius
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.002"].outputs[6],
        ff_clover_nodes_1.nodes["Mesh Circle"].inputs[1]
    )
    # position_001.Position -> align_euler_to_vector.Vector
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Position.001"].outputs[0],
        ff_clover_nodes_1.nodes["Align Euler to Vector"].inputs[2]
    )
    # group_input_002.Petal Scale -> combine_xyz_002.X
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.002"].outputs[7],
        ff_clover_nodes_1.nodes["Combine XYZ.002"].inputs[0]
    )
    # group_input_002.Petal Scale -> combine_xyz_002.Y
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.002"].outputs[7],
        ff_clover_nodes_1.nodes["Combine XYZ.002"].inputs[1]
    )
    # group_input_002.Petal Scale -> combine_xyz_002.Z
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.002"].outputs[7],
        ff_clover_nodes_1.nodes["Combine XYZ.002"].inputs[2]
    )
    # mesh_circle.Mesh -> instance_on_points.Points
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Mesh Circle"].outputs[0],
        ff_clover_nodes_1.nodes["Instance on Points"].inputs[0]
    )
    # transform_geometry.Geometry -> instance_on_points.Instance
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Transform Geometry"].outputs[0],
        ff_clover_nodes_1.nodes["Instance on Points"].inputs[2]
    )
    # align_euler_to_vector.Rotation -> instance_on_points.Rotation
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Align Euler to Vector"].outputs[0],
        ff_clover_nodes_1.nodes["Instance on Points"].inputs[5]
    )
    # combine_xyz_002.Vector -> instance_on_points.Scale
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Combine XYZ.002"].outputs[0],
        ff_clover_nodes_1.nodes["Instance on Points"].inputs[6]
    )
    # instance_on_points.Instances -> realize_instances.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Instance on Points"].outputs[0],
        ff_clover_nodes_1.nodes["Realize Instances"].inputs[0]
    )
    # group_input_003.Subdivisions -> ico_sphere.Subdivisions
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.003"].outputs[9],
        ff_clover_nodes_1.nodes["Ico Sphere"].inputs[1]
    )
    # position_002.Position -> separate_xyz_001.Vector
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Position.002"].outputs[0],
        ff_clover_nodes_1.nodes["Separate XYZ.001"].inputs[0]
    )
    # separate_xyz_001.X -> map_range_003.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Separate XYZ.001"].outputs[0],
        ff_clover_nodes_1.nodes["Map Range.003"].inputs[0]
    )
    # separate_xyz_001.Y -> map_range_004.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Separate XYZ.001"].outputs[1],
        ff_clover_nodes_1.nodes["Map Range.004"].inputs[0]
    )
    # map_range_003.Result -> combine_xyz_003.X
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Map Range.003"].outputs[0],
        ff_clover_nodes_1.nodes["Combine XYZ.003"].inputs[0]
    )
    # map_range_004.Result -> combine_xyz_003.Y
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Map Range.004"].outputs[0],
        ff_clover_nodes_1.nodes["Combine XYZ.003"].inputs[1]
    )
    # ico_sphere.Mesh -> store_named_attribute_002.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Ico Sphere"].outputs[0],
        ff_clover_nodes_1.nodes["Store Named Attribute.002"].inputs[0]
    )
    # reroute_011.Output -> store_named_attribute_002.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Reroute.011"].outputs[0],
        ff_clover_nodes_1.nodes["Store Named Attribute.002"].inputs[3]
    )
    # store_named_attribute_002.Geometry -> store_named_attribute_003.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Store Named Attribute.002"].outputs[0],
        ff_clover_nodes_1.nodes["Store Named Attribute.003"].inputs[0]
    )
    # group_input_003.Center Color -> store_named_attribute_003.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.003"].outputs[24],
        ff_clover_nodes_1.nodes["Store Named Attribute.003"].inputs[3]
    )
    # math_032.Value -> combine_xyz_004.Z
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.032"].outputs[0],
        ff_clover_nodes_1.nodes["Combine XYZ.004"].inputs[2]
    )
    # store_named_attribute_003.Geometry -> transform_geometry_001.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Store Named Attribute.003"].outputs[0],
        ff_clover_nodes_1.nodes["Transform Geometry.001"].inputs[0]
    )
    # combine_xyz_004.Vector -> transform_geometry_001.Translation
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Combine XYZ.004"].outputs[0],
        ff_clover_nodes_1.nodes["Transform Geometry.001"].inputs[2]
    )
    # reroute_002.Output -> transform_geometry_001.Scale
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Reroute.002"].outputs[0],
        ff_clover_nodes_1.nodes["Transform Geometry.001"].inputs[4]
    )
    # group_input_004.Stem Resolution -> math_033.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.004"].outputs[12],
        ff_clover_nodes_1.nodes["Math.033"].inputs[0]
    )
    # math_033.Value -> grid_001.Vertices X
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.033"].outputs[0],
        ff_clover_nodes_1.nodes["Grid.001"].inputs[2]
    )
    # position_003.Position -> separate_xyz_002.Vector
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Position.003"].outputs[0],
        ff_clover_nodes_1.nodes["Separate XYZ.002"].inputs[0]
    )
    # separate_xyz_002.Y -> math_034.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Separate XYZ.002"].outputs[1],
        ff_clover_nodes_1.nodes["Math.034"].inputs[0]
    )
    # separate_xyz_002.X -> map_range_005.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Separate XYZ.002"].outputs[0],
        ff_clover_nodes_1.nodes["Map Range.005"].inputs[0]
    )
    # math_034.Value -> map_range_006.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.034"].outputs[0],
        ff_clover_nodes_1.nodes["Map Range.006"].inputs[0]
    )
    # map_range_005.Result -> combine_xyz_005.X
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Map Range.005"].outputs[0],
        ff_clover_nodes_1.nodes["Combine XYZ.005"].inputs[0]
    )
    # map_range_006.Result -> combine_xyz_005.Y
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Map Range.006"].outputs[0],
        ff_clover_nodes_1.nodes["Combine XYZ.005"].inputs[1]
    )
    # grid_001.Mesh -> store_named_attribute_004.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Grid.001"].outputs[0],
        ff_clover_nodes_1.nodes["Store Named Attribute.004"].inputs[0]
    )
    # combine_xyz_005.Vector -> store_named_attribute_004.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Combine XYZ.005"].outputs[0],
        ff_clover_nodes_1.nodes["Store Named Attribute.004"].inputs[3]
    )
    # separate_xyz_002.X -> math_035.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Separate XYZ.002"].outputs[0],
        ff_clover_nodes_1.nodes["Math.035"].inputs[0]
    )
    # math_035.Value -> math_036.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.035"].outputs[0],
        ff_clover_nodes_1.nodes["Math.036"].inputs[0]
    )
    # math_036.Value -> math_037.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.036"].outputs[0],
        ff_clover_nodes_1.nodes["Math.037"].inputs[0]
    )
    # math_037.Value -> math_038.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.037"].outputs[0],
        ff_clover_nodes_1.nodes["Math.038"].inputs[0]
    )
    # math_036.Value -> math_039.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.036"].outputs[0],
        ff_clover_nodes_1.nodes["Math.039"].inputs[0]
    )
    # math_039.Value -> math_040.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.039"].outputs[0],
        ff_clover_nodes_1.nodes["Math.040"].inputs[0]
    )
    # separate_xyz_002.Y -> math_042.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Separate XYZ.002"].outputs[1],
        ff_clover_nodes_1.nodes["Math.042"].inputs[0]
    )
    # math_041.Value -> math_042.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.041"].outputs[0],
        ff_clover_nodes_1.nodes["Math.042"].inputs[1]
    )
    # math_038.Value -> combine_xyz_006.X
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.038"].outputs[0],
        ff_clover_nodes_1.nodes["Combine XYZ.006"].inputs[0]
    )
    # math_040.Value -> combine_xyz_006.Y
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.040"].outputs[0],
        ff_clover_nodes_1.nodes["Combine XYZ.006"].inputs[1]
    )
    # math_042.Value -> combine_xyz_006.Z
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.042"].outputs[0],
        ff_clover_nodes_1.nodes["Combine XYZ.006"].inputs[2]
    )
    # store_named_attribute_004.Geometry -> set_position_001.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Store Named Attribute.004"].outputs[0],
        ff_clover_nodes_1.nodes["Set Position.001"].inputs[0]
    )
    # combine_xyz_006.Vector -> set_position_001.Position
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Combine XYZ.006"].outputs[0],
        ff_clover_nodes_1.nodes["Set Position.001"].inputs[2]
    )
    # set_position_001.Geometry -> merge_by_distance.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Set Position.001"].outputs[0],
        ff_clover_nodes_1.nodes["Merge by Distance"].inputs[0]
    )
    # merge_by_distance.Geometry -> flip_faces.Mesh
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Merge by Distance"].outputs[0],
        ff_clover_nodes_1.nodes["Flip Faces"].inputs[0]
    )
    # flip_faces.Mesh -> store_named_attribute_005.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Flip Faces"].outputs[0],
        ff_clover_nodes_1.nodes["Store Named Attribute.005"].inputs[0]
    )
    # store_named_attribute_005.Geometry -> transform_geometry_002.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Store Named Attribute.005"].outputs[0],
        ff_clover_nodes_1.nodes["Transform Geometry.002"].inputs[0]
    )
    # combine_xyz_004.Vector -> transform_geometry_002.Translation
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Combine XYZ.004"].outputs[0],
        ff_clover_nodes_1.nodes["Transform Geometry.002"].inputs[2]
    )
    # group_input_005.Smooth Shading -> set_shade_smooth.Shade Smooth
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.005"].outputs[21],
        ff_clover_nodes_1.nodes["Set Shade Smooth"].inputs[2]
    )
    # realize_instances.Geometry -> join_geometry.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Realize Instances"].outputs[0],
        ff_clover_nodes_1.nodes["Join Geometry"].inputs[0]
    )
    # join_geometry.Geometry -> set_shade_smooth.Mesh
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Join Geometry"].outputs[0],
        ff_clover_nodes_1.nodes["Set Shade Smooth"].inputs[0]
    )
    # group_input_005.Stem Length -> math_043.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.005"].outputs[10],
        ff_clover_nodes_1.nodes["Math.043"].inputs[0]
    )
    # reroute_009.Output -> math_043.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Reroute.009"].outputs[0],
        ff_clover_nodes_1.nodes["Math.043"].inputs[1]
    )
    # math_043.Value -> combine_xyz_007.Z
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.043"].outputs[0],
        ff_clover_nodes_1.nodes["Combine XYZ.007"].inputs[2]
    )
    # combine_xyz_007.Vector -> transform_geometry_003.Translation
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Combine XYZ.007"].outputs[0],
        ff_clover_nodes_1.nodes["Transform Geometry.003"].inputs[2]
    )
    # set_shade_smooth.Mesh -> transform_geometry_003.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Set Shade Smooth"].outputs[0],
        ff_clover_nodes_1.nodes["Transform Geometry.003"].inputs[0]
    )
    # group_input_006.Seed -> reroute_004.Input
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.006"].outputs[0],
        ff_clover_nodes_1.nodes["Reroute.004"].inputs[0]
    )
    # reroute_012.Output -> points.Count
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Reroute.012"].outputs[0],
        ff_clover_nodes_1.nodes["Points"].inputs[0]
    )
    # math_044.Value -> random_value_001.Seed
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.044"].outputs[0],
        ff_clover_nodes_1.nodes["Random Value.001"].inputs[3]
    )
    # reroute_004.Output -> math_045.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Reroute.004"].outputs[0],
        ff_clover_nodes_1.nodes["Math.045"].inputs[0]
    )
    # math_045.Value -> random_value_002.Seed
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.045"].outputs[0],
        ff_clover_nodes_1.nodes["Random Value.002"].inputs[3]
    )
    # reroute_004.Output -> math_046.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Reroute.004"].outputs[0],
        ff_clover_nodes_1.nodes["Math.046"].inputs[0]
    )
    # math_046.Value -> random_value_003.Seed
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.046"].outputs[0],
        ff_clover_nodes_1.nodes["Random Value.003"].inputs[3]
    )
    # random_value_001.Value -> math_047.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Random Value.001"].outputs[0],
        ff_clover_nodes_1.nodes["Math.047"].inputs[0]
    )
    # math_047.Value -> math_048.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.047"].outputs[0],
        ff_clover_nodes_1.nodes["Math.048"].inputs[0]
    )
    # group_input_006.Patch Radius -> math_048.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.006"].outputs[2],
        ff_clover_nodes_1.nodes["Math.048"].inputs[1]
    )
    # random_value.Value -> math_049.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Random Value"].outputs[0],
        ff_clover_nodes_1.nodes["Math.049"].inputs[0]
    )
    # random_value.Value -> math_050.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Random Value"].outputs[0],
        ff_clover_nodes_1.nodes["Math.050"].inputs[0]
    )
    # math_049.Value -> math_051.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.049"].outputs[0],
        ff_clover_nodes_1.nodes["Math.051"].inputs[0]
    )
    # math_048.Value -> math_051.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.048"].outputs[0],
        ff_clover_nodes_1.nodes["Math.051"].inputs[1]
    )
    # math_050.Value -> math_052.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.050"].outputs[0],
        ff_clover_nodes_1.nodes["Math.052"].inputs[0]
    )
    # math_048.Value -> math_052.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.048"].outputs[0],
        ff_clover_nodes_1.nodes["Math.052"].inputs[1]
    )
    # math_051.Value -> combine_xyz_008.X
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.051"].outputs[0],
        ff_clover_nodes_1.nodes["Combine XYZ.008"].inputs[0]
    )
    # math_052.Value -> combine_xyz_008.Y
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.052"].outputs[0],
        ff_clover_nodes_1.nodes["Combine XYZ.008"].inputs[1]
    )
    # points.Points -> set_position_002.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Points"].outputs[0],
        ff_clover_nodes_1.nodes["Set Position.002"].inputs[0]
    )
    # combine_xyz_008.Vector -> set_position_002.Position
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Combine XYZ.008"].outputs[0],
        ff_clover_nodes_1.nodes["Set Position.002"].inputs[2]
    )
    # set_position_002.Geometry -> instance_on_points_001.Points
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Set Position.002"].outputs[0],
        ff_clover_nodes_1.nodes["Instance on Points.001"].inputs[0]
    )
    # transform_geometry_003.Geometry -> instance_on_points_001.Instance
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Transform Geometry.003"].outputs[0],
        ff_clover_nodes_1.nodes["Instance on Points.001"].inputs[2]
    )
    # random_value_002.Value -> instance_on_points_001.Rotation
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Random Value.002"].outputs[0],
        ff_clover_nodes_1.nodes["Instance on Points.001"].inputs[5]
    )
    # random_value_003.Value -> instance_on_points_001.Scale
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Random Value.003"].outputs[0],
        ff_clover_nodes_1.nodes["Instance on Points.001"].inputs[6]
    )
    # instance_on_points_001.Instances -> store_named_attribute_006.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Instance on Points.001"].outputs[0],
        ff_clover_nodes_1.nodes["Store Named Attribute.006"].inputs[0]
    )
    # index.Index -> store_named_attribute_006.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Index"].outputs[0],
        ff_clover_nodes_1.nodes["Store Named Attribute.006"].inputs[3]
    )
    # store_named_attribute_006.Geometry -> realize_instances_001.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Store Named Attribute.006"].outputs[0],
        ff_clover_nodes_1.nodes["Realize Instances.001"].inputs[0]
    )
    # realize_instances_001.Geometry -> convex_hull.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Realize Instances.001"].outputs[0],
        ff_clover_nodes_1.nodes["Convex Hull"].inputs[0]
    )
    # convex_hull.Convex Hull -> set_shade_smooth_001.Mesh
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Convex Hull"].outputs[0],
        ff_clover_nodes_1.nodes["Set Shade Smooth.001"].inputs[0]
    )
    # set_shade_smooth_001.Mesh -> sample_nearest_surface.Mesh
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Set Shade Smooth.001"].outputs[0],
        ff_clover_nodes_1.nodes["Sample Nearest Surface"].inputs[0]
    )
    # normal.Normal -> sample_nearest_surface.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Normal"].outputs[0],
        ff_clover_nodes_1.nodes["Sample Nearest Surface"].inputs[1]
    )
    # normal.Normal -> vector_math.Vector
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Normal"].outputs[0],
        ff_clover_nodes_1.nodes["Vector Math"].inputs[0]
    )
    # math_053.Value -> vector_math.Scale
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.053"].outputs[0],
        ff_clover_nodes_1.nodes["Vector Math"].inputs[3]
    )
    # sample_nearest_surface.Value -> vector_math_001.Vector
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Sample Nearest Surface"].outputs[0],
        ff_clover_nodes_1.nodes["Vector Math.001"].inputs[0]
    )
    # vector_math.Vector -> vector_math_002.Vector
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Vector Math"].outputs[0],
        ff_clover_nodes_1.nodes["Vector Math.002"].inputs[0]
    )
    # vector_math_001.Vector -> vector_math_002.Vector
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Vector Math.001"].outputs[0],
        ff_clover_nodes_1.nodes["Vector Math.002"].inputs[1]
    )
    # vector_math_002.Vector -> vector_math_003.Vector
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Vector Math.002"].outputs[0],
        ff_clover_nodes_1.nodes["Vector Math.003"].inputs[0]
    )
    # reroute_005.Output -> set_mesh_normal.Mesh
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Reroute.005"].outputs[0],
        ff_clover_nodes_1.nodes["Set Mesh Normal"].inputs[0]
    )
    # vector_math_003.Vector -> set_mesh_normal.Custom Normal
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Vector Math.003"].outputs[0],
        ff_clover_nodes_1.nodes["Set Mesh Normal"].inputs[1]
    )
    # set_mesh_normal.Mesh -> set_material.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Set Mesh Normal"].outputs[0],
        ff_clover_nodes_1.nodes["Set Material"].inputs[0]
    )
    # group_input_007.Material -> set_material.Material
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.007"].outputs[20],
        ff_clover_nodes_1.nodes["Set Material"].inputs[2]
    )
    # separate_xyz.X -> math_005.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Separate XYZ"].outputs[0],
        ff_clover_nodes_1.nodes["Math.005"].inputs[0]
    )
    # separate_xyz.X -> math_006.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Separate XYZ"].outputs[0],
        ff_clover_nodes_1.nodes["Math.006"].inputs[0]
    )
    # reroute_006.Output -> map_range.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Reroute.006"].outputs[0],
        ff_clover_nodes_1.nodes["Map Range"].inputs[0]
    )
    # separate_xyz.Y -> math_025.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Separate XYZ"].outputs[1],
        ff_clover_nodes_1.nodes["Math.025"].inputs[0]
    )
    # group_input_008.Petal Color -> store_named_attribute_001.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.008"].outputs[23],
        ff_clover_nodes_1.nodes["Store Named Attribute.001"].inputs[3]
    )
    # separate_xyz.X -> math_024.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Separate XYZ"].outputs[0],
        ff_clover_nodes_1.nodes["Math.024"].inputs[0]
    )
    # group_input_001.Vertical Crease (X) -> math_028.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.001"].outputs[18],
        ff_clover_nodes_1.nodes["Math.028"].inputs[1]
    )
    # math_026.Value -> reroute.Input
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.026"].outputs[0],
        ff_clover_nodes_1.nodes["Reroute"].inputs[0]
    )
    # separate_xyz.Y -> reroute_006.Input
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Separate XYZ"].outputs[1],
        ff_clover_nodes_1.nodes["Reroute.006"].inputs[0]
    )
    # math_020.Value -> reroute_007.Input
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.020"].outputs[0],
        ff_clover_nodes_1.nodes["Reroute.007"].inputs[0]
    )
    # math_011.Value -> combine_xyz_001.X
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.011"].outputs[0],
        ff_clover_nodes_1.nodes["Combine XYZ.001"].inputs[0]
    )
    # math_011.Value -> reroute_001.Input
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.011"].outputs[0],
        ff_clover_nodes_1.nodes["Reroute.001"].inputs[0]
    )
    # combine_xyz_001.Vector -> reroute_008.Input
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Combine XYZ.001"].outputs[0],
        ff_clover_nodes_1.nodes["Reroute.008"].inputs[0]
    )
    # group_input_004.Stem Length -> math_034.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.004"].outputs[10],
        ff_clover_nodes_1.nodes["Math.034"].inputs[1]
    )
    # group_input_009.Stem Color -> store_named_attribute_005.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.009"].outputs[25],
        ff_clover_nodes_1.nodes["Store Named Attribute.005"].inputs[3]
    )
    # group_input_004.Stem Length -> math_041.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.004"].outputs[10],
        ff_clover_nodes_1.nodes["Math.041"].inputs[0]
    )
    # group_input_004.Stem Length -> grid_001.Size Y
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.004"].outputs[10],
        ff_clover_nodes_1.nodes["Grid.001"].inputs[1]
    )
    # group_input_004.Stem Thickness -> math_040.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.004"].outputs[11],
        ff_clover_nodes_1.nodes["Math.040"].inputs[1]
    )
    # group_input_004.Stem Thickness -> math_038.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.004"].outputs[11],
        ff_clover_nodes_1.nodes["Math.038"].inputs[1]
    )
    # group_input_010.Petal Scale -> math_032.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.010"].outputs[7],
        ff_clover_nodes_1.nodes["Math.032"].inputs[1]
    )
    # group_input_010.Vertical Crease (X) -> math_032.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.010"].outputs[18],
        ff_clover_nodes_1.nodes["Math.032"].inputs[0]
    )
    # group_input_003.Scale -> reroute_002.Input
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.003"].outputs[8],
        ff_clover_nodes_1.nodes["Reroute.002"].inputs[0]
    )
    # math_032.Value -> reroute_003.Input
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Math.032"].outputs[0],
        ff_clover_nodes_1.nodes["Reroute.003"].inputs[0]
    )
    # reroute_003.Output -> reroute_009.Input
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Reroute.003"].outputs[0],
        ff_clover_nodes_1.nodes["Reroute.009"].inputs[0]
    )
    # combine_xyz_003.Vector -> reroute_010.Input
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Combine XYZ.003"].outputs[0],
        ff_clover_nodes_1.nodes["Reroute.010"].inputs[0]
    )
    # reroute_010.Output -> reroute_011.Input
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Reroute.010"].outputs[0],
        ff_clover_nodes_1.nodes["Reroute.011"].inputs[0]
    )
    # group_input_011.Min Scale -> random_value_003.Min
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.011"].outputs[3],
        ff_clover_nodes_1.nodes["Random Value.003"].inputs[0]
    )
    # group_input_011.Max Scale -> random_value_003.Max
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.011"].outputs[4],
        ff_clover_nodes_1.nodes["Random Value.003"].inputs[1]
    )
    # group_input_006.Seed -> random_value.Seed
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.006"].outputs[0],
        ff_clover_nodes_1.nodes["Random Value"].inputs[3]
    )
    # group_input_006.Seed -> math_044.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.006"].outputs[0],
        ff_clover_nodes_1.nodes["Math.044"].inputs[0]
    )
    # group_input_006.Count -> reroute_012.Input
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.006"].outputs[1],
        ff_clover_nodes_1.nodes["Reroute.012"].inputs[0]
    )
    # group_input_007.Stylized Normals -> math_053.Value
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.007"].outputs[22],
        ff_clover_nodes_1.nodes["Math.053"].inputs[1]
    )
    # reroute_013.Output -> vector_math_001.Scale
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Reroute.013"].outputs[0],
        ff_clover_nodes_1.nodes["Vector Math.001"].inputs[3]
    )
    # realize_instances_001.Geometry -> reroute_005.Input
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Realize Instances.001"].outputs[0],
        ff_clover_nodes_1.nodes["Reroute.005"].inputs[0]
    )
    # group_input_007.Stylized Normals -> reroute_013.Input
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Group Input.007"].outputs[22],
        ff_clover_nodes_1.nodes["Reroute.013"].inputs[0]
    )
    # set_material.Geometry -> group_output_001.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Set Material"].outputs[0],
        ff_clover_nodes_1.nodes["Group Output.001"].inputs[0]
    )
    # transform_geometry_001.Geometry -> join_geometry.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Transform Geometry.001"].outputs[0],
        ff_clover_nodes_1.nodes["Join Geometry"].inputs[0]
    )
    # transform_geometry_002.Geometry -> join_geometry.Geometry
    ff_clover_nodes_1.links.new(
        ff_clover_nodes_1.nodes["Transform Geometry.002"].outputs[0],
        ff_clover_nodes_1.nodes["Join Geometry"].inputs[0]
    )

    return ff_clover_nodes_1


if __name__ == "__main__":
    # Maps node tree creation functions to the node tree 
    # name, such that we don't recreate node trees unnecessarily
    node_tree_names : dict[typing.Callable, str] = {}

    ff_clover_nodes = ff_clover_nodes_1_node_group(node_tree_names)
    node_tree_names[ff_clover_nodes_1_node_group] = ff_clover_nodes.name


# ============================================================================
#  FF BRIDGE 
# ============================================================================

from . import bridge

GROUP_NAME = "FF Clover Nodes"
MAT_NAME = "M_Clover"
MAT_HEX = "00FF00"


def create_node_group():
    return bridge.get_or_create_node_group(ff_clover_nodes_1_node_group, GROUP_NAME)


def get_or_create_material():
    return bridge.get_or_create_colormask_material(MAT_NAME, MAT_HEX)