import bpy
from character_lib.character import Character

api = Character()

character = api.add_empty({
    'name': 'character',
    'location': (0, 0, 172)
})

head = api.add_cube({
    'name': 'head',
    'width': 30,
    'depth': 30,
    'height': 30,
    'location': (0, 0, 142)
})

api.set_parent(character, head)

api.set_object_active(head)
    
api.set_edit_mode(head)

api.deselect()

api.select_bottom_face_by_normal()

api.extrude_selected_face(head, extrude_distance= 10)