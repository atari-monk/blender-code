import bpy
from character_lib.api.character import Character

api = Character()

empty = api.add_empty({
    'name': 'character_empty',
    'location': (0, 0, 172)
})

model = api.add_cube({
    'name': 'character_mesh',
    'width': 30,
    'depth': 30,
    'height': 30,
    'location': (0, 0, 142)
})

api.switch_to_vertex_mode(model)

api.set_parent(empty, model)

api.set_object_active(model)

api.set_edit_mode(model)

api.deselect()

api.select_bottom_face_by_normal()

api.switch_to_face_mode(model)

api.extrude_selected_face(model, extrude_distance=10)
