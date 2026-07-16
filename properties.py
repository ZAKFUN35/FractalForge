import bpy
from bpy.props import (
    IntProperty, FloatProperty, EnumProperty,
    PointerProperty, CollectionProperty, BoolProperty,
)
from bpy.types import PropertyGroup, AddonPreferences
from .i18n import t

def update_language(self, context):
    try:
        from . import panels
        panels.unregister()
        panels.update_labels()
        panels.register()

        from . import cel_shading
        cel_shading.update_labels()

        for window in context.window_manager.windows:
            for area in window.screen.areas:
                if area.type in {'VIEW_3D', 'PROPERTIES'}:
                    area.tag_redraw()
    except Exception:
        pass

class FF_AddonPreferences(AddonPreferences):
    bl_idname = __package__
    language: EnumProperty(
        name="Language / Язык",
        items=[('EN', "English", ""), ('RU', "Русский", "")],
        default='EN',
        update=update_language
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "language")

_lod_type_items_cache = []

def _lod_type_items(self, context):
    # Blender не копирует строки сразу — если список из callback не хранить
    # где-то ещё, Python может собрать его как мусор, и подписи/значения
    # enum'а поедут или Blender крашнется. Поэтому держим ссылку в кэше.
    global _lod_type_items_cache
    _lod_type_items_cache = [
        ('CLUSTER', t("lod_type_cluster"), ""),
        ('UNIT', t("lod_type_unit"), ""),
    ]
    return _lod_type_items_cache


class FF_LodUnitObject(PropertyGroup):
    object_ref: PointerProperty(name="Object", type=bpy.types.Object)
    include: BoolProperty(name="", default=False)


def sync_unit_objects(scene):
    """Держит unit_objects синхронным со всеми mesh-объектами сцены.
    Убирает записи на удалённые/сменившие тип объекты, добавляет новые меши.
    Флаг include у уже существующих записей не трогаем."""
    s = scene.ff_lod

    for i in range(len(s.unit_objects) - 1, -1, -1):
        obj = s.unit_objects[i].object_ref
        if obj is None or obj.type != 'MESH' or obj.name not in scene.objects:
            s.unit_objects.remove(i)

    existing = {item.object_ref for item in s.unit_objects}
    for obj in scene.objects:
        if obj.type == 'MESH' and obj not in existing:
            item = s.unit_objects.add()
            item.object_ref = obj
            item.include = False


def _on_lod_type_change(self, context):
    # Синк сразу при переключении на Unit, чтобы список не был пустым
    # до первого изменения сцены (depsgraph-хендлер ниже подхватит остальное).
    if self.lod_type == 'UNIT':
        try:
            sync_unit_objects(context.scene)
        except Exception:
            pass


@bpy.app.handlers.persistent
def ff_lod_auto_sync_handler(scene, depsgraph):
    # НИКОГДА не синхронизируем данные scene прямо в Panel.draw() —
    # Blender не любит менять ID/collection-property во время отрисовки UI
    # (из-за этого у Unit LOD панель обрывалась после переключателя типа).
    # Вместо этого держим список в актуальном состоянии через depsgraph.
    try:
        if scene.ff_lod.lod_type == 'UNIT':
            sync_unit_objects(scene)
    except Exception:
        pass


class FF_LodSettings(PropertyGroup):
    lod_type: EnumProperty(
        name="Type",
        items=_lod_type_items,
        update=_on_lod_type_change,
    )

    # --- Cluster (fractal_id based) ---
    levels: IntProperty(name="LOD Levels", default=3, min=2, max=8)
    ratio: FloatProperty(name="Ratio", default=0.5, min=0.1, max=0.9)

    # --- Unit (decimation based, arbitrary object list) ---
    unit_objects: CollectionProperty(type=FF_LodUnitObject)
    unit_list_index: IntProperty(default=0)
    unit_decimation_scale: FloatProperty(
        name="Decimation Scale",
        description="Scale for decimation modifier (1.0 = no change, 0.5 = half)",
        default=0.5, min=0.0, max=1.0
    )
    unit_iterations: IntProperty(
        name="Iterations",
        description="Number of LODs to generate",
        default=6, min=1
    )

class FF_AutoNormalsSettings(PropertyGroup):
    normal_strength: FloatProperty(name="Normal Blend", default=1.0, min=0.0, max=1.0)
    # Поставили дефолт на 100
    smooth_iterations: IntProperty(name="Smoothness", default=100, min=1, max=200)
    # Поставили дефолт на 0.5 (а максимум можно даже до 1.0 поднять, если нужно)
    thickness: FloatProperty(name="Thickness", default=0.5, min=0.01, max=1.0)

classes = (
    FF_AddonPreferences,
    FF_LodUnitObject,
    FF_LodSettings,
    FF_AutoNormalsSettings
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.ff_lod = bpy.props.PointerProperty(type=FF_LodSettings)
    bpy.types.Scene.ff_autonormals = bpy.props.PointerProperty(type=FF_AutoNormalsSettings)

    if ff_lod_auto_sync_handler not in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.append(ff_lod_auto_sync_handler)

def unregister():
    if ff_lod_auto_sync_handler in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(ff_lod_auto_sync_handler)

    del bpy.types.Scene.ff_lod
    del bpy.types.Scene.ff_autonormals
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)