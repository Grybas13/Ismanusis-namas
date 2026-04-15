from devices.light import Light
from devices.thermostat import Thermostat
from devices.camera import Camera

class DeviceFactory:
    @staticmethod
    def create(device_type: str, name: str, room: str):
        if device_type == "light":
            return Light(name, room)
        elif device_type == "thermostat":
            return Thermostat(name, room)
        elif device_type == "camera":
            return Camera(name, room)
        else:
            print(f"nežinomas įrenginys: {device_type}")
            return None