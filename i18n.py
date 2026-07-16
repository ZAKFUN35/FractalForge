import bpy

_DICT = {
    "pt_generators": {"EN": "Generators", "RU": "Генераторы"},
    "pt_clusters": {"EN": "Clusters", "RU": "Кластеры"},
    "pt_grass": {"EN": "Grass", "RU": "Трава"},
    "pt_clover": {"EN": "Clover", "RU": "Клевер"},
    "pt_chamomile": {"EN": "Chamomile", "RU": "Ромашка"},
    "pt_macadam": {"EN": "Macadam", "RU": "Щебёнка"},
    "pt_clouds": {"EN": "Clouds", "RU": "Облака"},
    "pt_unit": {"EN": "Unit", "RU": "Юнит"},
    "pt_blob": {"EN": "Blobs", "RU": "Блобы"},
    "pt_tools": {"EN": "Tools", "RU": "Инструменты"},
    "pt_lods": {"EN": "LODS", "RU": "LODS"},
    "lod_type_cluster": {"EN": "Cluster", "RU": "Кластер"},
    "lod_type_unit": {"EN": "Unit", "RU": "Юнит"},
    "lbl_lod_unit_objects": {"EN": "Objects:", "RU": "Объекты:"},
    "prop_unit_decimation": {"EN": "Decimation Scale", "RU": "Коэффициент децимации"},
    "prop_unit_iterations": {"EN": "Iterations", "RU": "Итераций"},
    "pt_autonormals": {"EN": "Foliage Auto-Normals", "RU": "Авто-нормали листвы"},
    "pt_butcher": {"EN": "Butcher", "RU": "Мясник"},
    "btn_create": {"EN": "Create", "RU": "Создать"},
    "btn_convert": {"EN": "Convert", "RU": "Превратить"},
    "btn_create_lod": {"EN": "Create LOD", "RU": "Создать LOD"},
    "btn_run": {"EN": "Run", "RU": "Запустить"},
    "btn_portion": {"EN": "Portion", "RU": "Порционировать"},
    "lbl_settings": {"EN": "Settings", "RU": "Настройки"},
    "prop_levels": {"EN": "LOD Levels", "RU": "Уровней LOD"},
    "prop_ratio": {"EN": "Ratio", "RU": "Коэффициент"},
    "prop_normal_strength": {"EN": "Normal Strength", "RU": "Сила нормали"},
    "prop_smooth_iterations": {"EN": "Smooth Iterations", "RU": "Сглаживание облака"},
    "prop_thickness": {"EN": "Thickness", "RU": "Толщина облака"},

    # --- Cel Shading (Pop Toon) ---
    "pt_pop_main": {"EN": "Toon", "RU": "Toon"},
    "pt_pop_material": {"EN": "Toon Shading", "RU": "Toon Shading"},
    "lbl_pop_no_materials": {"EN": "Select an object with materials!", "RU": "Выделите объект с материалами!"},
    "lbl_pop_materials": {"EN": "Materials:", "RU": "Материалы:"},
    "btn_all": {"EN": "All", "RU": "Все"},
    "btn_none": {"EN": "None", "RU": "Нет"},
    "btn_selected": {"EN": "Selected", "RU": "Выделенные"},
    "btn_unlink": {"EN": "Unlink", "RU": "Отвязать"},
    "lbl_pop_light_linking": {"EN": "Light Linking:", "RU": "Привязка света:"},
    "btn_pop_update_shaders": {"EN": "Update Shader", "RU": "Обновить шейдер"},
    "lbl_pop_bsdf": {"EN": "\u25bc Substrate Toon BSDF", "RU": "\u25bc Substrate Toon BSDF"},
    "prop_pop_base_color": {"EN": "Base Color", "RU": "Базовый цвет"},
    "prop_pop_receive_shadows": {"EN": "Receive Cast Shadows", "RU": "Получать падающие тени"},
    "prop_pop_metallic": {"EN": "Metallic", "RU": "Металличность"},
    "prop_pop_specular": {"EN": "Specular", "RU": "Отражение"},
    "prop_pop_roughness": {"EN": "Roughness", "RU": "Шероховатость"},
    "lbl_pop_normal_map": {"EN": "Normal Map:", "RU": "Карта нормалей:"},
    "prop_pop_strength": {"EN": "Strength", "RU": "Сила"},
    "prop_pop_emissive": {"EN": "Emissive Color", "RU": "Цвет свечения"},
    "lbl_pop_profile": {"EN": "\u25bc Toon Profile", "RU": "\u25bc Toon Profile"},
    "lbl_pop_diffuse": {"EN": "Diffuse:", "RU": "Диффузия:"},
    "prop_pop_size": {"EN": "Size", "RU": "Размер"},
    "lbl_pop_specular_section": {"EN": "Specular:", "RU": "Блики:"},
    "lbl_pop_hatching": {"EN": "Shadow Hatching:", "RU": "Штриховка теней:"},
}


def t(key):
    lang = 'EN'
    try:
        addon_name = __package__.split('.')[0] if __package__ else "fractal_forge"
        prefs = bpy.context.preferences.addons.get(addon_name)
        if prefs and hasattr(prefs, 'preferences'):
            lang = prefs.preferences.language
    except Exception:
        pass
    return _DICT.get(key, {}).get(lang, key)