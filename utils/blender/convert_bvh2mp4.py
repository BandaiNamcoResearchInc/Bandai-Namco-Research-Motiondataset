"""
You can run this program only on the Blender.
"""

from pathlib import Path

import bpy


# Set the absolute path to the input file or directory.
input_path = '/repository_name/dataset/dataset1/data'  # modify the path to the input file or directory.

# Set the absolute path to the output file.
output_path = '/repository_name/results'  # modify the path to the output directory.


def load(path):
    """Load a BVH file to Blender.

    Args:
        path (str or pathlib.Path): The path to the input file.
    """

    # Reset objects.
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(True)

    bpy.ops.import_anim.bvh(
        filepath=str(path),
        filter_glob='*.bvh',
        target='ARMATURE',
        global_scale=1,
        frame_start=1,
        use_fps_scale=False,
        use_cyclic=False,
        rotate_mode='NATIVE',
        axis_forward='-Z',
        axis_up='Y'
        )

    for armature in bpy.data.armatures:
        armature.bones[0].hide = True


def save(path, frame_num, viewpoint='FRONT'):
    """Save a BVH file.
    Save a motion as an MP4 file from Blender.

    Args:
        path (str or pathlib.Path): The path to the output file.
        frame_num (int): The number of frames of the video.
        viewpoint(str, optional): A variable that determines the direction to render.
            This variable must be selected from among 'FRONT', 'BACK', 'LEFT', and 'RIGHT'.
            The default value is set to 'FRONT'.
    """

    assert viewpoint in ['FRONT', 'BACK', 'LEFT', 'RIGHT'], f'Invalid argument ({viewpoint}) set to the viewpoint.'
    bpy.context.scene.frame_current = frame_num // 2

    # Set viewpoint to the front of the object.
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            ctx = bpy.context.copy()
            ctx['area'] = area
            ctx['region'] = area.regions[-1]
            with bpy.context.temp_override(**ctx):
                bpy.ops.view3d.view_selected()
                bpy.ops.view3d.view_axis(type=viewpoint)

    # Set resolution.
    bpy.context.scene.render.resolution_x = 640
    bpy.context.scene.render.resolution_y = 480

    # Select the directory to save file.
    bpy.data.scenes['Scene'].render.filepath = str(path)

    # Select the format of the saving file.
    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'

    # Select encoding type.
    bpy.context.scene.render.ffmpeg.format = 'MPEG4'

    # Set background color.
    bpy.data.worlds['World'].node_tree.nodes['Background'].\
        inputs[0].default_value = (1, 1, 1, 1)
    bpy.context.scene.world.color = (1, 1, 1)

    # Set View Transform as Standard in Color Management.
    bpy.context.scene.view_settings.view_transform = 'Standard'

    # Set start time and finish time.
    bpy.context.scene.frame_start = 0
    bpy.context.scene.frame_end = frame_num

    bpy.ops.render.opengl(animation=True)


def get_frame_num(path):
    """Get the number of frames from the BVH file.

    Args:
        path (pathlib.Path): The path to the input file.

    Returns:
        frame_num (int): The number of frames.
    """

    with path.open() as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.strip() == 'MOTION':
            frame_num = int(lines[i + 1].split(':')[1].strip())
            break

    return frame_num


def load_and_save_motion(path):
    """Load the BVH file and save motion as an MP4 file.

    Args:
        path (str or pathlib.Path): The path to the input file.
    """

    output_dir = Path(output_path)
    output_dir.mkdir(exist_ok=True)

    load(path)

    frame_num = get_frame_num(path)

    filename = path.stem + '.mp4'
    output_filepath = output_dir / filename
    save(output_filepath, frame_num)


def main():
    path = Path(input_path)

    if path.is_file():
        path = Path(input_path)
        assert path.suffix == '.bvh', 'The input file must be a BVH file.'

        load_and_save_motion(path)

    elif path.is_dir():
        data_dir = Path(input_path)

        for path in data_dir.iterdir():
            extension = path.suffix

            if extension == '.bvh':
                load_and_save_motion(path)


if __name__ == '__main__':
    main()
