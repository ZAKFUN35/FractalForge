bl_info = {
    "name": "Fractal Forge",
    "author": "ZAK_FUN_35",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "View3D > N-Panel > FF",
    "description": "Procedural foliage and terrain tools",
    "category": "Object",
}

import bpy
from . import properties, panels, cel_shading
from .operators import clusters, unit, lod, butcher, autonormals


def register():
    properties.register()
    clusters.register()
    unit.register()
    lod.register()
    butcher.register()
    autonormals.register()
    panels.register()
    cel_shading.register()


def unregister():
    cel_shading.unregister()
    panels.unregister()
    autonormals.unregister()
    butcher.unregister()
    lod.unregister()
    unit.unregister()
    clusters.unregister()
    properties.unregister()