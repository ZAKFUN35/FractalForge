"""
FF Cel-Shading - Ультимативный генератор аниме-шейдера ^_____^
Это тот самый монстр, который решает главную проблему сел-шейдинга в Блендере!

Знаете, почему большинство toon-шейдеров в Блендере выглядят так странно? 
Потому что движок "из коробки" сливает освещение от всех ламп в единый градиент. 
И если попытаться разрубить этот общий свет на жесткие полоски (каскады), 
получается грязь. Истинный сел-шейдинг требует обработки каждого источника света по отдельности!

Поэтому этот скрипт берет математику в свои руки. Он собирает гигантское дерево нод, 
которое физически циклом проходит по каждой привязанной лампочке, пускает Raycast-лучи 
для честных теней, накладывает штриховку и только потом аккуратно суммирует готовые 
аниме-блики. Мы делаем свой Substrate Toon BSDF прямо в нодах! (⌐■_■)
"""

import bpy
import math
from .i18n import t
from .panels import CAT

# ==========================================
# 1. СИНХРОНИЗАЦИЯ ДАННЫХ
# ==========================================
# Прямая связь между ползунками в UI и кишками нодового дерева.
# Чтобы каждый раз не ковыряться в паутине проводов при настройке материала,
# мы вывели все параметры наружу и обновляем их скриптом.
def update_pop_colors(self, context):
    mat = self
    if not mat.use_nodes: return
    for node in mat.node_tree.nodes:
        if node.get("is_pop_master_node"):
            def set_val(name, val):
                if name in node.inputs: node.inputs[name].default_value = val
            set_val("BaseColor", mat.pop_base_color)
            set_val("Metallic", mat.pop_metallic)
            set_val("Specular", mat.pop_specular_strength)
            set_val("Roughness", mat.pop_roughness)
            set_val("EmissiveColor", mat.pop_emissive_color)
            set_val("Diffuse Offset Strength", mat.pop_ramp_offset_strength)
            set_val("Spec Offset Strength", mat.pop_spec_ramp_offset_strength)
            set_val("Hatch Strength", mat.pop_hatch_strength)
            
        role = node.get("pop_role")
        if role:
            if role == "diffuse_offset_tex": node.image = mat.pop_ramp_offset_texture
            elif role == "diffuse_offset_map": node.inputs["Scale"].default_value = (mat.pop_ramp_offset_size,)*3
            elif role == "spec_offset_tex": node.image = mat.pop_spec_ramp_offset_texture
            elif role == "spec_offset_map": node.inputs["Scale"].default_value = (mat.pop_spec_ramp_offset_size,)*3
            elif role == "hatch_tex": node.image = mat.pop_hatch_texture
            elif role == "hatch_map": node.inputs["Scale"].default_value = (mat.pop_hatch_size,)*3
            elif role == "normal_tex":
                node.image = mat.pop_normal_texture
                # Нормалмапа обязана быть Non-Color, иначе освещение сломается
                if node.image and getattr(node.image, "colorspace_settings", None):
                    try: node.image.colorspace_settings.name = 'Non-Color'
                    except: pass
            elif role == "normal_strength_node": 
                if "Strength" in node.inputs: node.inputs["Strength"].default_value = mat.pop_normal_strength

