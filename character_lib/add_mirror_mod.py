import bpy
from character_lib.api.character import Character

api = Character()
model = api.select_object_by_name('character_mesh')
mirror_use_axis = (True, False, False)
mirror_modifier = api.add_or_set_mirror_modifier(
    model, use_axis=mirror_use_axis)
