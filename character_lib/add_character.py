import bpy
from character_lib.api.character import Character

api = Character()

empty = api.add_empty({
    'name': 'character_empty',
    'location': (0, 0, 172)
})

model = api.add_cube({
    'name': 'character_mesh',
    'width': 14,
    'depth': 19,
    'height': 22,
    'location': (0, 0, 160)
})

api.switch_to_vertex_mode(model)

api.set_parent(empty, model)

api.set_object_active(model)

api.set_edit_mode(model)

api.deselect()

api.select_bottom_face_by_normal()

api.switch_to_face_mode(model)

api.extrude_selected_face(model, extrude_distance=9)
api.extrude_selected_face(model, extrude_distance=46)
api.extrude_selected_face(model, extrude_distance=46)
api.extrude_selected_face(model, extrude_distance=40)
api.extrude_selected_face(model, extrude_distance=8)

# after that i remove left side of model
# and run add_mirror_mod script
# next i added reference images
# next i add loop cuts to fit cubes as body parts
