import bpy
import bmesh


class Character:
    def __init__(self):
        pass

    def add_empty(self, properties):
        bpy.ops.object.empty_add(location=properties['location'])
        empty = bpy.context.object
        empty.name = properties['name']
        return empty

    def add_cube(self, properties):
        bpy.ops.mesh.primitive_cube_add(
            size=1, location=properties['location'])
        cube = bpy.context.object
        cube.scale.x = properties['width']
        cube.scale.y = properties['depth']
        cube.scale.z = properties['height']
        cube.name = properties['name']
        return cube

    def set_parent(self, parent_object, child_object):
        parent_object.select_set(True)
        child_object.select_set(True)
        bpy.context.view_layer.objects.active = parent_object
        bpy.ops.object.parent_set(type='OBJECT')

    def set_edit_mode(self, cube_object):
        if cube_object.type != 'MESH':
            print("Error: Provided object is not a mesh.")
            return
        bpy.context.view_layer.objects.active = cube_object
        cube_object.select_set(True)
        bpy.ops.object.mode_set(mode='EDIT')

    def set_object_active(self, cube_object):
        bpy.context.view_layer.objects.active = cube_object

    def deselect(self):
        bpy.ops.mesh.select_all(action='DESELECT')

    def select_bottom_face_by_normal(self):
        # ob = bpy.data.objects['head']
        bpy.ops.object.mode_set(mode='EDIT')
        mesh = bmesh.from_edit_mesh(bpy.context.object.data)
        for f in mesh.faces:
            if f.normal.z == -1.0:
                f.select = True
                print('Bottom face selected')

    def extrude_selected_face(self, cube_object, extrude_distance=1.0):
        if cube_object.type != 'MESH':
            print("Error: Provided object is not a mesh.")
            return
        bpy.ops.object.mode_set(mode='EDIT')
        if not bpy.context.tool_settings.mesh_select_mode[0]:
            print("Error: Face Select Mode is not enabled.")
            bpy.ops.object.mode_set(mode='OBJECT')
            return
        bpy.ops.mesh.extrude_region_move(
            TRANSFORM_OT_translate={"value": (0, 0, -extrude_distance)})
        #bpy.ops.object.mode_set(mode='OBJECT')
