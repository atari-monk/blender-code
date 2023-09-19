import bpy


class PropertyLister:
    def __init__(self):
        pass

    def list_properties(self, obj=None):
        if obj is None:
            print("Please provide an object.")
            return
        for prop in dir(obj):
            if not callable(getattr(obj, prop)):
                print(prop)

    def list_Scene_Units(self):
        unit_settings = bpy.context.scene.unit_settings
        self.list_properties(unit_settings)


lister = PropertyLister()
print('-> Print no obj error')
lister.list_properties()
print('-> Print any obj props')
lister.list_properties(bpy.context.scene.unit_settings)
print('-> Print Scene Units props')
lister.list_Scene_Units()
