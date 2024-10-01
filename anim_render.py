from math import pi, sqrt

import bpy


print("\n\n---> Attempting to render animations...")

Z_HEIGHT = 8
X_DISTANCE = 10
X_ANGLE = 0.95
SQRT_2 = sqrt(2)

camera_positions_rotations = [
    # Top
    ((0, X_DISTANCE, Z_HEIGHT), (X_ANGLE, 0, pi)),
    # Top Right
    ((-X_DISTANCE / SQRT_2, X_DISTANCE / SQRT_2, Z_HEIGHT), (X_ANGLE, 0, 5 / 4 * pi)),
    # Right
    ((-X_DISTANCE, 0, Z_HEIGHT), (X_ANGLE, 0, - pi / 2)),
    # Bottom Right
    ((-X_DISTANCE / SQRT_2, -X_DISTANCE / SQRT_2, Z_HEIGHT), (X_ANGLE, 0, - 1 / 4 * pi)),
    # Bottom
    ((0, -X_DISTANCE, Z_HEIGHT), (X_ANGLE, 0, 0)),
    # Bottom Left
    ((X_DISTANCE / SQRT_2, -X_DISTANCE / SQRT_2, Z_HEIGHT), (X_ANGLE, 0, 1 / 4 * pi)),
    # Left
    ((X_DISTANCE, 0, Z_HEIGHT), (X_ANGLE, 0, pi / 2)),
    # Top Left
    ((X_DISTANCE / SQRT_2, X_DISTANCE / SQRT_2, Z_HEIGHT), (X_ANGLE, 0, -5 / 4 * pi)),
]

camera = bpy.data.objects["Camera"]
if camera is None:
    raise ValueError("Expected to find camera with name 'Camera' but none is present in scene.")

rig = bpy.data.objects["rig"]
if rig is None:
    raise ValueError("Expected to find rig with name 'rig' but none is present in scene.")


for action in bpy.data.actions:
    print(f"\n\n---> Rendering {action.name} now...")
    rig.animation_data.action = bpy.data.actions.get(action.name)

    for (orientation, (position, rotation)) in enumerate(camera_positions_rotations):
        camera.location = position
        camera.rotation_euler = rotation

        bpy.context.scene.render.filepath = f"render/{action.name}-o{orientation}-"
        bpy.ops.render.render(animation=True)
