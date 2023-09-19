import bpy
from character_lib.property_lister import PropertyLister
from character_lib.scene_units import SceneUnitsManager
from character_lib.character import Character

print('PropertyLister usage example:')
lister = PropertyLister()
print('-> Print no obj error')
lister.list_properties()
print('-> Print any obj props')
lister.list_properties(bpy.context.scene.unit_settings)
print('-> Print Scene Units props')
lister.list_Scene_Units()

print('SceneUnitsManager usage example:')
scene_units_manager = SceneUnitsManager()
scene_units_manager.setSceneUnitsToCentimeters()

print('Character usage example:')
character = Character()
character.add_body_cube(width=35, depth=20, height=60, location=(0, 0, 0))
