import csv
from devices.light import Light
from devices.thermostat import Thermostat
from devices.camera import Camera
from home.room import Room

class FileManager:

    FILE_PATH = "data/home_state.csv"

    @staticmethod
    def save(home):
        with open(FileManager.FILE_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["room", "type", "name", "is_on", "setting1", "setting2"])
            for room in home.get_rooms():
                for device in room.get_devices():
                    status = device.get_status()
                    if status["tipas"] == "light":
                        writer.writerow([status["kambarys"], status["tipas"], status["pavadinimas"], status["ar_ijungta"], status["ryskumas"], ""])
                    elif status["tipas"] == "thermostat":
                        writer.writerow([status["kambarys"], status["tipas"], status["pavadinimas"], status["ar_ijungta"], status["norima_temperatura"], status["dregme"]])
                    elif status["tipas"] == "camera":
                        writer.writerow([status["kambarys"], status["tipas"], status["pavadinimas"], status["ar_ijungta"], status["rezoliucija"], status["kampas"]])
                

    @staticmethod
    def load(home):
        try:
            with open(FileManager.FILE_PATH, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    room_name = row["room"]
                    device_type = row["type"]
                    device_name = row["name"]
                    is_on = row["is_on"] == "True"
                    setting1 = row["setting1"]
                    setting2 = row["setting2"]

                    room = home.get_room(room_name)
                    if not room:
                        room = Room(room_name)
                        home.add_room(room)

                    if device_type == "light":
                        device = Light(device_name, room_name, int(setting1))
                        if is_on:
                            device.turn_on()
                        room.add_device(device)
                    elif device_type == "thermostat":
                        device = Thermostat(device_name, room_name, 20.0, int(setting2))
                        device.set_target_temp(float(setting1))
                        if is_on:
                            device.turn_on()
                        room.add_device(device)
                    elif device_type == "camera":
                        device = Camera(device_name, room_name, setting1, int(setting2))
                        if is_on:
                            device.turn_on()
                        room.add_device(device)
        except FileNotFoundError:
            print("Nerasta išsaugojimo failas. Pradedama su tuščiu namu.")