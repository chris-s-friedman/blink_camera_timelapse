def list_cameras(blink):
    for name, camera in blink.cameras.items():
        attr = camera.attributes
        print(f"Camera: {name}")
        print(f"    serial: {attr['serial']}")
        print(f"    Sync Module: {attr['sync_module']}")
