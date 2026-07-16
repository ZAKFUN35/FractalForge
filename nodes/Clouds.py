import bpy
import mathutils
import os
import typing


def ff_clouds_nodes_1_node_group(node_tree_names: dict[typing.Callable, str]):
    """Initialize FF Clouds Nodes node group"""
    ff_clouds_nodes_1 = bpy.data.node_groups.new(type='GeometryNodeTree', name="FF Clouds Nodes")

    ff_clouds_nodes_1.color_tag = 'NONE'
    ff_clouds_nodes_1.description = ""
    ff_clouds_nodes_1.default_group_node_width = 140
    ff_clouds_nodes_1.is_modifier = True
    ff_clouds_nodes_1.show_modifier_manage_panel = True

    # ff_clouds_nodes_1 interface

    # Socket Geometry
    geometry_socket = ff_clouds_nodes_1.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Panel Global Settings
    global_settings_panel = ff_clouds_nodes_1.interface.new_panel("Global Settings")
    # Socket Field Size X
    field_size_x_socket = ff_clouds_nodes_1.interface.new_socket(name="Field Size X", in_out='INPUT', socket_type='NodeSocketFloat', parent = global_settings_panel)
    field_size_x_socket.default_value = 100.0
    field_size_x_socket.min_value = 0.0
    field_size_x_socket.max_value = 3.4028234663852886e+38
    field_size_x_socket.subtype = 'NONE'
    field_size_x_socket.attribute_domain = 'POINT'
    field_size_x_socket.default_input = 'VALUE'
    field_size_x_socket.structure_type = 'AUTO'

    # Socket Field Size Y
    field_size_y_socket = ff_clouds_nodes_1.interface.new_socket(name="Field Size Y", in_out='INPUT', socket_type='NodeSocketFloat', parent = global_settings_panel)
    field_size_y_socket.default_value = 100.0
    field_size_y_socket.min_value = 0.0
    field_size_y_socket.max_value = 3.4028234663852886e+38
    field_size_y_socket.subtype = 'NONE'
    field_size_y_socket.attribute_domain = 'POINT'
    field_size_y_socket.default_input = 'VALUE'
    field_size_y_socket.structure_type = 'AUTO'

    # Socket Cloud Count
    cloud_count_socket = ff_clouds_nodes_1.interface.new_socket(name="Cloud Count", in_out='INPUT', socket_type='NodeSocketInt', parent = global_settings_panel)
    cloud_count_socket.default_value = 80
    cloud_count_socket.min_value = 0
    cloud_count_socket.max_value = 2147483647
    cloud_count_socket.subtype = 'NONE'
    cloud_count_socket.attribute_domain = 'POINT'
    cloud_count_socket.default_input = 'VALUE'
    cloud_count_socket.structure_type = 'AUTO'

    # Socket Height Scatter (Z Randomness)
    height_scatter__z_randomness__socket = ff_clouds_nodes_1.interface.new_socket(name="Height Scatter (Z Randomness)", in_out='INPUT', socket_type='NodeSocketFloat', parent = global_settings_panel)
    height_scatter__z_randomness__socket.default_value = 0.5
    height_scatter__z_randomness__socket.min_value = 0.0
    height_scatter__z_randomness__socket.max_value = 3.4028234663852886e+38
    height_scatter__z_randomness__socket.subtype = 'NONE'
    height_scatter__z_randomness__socket.attribute_domain = 'POINT'
    height_scatter__z_randomness__socket.default_input = 'VALUE'
    height_scatter__z_randomness__socket.structure_type = 'AUTO'

    # Socket Voxel Size
    voxel_size_socket = ff_clouds_nodes_1.interface.new_socket(name="Voxel Size", in_out='INPUT', socket_type='NodeSocketFloat', parent = global_settings_panel)
    voxel_size_socket.default_value = 0.07999999821186066
    voxel_size_socket.min_value = 0.004999999888241291
    voxel_size_socket.max_value = 3.4028234663852886e+38
    voxel_size_socket.subtype = 'NONE'
    voxel_size_socket.attribute_domain = 'POINT'
    voxel_size_socket.default_input = 'VALUE'
    voxel_size_socket.structure_type = 'AUTO'

    # Socket Voxel Threshold
    voxel_threshold_socket = ff_clouds_nodes_1.interface.new_socket(name="Voxel Threshold", in_out='INPUT', socket_type='NodeSocketFloat', parent = global_settings_panel)
    voxel_threshold_socket.default_value = 0.4000000059604645
    voxel_threshold_socket.min_value = 0.0
    voxel_threshold_socket.max_value = 3.4028234663852886e+38
    voxel_threshold_socket.subtype = 'NONE'
    voxel_threshold_socket.attribute_domain = 'POINT'
    voxel_threshold_socket.default_input = 'VALUE'
    voxel_threshold_socket.structure_type = 'AUTO'

    # Socket Wind Offset X
    wind_offset_x_socket = ff_clouds_nodes_1.interface.new_socket(name="Wind Offset X", in_out='INPUT', socket_type='NodeSocketFloat', parent = global_settings_panel)
    wind_offset_x_socket.default_value = 0.0
    wind_offset_x_socket.min_value = -3.4028234663852886e+38
    wind_offset_x_socket.max_value = 3.4028234663852886e+38
    wind_offset_x_socket.subtype = 'NONE'
    wind_offset_x_socket.attribute_domain = 'POINT'
    wind_offset_x_socket.default_input = 'VALUE'
    wind_offset_x_socket.structure_type = 'AUTO'

    # Socket Wind Offset Y
    wind_offset_y_socket = ff_clouds_nodes_1.interface.new_socket(name="Wind Offset Y", in_out='INPUT', socket_type='NodeSocketFloat', parent = global_settings_panel)
    wind_offset_y_socket.default_value = 0.0
    wind_offset_y_socket.min_value = -3.4028234663852886e+38
    wind_offset_y_socket.max_value = 3.4028234663852886e+38
    wind_offset_y_socket.subtype = 'NONE'
    wind_offset_y_socket.attribute_domain = 'POINT'
    wind_offset_y_socket.default_input = 'VALUE'
    wind_offset_y_socket.structure_type = 'AUTO'

    # Socket Surface Detail Strength
    surface_detail_strength_socket = ff_clouds_nodes_1.interface.new_socket(name="Surface Detail Strength", in_out='INPUT', socket_type='NodeSocketFloat', parent = global_settings_panel)
    surface_detail_strength_socket.default_value = 0.6700000166893005
    surface_detail_strength_socket.min_value = 0.0
    surface_detail_strength_socket.max_value = 3.4028234663852886e+38
    surface_detail_strength_socket.subtype = 'NONE'
    surface_detail_strength_socket.attribute_domain = 'POINT'
    surface_detail_strength_socket.default_input = 'VALUE'
    surface_detail_strength_socket.structure_type = 'AUTO'

    # Socket Surface Detail Scale
    surface_detail_scale_socket = ff_clouds_nodes_1.interface.new_socket(name="Surface Detail Scale", in_out='INPUT', socket_type='NodeSocketFloat', parent = global_settings_panel)
    surface_detail_scale_socket.default_value = 3.0
    surface_detail_scale_socket.min_value = 0.009999999776482582
    surface_detail_scale_socket.max_value = 3.4028234663852886e+38
    surface_detail_scale_socket.subtype = 'NONE'
    surface_detail_scale_socket.attribute_domain = 'POINT'
    surface_detail_scale_socket.default_input = 'VALUE'
    surface_detail_scale_socket.structure_type = 'AUTO'


    # Panel Layer 1
    layer_1_panel = ff_clouds_nodes_1.interface.new_panel("Layer 1")
    # Socket Probability
    probability_socket = ff_clouds_nodes_1.interface.new_socket(name="Probability", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_1_panel)
    probability_socket.default_value = 1.0
    probability_socket.min_value = 0.0
    probability_socket.max_value = 1.0
    probability_socket.subtype = 'NONE'
    probability_socket.attribute_domain = 'POINT'
    probability_socket.default_input = 'VALUE'
    probability_socket.structure_type = 'AUTO'

    # Socket Layer Radius
    layer_radius_socket = ff_clouds_nodes_1.interface.new_socket(name="Layer Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_1_panel)
    layer_radius_socket.default_value = 0.0
    layer_radius_socket.min_value = 0.0
    layer_radius_socket.max_value = 3.4028234663852886e+38
    layer_radius_socket.subtype = 'NONE'
    layer_radius_socket.attribute_domain = 'POINT'
    layer_radius_socket.default_input = 'VALUE'
    layer_radius_socket.structure_type = 'AUTO'

    # Socket Layer Height (Z Offset)
    layer_height__z_offset__socket = ff_clouds_nodes_1.interface.new_socket(name="Layer Height (Z Offset)", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_1_panel)
    layer_height__z_offset__socket.default_value = 1.0
    layer_height__z_offset__socket.min_value = -3.4028234663852886e+38
    layer_height__z_offset__socket.max_value = 3.4028234663852886e+38
    layer_height__z_offset__socket.subtype = 'NONE'
    layer_height__z_offset__socket.attribute_domain = 'POINT'
    layer_height__z_offset__socket.default_input = 'VALUE'
    layer_height__z_offset__socket.structure_type = 'AUTO'

    # Socket Spheres Count
    spheres_count_socket = ff_clouds_nodes_1.interface.new_socket(name="Spheres Count", in_out='INPUT', socket_type='NodeSocketInt', parent = layer_1_panel)
    spheres_count_socket.default_value = 15
    spheres_count_socket.min_value = 0
    spheres_count_socket.max_value = 2147483647
    spheres_count_socket.subtype = 'NONE'
    spheres_count_socket.attribute_domain = 'POINT'
    spheres_count_socket.default_input = 'VALUE'
    spheres_count_socket.structure_type = 'AUTO'

    # Socket Min Sphere Size
    min_sphere_size_socket = ff_clouds_nodes_1.interface.new_socket(name="Min Sphere Size", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_1_panel)
    min_sphere_size_socket.default_value = 0.3499999940395355
    min_sphere_size_socket.min_value = 0.0
    min_sphere_size_socket.max_value = 3.4028234663852886e+38
    min_sphere_size_socket.subtype = 'NONE'
    min_sphere_size_socket.attribute_domain = 'POINT'
    min_sphere_size_socket.default_input = 'VALUE'
    min_sphere_size_socket.structure_type = 'AUTO'

    # Socket Max Sphere Size
    max_sphere_size_socket = ff_clouds_nodes_1.interface.new_socket(name="Max Sphere Size", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_1_panel)
    max_sphere_size_socket.default_value = 0.550000011920929
    max_sphere_size_socket.min_value = 0.0
    max_sphere_size_socket.max_value = 3.4028234663852886e+38
    max_sphere_size_socket.subtype = 'NONE'
    max_sphere_size_socket.attribute_domain = 'POINT'
    max_sphere_size_socket.default_input = 'VALUE'
    max_sphere_size_socket.structure_type = 'AUTO'

    # Socket Squash Probability
    squash_probability_socket = ff_clouds_nodes_1.interface.new_socket(name="Squash Probability", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_1_panel)
    squash_probability_socket.default_value = 0.3499999940395355
    squash_probability_socket.min_value = 0.0
    squash_probability_socket.max_value = 1.0
    squash_probability_socket.subtype = 'NONE'
    squash_probability_socket.attribute_domain = 'POINT'
    squash_probability_socket.default_input = 'VALUE'
    squash_probability_socket.structure_type = 'AUTO'

    # Socket Max Squash Strength
    max_squash_strength_socket = ff_clouds_nodes_1.interface.new_socket(name="Max Squash Strength", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_1_panel)
    max_squash_strength_socket.default_value = 0.44999998807907104
    max_squash_strength_socket.min_value = 0.0
    max_squash_strength_socket.max_value = 1.0
    max_squash_strength_socket.subtype = 'NONE'
    max_squash_strength_socket.attribute_domain = 'POINT'
    max_squash_strength_socket.default_input = 'VALUE'
    max_squash_strength_socket.structure_type = 'AUTO'


    # Panel Layer 2
    layer_2_panel = ff_clouds_nodes_1.interface.new_panel("Layer 2")
    # Socket Probability
    probability_socket_1 = ff_clouds_nodes_1.interface.new_socket(name="Probability", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_2_panel)
    probability_socket_1.default_value = 0.8500000238418579
    probability_socket_1.min_value = 0.0
    probability_socket_1.max_value = 1.0
    probability_socket_1.subtype = 'NONE'
    probability_socket_1.attribute_domain = 'POINT'
    probability_socket_1.default_input = 'VALUE'
    probability_socket_1.structure_type = 'AUTO'

    # Socket Layer Radius
    layer_radius_socket_1 = ff_clouds_nodes_1.interface.new_socket(name="Layer Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_2_panel)
    layer_radius_socket_1.default_value = 0.7599999904632568
    layer_radius_socket_1.min_value = 0.0
    layer_radius_socket_1.max_value = 3.4028234663852886e+38
    layer_radius_socket_1.subtype = 'NONE'
    layer_radius_socket_1.attribute_domain = 'POINT'
    layer_radius_socket_1.default_input = 'VALUE'
    layer_radius_socket_1.structure_type = 'AUTO'

    # Socket Layer Height (Z Offset)
    layer_height__z_offset__socket_1 = ff_clouds_nodes_1.interface.new_socket(name="Layer Height (Z Offset)", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_2_panel)
    layer_height__z_offset__socket_1.default_value = 0.550000011920929
    layer_height__z_offset__socket_1.min_value = -3.4028234663852886e+38
    layer_height__z_offset__socket_1.max_value = 3.4028234663852886e+38
    layer_height__z_offset__socket_1.subtype = 'NONE'
    layer_height__z_offset__socket_1.attribute_domain = 'POINT'
    layer_height__z_offset__socket_1.default_input = 'VALUE'
    layer_height__z_offset__socket_1.structure_type = 'AUTO'

    # Socket Spheres Count
    spheres_count_socket_1 = ff_clouds_nodes_1.interface.new_socket(name="Spheres Count", in_out='INPUT', socket_type='NodeSocketInt', parent = layer_2_panel)
    spheres_count_socket_1.default_value = 23
    spheres_count_socket_1.min_value = 0
    spheres_count_socket_1.max_value = 2147483647
    spheres_count_socket_1.subtype = 'NONE'
    spheres_count_socket_1.attribute_domain = 'POINT'
    spheres_count_socket_1.default_input = 'VALUE'
    spheres_count_socket_1.structure_type = 'AUTO'

    # Socket Min Sphere Size
    min_sphere_size_socket_1 = ff_clouds_nodes_1.interface.new_socket(name="Min Sphere Size", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_2_panel)
    min_sphere_size_socket_1.default_value = 0.30000001192092896
    min_sphere_size_socket_1.min_value = 0.0
    min_sphere_size_socket_1.max_value = 3.4028234663852886e+38
    min_sphere_size_socket_1.subtype = 'NONE'
    min_sphere_size_socket_1.attribute_domain = 'POINT'
    min_sphere_size_socket_1.default_input = 'VALUE'
    min_sphere_size_socket_1.structure_type = 'AUTO'

    # Socket Max Sphere Size
    max_sphere_size_socket_1 = ff_clouds_nodes_1.interface.new_socket(name="Max Sphere Size", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_2_panel)
    max_sphere_size_socket_1.default_value = 0.5
    max_sphere_size_socket_1.min_value = 0.0
    max_sphere_size_socket_1.max_value = 3.4028234663852886e+38
    max_sphere_size_socket_1.subtype = 'NONE'
    max_sphere_size_socket_1.attribute_domain = 'POINT'
    max_sphere_size_socket_1.default_input = 'VALUE'
    max_sphere_size_socket_1.structure_type = 'AUTO'

    # Socket Squash Probability
    squash_probability_socket_1 = ff_clouds_nodes_1.interface.new_socket(name="Squash Probability", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_2_panel)
    squash_probability_socket_1.default_value = 0.3499999940395355
    squash_probability_socket_1.min_value = 0.0
    squash_probability_socket_1.max_value = 1.0
    squash_probability_socket_1.subtype = 'NONE'
    squash_probability_socket_1.attribute_domain = 'POINT'
    squash_probability_socket_1.default_input = 'VALUE'
    squash_probability_socket_1.structure_type = 'AUTO'

    # Socket Max Squash Strength
    max_squash_strength_socket_1 = ff_clouds_nodes_1.interface.new_socket(name="Max Squash Strength", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_2_panel)
    max_squash_strength_socket_1.default_value = 0.4000000059604645
    max_squash_strength_socket_1.min_value = 0.0
    max_squash_strength_socket_1.max_value = 1.0
    max_squash_strength_socket_1.subtype = 'NONE'
    max_squash_strength_socket_1.attribute_domain = 'POINT'
    max_squash_strength_socket_1.default_input = 'VALUE'
    max_squash_strength_socket_1.structure_type = 'AUTO'


    # Panel Layer 3
    layer_3_panel = ff_clouds_nodes_1.interface.new_panel("Layer 3")
    # Socket Probability
    probability_socket_2 = ff_clouds_nodes_1.interface.new_socket(name="Probability", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_3_panel)
    probability_socket_2.default_value = 0.6000000238418579
    probability_socket_2.min_value = 0.0
    probability_socket_2.max_value = 1.0
    probability_socket_2.subtype = 'NONE'
    probability_socket_2.attribute_domain = 'POINT'
    probability_socket_2.default_input = 'VALUE'
    probability_socket_2.structure_type = 'AUTO'

    # Socket Layer Radius
    layer_radius_socket_2 = ff_clouds_nodes_1.interface.new_socket(name="Layer Radius", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_3_panel)
    layer_radius_socket_2.default_value = 1.2000000476837158
    layer_radius_socket_2.min_value = 0.0
    layer_radius_socket_2.max_value = 3.4028234663852886e+38
    layer_radius_socket_2.subtype = 'NONE'
    layer_radius_socket_2.attribute_domain = 'POINT'
    layer_radius_socket_2.default_input = 'VALUE'
    layer_radius_socket_2.structure_type = 'AUTO'

    # Socket Layer Height (Z Offset)
    layer_height__z_offset__socket_2 = ff_clouds_nodes_1.interface.new_socket(name="Layer Height (Z Offset)", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_3_panel)
    layer_height__z_offset__socket_2.default_value = 0.25
    layer_height__z_offset__socket_2.min_value = -3.4028234663852886e+38
    layer_height__z_offset__socket_2.max_value = 3.4028234663852886e+38
    layer_height__z_offset__socket_2.subtype = 'NONE'
    layer_height__z_offset__socket_2.attribute_domain = 'POINT'
    layer_height__z_offset__socket_2.default_input = 'VALUE'
    layer_height__z_offset__socket_2.structure_type = 'AUTO'

    # Socket Spheres Count
    spheres_count_socket_2 = ff_clouds_nodes_1.interface.new_socket(name="Spheres Count", in_out='INPUT', socket_type='NodeSocketInt', parent = layer_3_panel)
    spheres_count_socket_2.default_value = 125
    spheres_count_socket_2.min_value = 0
    spheres_count_socket_2.max_value = 2147483647
    spheres_count_socket_2.subtype = 'NONE'
    spheres_count_socket_2.attribute_domain = 'POINT'
    spheres_count_socket_2.default_input = 'VALUE'
    spheres_count_socket_2.structure_type = 'AUTO'

    # Socket Min Sphere Size
    min_sphere_size_socket_2 = ff_clouds_nodes_1.interface.new_socket(name="Min Sphere Size", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_3_panel)
    min_sphere_size_socket_2.default_value = 0.2199999988079071
    min_sphere_size_socket_2.min_value = 0.0
    min_sphere_size_socket_2.max_value = 3.4028234663852886e+38
    min_sphere_size_socket_2.subtype = 'NONE'
    min_sphere_size_socket_2.attribute_domain = 'POINT'
    min_sphere_size_socket_2.default_input = 'VALUE'
    min_sphere_size_socket_2.structure_type = 'AUTO'

    # Socket Max Sphere Size
    max_sphere_size_socket_2 = ff_clouds_nodes_1.interface.new_socket(name="Max Sphere Size", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_3_panel)
    max_sphere_size_socket_2.default_value = 0.4000000059604645
    max_sphere_size_socket_2.min_value = 0.0
    max_sphere_size_socket_2.max_value = 3.4028234663852886e+38
    max_sphere_size_socket_2.subtype = 'NONE'
    max_sphere_size_socket_2.attribute_domain = 'POINT'
    max_sphere_size_socket_2.default_input = 'VALUE'
    max_sphere_size_socket_2.structure_type = 'AUTO'

    # Socket Squash Probability
    squash_probability_socket_2 = ff_clouds_nodes_1.interface.new_socket(name="Squash Probability", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_3_panel)
    squash_probability_socket_2.default_value = 0.30000001192092896
    squash_probability_socket_2.min_value = 0.0
    squash_probability_socket_2.max_value = 1.0
    squash_probability_socket_2.subtype = 'NONE'
    squash_probability_socket_2.attribute_domain = 'POINT'
    squash_probability_socket_2.default_input = 'VALUE'
    squash_probability_socket_2.structure_type = 'AUTO'

    # Socket Max Squash Strength
    max_squash_strength_socket_2 = ff_clouds_nodes_1.interface.new_socket(name="Max Squash Strength", in_out='INPUT', socket_type='NodeSocketFloat', parent = layer_3_panel)
    max_squash_strength_socket_2.default_value = 0.3499999940395355
    max_squash_strength_socket_2.min_value = 0.0
    max_squash_strength_socket_2.max_value = 1.0
    max_squash_strength_socket_2.subtype = 'NONE'
    max_squash_strength_socket_2.attribute_domain = 'POINT'
    max_squash_strength_socket_2.default_input = 'VALUE'
    max_squash_strength_socket_2.structure_type = 'AUTO'


    # Panel Detail
    detail_panel = ff_clouds_nodes_1.interface.new_panel("Detail")
    # Socket Material
    material_socket = ff_clouds_nodes_1.interface.new_socket(name="Material", in_out='INPUT', socket_type='NodeSocketMaterial', parent = detail_panel)
    material_socket.attribute_domain = 'POINT'
    material_socket.default_input = 'VALUE'
    material_socket.structure_type = 'AUTO'
    material_socket.optional_label = True

    # Socket Normal Blur (Fluffiness)
    normal_blur__fluffiness__socket = ff_clouds_nodes_1.interface.new_socket(name="Normal Blur (Fluffiness)", in_out='INPUT', socket_type='NodeSocketInt', parent = detail_panel)
    normal_blur__fluffiness__socket.default_value = 8
    normal_blur__fluffiness__socket.min_value = 0
    normal_blur__fluffiness__socket.max_value = 32
    normal_blur__fluffiness__socket.subtype = 'NONE'
    normal_blur__fluffiness__socket.attribute_domain = 'POINT'
    normal_blur__fluffiness__socket.default_input = 'VALUE'
    normal_blur__fluffiness__socket.structure_type = 'AUTO'

    # Socket Cloud Color
    cloud_color_socket = ff_clouds_nodes_1.interface.new_socket(name="Cloud Color", in_out='INPUT', socket_type='NodeSocketColor', parent = detail_panel)
    cloud_color_socket.default_value = (0.550000011920929, 0.699999988079071, 0.949999988079071, 1.0)
    cloud_color_socket.attribute_domain = 'POINT'
    cloud_color_socket.default_input = 'VALUE'
    cloud_color_socket.structure_type = 'AUTO'


    # Initialize ff_clouds_nodes_1 nodes

    # Node Group Output
    group_output = ff_clouds_nodes_1.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.show_options = True
    group_output.is_active_output = True

    # Node Point Count Math
    point_count_math = ff_clouds_nodes_1.nodes.new("NodeFrame")
    point_count_math.label = "Point Count Math"
    point_count_math.name = "Point Count Math"
    point_count_math.use_custom_color = True
    point_count_math.color = (0.18000000715255737, 0.2800000011920929, 0.4000000059604645)
    point_count_math.show_options = True
    point_count_math.label_size = 20
    point_count_math.shrink = True

    # Node Group Input
    group_input = ff_clouds_nodes_1.nodes.new("NodeGroupInput")
    group_input.label = "Input: Counts"
    group_input.name = "Group Input"
    group_input.show_options = True

    # Node boundary2 (L1+L2)
    boundary2__l1_l2_ = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    boundary2__l1_l2_.label = "boundary2 (L1+L2)"
    boundary2__l1_l2_.name = "boundary2 (L1+L2)"
    boundary2__l1_l2_.show_options = True
    boundary2__l1_l2_.operation = 'ADD'
    boundary2__l1_l2_.use_clamp = False

    # Node max_per_cloud (L1+L2+L3)
    max_per_cloud__l1_l2_l3_ = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    max_per_cloud__l1_l2_l3_.label = "max_per_cloud (L1+L2+L3)"
    max_per_cloud__l1_l2_l3_.name = "max_per_cloud (L1+L2+L3)"
    max_per_cloud__l1_l2_l3_.show_options = True
    max_per_cloud__l1_l2_l3_.operation = 'ADD'
    max_per_cloud__l1_l2_l3_.use_clamp = False

    # Node slot_total
    slot_total = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    slot_total.label = "slot_total"
    slot_total.name = "slot_total"
    slot_total.show_options = True
    slot_total.operation = 'MULTIPLY'
    slot_total.use_clamp = False

    # Node total_points
    total_points = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    total_points.label = "total_points"
    total_points.name = "total_points"
    total_points.show_options = True
    total_points.operation = 'MULTIPLY'
    total_points.use_clamp = False
    # Value_001
    total_points.inputs[1].default_value = 4.0

    # Node total_points (int)
    total_points__int_ = ff_clouds_nodes_1.nodes.new("FunctionNodeFloatToInt")
    total_points__int_.label = "total_points (int)"
    total_points__int_.name = "total_points (int)"
    total_points__int_.show_options = True
    total_points__int_.rounding_mode = 'ROUND'

    # Node Base Point Cloud
    base_point_cloud = ff_clouds_nodes_1.nodes.new("NodeFrame")
    base_point_cloud.label = "Base Point Cloud"
    base_point_cloud.name = "Base Point Cloud"
    base_point_cloud.use_custom_color = True
    base_point_cloud.color = (0.18000000715255737, 0.2800000011920929, 0.4000000059604645)
    base_point_cloud.show_options = True
    base_point_cloud.label_size = 20
    base_point_cloud.shrink = True

    # Node Mesh Line
    mesh_line = ff_clouds_nodes_1.nodes.new("GeometryNodeMeshLine")
    mesh_line.label = "Mesh Line"
    mesh_line.name = "Mesh Line"
    mesh_line.show_options = True
    mesh_line.count_mode = 'TOTAL'
    mesh_line.mode = 'OFFSET'
    # Start Location
    mesh_line.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Offset
    mesh_line.inputs[3].default_value = (0.0, 0.0, 1.0)

    # Node Index
    index = ff_clouds_nodes_1.nodes.new("GeometryNodeInputIndex")
    index.label = "Index"
    index.name = "Index"
    index.show_options = True

    # Node Index Decomposition
    index_decomposition = ff_clouds_nodes_1.nodes.new("NodeFrame")
    index_decomposition.label = "Index Decomposition"
    index_decomposition.name = "Index Decomposition"
    index_decomposition.use_custom_color = True
    index_decomposition.color = (0.18000000715255737, 0.2800000011920929, 0.4000000059604645)
    index_decomposition.show_options = True
    index_decomposition.label_size = 20
    index_decomposition.shrink = True

    # Node i / 4
    i___4 = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    i___4.label = "i / 4"
    i___4.name = "i / 4"
    i___4.show_options = True
    i___4.operation = 'DIVIDE'
    i___4.use_clamp = False
    # Value_001
    i___4.inputs[1].default_value = 4.0

    # Node slot_index
    slot_index = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    slot_index.label = "slot_index"
    slot_index.name = "slot_index"
    slot_index.show_options = True
    slot_index.operation = 'FLOOR'
    slot_index.use_clamp = False

    # Node sub = i mod 4
    sub___i_mod_4 = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    sub___i_mod_4.label = "sub = i mod 4"
    sub___i_mod_4.name = "sub = i mod 4"
    sub___i_mod_4.show_options = True
    sub___i_mod_4.operation = 'MODULO'
    sub___i_mod_4.use_clamp = False
    # Value_001
    sub___i_mod_4.inputs[1].default_value = 4.0

    # Node slot/maxpc
    slot_maxpc = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    slot_maxpc.label = "slot/maxpc"
    slot_maxpc.name = "slot/maxpc"
    slot_maxpc.show_options = True
    slot_maxpc.operation = 'DIVIDE'
    slot_maxpc.use_clamp = False

    # Node cloud_index
    cloud_index = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    cloud_index.label = "cloud_index"
    cloud_index.name = "cloud_index"
    cloud_index.show_options = True
    cloud_index.operation = 'FLOOR'
    cloud_index.use_clamp = False

    # Node local_index
    local_index = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    local_index.label = "local_index"
    local_index.name = "local_index"
    local_index.show_options = True
    local_index.operation = 'MODULO'
    local_index.use_clamp = False

    # Node cloud_index (int)
    cloud_index__int_ = ff_clouds_nodes_1.nodes.new("FunctionNodeFloatToInt")
    cloud_index__int_.label = "cloud_index (int)"
    cloud_index__int_.name = "cloud_index (int)"
    cloud_index__int_.show_options = True
    cloud_index__int_.rounding_mode = 'ROUND'

    # Node slot_index (int)
    slot_index__int_ = ff_clouds_nodes_1.nodes.new("FunctionNodeFloatToInt")
    slot_index__int_.label = "slot_index (int)"
    slot_index__int_.name = "slot_index (int)"
    slot_index__int_.show_options = True
    slot_index__int_.rounding_mode = 'ROUND'

    # Node Layer Membership
    layer_membership = ff_clouds_nodes_1.nodes.new("NodeFrame")
    layer_membership.label = "Layer Membership"
    layer_membership.name = "Layer Membership"
    layer_membership.use_custom_color = True
    layer_membership.color = (0.18000000715255737, 0.2800000011920929, 0.4000000059604645)
    layer_membership.show_options = True
    layer_membership.label_size = 20
    layer_membership.shrink = True

    # Node is_L1
    is_l1 = ff_clouds_nodes_1.nodes.new("FunctionNodeCompare")
    is_l1.label = "is_L1"
    is_l1.name = "is_L1"
    is_l1.show_options = True
    is_l1.data_type = 'FLOAT'
    is_l1.mode = 'ELEMENT'
    is_l1.operation = 'LESS_THAN'

    # Node >= boundary1
    ___boundary1 = ff_clouds_nodes_1.nodes.new("FunctionNodeCompare")
    ___boundary1.label = ">= boundary1"
    ___boundary1.name = ">= boundary1"
    ___boundary1.show_options = True
    ___boundary1.data_type = 'FLOAT'
    ___boundary1.mode = 'ELEMENT'
    ___boundary1.operation = 'GREATER_EQUAL'

    # Node < boundary2
    __boundary2 = ff_clouds_nodes_1.nodes.new("FunctionNodeCompare")
    __boundary2.label = "< boundary2"
    __boundary2.name = "< boundary2"
    __boundary2.show_options = True
    __boundary2.data_type = 'FLOAT'
    __boundary2.mode = 'ELEMENT'
    __boundary2.operation = 'LESS_THAN'

    # Node is_L2
    is_l2 = ff_clouds_nodes_1.nodes.new("FunctionNodeBooleanMath")
    is_l2.label = "is_L2"
    is_l2.name = "is_L2"
    is_l2.show_options = True
    is_l2.operation = 'AND'

    # Node Layer Parameter Switching
    layer_parameter_switching = ff_clouds_nodes_1.nodes.new("NodeFrame")
    layer_parameter_switching.label = "Layer Parameter Switching"
    layer_parameter_switching.name = "Layer Parameter Switching"
    layer_parameter_switching.use_custom_color = True
    layer_parameter_switching.color = (0.4000000059604645, 0.20000000298023224, 0.20000000298023224)
    layer_parameter_switching.show_options = True
    layer_parameter_switching.label_size = 20
    layer_parameter_switching.shrink = True

    # Node Group Input.001
    group_input_001 = ff_clouds_nodes_1.nodes.new("NodeGroupInput")
    group_input_001.label = "Input: Layer Params"
    group_input_001.name = "Group Input.001"
    group_input_001.show_options = True

    # Node probability: L2 or L3
    probability__l2_or_l3 = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    probability__l2_or_l3.label = "probability: L2 or L3"
    probability__l2_or_l3.name = "probability: L2 or L3"
    probability__l2_or_l3.show_options = True
    probability__l2_or_l3.input_type = 'FLOAT'

    # Node probability: select layer
    probability__select_layer = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    probability__select_layer.label = "probability: select layer"
    probability__select_layer.name = "probability: select layer"
    probability__select_layer.show_options = True
    probability__select_layer.input_type = 'FLOAT'

    # Node radius: L2 or L3
    radius__l2_or_l3 = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    radius__l2_or_l3.label = "radius: L2 or L3"
    radius__l2_or_l3.name = "radius: L2 or L3"
    radius__l2_or_l3.show_options = True
    radius__l2_or_l3.input_type = 'FLOAT'

    # Node radius: select layer
    radius__select_layer = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    radius__select_layer.label = "radius: select layer"
    radius__select_layer.name = "radius: select layer"
    radius__select_layer.show_options = True
    radius__select_layer.input_type = 'FLOAT'

    # Node height: L2 or L3
    height__l2_or_l3 = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    height__l2_or_l3.label = "height: L2 or L3"
    height__l2_or_l3.name = "height: L2 or L3"
    height__l2_or_l3.show_options = True
    height__l2_or_l3.input_type = 'FLOAT'

    # Node height: select layer
    height__select_layer = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    height__select_layer.label = "height: select layer"
    height__select_layer.name = "height: select layer"
    height__select_layer.show_options = True
    height__select_layer.input_type = 'FLOAT'

    # Node min_size: L2 or L3
    min_size__l2_or_l3 = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    min_size__l2_or_l3.label = "min_size: L2 or L3"
    min_size__l2_or_l3.name = "min_size: L2 or L3"
    min_size__l2_or_l3.show_options = True
    min_size__l2_or_l3.input_type = 'FLOAT'

    # Node min_size: select layer
    min_size__select_layer = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    min_size__select_layer.label = "min_size: select layer"
    min_size__select_layer.name = "min_size: select layer"
    min_size__select_layer.show_options = True
    min_size__select_layer.input_type = 'FLOAT'

    # Node max_size: L2 or L3
    max_size__l2_or_l3 = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    max_size__l2_or_l3.label = "max_size: L2 or L3"
    max_size__l2_or_l3.name = "max_size: L2 or L3"
    max_size__l2_or_l3.show_options = True
    max_size__l2_or_l3.input_type = 'FLOAT'

    # Node max_size: select layer
    max_size__select_layer = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    max_size__select_layer.label = "max_size: select layer"
    max_size__select_layer.name = "max_size: select layer"
    max_size__select_layer.show_options = True
    max_size__select_layer.input_type = 'FLOAT'

    # Node squash_prob: L2 or L3
    squash_prob__l2_or_l3 = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    squash_prob__l2_or_l3.label = "squash_prob: L2 or L3"
    squash_prob__l2_or_l3.name = "squash_prob: L2 or L3"
    squash_prob__l2_or_l3.show_options = True
    squash_prob__l2_or_l3.input_type = 'FLOAT'

    # Node squash_prob: select layer
    squash_prob__select_layer = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    squash_prob__select_layer.label = "squash_prob: select layer"
    squash_prob__select_layer.name = "squash_prob: select layer"
    squash_prob__select_layer.show_options = True
    squash_prob__select_layer.input_type = 'FLOAT'

    # Node max_squash: L2 or L3
    max_squash__l2_or_l3 = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    max_squash__l2_or_l3.label = "max_squash: L2 or L3"
    max_squash__l2_or_l3.name = "max_squash: L2 or L3"
    max_squash__l2_or_l3.show_options = True
    max_squash__l2_or_l3.input_type = 'FLOAT'

    # Node max_squash: select layer
    max_squash__select_layer = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    max_squash__select_layer.label = "max_squash: select layer"
    max_squash__select_layer.name = "max_squash: select layer"
    max_squash__select_layer.show_options = True
    max_squash__select_layer.input_type = 'FLOAT'

    # Node presence_seed: L2 or L3
    presence_seed__l2_or_l3 = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    presence_seed__l2_or_l3.label = "presence_seed: L2 or L3"
    presence_seed__l2_or_l3.name = "presence_seed: L2 or L3"
    presence_seed__l2_or_l3.show_options = True
    presence_seed__l2_or_l3.input_type = 'INT'
    # False
    presence_seed__l2_or_l3.inputs[1].default_value = 3041
    # True
    presence_seed__l2_or_l3.inputs[2].default_value = 2027

    # Node presence_seed: select layer
    presence_seed__select_layer = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    presence_seed__select_layer.label = "presence_seed: select layer"
    presence_seed__select_layer.name = "presence_seed: select layer"
    presence_seed__select_layer.show_options = True
    presence_seed__select_layer.input_type = 'INT'
    # True
    presence_seed__select_layer.inputs[2].default_value = 1009

    # Node Layer Presence Check
    layer_presence_check = ff_clouds_nodes_1.nodes.new("NodeFrame")
    layer_presence_check.label = "Layer Presence Check"
    layer_presence_check.name = "Layer Presence Check"
    layer_presence_check.use_custom_color = True
    layer_presence_check.color = (0.4000000059604645, 0.20000000298023224, 0.20000000298023224)
    layer_presence_check.show_options = True
    layer_presence_check.label_size = 20
    layer_presence_check.shrink = True

    # Node layer_present?
    layer_present_ = ff_clouds_nodes_1.nodes.new("FunctionNodeRandomValue")
    layer_present_.label = "layer_present?"
    layer_present_.name = "layer_present?"
    layer_present_.show_options = True
    layer_present_.data_type = 'BOOLEAN'

    # Node NOT layer_present
    not_layer_present = ff_clouds_nodes_1.nodes.new("FunctionNodeBooleanMath")
    not_layer_present.label = "NOT layer_present"
    not_layer_present.name = "NOT layer_present"
    not_layer_present.show_options = True
    not_layer_present.operation = 'NOT'

    # Node Cloud Centers
    cloud_centers = ff_clouds_nodes_1.nodes.new("NodeFrame")
    cloud_centers.label = "Cloud Centers"
    cloud_centers.name = "Cloud Centers"
    cloud_centers.use_custom_color = True
    cloud_centers.color = (0.20000000298023224, 0.4000000059604645, 0.20000000298023224)
    cloud_centers.show_options = True
    cloud_centers.label_size = 20
    cloud_centers.shrink = True

    # Node Group Input.002
    group_input_002 = ff_clouds_nodes_1.nodes.new("NodeGroupInput")
    group_input_002.label = "Input: Field Sizes"
    group_input_002.name = "Group Input.002"
    group_input_002.show_options = True

    # Node FieldX/2
    fieldx_2 = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    fieldx_2.label = "FieldX/2"
    fieldx_2.name = "FieldX/2"
    fieldx_2.show_options = True
    fieldx_2.operation = 'MULTIPLY'
    fieldx_2.use_clamp = False
    # Value_001
    fieldx_2.inputs[1].default_value = 0.5

    # Node -FieldX/2
    _fieldx_2 = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    _fieldx_2.label = "-FieldX/2"
    _fieldx_2.name = "-FieldX/2"
    _fieldx_2.show_options = True
    _fieldx_2.operation = 'MULTIPLY'
    _fieldx_2.use_clamp = False
    # Value_001
    _fieldx_2.inputs[1].default_value = -1.0

    # Node FieldY/2
    fieldy_2 = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    fieldy_2.label = "FieldY/2"
    fieldy_2.name = "FieldY/2"
    fieldy_2.show_options = True
    fieldy_2.operation = 'MULTIPLY'
    fieldy_2.use_clamp = False
    # Value_001
    fieldy_2.inputs[1].default_value = 0.5

    # Node -FieldY/2
    _fieldy_2 = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    _fieldy_2.label = "-FieldY/2"
    _fieldy_2.name = "-FieldY/2"
    _fieldy_2.show_options = True
    _fieldy_2.operation = 'MULTIPLY'
    _fieldy_2.use_clamp = False
    # Value_001
    _fieldy_2.inputs[1].default_value = -1.0

    # Node HeightScatter/2
    heightscatter_2 = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    heightscatter_2.label = "HeightScatter/2"
    heightscatter_2.name = "HeightScatter/2"
    heightscatter_2.show_options = True
    heightscatter_2.operation = 'MULTIPLY'
    heightscatter_2.use_clamp = False
    # Value_001
    heightscatter_2.inputs[1].default_value = 0.5

    # Node -HeightScatter/2
    _heightscatter_2 = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    _heightscatter_2.label = "-HeightScatter/2"
    _heightscatter_2.name = "-HeightScatter/2"
    _heightscatter_2.show_options = True
    _heightscatter_2.operation = 'MULTIPLY'
    _heightscatter_2.use_clamp = False
    # Value_001
    _heightscatter_2.inputs[1].default_value = -1.0

    # Node Cloud Center X
    cloud_center_x = ff_clouds_nodes_1.nodes.new("FunctionNodeRandomValue")
    cloud_center_x.label = "Cloud Center X"
    cloud_center_x.name = "Cloud Center X"
    cloud_center_x.show_options = True
    cloud_center_x.data_type = 'FLOAT'
    # Seed
    cloud_center_x.inputs[3].default_value = 100

    # Node Cloud Center Y
    cloud_center_y = ff_clouds_nodes_1.nodes.new("FunctionNodeRandomValue")
    cloud_center_y.label = "Cloud Center Y"
    cloud_center_y.name = "Cloud Center Y"
    cloud_center_y.show_options = True
    cloud_center_y.data_type = 'FLOAT'
    # Seed
    cloud_center_y.inputs[3].default_value = 200

    # Node Cloud Center Z
    cloud_center_z = ff_clouds_nodes_1.nodes.new("FunctionNodeRandomValue")
    cloud_center_z.label = "Cloud Center Z"
    cloud_center_z.name = "Cloud Center Z"
    cloud_center_z.show_options = True
    cloud_center_z.data_type = 'FLOAT'
    # Seed
    cloud_center_z.inputs[3].default_value = 300

    # Node Cloud Center
    cloud_center = ff_clouds_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    cloud_center.label = "Cloud Center"
    cloud_center.name = "Cloud Center"
    cloud_center.show_options = True

    # Node Cloud Color Seed
    cloud_color_seed = ff_clouds_nodes_1.nodes.new("NodeFrame")
    cloud_color_seed.label = "Cloud Color Seed"
    cloud_color_seed.name = "Cloud Color Seed"
    cloud_color_seed.use_custom_color = True
    cloud_color_seed.color = (0.20000000298023224, 0.4000000059604645, 0.20000000298023224)
    cloud_color_seed.show_options = True
    cloud_color_seed.label_size = 20
    cloud_color_seed.shrink = True

    # Node Group Input.003
    group_input_003 = ff_clouds_nodes_1.nodes.new("NodeGroupInput")
    group_input_003.label = "Input: Cloud Color"
    group_input_003.name = "Group Input.003"
    group_input_003.show_options = True

    # Node Cloud Color To Seed
    cloud_color_to_seed = ff_clouds_nodes_1.nodes.new("ShaderNodeVectorMath")
    cloud_color_to_seed.label = "Cloud Color To Seed"
    cloud_color_to_seed.name = "Cloud Color To Seed"
    cloud_color_to_seed.show_options = True
    cloud_color_to_seed.operation = 'DOT_PRODUCT'
    # Vector_001
    cloud_color_to_seed.inputs[1].default_value = (311.70001220703125, 601.2999877929688, 927.0999755859375)

    # Node Cloud Random Color
    cloud_random_color = ff_clouds_nodes_1.nodes.new("FunctionNodeRandomValue")
    cloud_random_color.label = "Cloud Random Color"
    cloud_random_color.name = "Cloud Random Color"
    cloud_random_color.show_options = True
    cloud_random_color.data_type = 'FLOAT_VECTOR'
    # Min
    cloud_random_color.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Max
    cloud_random_color.inputs[1].default_value = (1.0, 1.0, 1.0)

    # Node Per-Sphere Randomization
    per_sphere_randomization = ff_clouds_nodes_1.nodes.new("NodeFrame")
    per_sphere_randomization.label = "Per-Sphere Randomization"
    per_sphere_randomization.name = "Per-Sphere Randomization"
    per_sphere_randomization.use_custom_color = True
    per_sphere_randomization.color = (0.20000000298023224, 0.4000000059604645, 0.20000000298023224)
    per_sphere_randomization.show_options = True
    per_sphere_randomization.label_size = 20
    per_sphere_randomization.shrink = True

    # Node Angle
    angle = ff_clouds_nodes_1.nodes.new("FunctionNodeRandomValue")
    angle.label = "Angle"
    angle.name = "Angle"
    angle.show_options = True
    angle.data_type = 'FLOAT'
    # Min
    angle.inputs[0].default_value = 0.0
    # Max
    angle.inputs[1].default_value = 6.2831854820251465
    # Seed
    angle.inputs[3].default_value = 10

    # Node Radius Frac
    radius_frac = ff_clouds_nodes_1.nodes.new("FunctionNodeRandomValue")
    radius_frac.label = "Radius Frac"
    radius_frac.name = "Radius Frac"
    radius_frac.show_options = True
    radius_frac.data_type = 'FLOAT'
    # Min
    radius_frac.inputs[0].default_value = 0.0
    # Max
    radius_frac.inputs[1].default_value = 1.0
    # Seed
    radius_frac.inputs[3].default_value = 20

    # Node sqrt(frac)
    sqrt_frac_ = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    sqrt_frac_.label = "sqrt(frac)"
    sqrt_frac_.name = "sqrt(frac)"
    sqrt_frac_.show_options = True
    sqrt_frac_.operation = 'SQRT'
    sqrt_frac_.use_clamp = False

    # Node local_radius
    local_radius = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    local_radius.label = "local_radius"
    local_radius.name = "local_radius"
    local_radius.show_options = True
    local_radius.operation = 'MULTIPLY'
    local_radius.use_clamp = False

    # Node cos(angle)
    cos_angle_ = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    cos_angle_.label = "cos(angle)"
    cos_angle_.name = "cos(angle)"
    cos_angle_.show_options = True
    cos_angle_.operation = 'COSINE'
    cos_angle_.use_clamp = False

    # Node sin(angle)
    sin_angle_ = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    sin_angle_.label = "sin(angle)"
    sin_angle_.name = "sin(angle)"
    sin_angle_.show_options = True
    sin_angle_.operation = 'SINE'
    sin_angle_.use_clamp = False

    # Node x_local
    x_local = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    x_local.label = "x_local"
    x_local.name = "x_local"
    x_local.show_options = True
    x_local.operation = 'MULTIPLY'
    x_local.use_clamp = False

    # Node y_local
    y_local = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    y_local.label = "y_local"
    y_local.name = "y_local"
    y_local.show_options = True
    y_local.operation = 'MULTIPLY'
    y_local.use_clamp = False

    # Node jag_amount
    jag_amount = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    jag_amount.label = "jag_amount"
    jag_amount.name = "jag_amount"
    jag_amount.show_options = True
    jag_amount.operation = 'MULTIPLY'
    jag_amount.use_clamp = False
    # Value_001
    jag_amount.inputs[1].default_value = 0.18000000715255737

    # Node -jag_amount
    _jag_amount = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    _jag_amount.label = "-jag_amount"
    _jag_amount.name = "-jag_amount"
    _jag_amount.show_options = True
    _jag_amount.operation = 'MULTIPLY'
    _jag_amount.use_clamp = False
    # Value_001
    _jag_amount.inputs[1].default_value = -1.0

    # Node jag_z
    jag_z = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    jag_z.label = "jag_z"
    jag_z.name = "jag_z"
    jag_z.show_options = True
    jag_z.operation = 'MULTIPLY'
    jag_z.use_clamp = False
    # Value_001
    jag_z.inputs[1].default_value = 0.30000001192092896

    # Node -jag_z
    _jag_z = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    _jag_z.label = "-jag_z"
    _jag_z.name = "-jag_z"
    _jag_z.show_options = True
    _jag_z.operation = 'MULTIPLY'
    _jag_z.use_clamp = False
    # Value_001
    _jag_z.inputs[1].default_value = -1.0

    # Node jag min vec
    jag_min_vec = ff_clouds_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    jag_min_vec.label = "jag min vec"
    jag_min_vec.name = "jag min vec"
    jag_min_vec.show_options = True

    # Node jag max vec
    jag_max_vec = ff_clouds_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    jag_max_vec.label = "jag max vec"
    jag_max_vec.name = "jag max vec"
    jag_max_vec.show_options = True

    # Node Jagged Offset
    jagged_offset = ff_clouds_nodes_1.nodes.new("FunctionNodeRandomValue")
    jagged_offset.label = "Jagged Offset"
    jagged_offset.name = "Jagged Offset"
    jagged_offset.show_options = True
    jagged_offset.data_type = 'FLOAT_VECTOR'
    # Seed
    jagged_offset.inputs[3].default_value = 60

    # Node Base Sphere Radius
    base_sphere_radius = ff_clouds_nodes_1.nodes.new("FunctionNodeRandomValue")
    base_sphere_radius.label = "Base Sphere Radius"
    base_sphere_radius.name = "Base Sphere Radius"
    base_sphere_radius.show_options = True
    base_sphere_radius.data_type = 'FLOAT'
    # Seed
    base_sphere_radius.inputs[3].default_value = 30

    # Node Squash Check
    squash_check = ff_clouds_nodes_1.nodes.new("FunctionNodeRandomValue")
    squash_check.label = "Squash Check"
    squash_check.name = "Squash Check"
    squash_check.show_options = True
    squash_check.data_type = 'BOOLEAN'
    # Seed
    squash_check.inputs[2].default_value = 40

    # Node Squash Amount (raw)
    squash_amount__raw_ = ff_clouds_nodes_1.nodes.new("FunctionNodeRandomValue")
    squash_amount__raw_.label = "Squash Amount (raw)"
    squash_amount__raw_.name = "Squash Amount (raw)"
    squash_amount__raw_.show_options = True
    squash_amount__raw_.data_type = 'FLOAT'
    # Min
    squash_amount__raw_.inputs[0].default_value = 0.0
    # Seed
    squash_amount__raw_.inputs[3].default_value = 50

    # Node Squash Amount
    squash_amount = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    squash_amount.label = "Squash Amount"
    squash_amount.name = "Squash Amount"
    squash_amount.show_options = True
    squash_amount.input_type = 'FLOAT'
    # False
    squash_amount.inputs[1].default_value = 0.0

    # Node Squash Logic
    squash_logic = ff_clouds_nodes_1.nodes.new("NodeFrame")
    squash_logic.label = "Squash Logic"
    squash_logic.name = "Squash Logic"
    squash_logic.use_custom_color = True
    squash_logic.color = (0.20000000298023224, 0.4000000059604645, 0.20000000298023224)
    squash_logic.show_options = True
    squash_logic.label_size = 20
    squash_logic.shrink = True

    # Node shrink
    shrink = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    shrink.label = "shrink"
    shrink.name = "shrink"
    shrink.show_options = True
    shrink.operation = 'MULTIPLY'
    shrink.use_clamp = False
    # Value_001
    shrink.inputs[1].default_value = 0.3499999940395355

    # Node 1 - shrink
    _1___shrink = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    _1___shrink.label = "1 - shrink"
    _1___shrink.name = "1 - shrink"
    _1___shrink.show_options = True
    _1___shrink.operation = 'SUBTRACT'
    _1___shrink.use_clamp = False
    # Value
    _1___shrink.inputs[0].default_value = 1.0

    # Node Sub-sphere Radius
    sub_sphere_radius = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    sub_sphere_radius.label = "Sub-sphere Radius"
    sub_sphere_radius.name = "Sub-sphere Radius"
    sub_sphere_radius.show_options = True
    sub_sphere_radius.operation = 'MULTIPLY'
    sub_sphere_radius.use_clamp = False

    # Node squash*base_radius
    squash_base_radius = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    squash_base_radius.label = "squash*base_radius"
    squash_base_radius.name = "squash*base_radius"
    squash_base_radius.show_options = True
    squash_base_radius.operation = 'MULTIPLY'
    squash_base_radius.use_clamp = False

    # Node Spread Distance
    spread_distance = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    spread_distance.label = "Spread Distance"
    spread_distance.name = "Spread Distance"
    spread_distance.show_options = True
    spread_distance.operation = 'MULTIPLY'
    spread_distance.use_clamp = False
    # Value_001
    spread_distance.inputs[1].default_value = 1.5

    # Node sub == 0
    sub____0 = ff_clouds_nodes_1.nodes.new("FunctionNodeCompare")
    sub____0.label = "sub == 0"
    sub____0.name = "sub == 0"
    sub____0.show_options = True
    sub____0.data_type = 'FLOAT'
    sub____0.mode = 'ELEMENT'
    sub____0.operation = 'EQUAL'
    # B
    sub____0.inputs[1].default_value = 0.0
    # Epsilon
    sub____0.inputs[2].default_value = 0.0010000000474974513

    # Node sub == 1
    sub____1 = ff_clouds_nodes_1.nodes.new("FunctionNodeCompare")
    sub____1.label = "sub == 1"
    sub____1.name = "sub == 1"
    sub____1.show_options = True
    sub____1.data_type = 'FLOAT'
    sub____1.mode = 'ELEMENT'
    sub____1.operation = 'EQUAL'
    # B
    sub____1.inputs[1].default_value = 1.0
    # Epsilon
    sub____1.inputs[2].default_value = 0.0010000000474974513

    # Node sub == 2
    sub____2 = ff_clouds_nodes_1.nodes.new("FunctionNodeCompare")
    sub____2.label = "sub == 2"
    sub____2.name = "sub == 2"
    sub____2.show_options = True
    sub____2.data_type = 'FLOAT'
    sub____2.mode = 'ELEMENT'
    sub____2.operation = 'EQUAL'
    # B
    sub____2.inputs[1].default_value = 2.0
    # Epsilon
    sub____2.inputs[2].default_value = 0.0010000000474974513

    # Node dir: +Y / -Y
    dir___y____y = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    dir___y____y.label = "dir: +Y / -Y"
    dir___y____y.name = "dir: +Y / -Y"
    dir___y____y.show_options = True
    dir___y____y.input_type = 'VECTOR'
    # False
    dir___y____y.inputs[1].default_value = (0.0, -1.0, 0.0)
    # True
    dir___y____y.inputs[2].default_value = (0.0, 1.0, 0.0)

    # Node dir: -X / (+-Y)
    dir___x______y_ = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    dir___x______y_.label = "dir: -X / (+-Y)"
    dir___x______y_.name = "dir: -X / (+-Y)"
    dir___x______y_.show_options = True
    dir___x______y_.input_type = 'VECTOR'
    # True
    dir___x______y_.inputs[2].default_value = (-1.0, 0.0, 0.0)

    # Node dir: +X
    dir___x = ff_clouds_nodes_1.nodes.new("GeometryNodeSwitch")
    dir___x.label = "dir: +X"
    dir___x.name = "dir: +X"
    dir___x.show_options = True
    dir___x.input_type = 'VECTOR'
    # True
    dir___x.inputs[2].default_value = (1.0, 0.0, 0.0)

    # Node Sub Offset sep
    sub_offset_sep = ff_clouds_nodes_1.nodes.new("ShaderNodeSeparateXYZ")
    sub_offset_sep.label = "Sub Offset sep"
    sub_offset_sep.name = "Sub Offset sep"
    sub_offset_sep.show_options = True

    # Node Sub Offset x
    sub_offset_x = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    sub_offset_x.label = "Sub Offset x"
    sub_offset_x.name = "Sub Offset x"
    sub_offset_x.show_options = True
    sub_offset_x.operation = 'MULTIPLY'
    sub_offset_x.use_clamp = False

    # Node Sub Offset y
    sub_offset_y = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    sub_offset_y.label = "Sub Offset y"
    sub_offset_y.name = "Sub Offset y"
    sub_offset_y.show_options = True
    sub_offset_y.operation = 'MULTIPLY'
    sub_offset_y.use_clamp = False

    # Node Sub Offset z
    sub_offset_z = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    sub_offset_z.label = "Sub Offset z"
    sub_offset_z.name = "Sub Offset z"
    sub_offset_z.show_options = True
    sub_offset_z.operation = 'MULTIPLY'
    sub_offset_z.use_clamp = False

    # Node Sub Offset
    sub_offset = ff_clouds_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    sub_offset.label = "Sub Offset"
    sub_offset.name = "Sub Offset"
    sub_offset.show_options = True

    # Node Position Assembly
    position_assembly = ff_clouds_nodes_1.nodes.new("NodeFrame")
    position_assembly.label = "Position Assembly"
    position_assembly.name = "Position Assembly"
    position_assembly.use_custom_color = True
    position_assembly.color = (0.20000000298023224, 0.4000000059604645, 0.20000000298023224)
    position_assembly.show_options = True
    position_assembly.label_size = 20
    position_assembly.shrink = True

    # Node Local XY
    local_xy = ff_clouds_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    local_xy.label = "Local XY"
    local_xy.name = "Local XY"
    local_xy.show_options = True
    # Z
    local_xy.inputs[2].default_value = 0.0

    # Node + jagged offset
    __jagged_offset = ff_clouds_nodes_1.nodes.new("ShaderNodeVectorMath")
    __jagged_offset.label = "+ jagged offset"
    __jagged_offset.name = "+ jagged offset"
    __jagged_offset.show_options = True
    __jagged_offset.operation = 'ADD'

    # Node + squash sub-offset
    __squash_sub_offset = ff_clouds_nodes_1.nodes.new("ShaderNodeVectorMath")
    __squash_sub_offset.label = "+ squash sub-offset"
    __squash_sub_offset.name = "+ squash sub-offset"
    __squash_sub_offset.show_options = True
    __squash_sub_offset.operation = 'ADD'

    # Node Layer Height Vec
    layer_height_vec = ff_clouds_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    layer_height_vec.label = "Layer Height Vec"
    layer_height_vec.name = "Layer Height Vec"
    layer_height_vec.show_options = True
    # X
    layer_height_vec.inputs[0].default_value = 0.0
    # Y
    layer_height_vec.inputs[1].default_value = 0.0

    # Node cloud_center + layer_height
    cloud_center___layer_height = ff_clouds_nodes_1.nodes.new("ShaderNodeVectorMath")
    cloud_center___layer_height.label = "cloud_center + layer_height"
    cloud_center___layer_height.name = "cloud_center + layer_height"
    cloud_center___layer_height.show_options = True
    cloud_center___layer_height.operation = 'ADD'

    # Node FINAL POSITION
    final_position = ff_clouds_nodes_1.nodes.new("ShaderNodeVectorMath")
    final_position.label = "FINAL POSITION"
    final_position.name = "FINAL POSITION"
    final_position.show_options = True
    final_position.operation = 'ADD'

    # Node Filter & Bake
    filter___bake = ff_clouds_nodes_1.nodes.new("NodeFrame")
    filter___bake.label = "Filter & Bake"
    filter___bake.name = "Filter & Bake"
    filter___bake.use_custom_color = True
    filter___bake.color = (0.4000000059604645, 0.25, 0.10000000149011612)
    filter___bake.show_options = True
    filter___bake.label_size = 20
    filter___bake.shrink = True

    # Node Set Position
    set_position = ff_clouds_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position.label = "Set Position"
    set_position.name = "Set Position"
    set_position.show_options = True
    # Selection
    set_position.inputs[1].default_value = True
    # Offset
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

    # Node Store 'sphere_radius'
    store__sphere_radius_ = ff_clouds_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store__sphere_radius_.label = "Store 'sphere_radius'"
    store__sphere_radius_.name = "Store 'sphere_radius'"
    store__sphere_radius_.show_options = True
    store__sphere_radius_.data_type = 'FLOAT'
    store__sphere_radius_.domain = 'POINT'
    # Selection
    store__sphere_radius_.inputs[1].default_value = True
    # Name
    store__sphere_radius_.inputs[2].default_value = "sphere_radius"

    # Node Store 'ColorMask'
    store__colormask_ = ff_clouds_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store__colormask_.label = "Store 'ColorMask'"
    store__colormask_.name = "Store 'ColorMask'"
    store__colormask_.show_options = True
    store__colormask_.data_type = 'FLOAT_COLOR'
    store__colormask_.domain = 'POINT'
    # Selection
    store__colormask_.inputs[1].default_value = True
    # Name
    store__colormask_.inputs[2].default_value = "ColorMask"

    # Node Delete absent points
    delete_absent_points = ff_clouds_nodes_1.nodes.new("GeometryNodeDeleteGeometry")
    delete_absent_points.label = "Delete absent points"
    delete_absent_points.name = "Delete absent points"
    delete_absent_points.show_options = True
    delete_absent_points.domain = 'POINT'
    delete_absent_points.mode = 'ALL'

    # Node Mesh Conversion
    mesh_conversion = ff_clouds_nodes_1.nodes.new("NodeFrame")
    mesh_conversion.label = "Mesh Conversion"
    mesh_conversion.name = "Mesh Conversion"
    mesh_conversion.use_custom_color = True
    mesh_conversion.color = (0.4000000059604645, 0.25, 0.10000000149011612)
    mesh_conversion.show_options = True
    mesh_conversion.label_size = 20
    mesh_conversion.shrink = True

    # Node Group Input.004
    group_input_004 = ff_clouds_nodes_1.nodes.new("NodeGroupInput")
    group_input_004.label = "Input: Voxel Settings"
    group_input_004.name = "Group Input.004"
    group_input_004.show_options = True

    # Node Read back 'sphere_radius'
    read_back__sphere_radius_ = ff_clouds_nodes_1.nodes.new("GeometryNodeInputNamedAttribute")
    read_back__sphere_radius_.label = "Read back 'sphere_radius'"
    read_back__sphere_radius_.name = "Read back 'sphere_radius'"
    read_back__sphere_radius_.show_options = True
    read_back__sphere_radius_.data_type = 'FLOAT'
    # Name
    read_back__sphere_radius_.inputs[0].default_value = "sphere_radius"

    # Node Points to Volume
    points_to_volume = ff_clouds_nodes_1.nodes.new("GeometryNodePointsToVolume")
    points_to_volume.label = "Points to Volume"
    points_to_volume.name = "Points to Volume"
    points_to_volume.show_options = True
    # Density
    points_to_volume.inputs[1].default_value = 1.0
    # Resolution Mode
    points_to_volume.inputs[2].default_value = 'Size'
    # Voxel Amount
    points_to_volume.inputs[4].default_value = 64.0

    # Node Volume to Mesh
    volume_to_mesh = ff_clouds_nodes_1.nodes.new("GeometryNodeVolumeToMesh")
    volume_to_mesh.label = "Volume to Mesh"
    volume_to_mesh.name = "Volume to Mesh"
    volume_to_mesh.show_options = True
    # Resolution Mode
    volume_to_mesh.inputs[1].default_value = 'Grid'
    # Voxel Size
    volume_to_mesh.inputs[2].default_value = 0.30000001192092896
    # Voxel Amount
    volume_to_mesh.inputs[3].default_value = 64.0
    # Adaptivity
    volume_to_mesh.inputs[5].default_value = 0.0

    # Node Cloud Color Transfer
    cloud_color_transfer = ff_clouds_nodes_1.nodes.new("NodeFrame")
    cloud_color_transfer.label = "Cloud Color Transfer"
    cloud_color_transfer.name = "Cloud Color Transfer"
    cloud_color_transfer.use_custom_color = True
    cloud_color_transfer.color = (0.4000000059604645, 0.25, 0.10000000149011612)
    cloud_color_transfer.show_options = True
    cloud_color_transfer.label_size = 20
    cloud_color_transfer.shrink = True

    # Node Position (voxel mesh)
    position__voxel_mesh_ = ff_clouds_nodes_1.nodes.new("GeometryNodeInputPosition")
    position__voxel_mesh_.label = "Position (voxel mesh)"
    position__voxel_mesh_.name = "Position (voxel mesh)"
    position__voxel_mesh_.show_options = True

    # Node Sample Nearest (cloud point)
    sample_nearest__cloud_point_ = ff_clouds_nodes_1.nodes.new("GeometryNodeSampleNearest")
    sample_nearest__cloud_point_.label = "Sample Nearest (cloud point)"
    sample_nearest__cloud_point_.name = "Sample Nearest (cloud point)"
    sample_nearest__cloud_point_.show_options = True
    sample_nearest__cloud_point_.domain = 'POINT'

    # Node Read 'ColorMask' (points)
    read__colormask___points_ = ff_clouds_nodes_1.nodes.new("GeometryNodeInputNamedAttribute")
    read__colormask___points_.label = "Read 'ColorMask' (points)"
    read__colormask___points_.name = "Read 'ColorMask' (points)"
    read__colormask___points_.show_options = True
    read__colormask___points_.data_type = 'FLOAT_COLOR'
    # Name
    read__colormask___points_.inputs[0].default_value = "ColorMask"

    # Node Sample Index (ColorMask)
    sample_index__colormask_ = ff_clouds_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index__colormask_.label = "Sample Index (ColorMask)"
    sample_index__colormask_.name = "Sample Index (ColorMask)"
    sample_index__colormask_.show_options = True
    sample_index__colormask_.clamp = False
    sample_index__colormask_.data_type = 'FLOAT_COLOR'
    sample_index__colormask_.domain = 'POINT'

    # Node Store 'ColorMask' (voxel mesh)
    store__colormask___voxel_mesh_ = ff_clouds_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store__colormask___voxel_mesh_.label = "Store 'ColorMask' (voxel mesh)"
    store__colormask___voxel_mesh_.name = "Store 'ColorMask' (voxel mesh)"
    store__colormask___voxel_mesh_.show_options = True
    store__colormask___voxel_mesh_.data_type = 'FLOAT_COLOR'
    store__colormask___voxel_mesh_.domain = 'POINT'
    # Selection
    store__colormask___voxel_mesh_.inputs[1].default_value = True
    # Name
    store__colormask___voxel_mesh_.inputs[2].default_value = "ColorMask"

    # Node Optional Polish: Wind & Surface Detail
    optional_polish__wind___surface_detail = ff_clouds_nodes_1.nodes.new("NodeFrame")
    optional_polish__wind___surface_detail.label = "Optional Polish: Wind & Surface Detail"
    optional_polish__wind___surface_detail.name = "Optional Polish: Wind & Surface Detail"
    optional_polish__wind___surface_detail.use_custom_color = True
    optional_polish__wind___surface_detail.color = (0.3499999940395355, 0.15000000596046448, 0.3499999940395355)
    optional_polish__wind___surface_detail.show_options = True
    optional_polish__wind___surface_detail.label_size = 20
    optional_polish__wind___surface_detail.shrink = True

    # Node Group Input.005
    group_input_005 = ff_clouds_nodes_1.nodes.new("NodeGroupInput")
    group_input_005.label = "Input: Surface Details"
    group_input_005.name = "Group Input.005"
    group_input_005.show_options = True

    # Node Wind Offset
    wind_offset = ff_clouds_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    wind_offset.label = "Wind Offset"
    wind_offset.name = "Wind Offset"
    wind_offset.show_options = True
    # Z
    wind_offset.inputs[2].default_value = 0.0

    # Node Set Position (wind)
    set_position__wind_ = ff_clouds_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position__wind_.label = "Set Position (wind)"
    set_position__wind_.name = "Set Position (wind)"
    set_position__wind_.show_options = True
    # Selection
    set_position__wind_.inputs[1].default_value = True
    # Position
    set_position__wind_.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Normal
    normal = ff_clouds_nodes_1.nodes.new("GeometryNodeInputNormal")
    normal.label = "Normal"
    normal.name = "Normal"
    normal.show_options = True
    normal.legacy_corner_normals = False

    # Node Position
    position = ff_clouds_nodes_1.nodes.new("GeometryNodeInputPosition")
    position.label = "Position"
    position.name = "Position"
    position.show_options = True

    # Node position * detail_scale sep
    position___detail_scale_sep = ff_clouds_nodes_1.nodes.new("ShaderNodeSeparateXYZ")
    position___detail_scale_sep.label = "position * detail_scale sep"
    position___detail_scale_sep.name = "position * detail_scale sep"
    position___detail_scale_sep.show_options = True

    # Node position * detail_scale x
    position___detail_scale_x = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    position___detail_scale_x.label = "position * detail_scale x"
    position___detail_scale_x.name = "position * detail_scale x"
    position___detail_scale_x.show_options = True
    position___detail_scale_x.operation = 'MULTIPLY'
    position___detail_scale_x.use_clamp = False

    # Node position * detail_scale y
    position___detail_scale_y = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    position___detail_scale_y.label = "position * detail_scale y"
    position___detail_scale_y.name = "position * detail_scale y"
    position___detail_scale_y.show_options = True
    position___detail_scale_y.operation = 'MULTIPLY'
    position___detail_scale_y.use_clamp = False

    # Node position * detail_scale z
    position___detail_scale_z = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    position___detail_scale_z.label = "position * detail_scale z"
    position___detail_scale_z.name = "position * detail_scale z"
    position___detail_scale_z.show_options = True
    position___detail_scale_z.operation = 'MULTIPLY'
    position___detail_scale_z.use_clamp = False

    # Node position * detail_scale
    position___detail_scale = ff_clouds_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    position___detail_scale.label = "position * detail_scale"
    position___detail_scale.name = "position * detail_scale"
    position___detail_scale.show_options = True

    # Node Noise Texture
    noise_texture = ff_clouds_nodes_1.nodes.new("ShaderNodeTexNoise")
    noise_texture.label = "Noise Texture"
    noise_texture.name = "Noise Texture"
    noise_texture.show_options = True
    noise_texture.show_texture = True
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    # Scale
    noise_texture.inputs[2].default_value = 1.0
    # Detail
    noise_texture.inputs[3].default_value = 2.0
    # Roughness
    noise_texture.inputs[4].default_value = 0.5
    # Lacunarity
    noise_texture.inputs[5].default_value = 2.0
    # Distortion
    noise_texture.inputs[8].default_value = 0.0

    # Node center noise around 0
    center_noise_around_0 = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    center_noise_around_0.label = "center noise around 0"
    center_noise_around_0.name = "center noise around 0"
    center_noise_around_0.show_options = True
    center_noise_around_0.operation = 'SUBTRACT'
    center_noise_around_0.use_clamp = False
    # Value_001
    center_noise_around_0.inputs[1].default_value = 0.5

    # Node disp_amount
    disp_amount = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    disp_amount.label = "disp_amount"
    disp_amount.name = "disp_amount"
    disp_amount.show_options = True
    disp_amount.operation = 'MULTIPLY'
    disp_amount.use_clamp = False

    # Node displacement vector sep
    displacement_vector_sep = ff_clouds_nodes_1.nodes.new("ShaderNodeSeparateXYZ")
    displacement_vector_sep.label = "displacement vector sep"
    displacement_vector_sep.name = "displacement vector sep"
    displacement_vector_sep.show_options = True

    # Node displacement vector x
    displacement_vector_x = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    displacement_vector_x.label = "displacement vector x"
    displacement_vector_x.name = "displacement vector x"
    displacement_vector_x.show_options = True
    displacement_vector_x.operation = 'MULTIPLY'
    displacement_vector_x.use_clamp = False

    # Node displacement vector y
    displacement_vector_y = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    displacement_vector_y.label = "displacement vector y"
    displacement_vector_y.name = "displacement vector y"
    displacement_vector_y.show_options = True
    displacement_vector_y.operation = 'MULTIPLY'
    displacement_vector_y.use_clamp = False

    # Node displacement vector z
    displacement_vector_z = ff_clouds_nodes_1.nodes.new("ShaderNodeMath")
    displacement_vector_z.label = "displacement vector z"
    displacement_vector_z.name = "displacement vector z"
    displacement_vector_z.show_options = True
    displacement_vector_z.operation = 'MULTIPLY'
    displacement_vector_z.use_clamp = False

    # Node displacement vector
    displacement_vector = ff_clouds_nodes_1.nodes.new("ShaderNodeCombineXYZ")
    displacement_vector.label = "displacement vector"
    displacement_vector.name = "displacement vector"
    displacement_vector.show_options = True

    # Node Set Position (surface detail)
    set_position__surface_detail_ = ff_clouds_nodes_1.nodes.new("GeometryNodeSetPosition")
    set_position__surface_detail_.label = "Set Position (surface detail)"
    set_position__surface_detail_.name = "Set Position (surface detail)"
    set_position__surface_detail_.show_options = True
    # Selection
    set_position__surface_detail_.inputs[1].default_value = True
    # Position
    set_position__surface_detail_.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Stylized Normals & Material
    stylized_normals___material = ff_clouds_nodes_1.nodes.new("NodeFrame")
    stylized_normals___material.label = "Stylized Normals & Material"
    stylized_normals___material.name = "Stylized Normals & Material"
    stylized_normals___material.use_custom_color = True
    stylized_normals___material.color = (0.3499999940395355, 0.15000000596046448, 0.3499999940395355)
    stylized_normals___material.show_options = True
    stylized_normals___material.label_size = 20
    stylized_normals___material.shrink = True

    # Node Group Input.006
    group_input_006 = ff_clouds_nodes_1.nodes.new("NodeGroupInput")
    group_input_006.label = "Input: Detail"
    group_input_006.name = "Group Input.006"
    group_input_006.show_options = True

    # Node Set Shade Smooth
    set_shade_smooth = ff_clouds_nodes_1.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.show_options = True
    set_shade_smooth.domain = 'FACE'
    # Selection
    set_shade_smooth.inputs[1].default_value = True
    # Shade Smooth
    set_shade_smooth.inputs[2].default_value = True

    # Node Blur Attribute
    blur_attribute = ff_clouds_nodes_1.nodes.new("GeometryNodeBlurAttribute")
    blur_attribute.name = "Blur Attribute"
    blur_attribute.show_options = True
    blur_attribute.data_type = 'FLOAT_VECTOR'
    # Weight
    blur_attribute.inputs[2].default_value = 1.0

    # Node Normal.001
    normal_001 = ff_clouds_nodes_1.nodes.new("GeometryNodeInputNormal")
    normal_001.name = "Normal.001"
    normal_001.show_options = True
    normal_001.legacy_corner_normals = False

    # Node Set Mesh Normal
    set_mesh_normal = ff_clouds_nodes_1.nodes.new("GeometryNodeSetMeshNormal")
    set_mesh_normal.name = "Set Mesh Normal"
    set_mesh_normal.show_options = True
    set_mesh_normal.domain = 'POINT'
    set_mesh_normal.mode = 'FREE'

    # Node Normalize Blurred Normal
    normalize_blurred_normal = ff_clouds_nodes_1.nodes.new("ShaderNodeVectorMath")
    normalize_blurred_normal.label = "Normalize Blurred Normal"
    normalize_blurred_normal.name = "Normalize Blurred Normal"
    normalize_blurred_normal.show_options = True
    normalize_blurred_normal.operation = 'NORMALIZE'

    # Node Set Material
    set_material = ff_clouds_nodes_1.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.show_options = True
    # Selection
    set_material.inputs[1].default_value = True

    # Node Reroute
    reroute = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.show_options = True
    reroute.socket_idname = "NodeSocketFloat"
    # Node Group Input.007
    group_input_007 = ff_clouds_nodes_1.nodes.new("NodeGroupInput")
    group_input_007.label = "Input: Counts"
    group_input_007.name = "Group Input.007"
    group_input_007.show_options = True

    # Node Reroute.002
    reroute_002 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.show_options = True
    reroute_002.socket_idname = "NodeSocketInt"
    # Node Reroute.003
    reroute_003 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.show_options = True
    reroute_003.socket_idname = "NodeSocketFloat"
    # Node Reroute.006
    reroute_006 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.show_options = True
    reroute_006.socket_idname = "NodeSocketInt"
    # Node Reroute.007
    reroute_007 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.show_options = True
    reroute_007.socket_idname = "NodeSocketBool"
    # Node Reroute.008
    reroute_008 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.show_options = True
    reroute_008.socket_idname = "NodeSocketBool"
    # Node Reroute.009
    reroute_009 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.show_options = True
    reroute_009.socket_idname = "NodeSocketInt"
    # Node Reroute.010
    reroute_010 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.show_options = True
    reroute_010.socket_idname = "NodeSocketInt"
    # Node Reroute.011
    reroute_011 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"
    reroute_011.show_options = True
    reroute_011.socket_idname = "NodeSocketVector"
    # Node Reroute.013
    reroute_013 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    reroute_013.show_options = True
    reroute_013.socket_idname = "NodeSocketInt"
    # Node Reroute.014
    reroute_014 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_014.name = "Reroute.014"
    reroute_014.show_options = True
    reroute_014.socket_idname = "NodeSocketInt"
    # Node Reroute.001
    reroute_001 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.show_options = True
    reroute_001.socket_idname = "NodeSocketFloat"
    # Node Reroute.015
    reroute_015 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_015.name = "Reroute.015"
    reroute_015.show_options = True
    reroute_015.socket_idname = "NodeSocketFloat"
    # Node Reroute.016
    reroute_016 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_016.name = "Reroute.016"
    reroute_016.show_options = True
    reroute_016.socket_idname = "NodeSocketFloat"
    # Node Reroute.017
    reroute_017 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_017.name = "Reroute.017"
    reroute_017.show_options = True
    reroute_017.socket_idname = "NodeSocketFloat"
    # Node Reroute.018
    reroute_018 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_018.name = "Reroute.018"
    reroute_018.show_options = True
    reroute_018.socket_idname = "NodeSocketFloat"
    # Node Reroute.019
    reroute_019 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_019.name = "Reroute.019"
    reroute_019.show_options = True
    reroute_019.socket_idname = "NodeSocketFloat"
    # Node Reroute.004
    reroute_004 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.show_options = True
    reroute_004.socket_idname = "NodeSocketFloat"
    # Node Reroute.005
    reroute_005 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.show_options = True
    reroute_005.socket_idname = "NodeSocketFloat"
    # Node Reroute.020
    reroute_020 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_020.name = "Reroute.020"
    reroute_020.show_options = True
    reroute_020.socket_idname = "NodeSocketVector"
    # Node Reroute.012
    reroute_012 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    reroute_012.show_options = True
    reroute_012.socket_idname = "NodeSocketGeometry"
    # Node Reroute.021
    reroute_021 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_021.name = "Reroute.021"
    reroute_021.show_options = True
    reroute_021.socket_idname = "NodeSocketGeometry"
    # Node Reroute.022
    reroute_022 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_022.name = "Reroute.022"
    reroute_022.show_options = True
    reroute_022.socket_idname = "NodeSocketVector"
    # Node Reroute.023
    reroute_023 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_023.name = "Reroute.023"
    reroute_023.show_options = True
    reroute_023.socket_idname = "NodeSocketBool"
    # Node Reroute.024
    reroute_024 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_024.name = "Reroute.024"
    reroute_024.show_options = True
    reroute_024.socket_idname = "NodeSocketBool"
    # Node Reroute.025
    reroute_025 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_025.name = "Reroute.025"
    reroute_025.show_options = True
    reroute_025.socket_idname = "NodeSocketGeometry"
    # Node Store 'fractal_id'
    store__fractal_id_ = ff_clouds_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store__fractal_id_.label = "Store 'fractal_id'"
    store__fractal_id_.name = "Store 'fractal_id'"
    store__fractal_id_.show_options = True
    store__fractal_id_.data_type = 'INT'
    store__fractal_id_.domain = 'POINT'
    # Selection
    store__fractal_id_.inputs[1].default_value = True
    # Name
    store__fractal_id_.inputs[2].default_value = "fractal_id"

    # Node Store 'fractal_id' (voxel mesh)
    store__fractal_id___voxel_mesh_ = ff_clouds_nodes_1.nodes.new("GeometryNodeStoreNamedAttribute")
    store__fractal_id___voxel_mesh_.label = "Store 'fractal_id' (voxel mesh)"
    store__fractal_id___voxel_mesh_.name = "Store 'fractal_id' (voxel mesh)"
    store__fractal_id___voxel_mesh_.show_options = True
    store__fractal_id___voxel_mesh_.data_type = 'INT'
    store__fractal_id___voxel_mesh_.domain = 'POINT'
    # Selection
    store__fractal_id___voxel_mesh_.inputs[1].default_value = True
    # Name
    store__fractal_id___voxel_mesh_.inputs[2].default_value = "fractal_id"

    # Node Read 'fractal_id' (points)
    read__fractal_id___points_ = ff_clouds_nodes_1.nodes.new("GeometryNodeInputNamedAttribute")
    read__fractal_id___points_.label = "Read 'fractal_id' (points)"
    read__fractal_id___points_.name = "Read 'fractal_id' (points)"
    read__fractal_id___points_.show_options = True
    read__fractal_id___points_.data_type = 'INT'
    # Name
    read__fractal_id___points_.inputs[0].default_value = "fractal_id"

    # Node Sample Index (fractal_id)
    sample_index__fractal_id_ = ff_clouds_nodes_1.nodes.new("GeometryNodeSampleIndex")
    sample_index__fractal_id_.label = "Sample Index (fractal_id)"
    sample_index__fractal_id_.name = "Sample Index (fractal_id)"
    sample_index__fractal_id_.show_options = True
    sample_index__fractal_id_.clamp = False
    sample_index__fractal_id_.data_type = 'INT'
    sample_index__fractal_id_.domain = 'POINT'

    # Node Reroute.026
    reroute_026 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_026.name = "Reroute.026"
    reroute_026.show_options = True
    reroute_026.socket_idname = "NodeSocketInt"
    # Node Reroute.027
    reroute_027 = ff_clouds_nodes_1.nodes.new("NodeReroute")
    reroute_027.name = "Reroute.027"
    reroute_027.show_options = True
    reroute_027.socket_idname = "NodeSocketInt"
    # Set parents
    ff_clouds_nodes_1.nodes["Group Input"].parent = ff_clouds_nodes_1.nodes["Point Count Math"]
    ff_clouds_nodes_1.nodes["boundary2 (L1+L2)"].parent = ff_clouds_nodes_1.nodes["Point Count Math"]
    ff_clouds_nodes_1.nodes["max_per_cloud (L1+L2+L3)"].parent = ff_clouds_nodes_1.nodes["Point Count Math"]
    ff_clouds_nodes_1.nodes["slot_total"].parent = ff_clouds_nodes_1.nodes["Point Count Math"]
    ff_clouds_nodes_1.nodes["total_points"].parent = ff_clouds_nodes_1.nodes["Point Count Math"]
    ff_clouds_nodes_1.nodes["total_points (int)"].parent = ff_clouds_nodes_1.nodes["Point Count Math"]
    ff_clouds_nodes_1.nodes["Mesh Line"].parent = ff_clouds_nodes_1.nodes["Base Point Cloud"]
    ff_clouds_nodes_1.nodes["Index"].parent = ff_clouds_nodes_1.nodes["Base Point Cloud"]
    ff_clouds_nodes_1.nodes["i / 4"].parent = ff_clouds_nodes_1.nodes["Index Decomposition"]
    ff_clouds_nodes_1.nodes["slot_index"].parent = ff_clouds_nodes_1.nodes["Index Decomposition"]
    ff_clouds_nodes_1.nodes["sub = i mod 4"].parent = ff_clouds_nodes_1.nodes["Index Decomposition"]
    ff_clouds_nodes_1.nodes["slot/maxpc"].parent = ff_clouds_nodes_1.nodes["Index Decomposition"]
    ff_clouds_nodes_1.nodes["cloud_index"].parent = ff_clouds_nodes_1.nodes["Index Decomposition"]
    ff_clouds_nodes_1.nodes["local_index"].parent = ff_clouds_nodes_1.nodes["Index Decomposition"]
    ff_clouds_nodes_1.nodes["cloud_index (int)"].parent = ff_clouds_nodes_1.nodes["Index Decomposition"]
    ff_clouds_nodes_1.nodes["slot_index (int)"].parent = ff_clouds_nodes_1.nodes["Index Decomposition"]
    ff_clouds_nodes_1.nodes["is_L1"].parent = ff_clouds_nodes_1.nodes["Layer Membership"]
    ff_clouds_nodes_1.nodes[">= boundary1"].parent = ff_clouds_nodes_1.nodes["Layer Membership"]
    ff_clouds_nodes_1.nodes["< boundary2"].parent = ff_clouds_nodes_1.nodes["Layer Membership"]
    ff_clouds_nodes_1.nodes["is_L2"].parent = ff_clouds_nodes_1.nodes["Layer Membership"]
    ff_clouds_nodes_1.nodes["Group Input.001"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["probability: L2 or L3"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["probability: select layer"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["radius: L2 or L3"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["radius: select layer"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["height: L2 or L3"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["height: select layer"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["min_size: L2 or L3"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["min_size: select layer"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["max_size: L2 or L3"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["max_size: select layer"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["squash_prob: L2 or L3"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["squash_prob: select layer"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["max_squash: L2 or L3"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["max_squash: select layer"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["presence_seed: L2 or L3"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["presence_seed: select layer"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["layer_present?"].parent = ff_clouds_nodes_1.nodes["Layer Presence Check"]
    ff_clouds_nodes_1.nodes["NOT layer_present"].parent = ff_clouds_nodes_1.nodes["Layer Presence Check"]
    ff_clouds_nodes_1.nodes["Group Input.002"].parent = ff_clouds_nodes_1.nodes["Cloud Centers"]
    ff_clouds_nodes_1.nodes["FieldX/2"].parent = ff_clouds_nodes_1.nodes["Cloud Centers"]
    ff_clouds_nodes_1.nodes["-FieldX/2"].parent = ff_clouds_nodes_1.nodes["Cloud Centers"]
    ff_clouds_nodes_1.nodes["FieldY/2"].parent = ff_clouds_nodes_1.nodes["Cloud Centers"]
    ff_clouds_nodes_1.nodes["-FieldY/2"].parent = ff_clouds_nodes_1.nodes["Cloud Centers"]
    ff_clouds_nodes_1.nodes["HeightScatter/2"].parent = ff_clouds_nodes_1.nodes["Cloud Centers"]
    ff_clouds_nodes_1.nodes["-HeightScatter/2"].parent = ff_clouds_nodes_1.nodes["Cloud Centers"]
    ff_clouds_nodes_1.nodes["Cloud Center X"].parent = ff_clouds_nodes_1.nodes["Cloud Centers"]
    ff_clouds_nodes_1.nodes["Cloud Center Y"].parent = ff_clouds_nodes_1.nodes["Cloud Centers"]
    ff_clouds_nodes_1.nodes["Cloud Center Z"].parent = ff_clouds_nodes_1.nodes["Cloud Centers"]
    ff_clouds_nodes_1.nodes["Cloud Center"].parent = ff_clouds_nodes_1.nodes["Cloud Centers"]
    ff_clouds_nodes_1.nodes["Group Input.003"].parent = ff_clouds_nodes_1.nodes["Cloud Color Seed"]
    ff_clouds_nodes_1.nodes["Cloud Color To Seed"].parent = ff_clouds_nodes_1.nodes["Cloud Color Seed"]
    ff_clouds_nodes_1.nodes["Cloud Random Color"].parent = ff_clouds_nodes_1.nodes["Cloud Color Seed"]
    ff_clouds_nodes_1.nodes["Angle"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["Radius Frac"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["sqrt(frac)"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["local_radius"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["cos(angle)"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["sin(angle)"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["x_local"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["y_local"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["jag_amount"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["-jag_amount"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["jag_z"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["-jag_z"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["jag min vec"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["jag max vec"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["Jagged Offset"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["Base Sphere Radius"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["Squash Check"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["Squash Amount (raw)"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["Squash Amount"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["shrink"].parent = ff_clouds_nodes_1.nodes["Squash Logic"]
    ff_clouds_nodes_1.nodes["1 - shrink"].parent = ff_clouds_nodes_1.nodes["Squash Logic"]
    ff_clouds_nodes_1.nodes["Sub-sphere Radius"].parent = ff_clouds_nodes_1.nodes["Squash Logic"]
    ff_clouds_nodes_1.nodes["squash*base_radius"].parent = ff_clouds_nodes_1.nodes["Squash Logic"]
    ff_clouds_nodes_1.nodes["Spread Distance"].parent = ff_clouds_nodes_1.nodes["Squash Logic"]
    ff_clouds_nodes_1.nodes["sub == 0"].parent = ff_clouds_nodes_1.nodes["Squash Logic"]
    ff_clouds_nodes_1.nodes["sub == 1"].parent = ff_clouds_nodes_1.nodes["Squash Logic"]
    ff_clouds_nodes_1.nodes["sub == 2"].parent = ff_clouds_nodes_1.nodes["Squash Logic"]
    ff_clouds_nodes_1.nodes["dir: +Y / -Y"].parent = ff_clouds_nodes_1.nodes["Squash Logic"]
    ff_clouds_nodes_1.nodes["dir: -X / (+-Y)"].parent = ff_clouds_nodes_1.nodes["Squash Logic"]
    ff_clouds_nodes_1.nodes["dir: +X"].parent = ff_clouds_nodes_1.nodes["Squash Logic"]
    ff_clouds_nodes_1.nodes["Sub Offset sep"].parent = ff_clouds_nodes_1.nodes["Squash Logic"]
    ff_clouds_nodes_1.nodes["Sub Offset x"].parent = ff_clouds_nodes_1.nodes["Squash Logic"]
    ff_clouds_nodes_1.nodes["Sub Offset y"].parent = ff_clouds_nodes_1.nodes["Squash Logic"]
    ff_clouds_nodes_1.nodes["Sub Offset z"].parent = ff_clouds_nodes_1.nodes["Squash Logic"]
    ff_clouds_nodes_1.nodes["Sub Offset"].parent = ff_clouds_nodes_1.nodes["Squash Logic"]
    ff_clouds_nodes_1.nodes["Local XY"].parent = ff_clouds_nodes_1.nodes["Position Assembly"]
    ff_clouds_nodes_1.nodes["+ jagged offset"].parent = ff_clouds_nodes_1.nodes["Position Assembly"]
    ff_clouds_nodes_1.nodes["+ squash sub-offset"].parent = ff_clouds_nodes_1.nodes["Position Assembly"]
    ff_clouds_nodes_1.nodes["Layer Height Vec"].parent = ff_clouds_nodes_1.nodes["Position Assembly"]
    ff_clouds_nodes_1.nodes["cloud_center + layer_height"].parent = ff_clouds_nodes_1.nodes["Position Assembly"]
    ff_clouds_nodes_1.nodes["FINAL POSITION"].parent = ff_clouds_nodes_1.nodes["Position Assembly"]
    ff_clouds_nodes_1.nodes["Set Position"].parent = ff_clouds_nodes_1.nodes["Filter & Bake"]
    ff_clouds_nodes_1.nodes["Store 'sphere_radius'"].parent = ff_clouds_nodes_1.nodes["Filter & Bake"]
    ff_clouds_nodes_1.nodes["Store 'ColorMask'"].parent = ff_clouds_nodes_1.nodes["Filter & Bake"]
    ff_clouds_nodes_1.nodes["Delete absent points"].parent = ff_clouds_nodes_1.nodes["Filter & Bake"]
    ff_clouds_nodes_1.nodes["Group Input.004"].parent = ff_clouds_nodes_1.nodes["Mesh Conversion"]
    ff_clouds_nodes_1.nodes["Read back 'sphere_radius'"].parent = ff_clouds_nodes_1.nodes["Mesh Conversion"]
    ff_clouds_nodes_1.nodes["Points to Volume"].parent = ff_clouds_nodes_1.nodes["Mesh Conversion"]
    ff_clouds_nodes_1.nodes["Volume to Mesh"].parent = ff_clouds_nodes_1.nodes["Mesh Conversion"]
    ff_clouds_nodes_1.nodes["Position (voxel mesh)"].parent = ff_clouds_nodes_1.nodes["Cloud Color Transfer"]
    ff_clouds_nodes_1.nodes["Sample Nearest (cloud point)"].parent = ff_clouds_nodes_1.nodes["Cloud Color Transfer"]
    ff_clouds_nodes_1.nodes["Read 'ColorMask' (points)"].parent = ff_clouds_nodes_1.nodes["Cloud Color Transfer"]
    ff_clouds_nodes_1.nodes["Sample Index (ColorMask)"].parent = ff_clouds_nodes_1.nodes["Cloud Color Transfer"]
    ff_clouds_nodes_1.nodes["Store 'ColorMask' (voxel mesh)"].parent = ff_clouds_nodes_1.nodes["Cloud Color Transfer"]
    ff_clouds_nodes_1.nodes["Group Input.005"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["Wind Offset"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["Set Position (wind)"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["Normal"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["Position"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["position * detail_scale sep"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["position * detail_scale x"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["position * detail_scale y"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["position * detail_scale z"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["position * detail_scale"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["Noise Texture"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["center noise around 0"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["disp_amount"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["displacement vector sep"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["displacement vector x"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["displacement vector y"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["displacement vector z"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["displacement vector"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["Set Position (surface detail)"].parent = ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"]
    ff_clouds_nodes_1.nodes["Group Input.006"].parent = ff_clouds_nodes_1.nodes["Stylized Normals & Material"]
    ff_clouds_nodes_1.nodes["Set Shade Smooth"].parent = ff_clouds_nodes_1.nodes["Stylized Normals & Material"]
    ff_clouds_nodes_1.nodes["Blur Attribute"].parent = ff_clouds_nodes_1.nodes["Stylized Normals & Material"]
    ff_clouds_nodes_1.nodes["Normal.001"].parent = ff_clouds_nodes_1.nodes["Stylized Normals & Material"]
    ff_clouds_nodes_1.nodes["Set Mesh Normal"].parent = ff_clouds_nodes_1.nodes["Stylized Normals & Material"]
    ff_clouds_nodes_1.nodes["Normalize Blurred Normal"].parent = ff_clouds_nodes_1.nodes["Stylized Normals & Material"]
    ff_clouds_nodes_1.nodes["Set Material"].parent = ff_clouds_nodes_1.nodes["Stylized Normals & Material"]
    ff_clouds_nodes_1.nodes["Reroute"].parent = ff_clouds_nodes_1.nodes["Index Decomposition"]
    ff_clouds_nodes_1.nodes["Group Input.007"].parent = ff_clouds_nodes_1.nodes["Index Decomposition"]
    ff_clouds_nodes_1.nodes["Reroute.002"].parent = ff_clouds_nodes_1.nodes["Layer Membership"]
    ff_clouds_nodes_1.nodes["Reroute.003"].parent = ff_clouds_nodes_1.nodes["Index Decomposition"]
    ff_clouds_nodes_1.nodes["Reroute.006"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["Reroute.007"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["Reroute.008"].parent = ff_clouds_nodes_1.nodes["Layer Membership"]
    ff_clouds_nodes_1.nodes["Reroute.009"].parent = ff_clouds_nodes_1.nodes["Cloud Centers"]
    ff_clouds_nodes_1.nodes["Reroute.011"].parent = ff_clouds_nodes_1.nodes["Cloud Color Seed"]
    ff_clouds_nodes_1.nodes["Reroute.013"].parent = ff_clouds_nodes_1.nodes["Layer Parameter Switching"]
    ff_clouds_nodes_1.nodes["Reroute.014"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["Reroute.001"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["Reroute.015"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["Reroute.016"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["Reroute.017"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["Reroute.018"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["Reroute.005"].parent = ff_clouds_nodes_1.nodes["Per-Sphere Randomization"]
    ff_clouds_nodes_1.nodes["Reroute.025"].parent = ff_clouds_nodes_1.nodes["Mesh Conversion"]
    ff_clouds_nodes_1.nodes["Store 'fractal_id'"].parent = ff_clouds_nodes_1.nodes["Filter & Bake"]
    ff_clouds_nodes_1.nodes["Store 'fractal_id' (voxel mesh)"].parent = ff_clouds_nodes_1.nodes["Cloud Color Transfer"]
    ff_clouds_nodes_1.nodes["Read 'fractal_id' (points)"].parent = ff_clouds_nodes_1.nodes["Cloud Color Transfer"]
    ff_clouds_nodes_1.nodes["Sample Index (fractal_id)"].parent = ff_clouds_nodes_1.nodes["Cloud Color Transfer"]

    # Set locations
    ff_clouds_nodes_1.nodes["Group Output"].location = (10884.837890625, 143.37867736816406)
    ff_clouds_nodes_1.nodes["Point Count Math"].location = (-2195.0, 588.0)
    ff_clouds_nodes_1.nodes["Group Input"].location = (29.779052734375, -187.21377563476562)
    ff_clouds_nodes_1.nodes["boundary2 (L1+L2)"].location = (200.5838623046875, -398.5798034667969)
    ff_clouds_nodes_1.nodes["max_per_cloud (L1+L2+L3)"].location = (370.3321533203125, -518.1026611328125)
    ff_clouds_nodes_1.nodes["slot_total"].location = (524.8262939453125, -159.76351928710938)
    ff_clouds_nodes_1.nodes["total_points"].location = (678.3646240234375, -84.56228637695312)
    ff_clouds_nodes_1.nodes["total_points (int)"].location = (837.7017822265625, -36.0733642578125)
    ff_clouds_nodes_1.nodes["Base Point Cloud"].location = (-1180.0, 637.0)
    ff_clouds_nodes_1.nodes["Mesh Line"].location = (30.0, -36.0587158203125)
    ff_clouds_nodes_1.nodes["Index"].location = (210.67645263671875, -151.93927001953125)
    ff_clouds_nodes_1.nodes["Index Decomposition"].location = (-741.0, 905.0)
    ff_clouds_nodes_1.nodes["i / 4"].location = (41.0, -305.0)
    ff_clouds_nodes_1.nodes["slot_index"].location = (198.5516357421875, -231.2554931640625)
    ff_clouds_nodes_1.nodes["sub = i mod 4"].location = (30.29913330078125, -462.7174377441406)
    ff_clouds_nodes_1.nodes["slot/maxpc"].location = (364.40478515625, -156.23248291015625)
    ff_clouds_nodes_1.nodes["cloud_index"].location = (522.5402221679688, -82.856689453125)
    ff_clouds_nodes_1.nodes["local_index"].location = (360.94610595703125, -311.673583984375)
    ff_clouds_nodes_1.nodes["cloud_index (int)"].location = (681.23583984375, -36.105224609375)
    ff_clouds_nodes_1.nodes["slot_index (int)"].location = (356.0793762207031, -554.0445556640625)
    ff_clouds_nodes_1.nodes["Layer Membership"].location = (123.0, 704.0)
    ff_clouds_nodes_1.nodes["is_L1"].location = (30.264785766601562, -36.3814697265625)
    ff_clouds_nodes_1.nodes[">= boundary1"].location = (30.55853271484375, -213.7806396484375)
    ff_clouds_nodes_1.nodes["< boundary2"].location = (29.541183471679688, -387.53924560546875)
    ff_clouds_nodes_1.nodes["is_L2"].location = (196.3770751953125, -284.3238220214844)
    ff_clouds_nodes_1.nodes["Layer Parameter Switching"].location = (514.0, 757.0)
    ff_clouds_nodes_1.nodes["Group Input.001"].location = (29.62249755859375, -825.7207641601562)
    ff_clouds_nodes_1.nodes["probability: L2 or L3"].location = (325.30755615234375, -294.7426452636719)
    ff_clouds_nodes_1.nodes["probability: select layer"].location = (699.6602783203125, -35.97100830078125)
    ff_clouds_nodes_1.nodes["radius: L2 or L3"].location = (465.1204833984375, -656.592529296875)
    ff_clouds_nodes_1.nodes["radius: select layer"].location = (923.0020751953125, -576.8564453125)
    ff_clouds_nodes_1.nodes["height: L2 or L3"].location = (465.77899169921875, -804.53125)
    ff_clouds_nodes_1.nodes["height: select layer"].location = (920.7674560546875, -725.482666015625)
    ff_clouds_nodes_1.nodes["min_size: L2 or L3"].location = (466.56207275390625, -951.9533081054688)
    ff_clouds_nodes_1.nodes["min_size: select layer"].location = (919.2777099609375, -874.10888671875)
    ff_clouds_nodes_1.nodes["max_size: L2 or L3"].location = (465.8687744140625, -1099.679931640625)
    ff_clouds_nodes_1.nodes["max_size: select layer"].location = (916.7080078125, -1023.1821899414062)
    ff_clouds_nodes_1.nodes["squash_prob: L2 or L3"].location = (467.143798828125, -1246.08056640625)
    ff_clouds_nodes_1.nodes["squash_prob: select layer"].location = (914.9761962890625, -1173.24267578125)
    ff_clouds_nodes_1.nodes["max_squash: L2 or L3"].location = (465.67315673828125, -1393.704345703125)
    ff_clouds_nodes_1.nodes["max_squash: select layer"].location = (915.8338623046875, -1317.9599609375)
    ff_clouds_nodes_1.nodes["presence_seed: L2 or L3"].location = (466.51025390625, -1540.896484375)
    ff_clouds_nodes_1.nodes["presence_seed: select layer"].location = (912.66650390625, -1467.617431640625)
    ff_clouds_nodes_1.nodes["Layer Presence Check"].location = (1627.0, 980.0)
    ff_clouds_nodes_1.nodes["layer_present?"].location = (30.3759765625, -35.7960205078125)
    ff_clouds_nodes_1.nodes["NOT layer_present"].location = (30.3759765625, -186.7381591796875)
    ff_clouds_nodes_1.nodes["Cloud Centers"].location = (267.0, 2311.0)
    ff_clouds_nodes_1.nodes["Group Input.002"].location = (29.90545654296875, -110.158935546875)
    ff_clouds_nodes_1.nodes["FieldX/2"].location = (300.07965087890625, -36.413818359375)
    ff_clouds_nodes_1.nodes["-FieldX/2"].location = (300.71697998046875, -189.36376953125)
    ff_clouds_nodes_1.nodes["FieldY/2"].location = (300.07965087890625, -340.6402587890625)
    ff_clouds_nodes_1.nodes["-FieldY/2"].location = (299.4901123046875, -493.04833984375)
    ff_clouds_nodes_1.nodes["HeightScatter/2"].location = (298.900634765625, -647.2254638671875)
    ff_clouds_nodes_1.nodes["-HeightScatter/2"].location = (297.63311767578125, -798.7490234375)
    ff_clouds_nodes_1.nodes["Cloud Center X"].location = (520.0391235351562, -776.551513671875)
    ff_clouds_nodes_1.nodes["Cloud Center Y"].location = (520.0796508789062, -946.413818359375)
    ff_clouds_nodes_1.nodes["Cloud Center Z"].location = (517.4680786132812, -1115.5989990234375)
    ff_clouds_nodes_1.nodes["Cloud Center"].location = (688.4891357421875, -898.5478515625)
    ff_clouds_nodes_1.nodes["Cloud Color Seed"].location = (1138.0, 2049.0)
    ff_clouds_nodes_1.nodes["Group Input.003"].location = (30.1712646484375, -35.973388671875)
    ff_clouds_nodes_1.nodes["Cloud Color To Seed"].location = (211.5936279296875, -779.54296875)
    ff_clouds_nodes_1.nodes["Cloud Random Color"].location = (467.219970703125, -701.77001953125)
    ff_clouds_nodes_1.nodes["Per-Sphere Randomization"].location = (1844.0, 826.0)
    ff_clouds_nodes_1.nodes["Angle"].location = (31.70556640625, -357.8460693359375)
    ff_clouds_nodes_1.nodes["Radius Frac"].location = (30.348876953125, -185.04638671875)
    ff_clouds_nodes_1.nodes["sqrt(frac)"].location = (252.16455078125, -111.487060546875)
    ff_clouds_nodes_1.nodes["local_radius"].location = (443.454833984375, -35.8922119140625)
    ff_clouds_nodes_1.nodes["cos(angle)"].location = (243.0029296875, -282.8994140625)
    ff_clouds_nodes_1.nodes["sin(angle)"].location = (239.997802734375, -415.90533447265625)
    ff_clouds_nodes_1.nodes["x_local"].location = (657.9599609375, -223.101806640625)
    ff_clouds_nodes_1.nodes["y_local"].location = (657.189697265625, -374.9137878417969)
    ff_clouds_nodes_1.nodes["jag_amount"].location = (29.6414794921875, -562.846435546875)
    ff_clouds_nodes_1.nodes["-jag_amount"].location = (240.9814453125, -546.5386352539062)
    ff_clouds_nodes_1.nodes["jag_z"].location = (239.0830078125, -695.52880859375)
    ff_clouds_nodes_1.nodes["-jag_z"].location = (440.3203125, -624.233154296875)
    ff_clouds_nodes_1.nodes["jag min vec"].location = (656.353515625, -527.0975341796875)
    ff_clouds_nodes_1.nodes["jag max vec"].location = (438.892333984375, -776.820556640625)
    ff_clouds_nodes_1.nodes["Jagged Offset"].location = (881.410888671875, -1500.25390625)
    ff_clouds_nodes_1.nodes["Base Sphere Radius"].location = (440.550537109375, -891.012451171875)
    ff_clouds_nodes_1.nodes["Squash Check"].location = (882.518310546875, -1671.748046875)
    ff_clouds_nodes_1.nodes["Squash Amount (raw)"].location = (879.794921875, -1822.3623046875)
    ff_clouds_nodes_1.nodes["Squash Amount"].location = (1057.994873046875, -1677.337890625)
    ff_clouds_nodes_1.nodes["Squash Logic"].location = (3105.0, -549.0)
    ff_clouds_nodes_1.nodes["shrink"].location = (33.269775390625, -228.536865234375)
    ff_clouds_nodes_1.nodes["1 - shrink"].location = (191.609130859375, -131.70379638671875)
    ff_clouds_nodes_1.nodes["Sub-sphere Radius"].location = (353.917236328125, -36.28424072265625)
    ff_clouds_nodes_1.nodes["squash*base_radius"].location = (30.28125, -385.56463623046875)
    ff_clouds_nodes_1.nodes["Spread Distance"].location = (502.953857421875, -312.90155029296875)
    ff_clouds_nodes_1.nodes["sub == 0"].location = (31.693359375, -539.4730224609375)
    ff_clouds_nodes_1.nodes["sub == 1"].location = (29.849609375, -714.6551513671875)
    ff_clouds_nodes_1.nodes["sub == 2"].location = (31.826904296875, -889.977294921875)
    ff_clouds_nodes_1.nodes["dir: +Y / -Y"].location = (186.71923828125, -840.615478515625)
    ff_clouds_nodes_1.nodes["dir: -X / (+-Y)"].location = (341.06494140625, -666.222412109375)
    ff_clouds_nodes_1.nodes["dir: +X"].location = (492.079833984375, -492.265625)
    ff_clouds_nodes_1.nodes["Sub Offset sep"].location = (648.912353515625, -423.022216796875)
    ff_clouds_nodes_1.nodes["Sub Offset x"].location = (957.8486328125, -54.72723388671875)
    ff_clouds_nodes_1.nodes["Sub Offset y"].location = (957.6240234375, -208.24847412109375)
    ff_clouds_nodes_1.nodes["Sub Offset z"].location = (956.9697265625, -362.36712646484375)
    ff_clouds_nodes_1.nodes["Sub Offset"].location = (1120.84619140625, -159.912109375)
    ff_clouds_nodes_1.nodes["Position Assembly"].location = (4375.0, 844.0)
    ff_clouds_nodes_1.nodes["Local XY"].location = (29.9677734375, -202.7379150390625)
    ff_clouds_nodes_1.nodes["+ jagged offset"].location = (181.53076171875, -153.4561767578125)
    ff_clouds_nodes_1.nodes["+ squash sub-offset"].location = (339.71142578125, -105.00537109375)
    ff_clouds_nodes_1.nodes["Layer Height Vec"].location = (149.6943359375, -1165.0523681640625)
    ff_clouds_nodes_1.nodes["cloud_center + layer_height"].location = (324.41162109375, -1092.946044921875)
    ff_clouds_nodes_1.nodes["FINAL POSITION"].location = (504.02294921875, -35.66845703125)
    ff_clouds_nodes_1.nodes["Filter & Bake"].location = (5127.0, -230.0)
    ff_clouds_nodes_1.nodes["Set Position"].location = (35.046875, -35.508209228515625)
    ff_clouds_nodes_1.nodes["Store 'sphere_radius'"].location = (34.18408203125, -217.13494873046875)
    ff_clouds_nodes_1.nodes["Store 'ColorMask'"].location = (32.67333984375, -391.9102783203125)
    ff_clouds_nodes_1.nodes["Delete absent points"].location = (30.41650390625, -739.637939453125)
    ff_clouds_nodes_1.nodes["Mesh Conversion"].location = (5348.0, 76.0)
    ff_clouds_nodes_1.nodes["Group Input.004"].location = (29.9892578125, -35.53878402709961)
    ff_clouds_nodes_1.nodes["Read back 'sphere_radius'"].location = (299.83642578125, -986.9908447265625)
    ff_clouds_nodes_1.nodes["Points to Volume"].location = (295.26123046875, -812.171630859375)
    ff_clouds_nodes_1.nodes["Volume to Mesh"].location = (585.8798828125, -76.04888916015625)
    ff_clouds_nodes_1.nodes["Cloud Color Transfer"].location = (6150.0, 86.0)
    ff_clouds_nodes_1.nodes["Position (voxel mesh)"].location = (30.46875, -465.01129150390625)
    ff_clouds_nodes_1.nodes["Sample Nearest (cloud point)"].location = (32.49853515625, -330.19854736328125)
    ff_clouds_nodes_1.nodes["Read 'ColorMask' (points)"].location = (34.4990234375, -198.86767578125)
    ff_clouds_nodes_1.nodes["Sample Index (ColorMask)"].location = (464.99072265625, -179.6787109375)
    ff_clouds_nodes_1.nodes["Store 'ColorMask' (voxel mesh)"].location = (648.32275390625, -35.98221969604492)
    ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"].location = (7161.0, 171.0)
    ff_clouds_nodes_1.nodes["Group Input.005"].location = (30.25830078125, -350.7565612792969)
    ff_clouds_nodes_1.nodes["Wind Offset"].location = (249.0361328125, -233.33450317382812)
    ff_clouds_nodes_1.nodes["Set Position (wind)"].location = (789.45849609375, -167.82150268554688)
    ff_clouds_nodes_1.nodes["Normal"].location = (1208.5498046875, -464.1315002441406)
    ff_clouds_nodes_1.nodes["Position"].location = (192.42626953125, -999.03955078125)
    ff_clouds_nodes_1.nodes["position * detail_scale sep"].location = (192.537109375, -866.6400146484375)
    ff_clouds_nodes_1.nodes["position * detail_scale x"].location = (427.30322265625, -524.736083984375)
    ff_clouds_nodes_1.nodes["position * detail_scale y"].location = (423.91162109375, -681.8775634765625)
    ff_clouds_nodes_1.nodes["position * detail_scale z"].location = (421.88427734375, -838.1558837890625)
    ff_clouds_nodes_1.nodes["position * detail_scale"].location = (715.16357421875, -501.2254333496094)
    ff_clouds_nodes_1.nodes["Noise Texture"].location = (874.25732421875, -379.7225646972656)
    ff_clouds_nodes_1.nodes["center noise around 0"].location = (1036.4677734375, -305.8274841308594)
    ff_clouds_nodes_1.nodes["disp_amount"].location = (1205.529296875, -159.49429321289062)
    ff_clouds_nodes_1.nodes["displacement vector sep"].location = (1205.88671875, -335.2701110839844)
    ff_clouds_nodes_1.nodes["displacement vector x"].location = (1508.7587890625, -125.6333999633789)
    ff_clouds_nodes_1.nodes["displacement vector y"].location = (1509.69140625, -285.0372619628906)
    ff_clouds_nodes_1.nodes["displacement vector z"].location = (1512.0302734375, -444.0838317871094)
    ff_clouds_nodes_1.nodes["displacement vector"].location = (1674.880859375, -100.9164810180664)
    ff_clouds_nodes_1.nodes["Set Position (surface detail)"].location = (2202.7333984375, -36.240936279296875)
    ff_clouds_nodes_1.nodes["Stylized Normals & Material"].location = (9559.0, 229.0)
    ff_clouds_nodes_1.nodes["Group Input.006"].location = (29.943359375, -318.8521728515625)
    ff_clouds_nodes_1.nodes["Set Shade Smooth"].location = (728.4873046875, -60.36370849609375)
    ff_clouds_nodes_1.nodes["Blur Attribute"].location = (199.3349609375, -210.81069946289062)
    ff_clouds_nodes_1.nodes["Normal.001"].location = (29.763671875, -237.1221923828125)
    ff_clouds_nodes_1.nodes["Set Mesh Normal"].location = (942.6015625, -35.59564208984375)
    ff_clouds_nodes_1.nodes["Normalize Blurred Normal"].location = (359.1064453125, -186.84075927734375)
    ff_clouds_nodes_1.nodes["Set Material"].location = (1121.2626953125, -85.612548828125)
    ff_clouds_nodes_1.nodes["Reroute"].location = (289.3636169433594, -860.4835815429688)
    ff_clouds_nodes_1.nodes["Group Input.007"].location = (365.86328125, -748.77978515625)
    ff_clouds_nodes_1.nodes["Reroute.002"].location = (45.100799560546875, -197.0718994140625)
    ff_clouds_nodes_1.nodes["Reroute.003"].location = (496.9218444824219, -493.8816833496094)
    ff_clouds_nodes_1.nodes["Reroute.006"].location = (49.74249267578125, -1721.9044189453125)
    ff_clouds_nodes_1.nodes["Reroute.007"].location = (708.032470703125, -205.16900634765625)
    ff_clouds_nodes_1.nodes["Reroute.008"].location = (226.35406494140625, -157.46197509765625)
    ff_clouds_nodes_1.nodes["Reroute.009"].location = (418.52899169921875, -1074.485595703125)
    ff_clouds_nodes_1.nodes["Reroute.010"].location = (1019.670654296875, 836.3847045898438)
    ff_clouds_nodes_1.nodes["Reroute.011"].location = (41.0478515625, -1015.687744140625)
    ff_clouds_nodes_1.nodes["Reroute.013"].location = (1057.13427734375, -247.39932250976562)
    ff_clouds_nodes_1.nodes["Reroute.014"].location = (341.367919921875, -1779.8916015625)
    ff_clouds_nodes_1.nodes["Reroute.001"].location = (247.70703125, -861.9248046875)
    ff_clouds_nodes_1.nodes["Reroute.015"].location = (370.85302734375, -860.8053588867188)
    ff_clouds_nodes_1.nodes["Reroute.016"].location = (42.3419189453125, -172.326416015625)
    ff_clouds_nodes_1.nodes["Reroute.017"].location = (75.5384521484375, -1922.0093994140625)
    ff_clouds_nodes_1.nodes["Reroute.018"].location = (78.4681396484375, -1760.399658203125)
    ff_clouds_nodes_1.nodes["Reroute.019"].location = (101.93711853027344, -1381.7894287109375)
    ff_clouds_nodes_1.nodes["Reroute.004"].location = (3060.4111328125, -1373.1688232421875)
    ff_clouds_nodes_1.nodes["Reroute.005"].location = (69.826416015625, -1281.693359375)
    ff_clouds_nodes_1.nodes["Reroute.020"].location = (4057.68408203125, 1068.1187744140625)
    ff_clouds_nodes_1.nodes["Reroute.012"].location = (174.05758666992188, 2337.11328125)
    ff_clouds_nodes_1.nodes["Reroute.021"].location = (5030.4404296875, 2349.65234375)
    ff_clouds_nodes_1.nodes["Reroute.022"].location = (4983.06201171875, 1338.077392578125)
    ff_clouds_nodes_1.nodes["Reroute.023"].location = (1911.5643310546875, -1750.31884765625)
    ff_clouds_nodes_1.nodes["Reroute.024"].location = (4902.88232421875, -1721.673828125)
    ff_clouds_nodes_1.nodes["Reroute.025"].location = (644.1357421875, -1126.103271484375)
    ff_clouds_nodes_1.nodes["Store 'fractal_id'"].location = (31.4443359375, -566.4378051757812)
    ff_clouds_nodes_1.nodes["Store 'fractal_id' (voxel mesh)"].location = (824.39208984375, -36.700679779052734)
    ff_clouds_nodes_1.nodes["Read 'fractal_id' (points)"].location = (639.080078125, -541.6144409179688)
    ff_clouds_nodes_1.nodes["Sample Index (fractal_id)"].location = (642.02197265625, -338.21978759765625)
    ff_clouds_nodes_1.nodes["Reroute.026"].location = (1636.789306640625, 989.6063842773438)
    ff_clouds_nodes_1.nodes["Reroute.027"].location = (5000.40771484375, 1009.5285034179688)

    # Set dimensions
    ff_clouds_nodes_1.nodes["Group Output"].width  = 140.0
    ff_clouds_nodes_1.nodes["Group Output"].height = 100.0

    ff_clouds_nodes_1.nodes["Point Count Math"].width  = 1008.0
    ff_clouds_nodes_1.nodes["Point Count Math"].height = 1081.0

    ff_clouds_nodes_1.nodes["Group Input"].width  = 140.0
    ff_clouds_nodes_1.nodes["Group Input"].height = 100.0

    ff_clouds_nodes_1.nodes["boundary2 (L1+L2)"].width  = 140.0
    ff_clouds_nodes_1.nodes["boundary2 (L1+L2)"].height = 100.0

    ff_clouds_nodes_1.nodes["max_per_cloud (L1+L2+L3)"].width  = 140.0
    ff_clouds_nodes_1.nodes["max_per_cloud (L1+L2+L3)"].height = 100.0

    ff_clouds_nodes_1.nodes["slot_total"].width  = 140.0
    ff_clouds_nodes_1.nodes["slot_total"].height = 100.0

    ff_clouds_nodes_1.nodes["total_points"].width  = 140.0
    ff_clouds_nodes_1.nodes["total_points"].height = 100.0

    ff_clouds_nodes_1.nodes["total_points (int)"].width  = 140.0
    ff_clouds_nodes_1.nodes["total_points (int)"].height = 100.0

    ff_clouds_nodes_1.nodes["Base Point Cloud"].width  = 381.0
    ff_clouds_nodes_1.nodes["Base Point Cloud"].height = 333.0

    ff_clouds_nodes_1.nodes["Mesh Line"].width  = 140.0
    ff_clouds_nodes_1.nodes["Mesh Line"].height = 100.0

    ff_clouds_nodes_1.nodes["Index"].width  = 140.0
    ff_clouds_nodes_1.nodes["Index"].height = 100.0

    ff_clouds_nodes_1.nodes["Index Decomposition"].width  = 851.0
    ff_clouds_nodes_1.nodes["Index Decomposition"].height = 1643.0

    ff_clouds_nodes_1.nodes["i / 4"].width  = 140.0
    ff_clouds_nodes_1.nodes["i / 4"].height = 100.0

    ff_clouds_nodes_1.nodes["slot_index"].width  = 140.0
    ff_clouds_nodes_1.nodes["slot_index"].height = 100.0

    ff_clouds_nodes_1.nodes["sub = i mod 4"].width  = 140.0
    ff_clouds_nodes_1.nodes["sub = i mod 4"].height = 100.0

    ff_clouds_nodes_1.nodes["slot/maxpc"].width  = 140.0
    ff_clouds_nodes_1.nodes["slot/maxpc"].height = 100.0

    ff_clouds_nodes_1.nodes["cloud_index"].width  = 140.0
    ff_clouds_nodes_1.nodes["cloud_index"].height = 100.0

    ff_clouds_nodes_1.nodes["local_index"].width  = 140.0
    ff_clouds_nodes_1.nodes["local_index"].height = 100.0

    ff_clouds_nodes_1.nodes["cloud_index (int)"].width  = 140.0
    ff_clouds_nodes_1.nodes["cloud_index (int)"].height = 100.0

    ff_clouds_nodes_1.nodes["slot_index (int)"].width  = 140.0
    ff_clouds_nodes_1.nodes["slot_index (int)"].height = 100.0

    ff_clouds_nodes_1.nodes["Layer Membership"].width  = 366.0
    ff_clouds_nodes_1.nodes["Layer Membership"].height = 564.0

    ff_clouds_nodes_1.nodes["is_L1"].width  = 140.0
    ff_clouds_nodes_1.nodes["is_L1"].height = 100.0

    ff_clouds_nodes_1.nodes[">= boundary1"].width  = 140.0
    ff_clouds_nodes_1.nodes[">= boundary1"].height = 100.0

    ff_clouds_nodes_1.nodes["< boundary2"].width  = 140.0
    ff_clouds_nodes_1.nodes["< boundary2"].height = 100.0

    ff_clouds_nodes_1.nodes["is_L2"].width  = 140.0
    ff_clouds_nodes_1.nodes["is_L2"].height = 100.0

    ff_clouds_nodes_1.nodes["Layer Parameter Switching"].width  = 1093.0
    ff_clouds_nodes_1.nodes["Layer Parameter Switching"].height = 1756.9044189453125

    ff_clouds_nodes_1.nodes["Group Input.001"].width  = 140.0
    ff_clouds_nodes_1.nodes["Group Input.001"].height = 100.0

    ff_clouds_nodes_1.nodes["probability: L2 or L3"].width  = 140.0
    ff_clouds_nodes_1.nodes["probability: L2 or L3"].height = 100.0

    ff_clouds_nodes_1.nodes["probability: select layer"].width  = 140.0
    ff_clouds_nodes_1.nodes["probability: select layer"].height = 100.0

    ff_clouds_nodes_1.nodes["radius: L2 or L3"].width  = 140.0
    ff_clouds_nodes_1.nodes["radius: L2 or L3"].height = 100.0

    ff_clouds_nodes_1.nodes["radius: select layer"].width  = 140.0
    ff_clouds_nodes_1.nodes["radius: select layer"].height = 100.0

    ff_clouds_nodes_1.nodes["height: L2 or L3"].width  = 140.0
    ff_clouds_nodes_1.nodes["height: L2 or L3"].height = 100.0

    ff_clouds_nodes_1.nodes["height: select layer"].width  = 140.0
    ff_clouds_nodes_1.nodes["height: select layer"].height = 100.0

    ff_clouds_nodes_1.nodes["min_size: L2 or L3"].width  = 140.0
    ff_clouds_nodes_1.nodes["min_size: L2 or L3"].height = 100.0

    ff_clouds_nodes_1.nodes["min_size: select layer"].width  = 140.0
    ff_clouds_nodes_1.nodes["min_size: select layer"].height = 100.0

    ff_clouds_nodes_1.nodes["max_size: L2 or L3"].width  = 140.0
    ff_clouds_nodes_1.nodes["max_size: L2 or L3"].height = 100.0

    ff_clouds_nodes_1.nodes["max_size: select layer"].width  = 140.0
    ff_clouds_nodes_1.nodes["max_size: select layer"].height = 100.0

    ff_clouds_nodes_1.nodes["squash_prob: L2 or L3"].width  = 140.0
    ff_clouds_nodes_1.nodes["squash_prob: L2 or L3"].height = 100.0

    ff_clouds_nodes_1.nodes["squash_prob: select layer"].width  = 140.0
    ff_clouds_nodes_1.nodes["squash_prob: select layer"].height = 100.0

    ff_clouds_nodes_1.nodes["max_squash: L2 or L3"].width  = 140.0
    ff_clouds_nodes_1.nodes["max_squash: L2 or L3"].height = 100.0

    ff_clouds_nodes_1.nodes["max_squash: select layer"].width  = 140.0
    ff_clouds_nodes_1.nodes["max_squash: select layer"].height = 100.0

    ff_clouds_nodes_1.nodes["presence_seed: L2 or L3"].width  = 140.0
    ff_clouds_nodes_1.nodes["presence_seed: L2 or L3"].height = 100.0

    ff_clouds_nodes_1.nodes["presence_seed: select layer"].width  = 140.0
    ff_clouds_nodes_1.nodes["presence_seed: select layer"].height = 100.0

    ff_clouds_nodes_1.nodes["Layer Presence Check"].width  = 200.0
    ff_clouds_nodes_1.nodes["Layer Presence Check"].height = 316.0

    ff_clouds_nodes_1.nodes["layer_present?"].width  = 140.0
    ff_clouds_nodes_1.nodes["layer_present?"].height = 100.0

    ff_clouds_nodes_1.nodes["NOT layer_present"].width  = 140.0
    ff_clouds_nodes_1.nodes["NOT layer_present"].height = 100.0

    ff_clouds_nodes_1.nodes["Cloud Centers"].width  = 858.0
    ff_clouds_nodes_1.nodes["Cloud Centers"].height = 1311.0

    ff_clouds_nodes_1.nodes["Group Input.002"].width  = 140.0
    ff_clouds_nodes_1.nodes["Group Input.002"].height = 100.0

    ff_clouds_nodes_1.nodes["FieldX/2"].width  = 140.0
    ff_clouds_nodes_1.nodes["FieldX/2"].height = 100.0

    ff_clouds_nodes_1.nodes["-FieldX/2"].width  = 140.0
    ff_clouds_nodes_1.nodes["-FieldX/2"].height = 100.0

    ff_clouds_nodes_1.nodes["FieldY/2"].width  = 140.0
    ff_clouds_nodes_1.nodes["FieldY/2"].height = 100.0

    ff_clouds_nodes_1.nodes["-FieldY/2"].width  = 140.0
    ff_clouds_nodes_1.nodes["-FieldY/2"].height = 100.0

    ff_clouds_nodes_1.nodes["HeightScatter/2"].width  = 140.0
    ff_clouds_nodes_1.nodes["HeightScatter/2"].height = 100.0

    ff_clouds_nodes_1.nodes["-HeightScatter/2"].width  = 140.0
    ff_clouds_nodes_1.nodes["-HeightScatter/2"].height = 100.0

    ff_clouds_nodes_1.nodes["Cloud Center X"].width  = 140.0
    ff_clouds_nodes_1.nodes["Cloud Center X"].height = 100.0

    ff_clouds_nodes_1.nodes["Cloud Center Y"].width  = 140.0
    ff_clouds_nodes_1.nodes["Cloud Center Y"].height = 100.0

    ff_clouds_nodes_1.nodes["Cloud Center Z"].width  = 140.0
    ff_clouds_nodes_1.nodes["Cloud Center Z"].height = 100.0

    ff_clouds_nodes_1.nodes["Cloud Center"].width  = 140.0
    ff_clouds_nodes_1.nodes["Cloud Center"].height = 100.0

    ff_clouds_nodes_1.nodes["Cloud Color Seed"].width  = 637.0
    ff_clouds_nodes_1.nodes["Cloud Color Seed"].height = 1050.687744140625

    ff_clouds_nodes_1.nodes["Group Input.003"].width  = 140.0
    ff_clouds_nodes_1.nodes["Group Input.003"].height = 100.0

    ff_clouds_nodes_1.nodes["Cloud Color To Seed"].width  = 140.0
    ff_clouds_nodes_1.nodes["Cloud Color To Seed"].height = 100.0

    ff_clouds_nodes_1.nodes["Cloud Random Color"].width  = 140.0
    ff_clouds_nodes_1.nodes["Cloud Random Color"].height = 100.0

    ff_clouds_nodes_1.nodes["Per-Sphere Randomization"].width  = 1228.0
    ff_clouds_nodes_1.nodes["Per-Sphere Randomization"].height = 2017.0

    ff_clouds_nodes_1.nodes["Angle"].width  = 140.0
    ff_clouds_nodes_1.nodes["Angle"].height = 100.0

    ff_clouds_nodes_1.nodes["Radius Frac"].width  = 140.0
    ff_clouds_nodes_1.nodes["Radius Frac"].height = 100.0

    ff_clouds_nodes_1.nodes["sqrt(frac)"].width  = 140.0
    ff_clouds_nodes_1.nodes["sqrt(frac)"].height = 100.0

    ff_clouds_nodes_1.nodes["local_radius"].width  = 140.0
    ff_clouds_nodes_1.nodes["local_radius"].height = 100.0

    ff_clouds_nodes_1.nodes["cos(angle)"].width  = 140.0
    ff_clouds_nodes_1.nodes["cos(angle)"].height = 100.0

    ff_clouds_nodes_1.nodes["sin(angle)"].width  = 140.0
    ff_clouds_nodes_1.nodes["sin(angle)"].height = 100.0

    ff_clouds_nodes_1.nodes["x_local"].width  = 140.0
    ff_clouds_nodes_1.nodes["x_local"].height = 100.0

    ff_clouds_nodes_1.nodes["y_local"].width  = 140.0
    ff_clouds_nodes_1.nodes["y_local"].height = 100.0

    ff_clouds_nodes_1.nodes["jag_amount"].width  = 140.0
    ff_clouds_nodes_1.nodes["jag_amount"].height = 100.0

    ff_clouds_nodes_1.nodes["-jag_amount"].width  = 140.0
    ff_clouds_nodes_1.nodes["-jag_amount"].height = 100.0

    ff_clouds_nodes_1.nodes["jag_z"].width  = 140.0
    ff_clouds_nodes_1.nodes["jag_z"].height = 100.0

    ff_clouds_nodes_1.nodes["-jag_z"].width  = 140.0
    ff_clouds_nodes_1.nodes["-jag_z"].height = 100.0

    ff_clouds_nodes_1.nodes["jag min vec"].width  = 140.0
    ff_clouds_nodes_1.nodes["jag min vec"].height = 100.0

    ff_clouds_nodes_1.nodes["jag max vec"].width  = 140.0
    ff_clouds_nodes_1.nodes["jag max vec"].height = 100.0

    ff_clouds_nodes_1.nodes["Jagged Offset"].width  = 140.0
    ff_clouds_nodes_1.nodes["Jagged Offset"].height = 100.0

    ff_clouds_nodes_1.nodes["Base Sphere Radius"].width  = 140.0
    ff_clouds_nodes_1.nodes["Base Sphere Radius"].height = 100.0

    ff_clouds_nodes_1.nodes["Squash Check"].width  = 140.0
    ff_clouds_nodes_1.nodes["Squash Check"].height = 100.0

    ff_clouds_nodes_1.nodes["Squash Amount (raw)"].width  = 140.0
    ff_clouds_nodes_1.nodes["Squash Amount (raw)"].height = 100.0

    ff_clouds_nodes_1.nodes["Squash Amount"].width  = 140.0
    ff_clouds_nodes_1.nodes["Squash Amount"].height = 100.0

    ff_clouds_nodes_1.nodes["Squash Logic"].width  = 1291.0
    ff_clouds_nodes_1.nodes["Squash Logic"].height = 1138.0

    ff_clouds_nodes_1.nodes["shrink"].width  = 140.0
    ff_clouds_nodes_1.nodes["shrink"].height = 100.0

    ff_clouds_nodes_1.nodes["1 - shrink"].width  = 140.0
    ff_clouds_nodes_1.nodes["1 - shrink"].height = 100.0

    ff_clouds_nodes_1.nodes["Sub-sphere Radius"].width  = 140.0
    ff_clouds_nodes_1.nodes["Sub-sphere Radius"].height = 100.0

    ff_clouds_nodes_1.nodes["squash*base_radius"].width  = 140.0
    ff_clouds_nodes_1.nodes["squash*base_radius"].height = 100.0

    ff_clouds_nodes_1.nodes["Spread Distance"].width  = 140.0
    ff_clouds_nodes_1.nodes["Spread Distance"].height = 100.0

    ff_clouds_nodes_1.nodes["sub == 0"].width  = 140.0
    ff_clouds_nodes_1.nodes["sub == 0"].height = 100.0

    ff_clouds_nodes_1.nodes["sub == 1"].width  = 140.0
    ff_clouds_nodes_1.nodes["sub == 1"].height = 100.0

    ff_clouds_nodes_1.nodes["sub == 2"].width  = 140.0
    ff_clouds_nodes_1.nodes["sub == 2"].height = 100.0

    ff_clouds_nodes_1.nodes["dir: +Y / -Y"].width  = 140.0
    ff_clouds_nodes_1.nodes["dir: +Y / -Y"].height = 100.0

    ff_clouds_nodes_1.nodes["dir: -X / (+-Y)"].width  = 140.0
    ff_clouds_nodes_1.nodes["dir: -X / (+-Y)"].height = 100.0

    ff_clouds_nodes_1.nodes["dir: +X"].width  = 140.0
    ff_clouds_nodes_1.nodes["dir: +X"].height = 100.0

    ff_clouds_nodes_1.nodes["Sub Offset sep"].width  = 140.0
    ff_clouds_nodes_1.nodes["Sub Offset sep"].height = 100.0

    ff_clouds_nodes_1.nodes["Sub Offset x"].width  = 140.0
    ff_clouds_nodes_1.nodes["Sub Offset x"].height = 100.0

    ff_clouds_nodes_1.nodes["Sub Offset y"].width  = 140.0
    ff_clouds_nodes_1.nodes["Sub Offset y"].height = 100.0

    ff_clouds_nodes_1.nodes["Sub Offset z"].width  = 140.0
    ff_clouds_nodes_1.nodes["Sub Offset z"].height = 100.0

    ff_clouds_nodes_1.nodes["Sub Offset"].width  = 140.0
    ff_clouds_nodes_1.nodes["Sub Offset"].height = 100.0

    ff_clouds_nodes_1.nodes["Position Assembly"].width  = 674.0
    ff_clouds_nodes_1.nodes["Position Assembly"].height = 1314.0

    ff_clouds_nodes_1.nodes["Local XY"].width  = 140.0
    ff_clouds_nodes_1.nodes["Local XY"].height = 100.0

    ff_clouds_nodes_1.nodes["+ jagged offset"].width  = 140.0
    ff_clouds_nodes_1.nodes["+ jagged offset"].height = 100.0

    ff_clouds_nodes_1.nodes["+ squash sub-offset"].width  = 140.0
    ff_clouds_nodes_1.nodes["+ squash sub-offset"].height = 100.0

    ff_clouds_nodes_1.nodes["Layer Height Vec"].width  = 140.0
    ff_clouds_nodes_1.nodes["Layer Height Vec"].height = 100.0

    ff_clouds_nodes_1.nodes["cloud_center + layer_height"].width  = 140.0
    ff_clouds_nodes_1.nodes["cloud_center + layer_height"].height = 100.0

    ff_clouds_nodes_1.nodes["FINAL POSITION"].width  = 140.0
    ff_clouds_nodes_1.nodes["FINAL POSITION"].height = 100.0

    ff_clouds_nodes_1.nodes["Filter & Bake"].width  = 205.0
    ff_clouds_nodes_1.nodes["Filter & Bake"].height = 891.0

    ff_clouds_nodes_1.nodes["Set Position"].width  = 140.0
    ff_clouds_nodes_1.nodes["Set Position"].height = 100.0

    ff_clouds_nodes_1.nodes["Store 'sphere_radius'"].width  = 140.0
    ff_clouds_nodes_1.nodes["Store 'sphere_radius'"].height = 100.0

    ff_clouds_nodes_1.nodes["Store 'ColorMask'"].width  = 140.0
    ff_clouds_nodes_1.nodes["Store 'ColorMask'"].height = 100.0

    ff_clouds_nodes_1.nodes["Delete absent points"].width  = 140.0
    ff_clouds_nodes_1.nodes["Delete absent points"].height = 100.0

    ff_clouds_nodes_1.nodes["Mesh Conversion"].width  = 786.0
    ff_clouds_nodes_1.nodes["Mesh Conversion"].height = 1161.103271484375

    ff_clouds_nodes_1.nodes["Group Input.004"].width  = 140.0
    ff_clouds_nodes_1.nodes["Group Input.004"].height = 100.0

    ff_clouds_nodes_1.nodes["Read back 'sphere_radius'"].width  = 140.0
    ff_clouds_nodes_1.nodes["Read back 'sphere_radius'"].height = 100.0

    ff_clouds_nodes_1.nodes["Points to Volume"].width  = 170.0
    ff_clouds_nodes_1.nodes["Points to Volume"].height = 100.0

    ff_clouds_nodes_1.nodes["Volume to Mesh"].width  = 170.0
    ff_clouds_nodes_1.nodes["Volume to Mesh"].height = 100.0

    ff_clouds_nodes_1.nodes["Cloud Color Transfer"].width  = 994.0
    ff_clouds_nodes_1.nodes["Cloud Color Transfer"].height = 693.0

    ff_clouds_nodes_1.nodes["Position (voxel mesh)"].width  = 140.0
    ff_clouds_nodes_1.nodes["Position (voxel mesh)"].height = 100.0

    ff_clouds_nodes_1.nodes["Sample Nearest (cloud point)"].width  = 140.0
    ff_clouds_nodes_1.nodes["Sample Nearest (cloud point)"].height = 100.0

    ff_clouds_nodes_1.nodes["Read 'ColorMask' (points)"].width  = 140.0
    ff_clouds_nodes_1.nodes["Read 'ColorMask' (points)"].height = 100.0

    ff_clouds_nodes_1.nodes["Sample Index (ColorMask)"].width  = 140.0
    ff_clouds_nodes_1.nodes["Sample Index (ColorMask)"].height = 100.0

    ff_clouds_nodes_1.nodes["Store 'ColorMask' (voxel mesh)"].width  = 140.0
    ff_clouds_nodes_1.nodes["Store 'ColorMask' (voxel mesh)"].height = 100.0

    ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"].width  = 2373.0
    ff_clouds_nodes_1.nodes["Optional Polish: Wind & Surface Detail"].height = 1245.0

    ff_clouds_nodes_1.nodes["Group Input.005"].width  = 140.0
    ff_clouds_nodes_1.nodes["Group Input.005"].height = 100.0

    ff_clouds_nodes_1.nodes["Wind Offset"].width  = 140.0
    ff_clouds_nodes_1.nodes["Wind Offset"].height = 100.0

    ff_clouds_nodes_1.nodes["Set Position (wind)"].width  = 140.0
    ff_clouds_nodes_1.nodes["Set Position (wind)"].height = 100.0

    ff_clouds_nodes_1.nodes["Normal"].width  = 140.0
    ff_clouds_nodes_1.nodes["Normal"].height = 100.0

    ff_clouds_nodes_1.nodes["Position"].width  = 140.0
    ff_clouds_nodes_1.nodes["Position"].height = 100.0

    ff_clouds_nodes_1.nodes["position * detail_scale sep"].width  = 140.0
    ff_clouds_nodes_1.nodes["position * detail_scale sep"].height = 100.0

    ff_clouds_nodes_1.nodes["position * detail_scale x"].width  = 140.0
    ff_clouds_nodes_1.nodes["position * detail_scale x"].height = 100.0

    ff_clouds_nodes_1.nodes["position * detail_scale y"].width  = 140.0
    ff_clouds_nodes_1.nodes["position * detail_scale y"].height = 100.0

    ff_clouds_nodes_1.nodes["position * detail_scale z"].width  = 140.0
    ff_clouds_nodes_1.nodes["position * detail_scale z"].height = 100.0

    ff_clouds_nodes_1.nodes["position * detail_scale"].width  = 140.0
    ff_clouds_nodes_1.nodes["position * detail_scale"].height = 100.0

    ff_clouds_nodes_1.nodes["Noise Texture"].width  = 145.0
    ff_clouds_nodes_1.nodes["Noise Texture"].height = 100.0

    ff_clouds_nodes_1.nodes["center noise around 0"].width  = 140.0
    ff_clouds_nodes_1.nodes["center noise around 0"].height = 100.0

    ff_clouds_nodes_1.nodes["disp_amount"].width  = 140.0
    ff_clouds_nodes_1.nodes["disp_amount"].height = 100.0

    ff_clouds_nodes_1.nodes["displacement vector sep"].width  = 140.0
    ff_clouds_nodes_1.nodes["displacement vector sep"].height = 100.0

    ff_clouds_nodes_1.nodes["displacement vector x"].width  = 140.0
    ff_clouds_nodes_1.nodes["displacement vector x"].height = 100.0

    ff_clouds_nodes_1.nodes["displacement vector y"].width  = 140.0
    ff_clouds_nodes_1.nodes["displacement vector y"].height = 100.0

    ff_clouds_nodes_1.nodes["displacement vector z"].width  = 140.0
    ff_clouds_nodes_1.nodes["displacement vector z"].height = 100.0

    ff_clouds_nodes_1.nodes["displacement vector"].width  = 140.0
    ff_clouds_nodes_1.nodes["displacement vector"].height = 100.0

    ff_clouds_nodes_1.nodes["Set Position (surface detail)"].width  = 140.0
    ff_clouds_nodes_1.nodes["Set Position (surface detail)"].height = 100.0

    ff_clouds_nodes_1.nodes["Stylized Normals & Material"].width  = 1291.0
    ff_clouds_nodes_1.nodes["Stylized Normals & Material"].height = 1213.0

    ff_clouds_nodes_1.nodes["Group Input.006"].width  = 140.0
    ff_clouds_nodes_1.nodes["Group Input.006"].height = 100.0

    ff_clouds_nodes_1.nodes["Set Shade Smooth"].width  = 140.0
    ff_clouds_nodes_1.nodes["Set Shade Smooth"].height = 100.0

    ff_clouds_nodes_1.nodes["Blur Attribute"].width  = 140.0
    ff_clouds_nodes_1.nodes["Blur Attribute"].height = 100.0

    ff_clouds_nodes_1.nodes["Normal.001"].width  = 140.0
    ff_clouds_nodes_1.nodes["Normal.001"].height = 100.0

    ff_clouds_nodes_1.nodes["Set Mesh Normal"].width  = 140.0
    ff_clouds_nodes_1.nodes["Set Mesh Normal"].height = 100.0

    ff_clouds_nodes_1.nodes["Normalize Blurred Normal"].width  = 140.0
    ff_clouds_nodes_1.nodes["Normalize Blurred Normal"].height = 100.0

    ff_clouds_nodes_1.nodes["Set Material"].width  = 140.0
    ff_clouds_nodes_1.nodes["Set Material"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute"].height = 100.0

    ff_clouds_nodes_1.nodes["Group Input.007"].width  = 140.0
    ff_clouds_nodes_1.nodes["Group Input.007"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.002"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.002"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.003"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.003"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.006"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.006"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.007"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.007"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.008"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.008"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.009"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.009"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.010"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.010"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.011"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.011"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.013"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.013"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.014"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.014"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.001"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.001"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.015"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.015"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.016"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.016"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.017"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.017"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.018"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.018"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.019"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.019"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.004"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.004"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.005"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.005"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.020"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.020"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.012"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.012"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.021"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.021"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.022"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.022"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.023"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.023"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.024"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.024"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.025"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.025"].height = 100.0

    ff_clouds_nodes_1.nodes["Store 'fractal_id'"].width  = 140.0
    ff_clouds_nodes_1.nodes["Store 'fractal_id'"].height = 100.0

    ff_clouds_nodes_1.nodes["Store 'fractal_id' (voxel mesh)"].width  = 140.0
    ff_clouds_nodes_1.nodes["Store 'fractal_id' (voxel mesh)"].height = 100.0

    ff_clouds_nodes_1.nodes["Read 'fractal_id' (points)"].width  = 140.0
    ff_clouds_nodes_1.nodes["Read 'fractal_id' (points)"].height = 100.0

    ff_clouds_nodes_1.nodes["Sample Index (fractal_id)"].width  = 140.0
    ff_clouds_nodes_1.nodes["Sample Index (fractal_id)"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.026"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.026"].height = 100.0

    ff_clouds_nodes_1.nodes["Reroute.027"].width  = 10.0
    ff_clouds_nodes_1.nodes["Reroute.027"].height = 100.0


    # Initialize ff_clouds_nodes_1 links

    # group_input.Spheres Count -> boundary2__l1_l2_.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input"].outputs[21],
        ff_clouds_nodes_1.nodes["boundary2 (L1+L2)"].inputs[1]
    )
    # boundary2__l1_l2_.Value -> max_per_cloud__l1_l2_l3_.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["boundary2 (L1+L2)"].outputs[0],
        ff_clouds_nodes_1.nodes["max_per_cloud (L1+L2+L3)"].inputs[0]
    )
    # group_input.Spheres Count -> max_per_cloud__l1_l2_l3_.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input"].outputs[29],
        ff_clouds_nodes_1.nodes["max_per_cloud (L1+L2+L3)"].inputs[1]
    )
    # group_input.Cloud Count -> slot_total.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input"].outputs[2],
        ff_clouds_nodes_1.nodes["slot_total"].inputs[0]
    )
    # max_per_cloud__l1_l2_l3_.Value -> slot_total.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["max_per_cloud (L1+L2+L3)"].outputs[0],
        ff_clouds_nodes_1.nodes["slot_total"].inputs[1]
    )
    # slot_total.Value -> total_points.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["slot_total"].outputs[0],
        ff_clouds_nodes_1.nodes["total_points"].inputs[0]
    )
    # total_points.Value -> total_points__int_.Float
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["total_points"].outputs[0],
        ff_clouds_nodes_1.nodes["total_points (int)"].inputs[0]
    )
    # total_points__int_.Integer -> mesh_line.Count
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["total_points (int)"].outputs[0],
        ff_clouds_nodes_1.nodes["Mesh Line"].inputs[0]
    )
    # i___4.Value -> slot_index.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["i / 4"].outputs[0],
        ff_clouds_nodes_1.nodes["slot_index"].inputs[0]
    )
    # slot_index.Value -> slot_maxpc.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["slot_index"].outputs[0],
        ff_clouds_nodes_1.nodes["slot/maxpc"].inputs[0]
    )
    # reroute.Output -> slot_maxpc.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute"].outputs[0],
        ff_clouds_nodes_1.nodes["slot/maxpc"].inputs[1]
    )
    # slot_maxpc.Value -> cloud_index.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["slot/maxpc"].outputs[0],
        ff_clouds_nodes_1.nodes["cloud_index"].inputs[0]
    )
    # slot_index.Value -> local_index.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["slot_index"].outputs[0],
        ff_clouds_nodes_1.nodes["local_index"].inputs[0]
    )
    # reroute.Output -> local_index.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute"].outputs[0],
        ff_clouds_nodes_1.nodes["local_index"].inputs[1]
    )
    # cloud_index.Value -> cloud_index__int_.Float
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["cloud_index"].outputs[0],
        ff_clouds_nodes_1.nodes["cloud_index (int)"].inputs[0]
    )
    # slot_index.Value -> slot_index__int_.Float
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["slot_index"].outputs[0],
        ff_clouds_nodes_1.nodes["slot_index (int)"].inputs[0]
    )
    # local_index.Value -> is_l1.A
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["local_index"].outputs[0],
        ff_clouds_nodes_1.nodes["is_L1"].inputs[0]
    )
    # local_index.Value -> ___boundary1.A
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["local_index"].outputs[0],
        ff_clouds_nodes_1.nodes[">= boundary1"].inputs[0]
    )
    # local_index.Value -> __boundary2.A
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["local_index"].outputs[0],
        ff_clouds_nodes_1.nodes["< boundary2"].inputs[0]
    )
    # boundary2__l1_l2_.Value -> __boundary2.B
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["boundary2 (L1+L2)"].outputs[0],
        ff_clouds_nodes_1.nodes["< boundary2"].inputs[1]
    )
    # ___boundary1.Result -> is_l2.Boolean
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes[">= boundary1"].outputs[0],
        ff_clouds_nodes_1.nodes["is_L2"].inputs[0]
    )
    # __boundary2.Result -> is_l2.Boolean
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["< boundary2"].outputs[0],
        ff_clouds_nodes_1.nodes["is_L2"].inputs[1]
    )
    # is_l2.Boolean -> probability__l2_or_l3.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["is_L2"].outputs[0],
        ff_clouds_nodes_1.nodes["probability: L2 or L3"].inputs[0]
    )
    # group_input_001.Probability -> probability__l2_or_l3.False
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[26],
        ff_clouds_nodes_1.nodes["probability: L2 or L3"].inputs[1]
    )
    # group_input_001.Probability -> probability__l2_or_l3.True
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[18],
        ff_clouds_nodes_1.nodes["probability: L2 or L3"].inputs[2]
    )
    # is_l1.Result -> probability__select_layer.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["is_L1"].outputs[0],
        ff_clouds_nodes_1.nodes["probability: select layer"].inputs[0]
    )
    # probability__l2_or_l3.Output -> probability__select_layer.False
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["probability: L2 or L3"].outputs[0],
        ff_clouds_nodes_1.nodes["probability: select layer"].inputs[1]
    )
    # group_input_001.Probability -> probability__select_layer.True
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[10],
        ff_clouds_nodes_1.nodes["probability: select layer"].inputs[2]
    )
    # is_l2.Boolean -> radius__l2_or_l3.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["is_L2"].outputs[0],
        ff_clouds_nodes_1.nodes["radius: L2 or L3"].inputs[0]
    )
    # group_input_001.Layer Radius -> radius__l2_or_l3.False
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[27],
        ff_clouds_nodes_1.nodes["radius: L2 or L3"].inputs[1]
    )
    # group_input_001.Layer Radius -> radius__l2_or_l3.True
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[19],
        ff_clouds_nodes_1.nodes["radius: L2 or L3"].inputs[2]
    )
    # reroute_007.Output -> radius__select_layer.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.007"].outputs[0],
        ff_clouds_nodes_1.nodes["radius: select layer"].inputs[0]
    )
    # radius__l2_or_l3.Output -> radius__select_layer.False
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["radius: L2 or L3"].outputs[0],
        ff_clouds_nodes_1.nodes["radius: select layer"].inputs[1]
    )
    # group_input_001.Layer Radius -> radius__select_layer.True
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[11],
        ff_clouds_nodes_1.nodes["radius: select layer"].inputs[2]
    )
    # is_l2.Boolean -> height__l2_or_l3.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["is_L2"].outputs[0],
        ff_clouds_nodes_1.nodes["height: L2 or L3"].inputs[0]
    )
    # group_input_001.Layer Height (Z Offset) -> height__l2_or_l3.False
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[28],
        ff_clouds_nodes_1.nodes["height: L2 or L3"].inputs[1]
    )
    # group_input_001.Layer Height (Z Offset) -> height__l2_or_l3.True
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[20],
        ff_clouds_nodes_1.nodes["height: L2 or L3"].inputs[2]
    )
    # reroute_007.Output -> height__select_layer.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.007"].outputs[0],
        ff_clouds_nodes_1.nodes["height: select layer"].inputs[0]
    )
    # height__l2_or_l3.Output -> height__select_layer.False
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["height: L2 or L3"].outputs[0],
        ff_clouds_nodes_1.nodes["height: select layer"].inputs[1]
    )
    # group_input_001.Layer Height (Z Offset) -> height__select_layer.True
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[12],
        ff_clouds_nodes_1.nodes["height: select layer"].inputs[2]
    )
    # is_l2.Boolean -> min_size__l2_or_l3.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["is_L2"].outputs[0],
        ff_clouds_nodes_1.nodes["min_size: L2 or L3"].inputs[0]
    )
    # group_input_001.Min Sphere Size -> min_size__l2_or_l3.False
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[30],
        ff_clouds_nodes_1.nodes["min_size: L2 or L3"].inputs[1]
    )
    # group_input_001.Min Sphere Size -> min_size__l2_or_l3.True
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[22],
        ff_clouds_nodes_1.nodes["min_size: L2 or L3"].inputs[2]
    )
    # reroute_007.Output -> min_size__select_layer.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.007"].outputs[0],
        ff_clouds_nodes_1.nodes["min_size: select layer"].inputs[0]
    )
    # min_size__l2_or_l3.Output -> min_size__select_layer.False
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["min_size: L2 or L3"].outputs[0],
        ff_clouds_nodes_1.nodes["min_size: select layer"].inputs[1]
    )
    # group_input_001.Min Sphere Size -> min_size__select_layer.True
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[14],
        ff_clouds_nodes_1.nodes["min_size: select layer"].inputs[2]
    )
    # is_l2.Boolean -> max_size__l2_or_l3.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["is_L2"].outputs[0],
        ff_clouds_nodes_1.nodes["max_size: L2 or L3"].inputs[0]
    )
    # group_input_001.Max Sphere Size -> max_size__l2_or_l3.False
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[31],
        ff_clouds_nodes_1.nodes["max_size: L2 or L3"].inputs[1]
    )
    # group_input_001.Max Sphere Size -> max_size__l2_or_l3.True
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[23],
        ff_clouds_nodes_1.nodes["max_size: L2 or L3"].inputs[2]
    )
    # reroute_007.Output -> max_size__select_layer.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.007"].outputs[0],
        ff_clouds_nodes_1.nodes["max_size: select layer"].inputs[0]
    )
    # max_size__l2_or_l3.Output -> max_size__select_layer.False
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["max_size: L2 or L3"].outputs[0],
        ff_clouds_nodes_1.nodes["max_size: select layer"].inputs[1]
    )
    # group_input_001.Max Sphere Size -> max_size__select_layer.True
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[15],
        ff_clouds_nodes_1.nodes["max_size: select layer"].inputs[2]
    )
    # is_l2.Boolean -> squash_prob__l2_or_l3.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["is_L2"].outputs[0],
        ff_clouds_nodes_1.nodes["squash_prob: L2 or L3"].inputs[0]
    )
    # group_input_001.Squash Probability -> squash_prob__l2_or_l3.False
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[32],
        ff_clouds_nodes_1.nodes["squash_prob: L2 or L3"].inputs[1]
    )
    # group_input_001.Squash Probability -> squash_prob__l2_or_l3.True
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[24],
        ff_clouds_nodes_1.nodes["squash_prob: L2 or L3"].inputs[2]
    )
    # reroute_007.Output -> squash_prob__select_layer.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.007"].outputs[0],
        ff_clouds_nodes_1.nodes["squash_prob: select layer"].inputs[0]
    )
    # squash_prob__l2_or_l3.Output -> squash_prob__select_layer.False
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["squash_prob: L2 or L3"].outputs[0],
        ff_clouds_nodes_1.nodes["squash_prob: select layer"].inputs[1]
    )
    # group_input_001.Squash Probability -> squash_prob__select_layer.True
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[16],
        ff_clouds_nodes_1.nodes["squash_prob: select layer"].inputs[2]
    )
    # is_l2.Boolean -> max_squash__l2_or_l3.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["is_L2"].outputs[0],
        ff_clouds_nodes_1.nodes["max_squash: L2 or L3"].inputs[0]
    )
    # group_input_001.Max Squash Strength -> max_squash__l2_or_l3.False
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[33],
        ff_clouds_nodes_1.nodes["max_squash: L2 or L3"].inputs[1]
    )
    # group_input_001.Max Squash Strength -> max_squash__l2_or_l3.True
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[25],
        ff_clouds_nodes_1.nodes["max_squash: L2 or L3"].inputs[2]
    )
    # reroute_007.Output -> max_squash__select_layer.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.007"].outputs[0],
        ff_clouds_nodes_1.nodes["max_squash: select layer"].inputs[0]
    )
    # max_squash__l2_or_l3.Output -> max_squash__select_layer.False
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["max_squash: L2 or L3"].outputs[0],
        ff_clouds_nodes_1.nodes["max_squash: select layer"].inputs[1]
    )
    # group_input_001.Max Squash Strength -> max_squash__select_layer.True
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.001"].outputs[17],
        ff_clouds_nodes_1.nodes["max_squash: select layer"].inputs[2]
    )
    # is_l2.Boolean -> presence_seed__l2_or_l3.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["is_L2"].outputs[0],
        ff_clouds_nodes_1.nodes["presence_seed: L2 or L3"].inputs[0]
    )
    # reroute_007.Output -> presence_seed__select_layer.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.007"].outputs[0],
        ff_clouds_nodes_1.nodes["presence_seed: select layer"].inputs[0]
    )
    # presence_seed__l2_or_l3.Output -> presence_seed__select_layer.False
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["presence_seed: L2 or L3"].outputs[0],
        ff_clouds_nodes_1.nodes["presence_seed: select layer"].inputs[1]
    )
    # probability__select_layer.Output -> layer_present_.Probability
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["probability: select layer"].outputs[0],
        ff_clouds_nodes_1.nodes["layer_present?"].inputs[0]
    )
    # reroute_010.Output -> layer_present_.ID
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.010"].outputs[0],
        ff_clouds_nodes_1.nodes["layer_present?"].inputs[1]
    )
    # presence_seed__select_layer.Output -> layer_present_.Seed
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["presence_seed: select layer"].outputs[0],
        ff_clouds_nodes_1.nodes["layer_present?"].inputs[2]
    )
    # layer_present_.Value -> not_layer_present.Boolean
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["layer_present?"].outputs[0],
        ff_clouds_nodes_1.nodes["NOT layer_present"].inputs[0]
    )
    # group_input_002.Field Size X -> fieldx_2.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.002"].outputs[0],
        ff_clouds_nodes_1.nodes["FieldX/2"].inputs[0]
    )
    # fieldx_2.Value -> _fieldx_2.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["FieldX/2"].outputs[0],
        ff_clouds_nodes_1.nodes["-FieldX/2"].inputs[0]
    )
    # group_input_002.Field Size Y -> fieldy_2.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.002"].outputs[1],
        ff_clouds_nodes_1.nodes["FieldY/2"].inputs[0]
    )
    # fieldy_2.Value -> _fieldy_2.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["FieldY/2"].outputs[0],
        ff_clouds_nodes_1.nodes["-FieldY/2"].inputs[0]
    )
    # group_input_002.Height Scatter (Z Randomness) -> heightscatter_2.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.002"].outputs[3],
        ff_clouds_nodes_1.nodes["HeightScatter/2"].inputs[0]
    )
    # heightscatter_2.Value -> _heightscatter_2.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["HeightScatter/2"].outputs[0],
        ff_clouds_nodes_1.nodes["-HeightScatter/2"].inputs[0]
    )
    # _fieldx_2.Value -> cloud_center_x.Min
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["-FieldX/2"].outputs[0],
        ff_clouds_nodes_1.nodes["Cloud Center X"].inputs[0]
    )
    # fieldx_2.Value -> cloud_center_x.Max
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["FieldX/2"].outputs[0],
        ff_clouds_nodes_1.nodes["Cloud Center X"].inputs[1]
    )
    # reroute_009.Output -> cloud_center_x.ID
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.009"].outputs[0],
        ff_clouds_nodes_1.nodes["Cloud Center X"].inputs[2]
    )
    # _fieldy_2.Value -> cloud_center_y.Min
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["-FieldY/2"].outputs[0],
        ff_clouds_nodes_1.nodes["Cloud Center Y"].inputs[0]
    )
    # fieldy_2.Value -> cloud_center_y.Max
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["FieldY/2"].outputs[0],
        ff_clouds_nodes_1.nodes["Cloud Center Y"].inputs[1]
    )
    # reroute_009.Output -> cloud_center_y.ID
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.009"].outputs[0],
        ff_clouds_nodes_1.nodes["Cloud Center Y"].inputs[2]
    )
    # _heightscatter_2.Value -> cloud_center_z.Min
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["-HeightScatter/2"].outputs[0],
        ff_clouds_nodes_1.nodes["Cloud Center Z"].inputs[0]
    )
    # heightscatter_2.Value -> cloud_center_z.Max
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["HeightScatter/2"].outputs[0],
        ff_clouds_nodes_1.nodes["Cloud Center Z"].inputs[1]
    )
    # reroute_009.Output -> cloud_center_z.ID
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.009"].outputs[0],
        ff_clouds_nodes_1.nodes["Cloud Center Z"].inputs[2]
    )
    # cloud_center_x.Value -> cloud_center.X
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Cloud Center X"].outputs[0],
        ff_clouds_nodes_1.nodes["Cloud Center"].inputs[0]
    )
    # cloud_center_y.Value -> cloud_center.Y
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Cloud Center Y"].outputs[0],
        ff_clouds_nodes_1.nodes["Cloud Center"].inputs[1]
    )
    # cloud_center_z.Value -> cloud_center.Z
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Cloud Center Z"].outputs[0],
        ff_clouds_nodes_1.nodes["Cloud Center"].inputs[2]
    )
    # group_input_003.Cloud Color -> cloud_color_to_seed.Vector
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.003"].outputs[36],
        ff_clouds_nodes_1.nodes["Cloud Color To Seed"].inputs[0]
    )
    # cloud_color_to_seed.Value -> cloud_random_color.Seed
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Cloud Color To Seed"].outputs[1],
        ff_clouds_nodes_1.nodes["Cloud Random Color"].inputs[3]
    )
    # reroute_013.Output -> angle.ID
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.013"].outputs[0],
        ff_clouds_nodes_1.nodes["Angle"].inputs[2]
    )
    # reroute_013.Output -> radius_frac.ID
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.013"].outputs[0],
        ff_clouds_nodes_1.nodes["Radius Frac"].inputs[2]
    )
    # radius_frac.Value -> sqrt_frac_.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Radius Frac"].outputs[0],
        ff_clouds_nodes_1.nodes["sqrt(frac)"].inputs[0]
    )
    # sqrt_frac_.Value -> local_radius.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["sqrt(frac)"].outputs[0],
        ff_clouds_nodes_1.nodes["local_radius"].inputs[0]
    )
    # reroute_016.Output -> local_radius.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.016"].outputs[0],
        ff_clouds_nodes_1.nodes["local_radius"].inputs[1]
    )
    # angle.Value -> cos_angle_.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Angle"].outputs[0],
        ff_clouds_nodes_1.nodes["cos(angle)"].inputs[0]
    )
    # angle.Value -> sin_angle_.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Angle"].outputs[0],
        ff_clouds_nodes_1.nodes["sin(angle)"].inputs[0]
    )
    # cos_angle_.Value -> x_local.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["cos(angle)"].outputs[0],
        ff_clouds_nodes_1.nodes["x_local"].inputs[0]
    )
    # local_radius.Value -> x_local.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["local_radius"].outputs[0],
        ff_clouds_nodes_1.nodes["x_local"].inputs[1]
    )
    # sin_angle_.Value -> y_local.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["sin(angle)"].outputs[0],
        ff_clouds_nodes_1.nodes["y_local"].inputs[0]
    )
    # local_radius.Value -> y_local.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["local_radius"].outputs[0],
        ff_clouds_nodes_1.nodes["y_local"].inputs[1]
    )
    # radius__select_layer.Output -> jag_amount.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["radius: select layer"].outputs[0],
        ff_clouds_nodes_1.nodes["jag_amount"].inputs[0]
    )
    # jag_amount.Value -> _jag_amount.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["jag_amount"].outputs[0],
        ff_clouds_nodes_1.nodes["-jag_amount"].inputs[0]
    )
    # jag_amount.Value -> jag_z.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["jag_amount"].outputs[0],
        ff_clouds_nodes_1.nodes["jag_z"].inputs[0]
    )
    # jag_z.Value -> _jag_z.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["jag_z"].outputs[0],
        ff_clouds_nodes_1.nodes["-jag_z"].inputs[0]
    )
    # _jag_amount.Value -> jag_min_vec.X
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["-jag_amount"].outputs[0],
        ff_clouds_nodes_1.nodes["jag min vec"].inputs[0]
    )
    # _jag_amount.Value -> jag_min_vec.Y
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["-jag_amount"].outputs[0],
        ff_clouds_nodes_1.nodes["jag min vec"].inputs[1]
    )
    # _jag_z.Value -> jag_min_vec.Z
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["-jag_z"].outputs[0],
        ff_clouds_nodes_1.nodes["jag min vec"].inputs[2]
    )
    # reroute_015.Output -> jag_max_vec.X
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.015"].outputs[0],
        ff_clouds_nodes_1.nodes["jag max vec"].inputs[0]
    )
    # reroute_015.Output -> jag_max_vec.Y
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.015"].outputs[0],
        ff_clouds_nodes_1.nodes["jag max vec"].inputs[1]
    )
    # jag_z.Value -> jag_max_vec.Z
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["jag_z"].outputs[0],
        ff_clouds_nodes_1.nodes["jag max vec"].inputs[2]
    )
    # jag_min_vec.Vector -> jagged_offset.Min
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["jag min vec"].outputs[0],
        ff_clouds_nodes_1.nodes["Jagged Offset"].inputs[0]
    )
    # jag_max_vec.Vector -> jagged_offset.Max
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["jag max vec"].outputs[0],
        ff_clouds_nodes_1.nodes["Jagged Offset"].inputs[1]
    )
    # reroute_014.Output -> jagged_offset.ID
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.014"].outputs[0],
        ff_clouds_nodes_1.nodes["Jagged Offset"].inputs[2]
    )
    # min_size__select_layer.Output -> base_sphere_radius.Min
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["min_size: select layer"].outputs[0],
        ff_clouds_nodes_1.nodes["Base Sphere Radius"].inputs[0]
    )
    # max_size__select_layer.Output -> base_sphere_radius.Max
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["max_size: select layer"].outputs[0],
        ff_clouds_nodes_1.nodes["Base Sphere Radius"].inputs[1]
    )
    # reroute_018.Output -> squash_check.Probability
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.018"].outputs[0],
        ff_clouds_nodes_1.nodes["Squash Check"].inputs[0]
    )
    # reroute_017.Output -> squash_amount__raw_.Max
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.017"].outputs[0],
        ff_clouds_nodes_1.nodes["Squash Amount (raw)"].inputs[1]
    )
    # squash_check.Value -> squash_amount.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Squash Check"].outputs[0],
        ff_clouds_nodes_1.nodes["Squash Amount"].inputs[0]
    )
    # squash_amount__raw_.Value -> squash_amount.True
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Squash Amount (raw)"].outputs[0],
        ff_clouds_nodes_1.nodes["Squash Amount"].inputs[2]
    )
    # squash_amount.Output -> shrink.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Squash Amount"].outputs[0],
        ff_clouds_nodes_1.nodes["shrink"].inputs[0]
    )
    # shrink.Value -> _1___shrink.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["shrink"].outputs[0],
        ff_clouds_nodes_1.nodes["1 - shrink"].inputs[1]
    )
    # base_sphere_radius.Value -> sub_sphere_radius.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Base Sphere Radius"].outputs[0],
        ff_clouds_nodes_1.nodes["Sub-sphere Radius"].inputs[0]
    )
    # _1___shrink.Value -> sub_sphere_radius.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["1 - shrink"].outputs[0],
        ff_clouds_nodes_1.nodes["Sub-sphere Radius"].inputs[1]
    )
    # squash_amount.Output -> squash_base_radius.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Squash Amount"].outputs[0],
        ff_clouds_nodes_1.nodes["squash*base_radius"].inputs[0]
    )
    # base_sphere_radius.Value -> squash_base_radius.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Base Sphere Radius"].outputs[0],
        ff_clouds_nodes_1.nodes["squash*base_radius"].inputs[1]
    )
    # squash_base_radius.Value -> spread_distance.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["squash*base_radius"].outputs[0],
        ff_clouds_nodes_1.nodes["Spread Distance"].inputs[0]
    )
    # reroute_004.Output -> sub____0.A
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.004"].outputs[0],
        ff_clouds_nodes_1.nodes["sub == 0"].inputs[0]
    )
    # reroute_004.Output -> sub____1.A
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.004"].outputs[0],
        ff_clouds_nodes_1.nodes["sub == 1"].inputs[0]
    )
    # reroute_004.Output -> sub____2.A
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.004"].outputs[0],
        ff_clouds_nodes_1.nodes["sub == 2"].inputs[0]
    )
    # sub____2.Result -> dir___y____y.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["sub == 2"].outputs[0],
        ff_clouds_nodes_1.nodes["dir: +Y / -Y"].inputs[0]
    )
    # sub____1.Result -> dir___x______y_.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["sub == 1"].outputs[0],
        ff_clouds_nodes_1.nodes["dir: -X / (+-Y)"].inputs[0]
    )
    # dir___y____y.Output -> dir___x______y_.False
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["dir: +Y / -Y"].outputs[0],
        ff_clouds_nodes_1.nodes["dir: -X / (+-Y)"].inputs[1]
    )
    # sub____0.Result -> dir___x.Switch
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["sub == 0"].outputs[0],
        ff_clouds_nodes_1.nodes["dir: +X"].inputs[0]
    )
    # dir___x______y_.Output -> dir___x.False
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["dir: -X / (+-Y)"].outputs[0],
        ff_clouds_nodes_1.nodes["dir: +X"].inputs[1]
    )
    # dir___x.Output -> sub_offset_sep.Vector
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["dir: +X"].outputs[0],
        ff_clouds_nodes_1.nodes["Sub Offset sep"].inputs[0]
    )
    # sub_offset_sep.X -> sub_offset_x.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Sub Offset sep"].outputs[0],
        ff_clouds_nodes_1.nodes["Sub Offset x"].inputs[0]
    )
    # spread_distance.Value -> sub_offset_x.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Spread Distance"].outputs[0],
        ff_clouds_nodes_1.nodes["Sub Offset x"].inputs[1]
    )
    # sub_offset_sep.Y -> sub_offset_y.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Sub Offset sep"].outputs[1],
        ff_clouds_nodes_1.nodes["Sub Offset y"].inputs[0]
    )
    # spread_distance.Value -> sub_offset_y.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Spread Distance"].outputs[0],
        ff_clouds_nodes_1.nodes["Sub Offset y"].inputs[1]
    )
    # sub_offset_sep.Z -> sub_offset_z.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Sub Offset sep"].outputs[2],
        ff_clouds_nodes_1.nodes["Sub Offset z"].inputs[0]
    )
    # spread_distance.Value -> sub_offset_z.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Spread Distance"].outputs[0],
        ff_clouds_nodes_1.nodes["Sub Offset z"].inputs[1]
    )
    # sub_offset_x.Value -> sub_offset.X
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Sub Offset x"].outputs[0],
        ff_clouds_nodes_1.nodes["Sub Offset"].inputs[0]
    )
    # sub_offset_y.Value -> sub_offset.Y
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Sub Offset y"].outputs[0],
        ff_clouds_nodes_1.nodes["Sub Offset"].inputs[1]
    )
    # sub_offset_z.Value -> sub_offset.Z
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Sub Offset z"].outputs[0],
        ff_clouds_nodes_1.nodes["Sub Offset"].inputs[2]
    )
    # x_local.Value -> local_xy.X
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["x_local"].outputs[0],
        ff_clouds_nodes_1.nodes["Local XY"].inputs[0]
    )
    # y_local.Value -> local_xy.Y
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["y_local"].outputs[0],
        ff_clouds_nodes_1.nodes["Local XY"].inputs[1]
    )
    # local_xy.Vector -> __jagged_offset.Vector
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Local XY"].outputs[0],
        ff_clouds_nodes_1.nodes["+ jagged offset"].inputs[0]
    )
    # jagged_offset.Value -> __jagged_offset.Vector
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Jagged Offset"].outputs[0],
        ff_clouds_nodes_1.nodes["+ jagged offset"].inputs[1]
    )
    # __jagged_offset.Vector -> __squash_sub_offset.Vector
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["+ jagged offset"].outputs[0],
        ff_clouds_nodes_1.nodes["+ squash sub-offset"].inputs[0]
    )
    # sub_offset.Vector -> __squash_sub_offset.Vector
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Sub Offset"].outputs[0],
        ff_clouds_nodes_1.nodes["+ squash sub-offset"].inputs[1]
    )
    # reroute_005.Output -> layer_height_vec.Z
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.005"].outputs[0],
        ff_clouds_nodes_1.nodes["Layer Height Vec"].inputs[2]
    )
    # reroute_020.Output -> cloud_center___layer_height.Vector
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.020"].outputs[0],
        ff_clouds_nodes_1.nodes["cloud_center + layer_height"].inputs[0]
    )
    # layer_height_vec.Vector -> cloud_center___layer_height.Vector
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Layer Height Vec"].outputs[0],
        ff_clouds_nodes_1.nodes["cloud_center + layer_height"].inputs[1]
    )
    # cloud_center___layer_height.Vector -> final_position.Vector
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["cloud_center + layer_height"].outputs[0],
        ff_clouds_nodes_1.nodes["FINAL POSITION"].inputs[0]
    )
    # __squash_sub_offset.Vector -> final_position.Vector
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["+ squash sub-offset"].outputs[0],
        ff_clouds_nodes_1.nodes["FINAL POSITION"].inputs[1]
    )
    # reroute_021.Output -> set_position.Geometry
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.021"].outputs[0],
        ff_clouds_nodes_1.nodes["Set Position"].inputs[0]
    )
    # final_position.Vector -> set_position.Position
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["FINAL POSITION"].outputs[0],
        ff_clouds_nodes_1.nodes["Set Position"].inputs[2]
    )
    # set_position.Geometry -> store__sphere_radius_.Geometry
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Set Position"].outputs[0],
        ff_clouds_nodes_1.nodes["Store 'sphere_radius'"].inputs[0]
    )
    # sub_sphere_radius.Value -> store__sphere_radius_.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Sub-sphere Radius"].outputs[0],
        ff_clouds_nodes_1.nodes["Store 'sphere_radius'"].inputs[3]
    )
    # store__sphere_radius_.Geometry -> store__colormask_.Geometry
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Store 'sphere_radius'"].outputs[0],
        ff_clouds_nodes_1.nodes["Store 'ColorMask'"].inputs[0]
    )
    # reroute_022.Output -> store__colormask_.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.022"].outputs[0],
        ff_clouds_nodes_1.nodes["Store 'ColorMask'"].inputs[3]
    )
    # store__fractal_id_.Geometry -> delete_absent_points.Geometry
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Store 'fractal_id'"].outputs[0],
        ff_clouds_nodes_1.nodes["Delete absent points"].inputs[0]
    )
    # reroute_024.Output -> delete_absent_points.Selection
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.024"].outputs[0],
        ff_clouds_nodes_1.nodes["Delete absent points"].inputs[1]
    )
    # group_input_004.Voxel Size -> points_to_volume.Voxel Size
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.004"].outputs[4],
        ff_clouds_nodes_1.nodes["Points to Volume"].inputs[3]
    )
    # read_back__sphere_radius_.Attribute -> points_to_volume.Radius
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Read back 'sphere_radius'"].outputs[0],
        ff_clouds_nodes_1.nodes["Points to Volume"].inputs[5]
    )
    # points_to_volume.Volume -> volume_to_mesh.Volume
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Points to Volume"].outputs[0],
        ff_clouds_nodes_1.nodes["Volume to Mesh"].inputs[0]
    )
    # group_input_004.Voxel Threshold -> volume_to_mesh.Threshold
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.004"].outputs[5],
        ff_clouds_nodes_1.nodes["Volume to Mesh"].inputs[4]
    )
    # reroute_025.Output -> sample_nearest__cloud_point_.Geometry
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.025"].outputs[0],
        ff_clouds_nodes_1.nodes["Sample Nearest (cloud point)"].inputs[0]
    )
    # position__voxel_mesh_.Position -> sample_nearest__cloud_point_.Sample Position
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Position (voxel mesh)"].outputs[0],
        ff_clouds_nodes_1.nodes["Sample Nearest (cloud point)"].inputs[1]
    )
    # reroute_025.Output -> sample_index__colormask_.Geometry
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.025"].outputs[0],
        ff_clouds_nodes_1.nodes["Sample Index (ColorMask)"].inputs[0]
    )
    # read__colormask___points_.Attribute -> sample_index__colormask_.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Read 'ColorMask' (points)"].outputs[0],
        ff_clouds_nodes_1.nodes["Sample Index (ColorMask)"].inputs[1]
    )
    # sample_nearest__cloud_point_.Index -> sample_index__colormask_.Index
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Sample Nearest (cloud point)"].outputs[0],
        ff_clouds_nodes_1.nodes["Sample Index (ColorMask)"].inputs[2]
    )
    # volume_to_mesh.Mesh -> store__colormask___voxel_mesh_.Geometry
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Volume to Mesh"].outputs[0],
        ff_clouds_nodes_1.nodes["Store 'ColorMask' (voxel mesh)"].inputs[0]
    )
    # sample_index__colormask_.Value -> store__colormask___voxel_mesh_.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Sample Index (ColorMask)"].outputs[0],
        ff_clouds_nodes_1.nodes["Store 'ColorMask' (voxel mesh)"].inputs[3]
    )
    # group_input_005.Wind Offset X -> wind_offset.X
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.005"].outputs[6],
        ff_clouds_nodes_1.nodes["Wind Offset"].inputs[0]
    )
    # group_input_005.Wind Offset Y -> wind_offset.Y
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.005"].outputs[7],
        ff_clouds_nodes_1.nodes["Wind Offset"].inputs[1]
    )
    # store__fractal_id___voxel_mesh_.Geometry -> set_position__wind_.Geometry
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Store 'fractal_id' (voxel mesh)"].outputs[0],
        ff_clouds_nodes_1.nodes["Set Position (wind)"].inputs[0]
    )
    # wind_offset.Vector -> set_position__wind_.Offset
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Wind Offset"].outputs[0],
        ff_clouds_nodes_1.nodes["Set Position (wind)"].inputs[3]
    )
    # position.Position -> position___detail_scale_sep.Vector
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Position"].outputs[0],
        ff_clouds_nodes_1.nodes["position * detail_scale sep"].inputs[0]
    )
    # position___detail_scale_sep.X -> position___detail_scale_x.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["position * detail_scale sep"].outputs[0],
        ff_clouds_nodes_1.nodes["position * detail_scale x"].inputs[0]
    )
    # group_input_005.Surface Detail Scale -> position___detail_scale_x.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.005"].outputs[9],
        ff_clouds_nodes_1.nodes["position * detail_scale x"].inputs[1]
    )
    # position___detail_scale_sep.Y -> position___detail_scale_y.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["position * detail_scale sep"].outputs[1],
        ff_clouds_nodes_1.nodes["position * detail_scale y"].inputs[0]
    )
    # group_input_005.Surface Detail Scale -> position___detail_scale_y.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.005"].outputs[9],
        ff_clouds_nodes_1.nodes["position * detail_scale y"].inputs[1]
    )
    # position___detail_scale_sep.Z -> position___detail_scale_z.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["position * detail_scale sep"].outputs[2],
        ff_clouds_nodes_1.nodes["position * detail_scale z"].inputs[0]
    )
    # group_input_005.Surface Detail Scale -> position___detail_scale_z.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.005"].outputs[9],
        ff_clouds_nodes_1.nodes["position * detail_scale z"].inputs[1]
    )
    # position___detail_scale_x.Value -> position___detail_scale.X
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["position * detail_scale x"].outputs[0],
        ff_clouds_nodes_1.nodes["position * detail_scale"].inputs[0]
    )
    # position___detail_scale_y.Value -> position___detail_scale.Y
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["position * detail_scale y"].outputs[0],
        ff_clouds_nodes_1.nodes["position * detail_scale"].inputs[1]
    )
    # position___detail_scale_z.Value -> position___detail_scale.Z
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["position * detail_scale z"].outputs[0],
        ff_clouds_nodes_1.nodes["position * detail_scale"].inputs[2]
    )
    # position___detail_scale.Vector -> noise_texture.Vector
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["position * detail_scale"].outputs[0],
        ff_clouds_nodes_1.nodes["Noise Texture"].inputs[0]
    )
    # noise_texture.Factor -> center_noise_around_0.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Noise Texture"].outputs[0],
        ff_clouds_nodes_1.nodes["center noise around 0"].inputs[0]
    )
    # center_noise_around_0.Value -> disp_amount.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["center noise around 0"].outputs[0],
        ff_clouds_nodes_1.nodes["disp_amount"].inputs[0]
    )
    # group_input_005.Surface Detail Strength -> disp_amount.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.005"].outputs[8],
        ff_clouds_nodes_1.nodes["disp_amount"].inputs[1]
    )
    # normal.Normal -> displacement_vector_sep.Vector
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Normal"].outputs[0],
        ff_clouds_nodes_1.nodes["displacement vector sep"].inputs[0]
    )
    # displacement_vector_sep.X -> displacement_vector_x.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["displacement vector sep"].outputs[0],
        ff_clouds_nodes_1.nodes["displacement vector x"].inputs[0]
    )
    # disp_amount.Value -> displacement_vector_x.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["disp_amount"].outputs[0],
        ff_clouds_nodes_1.nodes["displacement vector x"].inputs[1]
    )
    # displacement_vector_sep.Y -> displacement_vector_y.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["displacement vector sep"].outputs[1],
        ff_clouds_nodes_1.nodes["displacement vector y"].inputs[0]
    )
    # disp_amount.Value -> displacement_vector_y.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["disp_amount"].outputs[0],
        ff_clouds_nodes_1.nodes["displacement vector y"].inputs[1]
    )
    # displacement_vector_sep.Z -> displacement_vector_z.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["displacement vector sep"].outputs[2],
        ff_clouds_nodes_1.nodes["displacement vector z"].inputs[0]
    )
    # disp_amount.Value -> displacement_vector_z.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["disp_amount"].outputs[0],
        ff_clouds_nodes_1.nodes["displacement vector z"].inputs[1]
    )
    # displacement_vector_x.Value -> displacement_vector.X
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["displacement vector x"].outputs[0],
        ff_clouds_nodes_1.nodes["displacement vector"].inputs[0]
    )
    # displacement_vector_y.Value -> displacement_vector.Y
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["displacement vector y"].outputs[0],
        ff_clouds_nodes_1.nodes["displacement vector"].inputs[1]
    )
    # displacement_vector_z.Value -> displacement_vector.Z
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["displacement vector z"].outputs[0],
        ff_clouds_nodes_1.nodes["displacement vector"].inputs[2]
    )
    # set_position__wind_.Geometry -> set_position__surface_detail_.Geometry
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Set Position (wind)"].outputs[0],
        ff_clouds_nodes_1.nodes["Set Position (surface detail)"].inputs[0]
    )
    # displacement_vector.Vector -> set_position__surface_detail_.Offset
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["displacement vector"].outputs[0],
        ff_clouds_nodes_1.nodes["Set Position (surface detail)"].inputs[3]
    )
    # set_position__surface_detail_.Geometry -> set_shade_smooth.Mesh
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Set Position (surface detail)"].outputs[0],
        ff_clouds_nodes_1.nodes["Set Shade Smooth"].inputs[0]
    )
    # normal_001.Normal -> blur_attribute.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Normal.001"].outputs[0],
        ff_clouds_nodes_1.nodes["Blur Attribute"].inputs[0]
    )
    # group_input_006.Normal Blur (Fluffiness) -> blur_attribute.Iterations
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.006"].outputs[35],
        ff_clouds_nodes_1.nodes["Blur Attribute"].inputs[1]
    )
    # set_shade_smooth.Mesh -> set_mesh_normal.Mesh
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Set Shade Smooth"].outputs[0],
        ff_clouds_nodes_1.nodes["Set Mesh Normal"].inputs[0]
    )
    # blur_attribute.Value -> normalize_blurred_normal.Vector
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Blur Attribute"].outputs[0],
        ff_clouds_nodes_1.nodes["Normalize Blurred Normal"].inputs[0]
    )
    # normalize_blurred_normal.Vector -> set_mesh_normal.Custom Normal
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Normalize Blurred Normal"].outputs[0],
        ff_clouds_nodes_1.nodes["Set Mesh Normal"].inputs[1]
    )
    # set_mesh_normal.Mesh -> set_material.Geometry
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Set Mesh Normal"].outputs[0],
        ff_clouds_nodes_1.nodes["Set Material"].inputs[0]
    )
    # group_input_006.Material -> set_material.Material
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.006"].outputs[34],
        ff_clouds_nodes_1.nodes["Set Material"].inputs[2]
    )
    # set_material.Geometry -> group_output.Geometry
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Set Material"].outputs[0],
        ff_clouds_nodes_1.nodes["Group Output"].inputs[0]
    )
    # index.Index -> i___4.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Index"].outputs[0],
        ff_clouds_nodes_1.nodes["i / 4"].inputs[0]
    )
    # index.Index -> sub___i_mod_4.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Index"].outputs[0],
        ff_clouds_nodes_1.nodes["sub = i mod 4"].inputs[0]
    )
    # max_per_cloud__l1_l2_l3_.Value -> reroute.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["max_per_cloud (L1+L2+L3)"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute"].inputs[0]
    )
    # group_input_007.Spheres Count -> is_l1.B
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.007"].outputs[13],
        ff_clouds_nodes_1.nodes["is_L1"].inputs[1]
    )
    # group_input_007.Spheres Count -> ___boundary1.B
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input.007"].outputs[13],
        ff_clouds_nodes_1.nodes[">= boundary1"].inputs[1]
    )
    # group_input.Spheres Count -> boundary2__l1_l2_.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Group Input"].outputs[13],
        ff_clouds_nodes_1.nodes["boundary2 (L1+L2)"].inputs[0]
    )
    # slot_index__int_.Integer -> reroute_002.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["slot_index (int)"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.002"].inputs[0]
    )
    # sub___i_mod_4.Value -> reroute_003.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["sub = i mod 4"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.003"].inputs[0]
    )
    # reroute_008.Output -> reroute_007.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.008"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.007"].inputs[0]
    )
    # is_l1.Result -> reroute_008.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["is_L1"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.008"].inputs[0]
    )
    # cloud_index__int_.Integer -> reroute_009.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["cloud_index (int)"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.009"].inputs[0]
    )
    # cloud_index__int_.Integer -> reroute_010.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["cloud_index (int)"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.010"].inputs[0]
    )
    # reroute_010.Output -> cloud_random_color.ID
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.010"].outputs[0],
        ff_clouds_nodes_1.nodes["Cloud Random Color"].inputs[2]
    )
    # cloud_center.Vector -> reroute_011.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Cloud Center"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.011"].inputs[0]
    )
    # reroute_002.Output -> reroute_013.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.002"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.013"].inputs[0]
    )
    # reroute_006.Output -> reroute_014.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.006"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.014"].inputs[0]
    )
    # reroute_014.Output -> base_sphere_radius.ID
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.014"].outputs[0],
        ff_clouds_nodes_1.nodes["Base Sphere Radius"].inputs[2]
    )
    # reroute_014.Output -> squash_check.ID
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.014"].outputs[0],
        ff_clouds_nodes_1.nodes["Squash Check"].inputs[1]
    )
    # reroute_014.Output -> squash_amount__raw_.ID
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.014"].outputs[0],
        ff_clouds_nodes_1.nodes["Squash Amount (raw)"].inputs[2]
    )
    # slot_index__int_.Integer -> reroute_006.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["slot_index (int)"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.006"].inputs[0]
    )
    # jag_amount.Value -> reroute_001.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["jag_amount"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.001"].inputs[0]
    )
    # reroute_001.Output -> reroute_015.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.001"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.015"].inputs[0]
    )
    # radius__select_layer.Output -> reroute_016.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["radius: select layer"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.016"].inputs[0]
    )
    # max_squash__select_layer.Output -> reroute_017.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["max_squash: select layer"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.017"].inputs[0]
    )
    # squash_prob__select_layer.Output -> reroute_018.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["squash_prob: select layer"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.018"].inputs[0]
    )
    # reroute_003.Output -> reroute_019.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.003"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.019"].inputs[0]
    )
    # reroute_019.Output -> reroute_004.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.019"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.004"].inputs[0]
    )
    # height__select_layer.Output -> reroute_005.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["height: select layer"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.005"].inputs[0]
    )
    # reroute_011.Output -> reroute_020.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.011"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.020"].inputs[0]
    )
    # mesh_line.Mesh -> reroute_012.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Mesh Line"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.012"].inputs[0]
    )
    # reroute_012.Output -> reroute_021.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.012"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.021"].inputs[0]
    )
    # cloud_random_color.Value -> reroute_022.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Cloud Random Color"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.022"].inputs[0]
    )
    # not_layer_present.Boolean -> reroute_023.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["NOT layer_present"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.023"].inputs[0]
    )
    # reroute_023.Output -> reroute_024.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.023"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.024"].inputs[0]
    )
    # delete_absent_points.Geometry -> reroute_025.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Delete absent points"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.025"].inputs[0]
    )
    # store__colormask_.Geometry -> store__fractal_id_.Geometry
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Store 'ColorMask'"].outputs[0],
        ff_clouds_nodes_1.nodes["Store 'fractal_id'"].inputs[0]
    )
    # delete_absent_points.Geometry -> points_to_volume.Points
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Delete absent points"].outputs[0],
        ff_clouds_nodes_1.nodes["Points to Volume"].inputs[0]
    )
    # store__colormask___voxel_mesh_.Geometry -> store__fractal_id___voxel_mesh_.Geometry
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Store 'ColorMask' (voxel mesh)"].outputs[0],
        ff_clouds_nodes_1.nodes["Store 'fractal_id' (voxel mesh)"].inputs[0]
    )
    # read__fractal_id___points_.Attribute -> sample_index__fractal_id_.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Read 'fractal_id' (points)"].outputs[0],
        ff_clouds_nodes_1.nodes["Sample Index (fractal_id)"].inputs[1]
    )
    # sample_nearest__cloud_point_.Index -> sample_index__fractal_id_.Index
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Sample Nearest (cloud point)"].outputs[0],
        ff_clouds_nodes_1.nodes["Sample Index (fractal_id)"].inputs[2]
    )
    # sample_index__fractal_id_.Value -> store__fractal_id___voxel_mesh_.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Sample Index (fractal_id)"].outputs[0],
        ff_clouds_nodes_1.nodes["Store 'fractal_id' (voxel mesh)"].inputs[3]
    )
    # reroute_027.Output -> store__fractal_id_.Value
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.027"].outputs[0],
        ff_clouds_nodes_1.nodes["Store 'fractal_id'"].inputs[3]
    )
    # reroute_010.Output -> reroute_026.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.010"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.026"].inputs[0]
    )
    # reroute_026.Output -> reroute_027.Input
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.026"].outputs[0],
        ff_clouds_nodes_1.nodes["Reroute.027"].inputs[0]
    )
    # reroute_025.Output -> sample_index__fractal_id_.Geometry
    ff_clouds_nodes_1.links.new(
        ff_clouds_nodes_1.nodes["Reroute.025"].outputs[0],
        ff_clouds_nodes_1.nodes["Sample Index (fractal_id)"].inputs[0]
    )

    return ff_clouds_nodes_1


if __name__ == "__main__":
    # Maps node tree creation functions to the node tree 
    # name, such that we don't recreate node trees unnecessarily
    node_tree_names : dict[typing.Callable, str] = {}

    ff_clouds_nodes = ff_clouds_nodes_1_node_group(node_tree_names)
    node_tree_names[ff_clouds_nodes_1_node_group] = ff_clouds_nodes.name


# ============================================================================
#  FF BRIDGE
# ============================================================================
 
from . import bridge
 
GROUP_NAME = "FF Clouds Nodes"
MAT_NAME = "M_Clouds"
MAT_HEX = "8CB2F2"
 
 
def create_node_group():
    return bridge.get_or_create_node_group(ff_clouds_nodes_1_node_group, GROUP_NAME)
 
 
def get_or_create_material():
    return bridge.get_or_create_colormask_material(MAT_NAME, MAT_HEX)