import bpy
from bpy.props import IntProperty, FloatProperty, EnumProperty
from bpy.types import PropertyGroup, AddonPreferences


def update_language(self, context):
    try:
        from . import panels
        panels.unregister()
        panels.update_labels()
        panels.register()
        for window in context.window_manager.windows:
            for area in window.screen.areas:
                if area.type == 'VIEW_3D':
                    area.tag_redraw()
    except Exception:
        pass


class FF_AddonPreferences(AddonPreferences):
    bl_idname = __package__

    language: EnumProperty(
        name="Language / Язык",
        items=[
            ('EN', "English", ""),
            ('RU', "Русский", "")
        ],
        default='EN',
        update=update_language
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "language")


class FF_LodSettings(PropertyGroup):
    levels: IntProperty(
        name="LOD Levels",
        default=3, min=2, max=8,
    )
    ratio: FloatProperty(
        name="Ratio",
        default=0.5, min=0.1, max=0.9,
    )


class FF_AutoNormalsSettings(PropertyGroup):
    fog_radius: FloatProperty(
        name="Fog Radius",
        default=0.25, min=0.01,
    )
    voxel_size: FloatProperty(
        name="Voxel Size",
        default=0.05, min=0.001,
    )
    volume_threshold: FloatProperty(
        name="Volume Threshold",
        default=0.15, min=0.0, max=1.0,
    )
    smooth_factor: FloatProperty(
        name="Smooth Factor",
        default=1.0, min=0.0,
    )
    smooth_iterations: IntProperty(
        name="Smooth Iterations",
        default=35, min=1, max=200,
    )


classes = (
    FF_AddonPreferences,
    FF_LodSettings, 
    FF_AutoNormalsSettings
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.ff_lod = bpy.props.PointerProperty(type=FF_LodSettings)
    bpy.types.Scene.ff_autonormals = bpy.props.PointerProperty(type=FF_AutoNormalsSettings)


def unregister():
    del bpy.types.Scene.ff_lod
    del bpy.types.Scene.ff_autonormals
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)