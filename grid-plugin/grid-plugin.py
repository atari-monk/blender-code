import bpy

bl_info = {
    "name": "Custom Grid Creator",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Tool Shelf > Custom Grid",
    "description": "Create a custom grid of empty objects",
    "category": "Add Mesh",
}


def create_grid(width, height, spacing):
    for x in range(0, width, spacing):
        for y in range(0, height, spacing):
            bpy.ops.object.empty_add(location=(x, y, 0))


class CreateCustomGridOperator(bpy.types.Operator):
    bl_idname = "object.create_custom_grid"
    bl_label = "Create Custom Grid"

    def execute(self, context):
        width = context.scene.grid_width
        height = context.scene.grid_height
        spacing = context.scene.grid_spacing

        create_grid(width, height, spacing)
        return {'FINISHED'}


class CustomGridPanel(bpy.types.Panel):
    bl_label = "Custom Grid"
    bl_idname = "PT_CustomGridPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout

        col = layout.column()
        col.prop(context.scene, "grid_width")
        col.prop(context.scene, "grid_height")
        col.prop(context.scene, "grid_spacing")
        col.operator("object.create_custom_grid")


def register():
    bpy.utils.register_class(CustomGridPanel)
    bpy.utils.register_class(CreateCustomGridOperator)
    bpy.types.Scene.grid_width = bpy.props.IntProperty(
        name="Width", default=10)
    bpy.types.Scene.grid_height = bpy.props.IntProperty(
        name="Height", default=10)
    bpy.types.Scene.grid_spacing = bpy.props.IntProperty(
        name="Spacing", default=1)


def unregister():
    bpy.utils.unregister_class(CustomGridPanel)
    bpy.utils.unregister_class(CreateCustomGridOperator)
    del bpy.types.Scene.grid_width
    del bpy.types.Scene.grid_height
    del bpy.types.Scene.grid_spacing


if __name__ == "__main__":
    register()
