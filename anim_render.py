from math import pi, sqrt
from shutil import rmtree
from os.path import isdir

import bpy

# Camera settings
Z_HEIGHT = 9.5
X_DISTANCE = 10
X_ANGLE = 0.95
SQRT_2 = sqrt(2)

# Names for objects in Blender.
# It is required to name them this way, they are also the default name.
CAMERA_STRING_NAME = "Camera"
CHARACTER_RIG_NAME = "rig"

RENDER_RESOLUTION_X = 100
RENDER_RESOLUTION_Y = 100
COLOR_PALETTE_FILE = "./palette.png"
MATERIAL_NAME = "character"

# Output files
RENDER_OUTPUT_DIR = "render"
METADATA_OUTPUT_DIR = "metadata.csv"

bpy.context.scene.render.resolution_x = RENDER_RESOLUTION_X
bpy.context.scene.render.resolution_y = RENDER_RESOLUTION_Y

# Make sure the output has no anit-aliasing (make it pixel perfect)
bpy.context.scene.render.film_transparent = True
bpy.context.scene.render.filter_size = 0.0001


def create_and_assign_material():
    if MATERIAL_NAME in bpy.data.materials:
        return

    # Create a new material
    material = bpy.data.materials.new(name=MATERIAL_NAME)
    # Enable nodes to use shaders
    material.use_nodes = True

    # Access the material's node tree
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    nodes.clear()

    # Create and add the necessary
    output_node = nodes.new(type='ShaderNodeOutputMaterial')
    image_texture_node = nodes.new(type='ShaderNodeTexImage')

    image_texture_node.image = bpy.data.images.load(COLOR_PALETTE_FILE)
    image_texture_node.interpolation = 'Closest'

    links.new(image_texture_node.outputs['Color'], output_node.inputs['Surface'])

    for obj in bpy.context.scene.objects:
        if obj.type != "MESH":
            continue

        # Replace the first material slot
        if obj.data.materials:
            obj.data.materials[0] = material
        # Add material to the object (materials list is empty)
        else:
            obj.data.materials.append(material)


create_and_assign_material()


print("\n\n---> Attempting to remove render output dir...")


if isdir(RENDER_OUTPUT_DIR):
    rmtree(RENDER_OUTPUT_DIR)


print("\n\n---> Attempting to render animations...")

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

metadata = []

for action in bpy.data.actions:
    print(f"\n\n---> Rendering {action.name} now...")
    rig.animation_data.action = bpy.data.actions.get(action.name)

    for marker in action.pose_markers:
        metadata.append(f"{action.name},{marker.name},{marker.frame}\n")

    bpy.context.scene.frame_start = int(action.frame_start)
    bpy.context.scene.frame_end = int(action.frame_end)

    if bpy.context.scene.frame_start == bpy.context.scene.frame_end:
        raise ValueError("Animation has only a single frame. This is most likely not intended. You most likely forgot to set the 'Manual Frame Range' in the dropsheet Action Editor menu.")

    for (orientation, (position, rotation)) in enumerate(camera_positions_rotations):
        camera.location = position
        camera.rotation_euler = rotation

        bpy.context.scene.render.filepath = f"{RENDER_OUTPUT_DIR}/{action.name}-o{orientation}-"
        bpy.ops.render.render(animation=True)

with open(METADATA_OUTPUT_DIR, "w") as f:
    f.writelines(metadata)
