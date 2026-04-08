from devices.smart_device import SmartDevice

class Light(SmartDevice):

    def __init__(self, name: str, room: str, brightness: int = 100):
        super().__init__(name, room)
        self.__brightness = brightness

    def turn_on(self):
        self._set_on(True)
        print(f"{self.get_name()} įjungta. Ryškumas: {self.__brightness}%")

    def turn_off(self):
        self._set_on(False)
        print(f"{self.get_name()} išjungta.")

    def set_brightness(self, level: int):
        if 0 <= level <= 100:
            self.__brightness = level
            print(f"{self.get_name()} ryškumas nustatytas į {self.__brightness}%.")
        else:
            print("Ryškumo lygis turi būti tarp 0 ir 100.")

    def get_brightness(self):
        return self.__brightness
    
    def get_status(self) -> dict:
        return {
            "pavadinimas": self.get_name(),
            "kambarys": self.get_room(),
            "ar_ijungta": self.is_on(),
            "ryskumas": self.__brightness
        }
