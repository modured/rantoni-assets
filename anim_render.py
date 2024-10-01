from math import pi, sqrt

import bpy


print("\n\n---> Attempting to render animations...")

Z_HEIGHT = 8
X_DISTANCE = 10
X_ANGLE = 0.95
SQRT_2 = sqrt(2)

CAMERA_STRING_NAME = "Camera"
CHARACTER_RIG_NAME = "rig"

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

camera = bpy.data.objects[CAMERA_STRING_NAME]
if camera is None:
    raise ValueError("Expected to find camera with name 'Camera' but none is present in scene.")

rig = bpy.data.objects[CHARACTER_RIG_NAME]
if rig is None:
    raise ValueError("Expected to find rig with name 'rig' but none is present in scene.")


for action in bpy.data.actions:
    print(f"\n\n---> Rendering {action.name} now...")
    rig.animation_data.action = bpy.data.actions.get(action.name)

    bpy.context.scene.frame_start = int(action.frame_start)
    bpy.context.scene.frame_end = int(action.frame_end)

    if bpy.context.scene.frame_start == bpy.context.scene.frame_end:
        raise ValueError("Animation has only a single frame. This is most likely not intended. You most likely forgot to set the 'Manual Frame Range' in the dropsheet Action Editor menu.")

    for (orientation, (position, rotation)) in enumerate(camera_positions_rotations):
        camera.location = position
        camera.rotation_euler = rotation

        bpy.context.scene.render.filepath = f"render/{action.name}-o{orientation}-"
        bpy.ops.render.render(animation=True)
