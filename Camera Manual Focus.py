import time
import libcamera

def capture_image():
    manager = libcamera.CameraManager()
    manager.start()

    cameras = manager.cameras()
    if not cameras:
        print("No cameras found")
        return
    camera = cameras[0]

    camera_config = camera.generate_configuration([libcamera.StreamType.Still])
    camera_config[0].controls['AfMode'] = libcamera.AfMode.Manual

    camera.configure(camera_config)

    camera.start()

    camera.capture('output.jpg')

    camera.stop()

    manager.stop()

capture_image()