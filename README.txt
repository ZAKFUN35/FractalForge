Fractal Forge
=============
Tools for creating and optimizing procedural vegetation in Blender 4.0+
N-panel Tab: FF


REQUIREMENTS
------------
- Blender 4.0.0 or higher
- No additional dependencies -- just install and use!


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
  Procedural vegetation objects are created entirely using Geometry Nodes. 
  Each object stores system attributes required for the LODS and Butcher tools to work.

  Grass     - Grass patch with arc blade bending, UV, and ColorMask attribute
  Clover    - Clover patch with UV and ColorMask attribute
  Chamomile - Chamomile patch with UV and ColorMask attribute
  Macadam   - Stone patch with UV

UNIT
  Blobs  - Converts the selected object into blobs entirely using Geometry Nodes.

TOOLS > LODS
  Generates Levels of Detail (LOD) only for objects created by tools from the CLUSTERS category. 
  Creates a collection hierarchy with trimmed versions of the mesh.

TOOLS > FOLIAGE AUTO-NORMALS
  Transfers normals from a volumetric proxy mesh to the foliage geometry to create spherical normals for stylization.

  Important: select the foliage mesh before running.

TOOLS > BUTCHER
  Splits a generated cluster into separate, independent meshes (for example, divides a grass patch into all individual grass blades as separate objects).


FILE STRUCTURE
--------------
fractal_forge/
├── nodes/
│   ├── blob.py           <- Blob node group
│   ├── chamomile.py      <- Chamomile node group
│   ├── clover.py         <- Clover node group
│   ├── grass.py          <- Grass node group
│   ├── macadam.py        <- Macadam (stones) node group
│   └── __init__.py
├── operators/
│   ├── autonormals.py    <- Foliage Auto-normals operator
│   ├── butcher.py        <- Butcher operator
│   ├── clusters.py       <- Cluster creation operators
│   ├── lod.py            <- LOD creation operator
│   ├── unit.py           <- Blob conversion operator
│   └── __init__.py
├── __init__.py           <- Add-on entry point and bl_info
├── i18n.py               <- Localization (EN / RU)
├── panels.py             <- UI layout in the N-panel
├── properties.py         <- Add-on settings and property groups
├── README.txt            <- This file
└── ЧИТАЙМЕНЯ.txt         <- Russian version


TECHNICAL DETAILS
-----------------
- Fully procedural generation based on Geometry Nodes
- Communication between nodes and Python operators via custom attributes (fractal_id, ColorMask)
- Dynamic creation, linking, and cleanup of node groups via Blender Python API


TESTED ON
---------
- Blender 4.5.4 LTS
- Windows


WANT TO IMPROVE THE CODE?
-------------------------
Know how to improve it — improve it, know how to optimize it — optimize it!

Author: ZAKFUN35
Signature: T_T