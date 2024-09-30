import bpy


print("\n\n---> Attempting to render animations...")


for action in bpy.data.actions:
    print(f"\n\n---> Rendering {action.name} now...")
    bpy.context.object.animation_data.action = bpy.data.actions.get(action.name)
    bpy.context.scene.render.filepath = f"render/{action.name}-"
    bpy.ops.render.render(animation=True)
