import bpy
from bpy.types import Panel
from .i18n import t

CAT = "FF"


class FF_PT_Clusters(Panel):
    bl_label = "Clusters"
    bl_idname = "FF_PT_clusters"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = CAT

    def draw(self, context):
        pass


class FF_PT_Grass(Panel):
    bl_label = "Grass"
    bl_idname = "FF_PT_grass"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = CAT
    bl_parent_id = "FF_PT_clusters"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        self.layout.operator("ff.create_grass", text=t("btn_create"), icon='OUTLINER_OB_CURVES')


class FF_PT_Clover(Panel):
    bl_label = "Clover"
    bl_idname = "FF_PT_clover"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = CAT
    bl_parent_id = "FF_PT_clusters"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        self.layout.operator("ff.create_clover", text=t("btn_create"), icon='OUTLINER_OB_CURVES')


class FF_PT_Chamomile(Panel):
    bl_label = "Chamomile"
    bl_idname = "FF_PT_chamomile"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = CAT
    bl_parent_id = "FF_PT_clusters"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        self.layout.operator("ff.create_chamomile", text=t("btn_create"), icon='OUTLINER_OB_CURVES')


class FF_PT_Macadam(Panel):
    bl_label = "Macadam"
    bl_idname = "FF_PT_macadam"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = CAT
    bl_parent_id = "FF_PT_clusters"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        self.layout.operator("ff.create_macadam", text=t("btn_create"), icon='OUTLINER_OB_CURVES')


class FF_PT_Unit(Panel):
    bl_label = "Unit"
    bl_idname = "FF_PT_unit"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = CAT

    def draw(self, context):
        pass


class FF_PT_Blob(Panel):
    bl_label = "Blobs"
    bl_idname = "FF_PT_blob"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = CAT
    bl_parent_id = "FF_PT_unit"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        self.layout.operator("ff.convert_blob", text=t("btn_convert"), icon='MOD_FLUID')


class FF_PT_Tools(Panel):
    bl_label = "Tools"
    bl_idname = "FF_PT_tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = CAT

    def draw(self, context):
        pass


class FF_PT_LOD(Panel):
    bl_label = "LODS"
    bl_idname = "FF_PT_lod"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = CAT
    bl_parent_id = "FF_PT_tools"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        pass


class FF_PT_LOD_Cluster(Panel):
    bl_label = "Cluster"
    bl_idname = "FF_PT_lod_cluster"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = CAT
    bl_parent_id = "FF_PT_lod"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        s = context.scene.ff_lod
        layout.operator("ff.create_lod", text=t("btn_create_lod"), icon='RENDERLAYERS')
        col = layout.column(align=True)
        col.label(text=t("lbl_settings"))
        col.prop(s, "levels", text=t("prop_levels"))
        col.prop(s, "ratio", text=t("prop_ratio"))


class FF_PT_AutoNormals(Panel):
    bl_label = "Foliage Auto-Normals"
    bl_idname = "FF_PT_autonormals"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = CAT
    bl_parent_id = "FF_PT_tools"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        s = context.scene.ff_autonormals
        layout.operator("ff.auto_normals", text=t("btn_run"), icon='NORMALS_FACE')
        col = layout.column(align=True)
        col.label(text=t("lbl_settings"))
        col.prop(s, "fog_radius", text=t("prop_fog_radius"))
        col.prop(s, "voxel_size", text=t("prop_voxel_size"))
        col.prop(s, "volume_threshold", text=t("prop_volume_threshold"))
        col.prop(s, "smooth_factor", text=t("prop_smooth_factor"))
        col.prop(s, "smooth_iterations", text=t("prop_smooth_iterations"))


class FF_PT_Butcher(Panel):
    bl_label = "Butcher"
    bl_idname = "FF_PT_butcher"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = CAT
    bl_parent_id = "FF_PT_tools"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        self.layout.operator("ff.butcher", text=t("btn_portion"), icon='MOD_BOOLEAN')


classes = (
    FF_PT_Clusters,
    FF_PT_Grass,
    FF_PT_Clover,
    FF_PT_Chamomile,
    FF_PT_Macadam,
    FF_PT_Unit,
    FF_PT_Blob,
    FF_PT_Tools,
    FF_PT_LOD,
    FF_PT_LOD_Cluster,
    FF_PT_AutoNormals,
    FF_PT_Butcher,
)


def update_labels():
    FF_PT_Clusters.bl_label = t("pt_clusters")
    FF_PT_Grass.bl_label = t("pt_grass")
    FF_PT_Clover.bl_label = t("pt_clover")
    FF_PT_Chamomile.bl_label = t("pt_chamomile")
    FF_PT_Macadam.bl_label = t("pt_macadam")
    FF_PT_Unit.bl_label = t("pt_unit")
    FF_PT_Blob.bl_label = t("pt_blob")
    FF_PT_Tools.bl_label = t("pt_tools")
    FF_PT_LOD.bl_label = t("pt_lods")
    FF_PT_LOD_Cluster.bl_label = t("pt_lod_cluster")
    FF_PT_AutoNormals.bl_label = t("pt_autonormals")
    FF_PT_Butcher.bl_label = t("pt_butcher")


def register():
    update_labels()
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)