import bpy


class Character:
    def __init__(self):
        pass

    def add_body_cube(self, width, depth, height, location=(0, 0, 0)):
        # Create a new cube object for the character's body
        bpy.ops.mesh.primitive_cube_add(size=1, location=location)
        cube = bpy.context.object

        # Set the dimensions of the body cube
        cube.scale.x = width
        cube.scale.y = depth
        cube.scale.z = height


# Example usage:
character = Character()
character.add_body_cube(width=35, depth=20, height=60, location=(0, 0, 0))
