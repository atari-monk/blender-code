import bpy
from character_lib.api.property_lister import PropertyLister

lister = PropertyLister()
print('-> Print no obj error')
lister.list_properties()
print('-> Print custom obj props')
lister.list_properties(bpy.context.scene.unit_settings)
print('-> Print Scene Units props')
lister.list_Scene_Units()
