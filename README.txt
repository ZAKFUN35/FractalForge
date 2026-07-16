Fractal Forge
=============
Tools for creating and brutally optimizing procedural vegetation in Blender 5.2+
N-panel Tab: FF


REQUIREMENTS
------------
- Blender 5.2.0 or higher
- No annoying dependencies - just install and use!


INSTALLATION
------------
1. Download the fractal_forge .zip archive
2. In Blender: Edit > Preferences > Add-ons > Install
3. Select the file and enable Fractal Forge
4. The FF tab will appear in the N-panel (press N in the viewport)


UI LANGUAGE
-----------
Edit > Preferences > Add-ons > Fractal Forge > Preferences
Select English or Russian


TOOLS
-----

CLUSTERS
  Pure geometry without alpha masks (no Overdraw).
  Stores system attributes (fractal_id and ColorMask) for LODS, Butcher, and UE.

  Grass     - Grass patch with arc bending, UV, and ColorMask
  Clover    - Clover patch with UV and ColorMask
  Chamomile - Chamomile patch with UV and ColorMask
  Macadam   - Stone patch with UV
  Clouds    - Procedural clouds with UV and ColorMask

UNIT
  Blobs - Wraps any mesh with a procedural Ghibli-bush generator for backgrounds.

TOOLS > LODS
  Two FPS-saving modes:
  Clusters: deletes parts of geometry entirely by ID (keeps the 2D silhouette).
  Units: classic harsh decimation on copies.

TOOLS > FOLIAGE AUTO-NORMALS
  Wraps foliage in a fog proxy and steals spherical normals for the anime style ^_____^
  (Important: select the mesh before running).

TOOLS > BUTCHER
  Slices a cluster into independent blades by fractal_id and puts the Origin strictly at the root. 
  Without this, WPO wind in Unreal Engine will rip the grass off the ground! (⌐■_■)

TOON SHADING (CEL-SHADING)
  The ultimate anime shader. Embeds lighting math directly into material nodes, 
  calculates cascades and shadows (Raycast) for each light separately. Light lays in crisp bands.


FILE STRUCTURE
--------------
fractal_forge/
├── nodes/
│   ├── blob.py           <- Blob node group
│   ├── chamomile.py      <- Chamomile node group
│   ├── clover.py         <- Clover node group
│   ├── clouds.py         <- Clouds node group
│   ├── grass.py          <- Grass node group
│   ├── macadam.py        <- Macadam (stones) node group
│   ├── bridge.py         <- Python to nodes bridge
│   └── __init__.py
├── operators/
│   ├── autonormals.py    <- Auto-normals operator
│   ├── butcher.py        <- Butcher operator
│   ├── clusters.py       <- Cluster spawners
│   ├── lod.py            <- LOD generator
│   ├── unit.py           <- Blob converter
│   └── __init__.py
├── cel_shading.py        <- Substrate Toon BSDF math and UI
├── i18n.py               <- Localization (EN / RU)
├── panels.py             <- N-panel UI
├── properties.py         <- Settings
├── __init__.py           <- Entry point
├── README.txt            <- This file
└── ЧИТАЙМЕНЯ.txt         <- RU version


TECHNICAL DETAILS
-----------------
- Geometry Nodes based generation.
- Node to Python communication via attributes (fractal_id, ColorMask).
- Dynamic node group creation via API.


TESTED ON
---------
- Blender 5.2.0
- Windows


WANT TO IMPROVE THE CODE?
-------------------------
Know how to improve it - improve it, know how to optimize it - optimize it!

Author: ZAKFUN35
Signature: T_T