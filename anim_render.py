import bpy


print("\n\n---> Attempting to render animations...")

camera_positions_rotations = [
    # Top
    ((0, 10, 8), (0.95, 0, 3.1415)),
    # Right
    ((-10, 0, 8), (0.95, 0, -1.57)),
    # Bottom
    ((0, -10, 8), (0.95, 0, 0)),
    # Left
    ((10, 0, 8), (0.95, 0, 1.57)),
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
