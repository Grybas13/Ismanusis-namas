from devices.smart_device import SmartDevice

class Camera(SmartDevice):

    def __init__(self, name: str, room: str, res: str = "2160p", fov: int = 120):
        super().__init__(name, room)
        self.__resolution = res
        self.__fov = fov
        self.__is_recording = False

    def turn_on(self):
        self._set_on(True)
        print(f"{self.get_name()} ijungta. Rezoliucija: {self.__resolution}, FOV: {self.__fov}°")

    def turn_off(self):
        self._set_on(False)
        print(f"{self.get_name()} isjungta.")

    def is_recording(self):
        return self.__is_recording
    
    def start_recording(self):
        if not self.is_on():
            self.turn_on()
        self.__is_recording = True
        print(f"{self.get_name()} pradeda įrašymą.")

    def stop_recording(self):
        if self.is_on():
            print(f"{self.get_name()} sustabdo įrašymą.")
            self.__is_recording = False
            self.turn_off()
        else:
            print(f"{self.get_name()} nebuvo ijungta.")

    def get_status(self) -> dict:
        return {
            "pavadinimas": self.get_name(),
            "kambarys": self.get_room(),
            "tipas": "camera",
            "ar_ijungta": self.is_on(),
            "rezoliucija": self.__resolution,
            "kampas": self.__fov,
            "irasoma": self.__is_recording  
        }