# ==========================================
# 2. СТРУКТУРЫ ДАННЫХ СВЕТА
# ==========================================
# Управляем списком источников света для материала (Light Linking).
class POP_LightItem(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty()
    is_enabled: bpy.props.BoolProperty(name="", default=False)

def sync_lights(mat):
    if not mat: return
    scene_lights = [o.name for o in bpy.context.scene.objects if o.type == 'LIGHT']
    mat_lights = [l.name for l in mat.pop_lights]
    if set(scene_lights) == set(mat_lights): return
    for i in range(len(mat.pop_lights)-1, -1, -1):
        if mat.pop_lights[i].name not in scene_lights:
            mat.pop_lights.remove(i)
    existing_names = [l.name for l in mat.pop_lights]
    for l_name in scene_lights:
        if l_name not in existing_names:
            item = mat.pop_lights.add()
            item.name = l_name
            item.is_enabled = False

@bpy.app.handlers.persistent
def pop_auto_sync_handler(scene, depsgraph):
    obj = bpy.context.active_object
    if obj and obj.material_slots:
        mat_idx = scene.pop_mat_index
        if mat_idx < len(obj.material_slots):
            mat = obj.material_slots[mat_idx].material
            if mat: sync_lights(mat)

def on_mat_index_change(self, context):
    obj = context.active_object
    if obj and obj.material_slots and len(obj.material_slots) > self.pop_mat_index:
        sync_lights(obj.material_slots[self.pop_mat_index].material)

# ==========================================
# 3. МАТЕМАТИКА ГЛОБАЛЬНЫХ НОД
# ==========================================
# Забываем про мягкие BSDF. Собираем базовые формулы расчета.
# Мы считаем чистый Dot Product (скалярное произведение) между нормалью 
# поверхности и вектором источника света, чтобы получить сырой градиент.
def ensure_math_groups():
    if "Toon_Sun_Math_V2" not in bpy.data.node_groups:
        g_sun = bpy.data.node_groups.new("Toon_Sun_Math_V2", 'ShaderNodeTree')
        g_sun.interface.new_socket("Normal", in_out='INPUT', socket_type='NodeSocketVector')
        g_sun.interface.new_socket("Sun Dir", in_out='INPUT', socket_type='NodeSocketVector')
        g_sun.interface.new_socket("Fac", in_out='OUTPUT', socket_type='NodeSocketFloat')

        n_sun = g_sun.nodes; l_sun = g_sun.links
        in_sun = n_sun.new('NodeGroupInput'); out_sun = n_sun.new('NodeGroupOutput')
        in_sun.location = (-400, 0); out_sun.location = (200, 0)
        dot_sun = n_sun.new('ShaderNodeVectorMath'); dot_sun.operation = 'DOT_PRODUCT'
        l_sun.new(in_sun.outputs["Normal"], dot_sun.inputs[0]); l_sun.new(in_sun.outputs["Sun Dir"], dot_sun.inputs[1])
        
        # Переводим Dot Product из диапазона [-1, 1] в удобные нам [0, 1]
        remap_sun = n_sun.new('ShaderNodeMath'); remap_sun.operation = 'MULTIPLY_ADD'
        remap_sun.inputs[1].default_value = 0.5; remap_sun.inputs[2].default_value = 0.5
        l_sun.new(dot_sun.outputs["Value"], remap_sun.inputs[0]); l_sun.new(remap_sun.outputs[0], out_sun.inputs["Fac"])

    if "Toon_Point_Math_V4" not in bpy.data.node_groups:
        g_pt = bpy.data.node_groups.new("Toon_Point_Math_V4", 'ShaderNodeTree')
        g_pt.interface.new_socket("Normal", in_out='INPUT', socket_type='NodeSocketVector')
        g_pt.interface.new_socket("Pixel Pos", in_out='INPUT', socket_type='NodeSocketVector')
        g_pt.interface.new_socket("Light Loc", in_out='INPUT', socket_type='NodeSocketVector')
        g_pt.interface.new_socket("Radius", in_out='INPUT', socket_type='NodeSocketFloat')
        g_pt.interface.new_socket("Fac", in_out='OUTPUT', socket_type='NodeSocketFloat')
        g_pt.interface.new_socket("Falloff", in_out='OUTPUT', socket_type='NodeSocketFloat')

        n_pt = g_pt.nodes; l_pt = g_pt.links
        in_pt = n_pt.new('NodeGroupInput'); in_pt.location = (-1000, 0)
        out_pt = n_pt.new('NodeGroupOutput'); out_pt.location = (800, 0)

        # Высчитываем физическое расстояние от пикселя до лампочки
        vec_dist = n_pt.new('ShaderNodeVectorMath'); vec_dist.operation = 'SUBTRACT'; vec_dist.location = (-800, 100)
        l_pt.new(in_pt.outputs["Light Loc"], vec_dist.inputs[0]); l_pt.new(in_pt.outputs["Pixel Pos"], vec_dist.inputs[1])
        dist = n_pt.new('ShaderNodeVectorMath'); dist.operation = 'LENGTH'; dist.location = (-600, 100)
        l_pt.new(vec_dist.outputs[0], dist.inputs[0])
        
        # Считаем затухание света (Falloff), чтобы он плавно растворялся в пространстве
        div1 = n_pt.new('ShaderNodeMath'); div1.operation = 'DIVIDE'; div1.location = (-400, 100)
        l_pt.new(dist.outputs["Value"], div1.inputs[0]); l_pt.new(in_pt.outputs["Radius"], div1.inputs[1])
        pow1 = n_pt.new('ShaderNodeMath'); pow1.operation = 'POWER'; pow1.inputs[1].default_value = 4.0; pow1.location = (-200, 100)
        l_pt.new(div1.outputs[0], pow1.inputs[0])
        sub1 = n_pt.new('ShaderNodeMath'); sub1.operation = 'SUBTRACT'; sub1.inputs[0].default_value = 1.0; sub1.location = (0, 100)
        l_pt.new(pow1.outputs[0], sub1.inputs[1])
        clamp1 = n_pt.new('ShaderNodeMath'); clamp1.operation = 'MAXIMUM'; clamp1.inputs[1].default_value = 0.0; clamp1.location = (200, 100)
        l_pt.new(sub1.outputs[0], clamp1.inputs[0])
        window = n_pt.new('ShaderNodeMath'); window.operation = 'POWER'; window.inputs[1].default_value = 2.0; window.location = (400, 100)
        l_pt.new(clamp1.outputs[0], window.inputs[0])

        dist_sq = n_pt.new('ShaderNodeMath'); dist_sq.operation = 'POWER'; dist_sq.inputs[1].default_value = 2.0; dist_sq.location = (-200, -100)
        l_pt.new(dist.outputs["Value"], dist_sq.inputs[0])
        dist_safe = n_pt.new('ShaderNodeMath'); dist_safe.operation = 'ADD'; dist_safe.inputs[1].default_value = 0.01; dist_safe.location = (0, -100)
        l_pt.new(dist_sq.outputs[0], dist_safe.inputs[0])
        attenuation = n_pt.new('ShaderNodeMath'); attenuation.operation = 'DIVIDE'; attenuation.inputs[0].default_value = 1.0; attenuation.location = (200, -100)
        l_pt.new(dist_safe.outputs[0], attenuation.inputs[1])

        final_falloff = n_pt.new('ShaderNodeMath'); final_falloff.operation = 'MULTIPLY'; final_falloff.location = (600, 0)
        l_pt.new(window.outputs[0], final_falloff.inputs[0])
        l_pt.new(attenuation.outputs[0], final_falloff.inputs[1])
        l_pt.new(final_falloff.outputs[0], out_pt.inputs["Falloff"])

        norm = n_pt.new('ShaderNodeVectorMath'); norm.operation = 'NORMALIZE'; norm.location = (-600, 300)
        l_pt.new(vec_dist.outputs[0], norm.inputs[0])
        dot_pt = n_pt.new('ShaderNodeVectorMath'); dot_pt.operation = 'DOT_PRODUCT'; dot_pt.location = (-400, 300)
        l_pt.new(in_pt.outputs["Normal"], dot_pt.inputs[0]); l_pt.new(norm.outputs[0], dot_pt.inputs[1])
        
        remap_pt = n_pt.new('ShaderNodeMath'); remap_pt.operation = 'MULTIPLY_ADD'; remap_pt.location = (-200, 300)
        remap_pt.inputs[1].default_value = 0.5; remap_pt.inputs[2].default_value = 0.5
        l_pt.new(dot_pt.outputs["Value"], remap_pt.inputs[0])
        l_pt.new(remap_pt.outputs[0], out_pt.inputs["Fac"])

# ==========================================
# 4. COLOR RAMPS (ЖЕСТКИЕ ПЕРЕХОДЫ)
# ==========================================
# Создаем ноды Color Ramp с интерполяцией CONSTANT. 
# Именно они режут плавный свет на 2-3 жесткие зоны (Highlight, Key, Shade), 
# создавая тот самый мультяшный эффект.
CASCADE_GROUP_VERSION = 7
SPECULAR_GROUP_VERSION = 7 

def hex_to_linear(h_str):
    v = int(h_str, 16) / 255.0
    return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4

def ensure_cascade_group(mat):
    group_name = f"Toon_Cascade_{mat.name}"
    existing = bpy.data.node_groups.get(group_name)
    if existing:
        if existing.get("pop_version") == CASCADE_GROUP_VERSION:
            return existing
        bpy.data.node_groups.remove(existing)

    g = bpy.data.node_groups.new(group_name, 'ShaderNodeTree')
    g.interface.new_socket("Fac", in_out='INPUT', socket_type='NodeSocketFloat')
    g.interface.new_socket("Offset Value", in_out='INPUT', socket_type='NodeSocketFloat')
    g.interface.new_socket("Offset Strength", in_out='INPUT', socket_type='NodeSocketFloat')
    g.interface.new_socket("Level", in_out='OUTPUT', socket_type='NodeSocketFloat')
    g.interface.new_socket("Color", in_out='OUTPUT', socket_type='NodeSocketColor')
    
    nodes = g.nodes; links = g.links
    n_in = nodes.new('NodeGroupInput'); n_in.location = (-600, 0)
    n_out = nodes.new('NodeGroupOutput'); n_out.location = (400, 0)

    centered = nodes.new('ShaderNodeMath'); centered.operation = 'SUBTRACT'; centered.inputs[1].default_value = 0.5; centered.location = (-400, -150)
    links.new(n_in.outputs["Offset Value"], centered.inputs[0])
    
    offset_strength = nodes.new('ShaderNodeMath'); offset_strength.operation = 'MULTIPLY'; offset_strength.location = (-200, -150)
    links.new(centered.outputs[0], offset_strength.inputs[0]); links.new(n_in.outputs["Offset Strength"], offset_strength.inputs[1])
    
    fac_offset = nodes.new('ShaderNodeMath'); fac_offset.operation = 'ADD'; fac_offset.use_clamp = True; fac_offset.location = (0, 0)
    links.new(n_in.outputs["Fac"], fac_offset.inputs[0]); links.new(offset_strength.outputs[0], fac_offset.inputs[1])
    
    ramp = nodes.new('ShaderNodeValToRGB'); ramp.name = "Cascade Ramp"
    
    ramp.color_ramp.interpolation = 'CONSTANT'
    cr = ramp.color_ramp
    c_shadow = hex_to_linear('89'); c_mid = hex_to_linear('BC')
    cr.elements[0].position = 0.0;  cr.elements[0].color = (c_shadow, c_shadow, c_shadow, 1.0)
    cr.elements[1].position = 0.5;  cr.elements[1].color = (c_mid, c_mid, c_mid, 1.0)
    e_a = cr.elements.new(0.75);    e_a.color = (1.0, 1.0, 1.0, 1.0)
    
    ramp.location = (150, 0)
    links.new(fac_offset.outputs[0], ramp.inputs["Fac"])
    
    sep = nodes.new('ShaderNodeSeparateColor'); sep.location = (400, -150)
    links.new(ramp.outputs["Color"], sep.inputs["Color"])
    
    links.new(sep.outputs["Red"], n_out.inputs["Level"]); links.new(ramp.outputs["Color"], n_out.inputs["Color"])
    g["pop_version"] = CASCADE_GROUP_VERSION
    return g

def ensure_specular_group(mat):
    group_name = f"Toon_Specular_{mat.name}"
    existing = bpy.data.node_groups.get(group_name)
    if existing:
        if existing.get("pop_version") == SPECULAR_GROUP_VERSION:
            return existing
        bpy.data.node_groups.remove(existing)

    g = bpy.data.node_groups.new(group_name, 'ShaderNodeTree')
    g.interface.new_socket("Fac", in_out='INPUT', socket_type='NodeSocketFloat') 
    g.interface.new_socket("Exponent", in_out='INPUT', socket_type='NodeSocketFloat') 
    g.interface.new_socket("Offset Value", in_out='INPUT', socket_type='NodeSocketFloat')
    g.interface.new_socket("Offset Strength", in_out='INPUT', socket_type='NodeSocketFloat')
    g.interface.new_socket("Level", in_out='OUTPUT', socket_type='NodeSocketFloat')
    nodes = g.nodes; links = g.links
    n_in = nodes.new('NodeGroupInput'); n_in.location = (-800, 0)
    n_out = nodes.new('NodeGroupOutput'); n_out.location = (600, 0)

    pow_node = nodes.new('ShaderNodeMath'); pow_node.operation = 'POWER'; pow_node.inputs[1].default_value = 5.29; pow_node.location = (-600, 150)
    links.new(n_in.outputs["Exponent"], pow_node.inputs[0])

    cutoff_node = nodes.new('ShaderNodeMath'); cutoff_node.operation = 'SUBTRACT'; cutoff_node.inputs[0].default_value = 1.001; cutoff_node.location = (-400, 150)
    links.new(pow_node.outputs[0], cutoff_node.inputs[1])

    sub_fac = nodes.new('ShaderNodeMath'); sub_fac.operation = 'SUBTRACT'; sub_fac.location = (-200, 50)
    links.new(n_in.outputs["Fac"], sub_fac.inputs[0])
    links.new(cutoff_node.outputs[0], sub_fac.inputs[1])

    add_offset = nodes.new('ShaderNodeMath'); add_offset.operation = 'ADD'; add_offset.inputs[1].default_value = 0.5; add_offset.location = (0, 50)
    links.new(sub_fac.outputs[0], add_offset.inputs[0])

    centered = nodes.new('ShaderNodeMath'); centered.operation = 'SUBTRACT'; centered.inputs[1].default_value = 0.5; centered.location = (-400, -150)
    links.new(n_in.outputs["Offset Value"], centered.inputs[0])
    
    offset_strength = nodes.new('ShaderNodeMath'); offset_strength.operation = 'MULTIPLY'; offset_strength.location = (-200, -150)
    links.new(centered.outputs[0], offset_strength.inputs[0]); links.new(n_in.outputs["Offset Strength"], offset_strength.inputs[1])
    
    fac_offset = nodes.new('ShaderNodeMath'); fac_offset.operation = 'ADD'; fac_offset.use_clamp = True; fac_offset.location = (200, 0)
    links.new(add_offset.outputs[0], fac_offset.inputs[0]); links.new(offset_strength.outputs[0], fac_offset.inputs[1])
    
    ramp = nodes.new('ShaderNodeValToRGB'); ramp.name = "Specular Ramp"
    
    ramp.color_ramp.interpolation = 'CONSTANT'
    cr = ramp.color_ramp
    cr.elements[0].position = 0.0;  cr.elements[0].color = (0.0, 0.0, 0.0, 1.0)
    cr.elements[1].position = 0.5;  cr.elements[1].color = (1.0, 1.0, 1.0, 1.0)
    
    ramp.location = (400, 0)
    links.new(fac_offset.outputs[0], ramp.inputs["Fac"])
    
    sep2 = nodes.new('ShaderNodeSeparateColor'); sep2.location = (650, 0)
    links.new(ramp.outputs["Color"], sep2.inputs["Color"]); links.new(sep2.outputs["Red"], n_out.inputs["Level"])
    
    g["pop_version"] = SPECULAR_GROUP_VERSION
    return g

# ==========================================
# 5. СБОРКА ОСНОВНОГО ГРАФА (ФРАНКЕНШТЕЙН)
# ==========================================
class POP_OT_UpdateShaders(bpy.types.Operator):
    bl_idname = "pop.update_shaders"
    bl_label = "Update Pop Shaders"
    bl_description = "Собрать Cel-Shading для выделенных материалов"

    def execute(self, context):
        obj = context.active_object
        if not obj: return {'CANCELLED'}
        selected_mats = [slot.material for slot in obj.material_slots if slot.material and slot.material.pop_is_selected]
        if not selected_mats:
            mat_idx = context.scene.pop_mat_index
            if len(obj.material_slots) > mat_idx and obj.material_slots[mat_idx].material:
                selected_mats = [obj.material_slots[mat_idx].material]
        if not selected_mats:
            self.report({'WARNING'}, "Нет материалов для обновления!")
            return {'CANCELLED'}

        ensure_math_groups()
        for mat in selected_mats:
            sync_lights(mat)
            cascade_group = ensure_cascade_group(mat)
            spec_group = ensure_specular_group(mat)
            self.build_cel_shader(mat, obj, cascade_group, spec_group)
        self.report({'INFO'}, f"Обновлено материалов: {len(selected_mats)}")
        return {'FINISHED'}

    def build_cel_shader(self, mat, obj, cascade_group, spec_group):
        # СЕРДЦЕ МОНСТРА! 
        # Здесь мы динамически прописываем логику освещения в шейдер.
        mat.use_nodes = True
        
        master_group_name = f"Substrate_Toon_BSDF_{mat.name}"
        is_master_new = False
        
        if master_group_name not in bpy.data.node_groups:
            master_group = bpy.data.node_groups.new(master_group_name, 'ShaderNodeTree')
            is_master_new = True
        else:
            master_group = bpy.data.node_groups[master_group_name]
            master_group.nodes.clear()
            is_master_new = False
            
        if is_master_new:
            def new_sock(name, s_type, default=None):
                if hasattr(master_group, 'interface'):
                    s = master_group.interface.new_socket(name, in_out='INPUT', socket_type=s_type)
                else:
                    s = master_group.inputs.new(s_type, name)
                if default is not None: s.default_value = default
                
            new_sock("BaseColor", 'NodeSocketColor', (0.9, 0.9, 0.9, 1.0))
            new_sock("Metallic", 'NodeSocketFloat', 0.5)
            new_sock("Specular", 'NodeSocketFloat', 0.5)
            new_sock("Roughness", 'NodeSocketFloat', 0.5)
            new_sock("Normal", 'NodeSocketVector', (0.0, 0.0, 0.0))
            new_sock("EmissiveColor", 'NodeSocketColor', (0.0, 0.0, 0.0, 1.0))
            
            new_sock("Diffuse Offset Strength", 'NodeSocketFloat', 0.0)
            new_sock("Diffuse Offset Map", 'NodeSocketFloat', 0.5)
            new_sock("Spec Offset Strength", 'NodeSocketFloat', 0.0)
            new_sock("Spec Offset Map", 'NodeSocketFloat', 0.5)
            new_sock("Hatch Strength", 'NodeSocketFloat', 0.0)
            new_sock("Hatch Map", 'NodeSocketFloat', 1.0)
            
            if hasattr(master_group, 'interface'):
                master_group.interface.new_socket("BSDF", in_out='OUTPUT', socket_type='NodeSocketShader')
            else:
                master_group.outputs.new('NodeSocketShader', "BSDF")

        m_nodes = master_group.nodes; m_links = master_group.links
        def new_pop_node(node_type, location):
            n = m_nodes.new(node_type); n.location = location; return n

        group_in = new_pop_node('NodeGroupInput', (-2500, 0))
        group_out = new_pop_node('NodeGroupOutput', (3000, 0))

        geo = new_pop_node("ShaderNodeNewGeometry", (-2200, -200))
        view_dir = geo.outputs["Incoming"]

        # Если юзер включил тени, мы будем пускать физический луч (Raycast).
        # Но чтобы луч не врезался в саму поверхность, откуда стартует, мы делаем ray_offset.
        ray_offset = new_pop_node("ShaderNodeVectorMath", (-1800, -400))
        ray_offset.operation = 'MULTIPLY_ADD'; ray_offset.inputs[1].default_value = (0.01, 0.01, 0.01)
        m_links.new(geo.outputs["Normal"], ray_offset.inputs[0]); m_links.new(geo.outputs["Position"], ray_offset.inputs[2])

        norm_len = new_pop_node("ShaderNodeVectorMath", (-1800, -200)); norm_len.operation = 'LENGTH'
        m_links.new(group_in.outputs["Normal"], norm_len.inputs[0])
        norm_mask = new_pop_node("ShaderNodeMath", (-1600, -200)); norm_mask.operation = 'GREATER_THAN'; norm_mask.inputs[1].default_value = 0.001
        m_links.new(norm_len.outputs["Value"], norm_mask.inputs[0])
        norm_mix = new_pop_node("ShaderNodeMix", (-1400, -200)); norm_mix.data_type = 'VECTOR'
        m_links.new(norm_mask.outputs[0], norm_mix.inputs[0])
        m_links.new(geo.outputs["Normal"], norm_mix.inputs[4]); m_links.new(group_in.outputs["Normal"], norm_mix.inputs[5])
        active_normal_socket = norm_mix.outputs[1]

        spec_pbr_mult = new_pop_node("ShaderNodeMath", (-2200, 600)); spec_pbr_mult.operation = 'MULTIPLY'; spec_pbr_mult.inputs[1].default_value = 0.08
        m_links.new(group_in.outputs["Specular"], spec_pbr_mult.inputs[0])
        
        f0_diel = new_pop_node("ShaderNodeCombineXYZ", (-2000, 600))
        for i in range(3): m_links.new(spec_pbr_mult.outputs[0], f0_diel.inputs[i])
        
        inv_met = new_pop_node("ShaderNodeMath", (-2000, 500)); inv_met.operation = 'SUBTRACT'; inv_met.inputs[0].default_value = 1.0
        m_links.new(group_in.outputs["Metallic"], inv_met.inputs[1])
        
        term1 = new_pop_node("ShaderNodeVectorMath", (-1800, 600)); term1.operation = 'MULTIPLY'
        m_links.new(f0_diel.outputs[0], term1.inputs[0]); m_links.new(inv_met.outputs[0], term1.inputs[1])

        met_vec = new_pop_node("ShaderNodeCombineXYZ", (-2000, 400))
        for i in range(3): m_links.new(group_in.outputs["Metallic"], met_vec.inputs[i])

        term2 = new_pop_node("ShaderNodeVectorMath", (-1800, 450)); term2.operation = 'MULTIPLY'
        m_links.new(group_in.outputs["BaseColor"], term2.inputs[0]); m_links.new(met_vec.outputs[0], term2.inputs[1])

        f0_mix_color = new_pop_node("ShaderNodeVectorMath", (-1600, 550)); f0_mix_color.operation = 'ADD'
        m_links.new(term1.outputs[0], f0_mix_color.inputs[0]); m_links.new(term2.outputs[0], f0_mix_color.inputs[1])

        enabled_names = [l.name for l in mat.pop_lights if l.is_enabled]
        enabled_objs = [bpy.data.objects.get(n) for n in enabled_names if bpy.data.objects.get(n)]
        suns = [o for o in enabled_objs if o.data.type == 'SUN']
        points = [o for o in enabled_objs if o.data.type != 'SUN']

        spec_contrib = None
        if suns:
            # Обработка Солнца. Извлекаем вектор направления через драйверы.
            key_sun = suns[0]
            sun_rot = new_pop_node("ShaderNodeCombineXYZ", (-1000, 300))
            for i, axis in enumerate(['X', 'Y', 'Z']):
                drv = sun_rot.inputs[i].driver_add('default_value').driver
                var = drv.variables.new(); var.name = 'rot'; var.type = 'TRANSFORMS'
                var.targets[0].id, var.targets[0].transform_type, var.targets[0].transform_space = key_sun, f'ROT_{axis}', 'WORLD_SPACE'
                drv.expression = 'rot'

            vec_rot = new_pop_node("ShaderNodeVectorRotate", (-800, 300)); vec_rot.rotation_type = 'EULER_XYZ'; vec_rot.inputs[0].default_value = (0.0, 0.0, 1.0)
            m_links.new(sun_rot.outputs[0], vec_rot.inputs["Rotation"])
            hack_sun = new_pop_node("ShaderNodeVectorMath", (-600, 300)); hack_sun.operation = 'ADD'
            m_links.new(vec_rot.outputs[0], hack_sun.inputs[0])

            dtc = new_pop_node("ShaderNodeTexCoord", (-1000, 150)); dtc.object = key_sun
            dmul = new_pop_node("ShaderNodeVectorMath", (-800, 150)); dmul.operation = 'MULTIPLY'; dmul.inputs[1].default_value = (0.0, 0.0, 0.0)
            m_links.new(dtc.outputs["Object"], dmul.inputs[0]); m_links.new(dmul.outputs[0], hack_sun.inputs[1])

            sun_math = new_pop_node("ShaderNodeGroup", (-400, 300)); sun_math.node_tree = bpy.data.node_groups["Toon_Sun_Math_V2"]
            m_links.new(active_normal_socket, sun_math.inputs["Normal"]); m_links.new(hack_sun.outputs[0], sun_math.inputs["Sun Dir"])

            final_sun_fac = sun_math.outputs["Fac"]
            raycast_mask_node = None
            
            # РАЙКАСТ (ТЕНИ)!
            # Если луч во что-то воткнулся - значит мы в тени, обнуляем освещение.
            if mat.pop_receive_shadows and hasattr(bpy.types, 'ShaderNodeRaycast'):
                sun_ray = new_pop_node("ShaderNodeRaycast", (-350, 450))
                m_links.new(ray_offset.outputs[0], sun_ray.inputs[0])
                m_links.new(hack_sun.outputs[0], sun_ray.inputs[1])   
                sun_ray_inv = new_pop_node("ShaderNodeMath", (-150, 450)); sun_ray_inv.operation = 'SUBTRACT'; sun_ray_inv.inputs[0].default_value = 1.0
                m_links.new(sun_ray.outputs[0], sun_ray_inv.inputs[1])
                raycast_mask_node = sun_ray_inv.outputs[0]
                sun_mask_mult = new_pop_node("ShaderNodeMath", (-50, 300)); sun_mask_mult.operation = 'MULTIPLY'
                m_links.new(sun_math.outputs["Fac"], sun_mask_mult.inputs[0]); m_links.new(raycast_mask_node, sun_mask_mult.inputs[1])
                final_sun_fac = sun_mask_mult.outputs[0]

            cascade_sun = new_pop_node("ShaderNodeGroup", (100, 300)); cascade_sun.node_tree = cascade_group
            m_links.new(final_sun_fac, cascade_sun.inputs["Fac"])
            m_links.new(group_in.outputs["Diffuse Offset Strength"], cascade_sun.inputs["Offset Strength"])
            m_links.new(group_in.outputs["Diffuse Offset Map"], cascade_sun.inputs["Offset Value"])

            sun_col = new_pop_node("ShaderNodeCombineXYZ", (200, 550))
            for i in range(3):
                d = sun_col.inputs[i].driver_add("default_value").driver; d.type = 'AVERAGE'
                v = d.variables.new(); v.targets[0].id = key_sun; v.targets[0].data_path = f"data.color[{i}]"

            sun_tinted = new_pop_node("ShaderNodeVectorMath", (500, 400)); sun_tinted.operation = 'MULTIPLY'
            m_links.new(cascade_sun.outputs["Color"], sun_tinted.inputs[0]); m_links.new(sun_col.outputs[0], sun_tinted.inputs[1])

            shadow_depth = new_pop_node("ShaderNodeMath", (500, 200)); shadow_depth.operation = 'SUBTRACT'; shadow_depth.inputs[0].default_value = 1.0
            m_links.new(cascade_sun.outputs["Level"], shadow_depth.inputs[1])

            hatch_ink = new_pop_node("ShaderNodeMath", (1100, -100)); hatch_ink.operation = 'SUBTRACT'; hatch_ink.inputs[0].default_value = 1.0
            m_links.new(group_in.outputs["Hatch Map"], hatch_ink.inputs[1])
            hatch_pattern = new_pop_node("ShaderNodeMath", (1250, -50)); hatch_pattern.operation = 'MULTIPLY'
            m_links.new(hatch_ink.outputs[0], hatch_pattern.inputs[0]); m_links.new(shadow_depth.outputs[0], hatch_pattern.inputs[1])

            hatch_strength_node = new_pop_node("ShaderNodeMath", (1400, 100)); hatch_strength_node.operation = 'MULTIPLY'
            m_links.new(hatch_pattern.outputs[0], hatch_strength_node.inputs[0]); m_links.new(group_in.outputs["Hatch Strength"], hatch_strength_node.inputs[1])
            hatch_inv = new_pop_node("ShaderNodeMath", (1550, 100)); hatch_inv.operation = 'SUBTRACT'; hatch_inv.inputs[0].default_value = 1.0
            m_links.new(hatch_strength_node.outputs[0], hatch_inv.inputs[1])
            
            sun_hatched = new_pop_node("ShaderNodeVectorMath", (1700, 400)); sun_hatched.operation = 'MULTIPLY'
            m_links.new(sun_tinted.outputs[0], sun_hatched.inputs[0]); m_links.new(hatch_inv.outputs[0], sun_hatched.inputs[1])
            
            sun_diffuse_out = sun_hatched.outputs[0]

            half_vec = new_pop_node("ShaderNodeVectorMath", (400, 900)); half_vec.operation = 'ADD'
            m_links.new(view_dir, half_vec.inputs[0]); m_links.new(hack_sun.outputs[0], half_vec.inputs[1])
            half_norm = new_pop_node("ShaderNodeVectorMath", (550, 900)); half_norm.operation = 'NORMALIZE'
            m_links.new(half_vec.outputs[0], half_norm.inputs[0])
            n_dot_h = new_pop_node("ShaderNodeVectorMath", (700, 900)); n_dot_h.operation = 'DOT_PRODUCT'
            m_links.new(active_normal_socket, n_dot_h.inputs[0]); m_links.new(half_norm.outputs[0], n_dot_h.inputs[1])
            n_dot_h_clamped = new_pop_node("ShaderNodeMath", (850, 900)); n_dot_h_clamped.operation = 'MAXIMUM'; n_dot_h_clamped.inputs[1].default_value = 0.0
            m_links.new(n_dot_h.outputs["Value"], n_dot_h_clamped.inputs[0])

            final_spec_fac = n_dot_h_clamped.outputs[0]
            if raycast_mask_node:
                spec_ray_mult = new_pop_node("ShaderNodeMath", (1000, 950)); spec_ray_mult.operation = 'MULTIPLY'
                m_links.new(final_spec_fac, spec_ray_mult.inputs[0]); m_links.new(raycast_mask_node, spec_ray_mult.inputs[1])
                final_spec_fac = spec_ray_mult.outputs[0]

            cascade_spec = new_pop_node("ShaderNodeGroup", (1150, 900)); cascade_spec.node_tree = spec_group
            m_links.new(final_spec_fac, cascade_spec.inputs["Fac"])
            m_links.new(group_in.outputs["Roughness"], cascade_spec.inputs["Exponent"])
            m_links.new(group_in.outputs["Spec Offset Strength"], cascade_spec.inputs["Offset Strength"])
            m_links.new(group_in.outputs["Spec Offset Map"], cascade_spec.inputs["Offset Value"])

            spec_level = new_pop_node("ShaderNodeVectorMath", (1400, 900)); spec_level.operation = 'MULTIPLY'
            m_links.new(cascade_spec.outputs["Level"], spec_level.inputs[0]); m_links.new(f0_mix_color.outputs[0], spec_level.inputs[1])
            
            spec_contrib_node = new_pop_node("ShaderNodeVectorMath", (1550, 900)); spec_contrib_node.operation = 'MULTIPLY'
            m_links.new(spec_level.outputs[0], spec_contrib_node.inputs[0]); m_links.new(sun_col.outputs[0], spec_contrib_node.inputs[1])

            spec_mask_node = new_pop_node("ShaderNodeMath", (1550, 750)); spec_mask_node.operation = 'GREATER_THAN'; spec_mask_node.inputs[1].default_value = 0.501
            m_links.new(final_sun_fac, spec_mask_node.inputs[0])
            
            spec_masked = new_pop_node("ShaderNodeVectorMath", (1700, 900)); spec_masked.operation = 'MULTIPLY'
            m_links.new(spec_contrib_node.outputs[0], spec_masked.inputs[0]); m_links.new(spec_mask_node.outputs[0], spec_masked.inputs[1])
            spec_contrib = spec_masked.outputs[0]
        else:
            fallback_illum = new_pop_node("ShaderNodeCombineXYZ", (1700, 400))
            sun_diffuse_out = fallback_illum.outputs[0]

        last_accum = None
        last_spec_accum = None
        
        # Самая тяжелая часть и суть нашего шейдера. Циклом пробегаемся по всем локальным лампочкам.
        # Вместо того чтобы брать общую "кашу" освещения, мы для каждой лампы индивидуально
        # высчитываем вектор, пускаем Raycast для тени и прогоняем результат через ColorRamp (каскад).
        # Только так свет ложится идеально ровными мультяшными полосками, не смешиваясь в грязь.
        # Да, нодовый граф разрастается до небес, но зато мы обманули систему! (⌐■_■)
        for i, light_obj in enumerate(points):
            y = -700 - 800 * i
            if not light_obj.data.use_custom_distance:
                light_obj.data.use_custom_distance = True; light_obj.data.cutoff_distance = 10.0
            
            is_spot = light_obj.data.type == 'SPOT'
            is_area = light_obj.data.type == 'AREA'

            light_loc = new_pop_node("ShaderNodeCombineXYZ", (-1000, y))
            for ax_i, axis in enumerate(['X', 'Y', 'Z']):
                drv = light_loc.inputs[ax_i].driver_add('default_value').driver
                var = drv.variables.new(); var.name = 'loc'; var.type = 'TRANSFORMS'
                var.targets[0].id, var.targets[0].transform_type, var.targets[0].transform_space = light_obj, f'LOC_{axis}', 'WORLD_SPACE'
                drv.expression = 'loc'
            
            radius_val = new_pop_node("ShaderNodeValue", (-1000, y - 300))
            d_r = radius_val.outputs[0].driver_add("default_value").driver; d_r.type = 'AVERAGE'
            v_r = d_r.variables.new(); v_r.targets[0].id = light_obj; v_r.targets[0].data_path = "data.cutoff_distance"
            radius_safe = new_pop_node("ShaderNodeMath", (-850, y - 300)); radius_safe.operation = 'MAXIMUM'; radius_safe.inputs[1].default_value = 0.05
            m_links.new(radius_val.outputs[0], radius_safe.inputs[0])

            intensity_val = new_pop_node("ShaderNodeValue", (-1000, y - 400))
            d_i = intensity_val.outputs[0].driver_add("default_value").driver; d_i.type = 'AVERAGE'
            v_i = d_i.variables.new(); v_i.targets[0].id = light_obj; v_i.targets[0].data_path = "data.energy"

            intensity_norm = new_pop_node("ShaderNodeMath", (-850, y - 400)); intensity_norm.operation = 'DIVIDE'
            intensity_norm.inputs[1].default_value = 10.0
            m_links.new(intensity_val.outputs[0], intensity_norm.inputs[0])

            pt_math = new_pop_node("ShaderNodeGroup", (-600, y)); pt_math.node_tree = bpy.data.node_groups["Toon_Point_Math_V4"]
            m_links.new(active_normal_socket, pt_math.inputs["Normal"])
            m_links.new(geo.outputs["Position"], pt_math.inputs["Pixel Pos"])
            m_links.new(light_loc.outputs[0], pt_math.inputs["Light Loc"])
            m_links.new(radius_safe.outputs[0], pt_math.inputs["Radius"])

            pt_ray_dir = new_pop_node("ShaderNodeVectorMath", (-500, y+100)); pt_ray_dir.operation = 'SUBTRACT'
            m_links.new(light_loc.outputs[0], pt_ray_dir.inputs[0]); m_links.new(geo.outputs["Position"], pt_ray_dir.inputs[1])

            pt_hit_inv_out = None
            if mat.pop_receive_shadows and hasattr(bpy.types, 'ShaderNodeRaycast'):
                pt_ray_len = new_pop_node("ShaderNodeVectorMath", (-300, y+150)); pt_ray_len.operation = 'LENGTH'
                m_links.new(pt_ray_dir.outputs[0], pt_ray_len.inputs[0])
                pt_ray = new_pop_node("ShaderNodeRaycast", (-100, y+100))
                m_links.new(ray_offset.outputs[0], pt_ray.inputs[0]); m_links.new(pt_ray_dir.outputs[0], pt_ray.inputs[1])
                m_links.new(pt_ray_len.outputs["Value"], pt_ray.inputs[2])
                pt_hit_inv = new_pop_node("ShaderNodeMath", (50, y+100)); pt_hit_inv.operation = 'SUBTRACT'; pt_hit_inv.inputs[0].default_value = 1.0
                m_links.new(pt_ray.outputs[0], pt_hit_inv.inputs[1])
                pt_hit_inv_out = pt_hit_inv.outputs[0]

            final_pt_fac = pt_math.outputs["Fac"]

            cascade_pt = new_pop_node("ShaderNodeGroup", (250, y)); cascade_pt.node_tree = cascade_group
            m_links.new(final_pt_fac, cascade_pt.inputs["Fac"])
            m_links.new(group_in.outputs["Diffuse Offset Strength"], cascade_pt.inputs["Offset Strength"])
            m_links.new(group_in.outputs["Diffuse Offset Map"], cascade_pt.inputs["Offset Value"])

            cascade_pt_zero = new_pop_node("ShaderNodeGroup", (250, y-200)); cascade_pt_zero.node_tree = cascade_group
            cascade_pt_zero.inputs["Fac"].default_value = 0.0
            m_links.new(group_in.outputs["Diffuse Offset Strength"], cascade_pt_zero.inputs["Offset Strength"])
            m_links.new(group_in.outputs["Diffuse Offset Map"], cascade_pt_zero.inputs["Offset Value"])

            pt_pure_light = new_pop_node("ShaderNodeVectorMath", (450, y-100)); pt_pure_light.operation = 'SUBTRACT'
            m_links.new(cascade_pt.outputs["Color"], pt_pure_light.inputs[0])
            m_links.new(cascade_pt_zero.outputs["Color"], pt_pure_light.inputs[1])
            
            pt_pure_light_clamp = new_pop_node("ShaderNodeVectorMath", (600, y-100)); pt_pure_light_clamp.operation = 'MAXIMUM'
            m_links.new(pt_pure_light.outputs[0], pt_pure_light_clamp.inputs[0])
            pt_pure_light_clamp.inputs[1].default_value = (0.0, 0.0, 0.0)

            pt_falloff_energy = new_pop_node("ShaderNodeMath", (600, y-250)); pt_falloff_energy.operation = 'MULTIPLY'
            m_links.new(pt_math.outputs["Falloff"], pt_falloff_energy.inputs[0])
            m_links.new(intensity_norm.outputs[0], pt_falloff_energy.inputs[1])

            pt_mask_final = pt_falloff_energy.outputs[0]
            if pt_hit_inv_out:
                pt_ray_mask = new_pop_node("ShaderNodeMath", (750, y-250)); pt_ray_mask.operation = 'MULTIPLY'
                m_links.new(pt_mask_final, pt_ray_mask.inputs[0])
                m_links.new(pt_hit_inv_out, pt_ray_mask.inputs[1])
                pt_mask_final = pt_ray_mask.outputs[0]
                
            if is_spot or is_area:
                light_rot = new_pop_node("ShaderNodeCombineXYZ", (-1000, y - 500))
                for ax_i, axis in enumerate(['X', 'Y', 'Z']):
                    drv = light_rot.inputs[ax_i].driver_add('default_value').driver
                    var = drv.variables.new(); var.name = 'rot'; var.type = 'TRANSFORMS'
                    var.targets[0].id, var.targets[0].transform_type, var.targets[0].transform_space = light_obj, f'ROT_{axis}', 'WORLD_SPACE'
                    drv.expression = 'rot'
                
                vec_rot = new_pop_node("ShaderNodeVectorRotate", (-800, y - 500))
                vec_rot.rotation_type = 'EULER_XYZ'; vec_rot.inputs[0].default_value = (0.0, 0.0, -1.0)
                m_links.new(light_rot.outputs[0], vec_rot.inputs["Rotation"])
                
                to_pixel = new_pop_node("ShaderNodeVectorMath", (-800, y - 600)); to_pixel.operation = 'SUBTRACT'
                m_links.new(geo.outputs["Position"], to_pixel.inputs[0]); m_links.new(light_loc.outputs[0], to_pixel.inputs[1])
                
                to_pixel_norm = new_pop_node("ShaderNodeVectorMath", (-600, y - 600)); to_pixel_norm.operation = 'NORMALIZE'
                m_links.new(to_pixel.outputs[0], to_pixel_norm.inputs[0])
                
                spot_dot = new_pop_node("ShaderNodeVectorMath", (-400, y - 500)); spot_dot.operation = 'DOT_PRODUCT'
                m_links.new(to_pixel_norm.outputs[0], spot_dot.inputs[0]); m_links.new(vec_rot.outputs[0], spot_dot.inputs[1])
                
                dir_mask_out = None
                if is_area:
                    area_mask = new_pop_node("ShaderNodeMath", (-200, y - 500)); area_mask.operation = 'MAXIMUM'; area_mask.inputs[1].default_value = 0.0
                    m_links.new(spot_dot.outputs["Value"], area_mask.inputs[0])
                    dir_mask_out = area_mask.outputs[0]
                elif is_spot:
                    spot_size = new_pop_node("ShaderNodeValue", (-1000, y - 650))
                    d_sz = spot_size.outputs[0].driver_add("default_value").driver; d_sz.type = 'AVERAGE'
                    v_sz = d_sz.variables.new(); v_sz.targets[0].id = light_obj; v_sz.targets[0].data_path = "data.spot_size"
                    
                    spot_blend = new_pop_node("ShaderNodeValue", (-1000, y - 750))
                    d_bl = spot_blend.outputs[0].driver_add("default_value").driver; d_bl.type = 'AVERAGE'
                    v_bl = d_bl.variables.new(); v_bl.targets[0].id = light_obj; v_bl.targets[0].data_path = "data.spot_blend"
                    
                    half_size = new_pop_node("ShaderNodeMath", (-800, y - 650)); half_size.operation = 'MULTIPLY'; half_size.inputs[1].default_value = 0.5
                    m_links.new(spot_size.outputs[0], half_size.inputs[0])
                    outer_cone = new_pop_node("ShaderNodeMath", (-600, y - 650)); outer_cone.operation = 'COSINE'
                    m_links.new(half_size.outputs[0], outer_cone.inputs[0])
                    
                    inv_blend = new_pop_node("ShaderNodeMath", (-800, y - 750)); inv_blend.operation = 'SUBTRACT'; inv_blend.inputs[0].default_value = 1.0
                    m_links.new(spot_blend.outputs[0], inv_blend.inputs[1])
                    inner_angle = new_pop_node("ShaderNodeMath", (-600, y - 750)); inner_angle.operation = 'MULTIPLY'
                    m_links.new(half_size.outputs[0], inner_angle.inputs[0]); m_links.new(inv_blend.outputs[0], inner_angle.inputs[1])
                    inner_cone = new_pop_node("ShaderNodeMath", (-400, y - 750)); inner_cone.operation = 'COSINE'
                    m_links.new(inner_angle.outputs[0], inner_cone.inputs[0])
                    
                    spot_mask = new_pop_node("ShaderNodeMapRange", (-200, y - 600)); spot_mask.interpolation_type = 'SMOOTHSTEP'; spot_mask.clamp = True
                    m_links.new(spot_dot.outputs["Value"], spot_mask.inputs[0])
                    m_links.new(outer_cone.outputs[0], spot_mask.inputs[1])
                    m_links.new(inner_cone.outputs[0], spot_mask.inputs[2])
                    dir_mask_out = spot_mask.outputs[0]

                dir_mask_mult = new_pop_node("ShaderNodeMath", (850, y - 300)); dir_mask_mult.operation = 'MULTIPLY'
                m_links.new(pt_mask_final, dir_mask_mult.inputs[0]); m_links.new(dir_mask_out, dir_mask_mult.inputs[1])
                pt_mask_final = dir_mask_mult.outputs[0]

            light_col = new_pop_node("ShaderNodeCombineXYZ", (600, y - 400))
            for ci in range(3):
                d_c = light_col.inputs[ci].driver_add("default_value").driver; d_c.type = 'AVERAGE'
                v_c = d_c.variables.new(); v_c.targets[0].id = light_obj; v_c.targets[0].data_path = f"data.color[{ci}]"

            tinted_col = new_pop_node("ShaderNodeVectorMath", (900, y-100)); tinted_col.operation = 'MULTIPLY'
            m_links.new(pt_pure_light_clamp.outputs[0], tinted_col.inputs[0]); m_links.new(light_col.outputs[0], tinted_col.inputs[1])
            
            pt_diffuse_final = new_pop_node("ShaderNodeVectorMath", (1050, y-100)); pt_diffuse_final.operation = 'MULTIPLY'
            m_links.new(tinted_col.outputs[0], pt_diffuse_final.inputs[0])
            m_links.new(pt_mask_final, pt_diffuse_final.inputs[1])

            if last_accum is None: last_accum = pt_diffuse_final.outputs[0]
            else:
                add_node = new_pop_node("ShaderNodeVectorMath", (1200, y-100)); add_node.operation = 'ADD'
                m_links.new(last_accum, add_node.inputs[0]); m_links.new(pt_diffuse_final.outputs[0], add_node.inputs[1])
                last_accum = add_node.outputs[0]

            # --- SPECULAR ---
            pt_dir_norm = new_pop_node("ShaderNodeVectorMath", (-300, y+250)); pt_dir_norm.operation = 'NORMALIZE'
            m_links.new(pt_ray_dir.outputs[0], pt_dir_norm.inputs[0])
            pt_half_vec = new_pop_node("ShaderNodeVectorMath", (-150, y+250)); pt_half_vec.operation = 'ADD'
            m_links.new(view_dir, pt_half_vec.inputs[0]); m_links.new(pt_dir_norm.outputs[0], pt_half_vec.inputs[1])
            pt_half_norm = new_pop_node("ShaderNodeVectorMath", (0, y+250)); pt_half_norm.operation = 'NORMALIZE'
            m_links.new(pt_half_vec.outputs[0], pt_half_norm.inputs[0])
            pt_n_dot_h = new_pop_node("ShaderNodeVectorMath", (150, y+250)); pt_n_dot_h.operation = 'DOT_PRODUCT'
            m_links.new(active_normal_socket, pt_n_dot_h.inputs[0]); m_links.new(pt_half_norm.outputs[0], pt_n_dot_h.inputs[1])
            pt_n_dot_h_clamped = new_pop_node("ShaderNodeMath", (300, y+250)); pt_n_dot_h_clamped.operation = 'MAXIMUM'; pt_n_dot_h_clamped.inputs[1].default_value = 0.0
            m_links.new(pt_n_dot_h.outputs["Value"], pt_n_dot_h_clamped.inputs[0])

            pt_cascade_spec = new_pop_node("ShaderNodeGroup", (600, y+300)); pt_cascade_spec.node_tree = spec_group
            m_links.new(pt_n_dot_h_clamped.outputs[0], pt_cascade_spec.inputs["Fac"])
            m_links.new(group_in.outputs["Roughness"], pt_cascade_spec.inputs["Exponent"])
            m_links.new(group_in.outputs["Spec Offset Strength"], pt_cascade_spec.inputs["Offset Strength"])
            m_links.new(group_in.outputs["Spec Offset Map"], pt_cascade_spec.inputs["Offset Value"])

            pt_spec_level = new_pop_node("ShaderNodeVectorMath", (750, y+300)); pt_spec_level.operation = 'MULTIPLY'
            m_links.new(pt_cascade_spec.outputs["Level"], pt_spec_level.inputs[0]); m_links.new(f0_mix_color.outputs[0], pt_spec_level.inputs[1])

            pt_spec_col = new_pop_node("ShaderNodeVectorMath", (900, y+300)); pt_spec_col.operation = 'MULTIPLY'
            m_links.new(pt_spec_level.outputs[0], pt_spec_col.inputs[0]); m_links.new(light_col.outputs[0], pt_spec_col.inputs[1])
            
            pt_spec_intensity = new_pop_node("ShaderNodeVectorMath", (1050, y+300)); pt_spec_intensity.operation = 'MULTIPLY'
            m_links.new(pt_spec_col.outputs[0], pt_spec_intensity.inputs[0]); m_links.new(pt_mask_final, pt_spec_intensity.inputs[1])

            pt_spec_nl_mask = new_pop_node("ShaderNodeMath", (900, y+150)); pt_spec_nl_mask.operation = 'GREATER_THAN'; pt_spec_nl_mask.inputs[1].default_value = 0.501
            m_links.new(final_pt_fac, pt_spec_nl_mask.inputs[0])

            pt_spec_masked = new_pop_node("ShaderNodeVectorMath", (1200, y+300)); pt_spec_masked.operation = 'MULTIPLY'
            m_links.new(pt_spec_intensity.outputs[0], pt_spec_masked.inputs[0]); m_links.new(pt_spec_nl_mask.outputs[0], pt_spec_masked.inputs[1])

            if last_spec_accum is None: last_spec_accum = pt_spec_masked.outputs[0]
            else:
                add_spec_node = new_pop_node("ShaderNodeVectorMath", (1350, y+300)); add_spec_node.operation = 'ADD'
                m_links.new(last_spec_accum, add_spec_node.inputs[0]); m_links.new(pt_spec_masked.outputs[0], add_spec_node.inputs[1])
                last_spec_accum = add_spec_node.outputs[0]

        total_illum = sun_diffuse_out
        if last_accum is not None:
            add_pts = new_pop_node("ShaderNodeVectorMath", (1900, 300)); add_pts.operation = 'ADD'
            m_links.new(total_illum, add_pts.inputs[0]); m_links.new(last_accum, add_pts.inputs[1])
            total_illum = add_pts.outputs[0]

        apply_base_color = new_pop_node("ShaderNodeVectorMath", (2050, 300)); apply_base_color.operation = 'MULTIPLY'
        m_links.new(total_illum, apply_base_color.inputs[0]); m_links.new(group_in.outputs["BaseColor"], apply_base_color.inputs[1])
        final_diffuse = apply_base_color.outputs[0]

        inv_met_vec = new_pop_node("ShaderNodeCombineXYZ", (2050, 450))
        for i in range(3): m_links.new(inv_met.outputs[0], inv_met_vec.inputs[i])
        diffuse_metallic_dark = new_pop_node("ShaderNodeVectorMath", (2150, 300)); diffuse_metallic_dark.operation = 'MULTIPLY'
        m_links.new(final_diffuse, diffuse_metallic_dark.inputs[0]); m_links.new(inv_met_vec.outputs[0], diffuse_metallic_dark.inputs[1])
        final_diffuse = diffuse_metallic_dark.outputs[0]

        combined_spec = spec_contrib
        if last_spec_accum is not None:
            if combined_spec is None: combined_spec = last_spec_accum
            else:
                add_spec_tot = new_pop_node("ShaderNodeVectorMath", (2100, 100)); add_spec_tot.operation = 'ADD'
                m_links.new(combined_spec, add_spec_tot.inputs[0]); m_links.new(last_spec_accum, add_spec_tot.inputs[1])
                combined_spec = add_spec_tot.outputs[0]

        combined = final_diffuse
        if combined_spec is not None:
            add_diff_spec = new_pop_node("ShaderNodeVectorMath", (2350, 200)); add_diff_spec.operation = 'ADD'
            m_links.new(combined, add_diff_spec.inputs[0]); m_links.new(combined_spec, add_diff_spec.inputs[1])
            combined = add_diff_spec.outputs[0]

        add_emissive = new_pop_node("ShaderNodeVectorMath", (2550, 200)); add_emissive.operation = 'ADD'
        m_links.new(combined, add_emissive.inputs[0]); m_links.new(group_in.outputs["EmissiveColor"], add_emissive.inputs[1])
        combined = add_emissive.outputs[0]

        emission = new_pop_node("ShaderNodeEmission", (2700, 200))
        m_links.new(combined, emission.inputs['Color']); m_links.new(emission.outputs[0], group_out.inputs["BSDF"])

        # Внешний граф материала
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        
        master_node = None
        for n in nodes:
            if n.get("is_pop_master_node"):
                master_node = n; break
                
        if not master_node:
            extracted_color = [0.9, 0.9, 0.9, 1.0]
            for n in nodes:
                if n.type == 'BSDF_PRINCIPLED':
                    extracted_color = list(n.inputs['Base Color'].default_value)
                    break
            mat.pop_base_color = extracted_color
            
            for n in list(nodes):
                if n.type != 'OUTPUT_MATERIAL':
                    nodes.remove(n)
            
            master_node = nodes.new("ShaderNodeGroup")
            master_node.location = (300, 0)
            master_node.label = "Substrate Toon BSDF"
            master_node.width = 250
            master_node["is_pop_master_node"] = True
            
        master_node.node_tree = master_group

        mat_out = None
        for n in nodes:
            if n.type == 'OUTPUT_MATERIAL':
                mat_out = n; break
        if not mat_out:
            mat_out = nodes.new('ShaderNodeOutputMaterial')
            
        mat_out.location = (master_node.location[0] + 300, master_node.location[1])

        if not any(n.get("pop_role") for n in nodes):
            links.new(master_node.outputs["BSDF"], mat_out.inputs["Surface"])
            
            tex_coord = nodes.new("ShaderNodeTexCoord"); tex_coord.location = (master_node.location[0] - 1200, 0)
            
            def create_texture_block(y_offset, label, socket_name, tex_role, map_role, is_normal=False):
                mapping = nodes.new("ShaderNodeMapping"); mapping.location = (master_node.location[0] - 1000, y_offset)
                if map_role: mapping["pop_role"] = map_role
                
                tex = nodes.new("ShaderNodeTexImage"); tex.location = (master_node.location[0] - 800, y_offset); tex.label = label
                if tex_role: tex["pop_role"] = tex_role
                
                links.new(tex_coord.outputs["UV"], mapping.inputs["Vector"])
                links.new(mapping.outputs["Vector"], tex.inputs["Vector"])
                
                if is_normal:
                    norm_map = nodes.new("ShaderNodeNormalMap"); norm_map.location = (master_node.location[0] - 500, y_offset)
                    norm_map["pop_role"] = "normal_strength_node"
                    links.new(tex.outputs["Color"], norm_map.inputs["Color"])
                    links.new(norm_map.outputs["Normal"], master_node.inputs[socket_name])
                else:
                    rgb2bw = nodes.new("ShaderNodeRGBToBW"); rgb2bw.location = (master_node.location[0] - 500, y_offset)
                    links.new(tex.outputs["Color"], rgb2bw.inputs["Color"])
                    links.new(rgb2bw.outputs["Val"], master_node.inputs[socket_name])

            create_texture_block(200, "Diffuse Offset Texture", "Diffuse Offset Map", "diffuse_offset_tex", "diffuse_offset_map")
            create_texture_block(-100, "Specular Offset Texture", "Spec Offset Map", "spec_offset_tex", "spec_offset_map")
            create_texture_block(-400, "Hatch Texture", "Hatch Map", "hatch_tex", "hatch_map")
            create_texture_block(-700, "Normal Map", "Normal", "normal_tex", None, is_normal=True)

        update_pop_colors(mat, None)

# ==========================================
# 6. UI: N-ПАНЕЛЬ И ИНСПЕКТОР МАТЕРИАЛА
# ==========================================
# Рисуем удобные кнопочки. В том числе систему Light Linking, 
# чтобы материал реагировал только на те источники света, которые мы ему укажем.
class POP_UL_MaterialList(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        mat = item.material
        if mat:
            row = layout.row(align=True)
            row.prop(mat, "pop_is_selected", text="", icon_only=True)
            row.label(text=mat.name, icon='MATERIAL')

class POP_UL_LightList(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        light_obj = bpy.data.objects.get(item.name)
        type_icon = 'LIGHT'
        if light_obj: type_icon = {'SUN':'LIGHT_SUN', 'POINT':'LIGHT_POINT', 'SPOT':'LIGHT_SPOT', 'AREA':'LIGHT_AREA'}.get(light_obj.data.type, 'LIGHT')
        row = layout.row(align=True)
        row.prop(item, "is_enabled", text="", icon_only=True)
        row.label(text=item.name, icon=type_icon)

class POP_OT_RefreshMaterials(bpy.types.Operator):
    bl_idname = "pop.refresh_materials"
    bl_label = "Обновить список"
    bl_description = "Список материалов и так всегда актуален (привязан напрямую к слотам объекта) - просто перерисовывает панель"
    def execute(self, context):
        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                area.tag_redraw()
        return {'FINISHED'}

class POP_OT_RefreshLights(bpy.types.Operator):
    bl_idname = "pop.refresh_lights"
    bl_label = "Обновить список"
    bl_description = "Пересобрать список источников света для текущего материала"
    def execute(self, context):
        obj = context.active_object
        mat_idx = context.scene.pop_mat_index
        if obj and len(obj.material_slots) > mat_idx:
            mat = obj.material_slots[mat_idx].material
            if mat:
                sync_lights(mat)
        return {'FINISHED'}

class POP_OT_MatSelectAll(bpy.types.Operator):
    bl_idname = "pop.mat_select_all"
    bl_label = "Выделить все"
    action: bpy.props.BoolProperty()
    def execute(self, context):
        obj = context.active_object
        if obj:
            for slot in obj.material_slots:
                if slot.material: slot.material.pop_is_selected = self.action
        return {'FINISHED'}

class POP_OT_LightSelectAll(bpy.types.Operator):
    bl_idname = "pop.light_select_all"
    bl_label = "Вкл/выкл все"
    action: bpy.props.BoolProperty()
    def execute(self, context):
        obj = context.active_object
        mat_idx = context.scene.pop_mat_index
        if obj and len(obj.material_slots) > mat_idx:
            mat = obj.material_slots[mat_idx].material
            if mat:
                for light in mat.pop_lights: light.is_enabled = self.action
        return {'FINISHED'}

class POP_OT_LinkSelectedLights(bpy.types.Operator):
    bl_idname = "pop.link_selected_lights"
    bl_label = "Привязать выделенные"
    bl_description = "Отметить/Снять галочки для света, выделенного в 3D окне"
    action: bpy.props.BoolProperty()

    def execute(self, context):
        obj = context.active_object
        mat_idx = context.scene.pop_mat_index
        if not obj or len(obj.material_slots) <= mat_idx: return {'CANCELLED'}
        mat = obj.material_slots[mat_idx].material
        if not mat: return {'CANCELLED'}
        
        selected_lights = [o.name for o in context.selected_objects if o.type == 'LIGHT']
        if not selected_lights:
            self.report({'WARNING'}, "Нет выделенных источников света в 3D окне!")
            return {'CANCELLED'}
        
        count = 0
        for light_item in mat.pop_lights:
            if light_item.name in selected_lights:
                light_item.is_enabled = self.action
                count += 1
                
        self.report({'INFO'}, f"{'Включено' if self.action else 'Выключено'} источников света: {count}")
        return {'FINISHED'}

class POP_OT_LinkCollectionLights(bpy.types.Operator):
    bl_idname = "pop.link_collection_lights"
    bl_label = "Привязать из Коллекции"
    bl_description = "Отметить/Снять галочки для света из выбранной коллекции (папки)"
    action: bpy.props.BoolProperty()

    def execute(self, context):
        obj = context.active_object
        mat_idx = context.scene.pop_mat_index
        if not obj or len(obj.material_slots) <= mat_idx: return {'CANCELLED'}
        mat = obj.material_slots[mat_idx].material
        if not mat: return {'CANCELLED'}
        
        target_col = context.scene.pop_target_collection
        if not target_col:
            self.report({'WARNING'}, "Сначала выберите коллекцию слева от кнопки!")
            return {'CANCELLED'}
            
        col_lights = [o.name for o in target_col.all_objects if o.type == 'LIGHT']
        if not col_lights:
            self.report({'INFO'}, "В выбранной коллекции нет источников света.")
            return {'CANCELLED'}
        
        count = 0
        for light_item in mat.pop_lights:
            if light_item.name in col_lights:
                light_item.is_enabled = self.action
                count += 1
                
        self.report({'INFO'}, f"{'Включено' if self.action else 'Выключено'} источников света: {count}")
        return {'FINISHED'}

class POP_PT_MainPanel(bpy.types.Panel):
    bl_label = "Toon"
    bl_idname = "POP_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = CAT
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        if not obj or not obj.material_slots:
            layout.label(text=t("lbl_pop_no_materials"), icon='INFO')
            return

        box = layout.box()
        header = box.row(align=True)
        header.label(text=t("lbl_pop_materials"), icon='MATERIAL')
        header.operator("pop.refresh_materials", text="", icon='FILE_REFRESH')
        box.template_list("POP_UL_MaterialList", "", obj, "material_slots", context.scene, "pop_mat_index")
        row = box.row(align=True)
        row.operator("pop.mat_select_all", text=t("btn_all")).action = True
        row.operator("pop.mat_select_all", text=t("btn_none")).action = False

        mat_idx = context.scene.pop_mat_index
        active_mat = obj.material_slots[mat_idx].material if len(obj.material_slots) > mat_idx else None
        if active_mat:
            layout.separator()
            box2 = layout.box()
            header2 = box2.row(align=True)
            header2.label(text=t("lbl_pop_light_linking"), icon='OUTLINER_OB_LIGHT')
            header2.operator("pop.refresh_lights", text="", icon='FILE_REFRESH')
            box2.template_list("POP_UL_LightList", "", active_mat, "pop_lights", context.scene, "pop_light_index")
            
            row2 = box2.row(align=True)
            row2.operator("pop.light_select_all", text=t("btn_all")).action = True
            row2.operator("pop.light_select_all", text=t("btn_none")).action = False
            
            row3 = box2.row(align=True)
            row3.operator("pop.link_selected_lights", text=t("btn_selected")).action = True
            row3.operator("pop.link_selected_lights", text=t("btn_unlink")).action = False
            
            box2.separator()
            row4 = box2.row(align=True)
            row4.prop(context.scene, "pop_target_collection", text="")
            row4.operator("pop.link_collection_lights", text="", icon='ADD').action = True
            row4.operator("pop.link_collection_lights", text="", icon='REMOVE').action = False

        layout.separator()
        layout.operator("pop.update_shaders", icon='NODE_MATERIAL')

class POP_PT_MaterialSettings(bpy.types.Panel):
    bl_label = "Pop Cel-Shading"
    bl_idname = "POP_PT_material_settings"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'material'
    bl_order = -100

    @classmethod
    def poll(cls, context):
        mat = context.material
        if not mat or not mat.use_nodes: return False
        return any(n.get("is_pop_master_node") for n in mat.node_tree.nodes)

    def draw(self, context):
        mat = context.material
        layout = self.layout

        box_bsdf = layout.box()
        box_bsdf.label(text=t("lbl_pop_bsdf"), icon='SHADING_RENDERED')
        
        box_bsdf.prop(mat, "pop_base_color", text=t("prop_pop_base_color"))
        box_bsdf.prop(mat, "pop_receive_shadows", text=t("prop_pop_receive_shadows"))

        box_bsdf.prop(mat, "pop_metallic", text=t("prop_pop_metallic"))
        box_bsdf.prop(mat, "pop_specular_strength", text=t("prop_pop_specular"))
        box_bsdf.prop(mat, "pop_roughness", text=t("prop_pop_roughness"))
        
        box_bsdf.separator()
        box_bsdf.label(text=t("lbl_pop_normal_map"), icon='NORMALS_VERTEX')
        box_bsdf.template_ID(mat, "pop_normal_texture", open="image.open", new="image.new")
        box_bsdf.prop(mat, "pop_normal_strength", text=t("prop_pop_strength"))

        box_bsdf.separator()
        box_bsdf.prop(mat, "pop_emissive_color", text=t("prop_pop_emissive"))

        layout.separator()

        box_profile = layout.box()
        box_profile.label(text=t("lbl_pop_profile"), icon='COLOR')
        
        box_profile.label(text=t("lbl_pop_diffuse"), icon='SHADING_TEXTURE')
        group = bpy.data.node_groups.get(f"Toon_Cascade_{mat.name}")
        ramp_node = group.nodes.get("Cascade Ramp") if group else None
        if ramp_node: box_profile.template_color_ramp(ramp_node, "color_ramp", expand=True)
        box_profile.template_ID(mat, "pop_ramp_offset_texture", open="image.open", new="image.new")
        row_diff = box_profile.row(align=True)
        row_diff.prop(mat, "pop_ramp_offset_strength", text=t("prop_pop_strength"))
        row_diff.prop(mat, "pop_ramp_offset_size", text=t("prop_pop_size"))
        
        box_profile.separator()
        
        box_profile.label(text=t("lbl_pop_specular_section"), icon='LIGHT_SUN')
        spec_group = bpy.data.node_groups.get(f"Toon_Specular_{mat.name}")
        spec_ramp_node = spec_group.nodes.get("Specular Ramp") if spec_group else None
        if spec_ramp_node: box_profile.template_color_ramp(spec_ramp_node, "color_ramp", expand=True)
        box_profile.template_ID(mat, "pop_spec_ramp_offset_texture", open="image.open", new="image.new")
        row_spec = box_profile.row(align=True)
        row_spec.prop(mat, "pop_spec_ramp_offset_strength", text=t("prop_pop_strength"))
        row_spec.prop(mat, "pop_spec_ramp_offset_size", text=t("prop_pop_size"))

        box_profile.separator()

        box_profile.label(text=t("lbl_pop_hatching"), icon='TEXTURE')
        box_profile.template_ID(mat, "pop_hatch_texture", open="image.open", new="image.new")
        row_hatch = box_profile.row(align=True)
        row_hatch.prop(mat, "pop_hatch_strength", text=t("prop_pop_strength"))
        row_hatch.prop(mat, "pop_hatch_size", text=t("prop_pop_size"))

# ==========================================
# 7. РЕГИСТРАЦИЯ
# ==========================================
classes = (
    POP_LightItem, 
    POP_UL_MaterialList, 
    POP_UL_LightList, 
    POP_OT_RefreshMaterials,
    POP_OT_RefreshLights,
    POP_OT_MatSelectAll, 
    POP_OT_LightSelectAll, 
    POP_OT_LinkSelectedLights,
    POP_OT_LinkCollectionLights,
    POP_OT_UpdateShaders, 
    POP_PT_MainPanel, 
    POP_PT_MaterialSettings
)

def update_labels():
    POP_PT_MainPanel.bl_label = t("pt_pop_main")
    POP_PT_MaterialSettings.bl_label = t("pt_pop_material")
    POP_OT_UpdateShaders.bl_label = t("btn_pop_update_shaders")


def register():
    update_labels()
    for cls in classes:
        try: bpy.utils.unregister_class(cls)
        except: pass
        bpy.utils.register_class(cls)

    bpy.types.Material.pop_is_selected = bpy.props.BoolProperty(default=False)
    bpy.types.Material.pop_lights = bpy.props.CollectionProperty(type=POP_LightItem)
    
    bpy.types.Material.pop_base_color = bpy.props.FloatVectorProperty(name="Base Color", subtype='COLOR', size=4, default=(0.9, 0.9, 0.9, 1.0), min=0.0, max=1.0, update=update_pop_colors)
    bpy.types.Material.pop_receive_shadows = bpy.props.BoolProperty(name="Receive Cast Shadows", default=True, description="Требует обновления шейдеров через 'Update Pop Shaders'")
    
    bpy.types.Material.pop_metallic = bpy.props.FloatProperty(name="Metallic", default=0.5, min=0.0, max=1.0, update=update_pop_colors)
    bpy.types.Material.pop_specular_strength = bpy.props.FloatProperty(name="Specular", default=0.5, min=0.0, max=5.0, update=update_pop_colors)
    bpy.types.Material.pop_roughness = bpy.props.FloatProperty(name="Roughness", default=0.5, min=0.0, max=1.0, update=update_pop_colors)
    
    bpy.types.Material.pop_normal_texture = bpy.props.PointerProperty(type=bpy.types.Image, name="Normal Texture", update=update_pop_colors)
    bpy.types.Material.pop_normal_strength = bpy.props.FloatProperty(name="Normal Strength", default=0.0, min=-10.0, max=10.0, update=update_pop_colors)

    bpy.types.Material.pop_emissive_color = bpy.props.FloatVectorProperty(name="Emissive Color", subtype='COLOR', size=4, default=(0.0, 0.0, 0.0, 1.0), min=0.0, max=1.0, update=update_pop_colors)
    
    bpy.types.Material.pop_ramp_offset_strength = bpy.props.FloatProperty(name="Diffuse Offset Strength", default=0.0, min=0.0, max=10.0, update=update_pop_colors)
    bpy.types.Material.pop_ramp_offset_size = bpy.props.FloatProperty(name="Diffuse Offset Size", default=1.0, min=0.01, max=10.0, update=update_pop_colors)
    bpy.types.Material.pop_ramp_offset_texture = bpy.props.PointerProperty(type=bpy.types.Image, name="Diffuse Offset Texture", update=update_pop_colors)
    
    bpy.types.Material.pop_spec_ramp_offset_strength = bpy.props.FloatProperty(name="Spec Offset Strength", default=0.0, min=0.0, max=10.0, update=update_pop_colors)
    bpy.types.Material.pop_spec_ramp_offset_size = bpy.props.FloatProperty(name="Spec Offset Size", default=1.0, min=0.01, max=10.0, update=update_pop_colors)
    bpy.types.Material.pop_spec_ramp_offset_texture = bpy.props.PointerProperty(type=bpy.types.Image, name="Spec Offset Texture", update=update_pop_colors)
    
    bpy.types.Material.pop_hatch_strength = bpy.props.FloatProperty(name="Hatch Strength", default=0.0, min=0.0, max=1.0, update=update_pop_colors)
    bpy.types.Material.pop_hatch_size = bpy.props.FloatProperty(name="Hatch Size", default=15.0, min=0.1, max=100.0, update=update_pop_colors)
    bpy.types.Material.pop_hatch_texture = bpy.props.PointerProperty(type=bpy.types.Image, name="Hatch Texture", update=update_pop_colors)
    
    bpy.types.Scene.pop_mat_index = bpy.props.IntProperty(update=on_mat_index_change)
    bpy.types.Scene.pop_light_index = bpy.props.IntProperty()
    
    bpy.types.Scene.pop_target_collection = bpy.props.PointerProperty(type=bpy.types.Collection, name="Папка со светом")

    if pop_auto_sync_handler not in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.append(pop_auto_sync_handler)

def unregister():
    if pop_auto_sync_handler in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(pop_auto_sync_handler)

    del bpy.types.Scene.pop_target_collection
    del bpy.types.Scene.pop_mat_index
    del bpy.types.Scene.pop_light_index
    del bpy.types.Material.pop_is_selected
    del bpy.types.Material.pop_lights
    del bpy.types.Material.pop_base_color
    del bpy.types.Material.pop_receive_shadows
    del bpy.types.Material.pop_metallic
    del bpy.types.Material.pop_specular_strength
    del bpy.types.Material.pop_roughness
    del bpy.types.Material.pop_normal_texture
    del bpy.types.Material.pop_normal_strength
    del bpy.types.Material.pop_emissive_color
    del bpy.types.Material.pop_ramp_offset_strength
    del bpy.types.Material.pop_ramp_offset_size
    del bpy.types.Material.pop_ramp_offset_texture
    del bpy.types.Material.pop_spec_ramp_offset_strength
    del bpy.types.Material.pop_spec_ramp_offset_size
    del bpy.types.Material.pop_spec_ramp_offset_texture
    del bpy.types.Material.pop_hatch_strength
    del bpy.types.Material.pop_hatch_size
    del bpy.types.Material.pop_hatch_texture

    for cls in reversed(classes):
        try: bpy.utils.unregister_class(cls)
        except: pass

if __name__ == "__main__":
    register()