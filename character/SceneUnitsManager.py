import bpy


class SceneUnitsManager:
    def __init__(self):
        pass

    def setSceneUnitsToCentimeters(self):
        # Access the scene unit settings
        unit_settings = bpy.context.scene.unit_settings

        # Set the scene units to centimeters
        unit_settings.system = 'METRIC'
        unit_settings.scale_length = 0.01  # 1 Blender unit will be equivalent to 1 cm
        unit_settings.length_unit = 'CENTIMETERS'
        print('Scene Units set to CENTIMETERS')


# Example usage:
scene_units_manager = SceneUnitsManager()
scene_units_manager.setSceneUnitsToCentimeters()
