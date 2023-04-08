import datetime


def make_and_save_snapshot(blink, photo_directory, camera_name):
    camera = blink.cameras[camera_name]
    print(f"Taking Picture with {camera_name}")
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    camera.snap_picture()  # Take a new picture with the camera
    blink.refresh()  # Get new information from server
    camera.image_to_file(f"{photo_directory}/{camera_name}-{timestamp}.jpg")


def take_photos(blink, photo_directory, cameras=None):
    if cameras is None:
        raise ValueError("Must supply camera name")
    elif isinstance(cameras, str):
        make_and_save_snapshot(blink, photo_directory, cameras)
    else:
        for camera_name in cameras:
            make_and_save_snapshot(blink, photo_directory, camera_name)
