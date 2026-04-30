import bpy

_DICT = {
    "pt_clusters": {"EN": "Clusters", "RU": "Кластеры"},
    "pt_grass": {"EN": "Grass", "RU": "Трава"},
    "pt_clover": {"EN": "Clover", "RU": "Клевер"},
    "pt_chamomile": {"EN": "Chamomile", "RU": "Ромашка"},
    "pt_macadam": {"EN": "Macadam", "RU": "Щебёнка"},
    "pt_unit": {"EN": "Unit", "RU": "Юнит"},
    "pt_blob": {"EN": "Blobs", "RU": "Блобы"},
    "pt_tools": {"EN": "Tools", "RU": "Инструменты"},
    "pt_lods": {"EN": "LODS", "RU": "LODS"},
    "pt_lod_cluster": {"EN": "Cluster", "RU": "Кластер"},
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
    "prop_fog_radius": {"EN": "Fog Radius", "RU": "Радиус тумана"},
    "prop_voxel_size": {"EN": "Voxel Size", "RU": "Размер вокселя"},
    "prop_volume_threshold": {"EN": "Volume Threshold", "RU": "Порог объема"},
    "prop_smooth_factor": {"EN": "Smooth Factor", "RU": "Фактор сглаживания"},
    "prop_smooth_iterations": {"EN": "Smooth Iterations", "RU": "Итерации сглаживания"},
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