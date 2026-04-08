from devices.smart_device import SmartDevice

class Thermostat(SmartDevice):

    def __init__(self, name: str, room: str, current_temp: float = 20.0, humidity: int = 50):
        super().__init__(name, room)
        self.__current_temp = current_temp
        self.__humidity = humidity
        self.__target_temp = 21.0

    def turn_on(self):
        self._set_on(True)
        print(f"{self.get_name()} įjungta. Dabartinė temperatūra: {self.__current_temp}°C, Drėgmė: {self.__humidity}%")

    def turn_off(self):
        self._set_on(False)
        print(f"{self.get_name()} išjungta.")
    
    def set_target_temp(self, temp: float):
        if 5 <= temp <= 35:
            self.__target_temp = temp
            print(f"{self.get_name()} norima temperatura nustatyta i {self.__target_temp}°C.")
        else:
            print("Temperatūra turi būti tarp 5°C ir 35°C.")

    def get_humidity(self):
        return self.__humidity
    
    def update_readings(self, temp: float, humidity: int):
        self.__current_temp = temp
        self.__humidity = humidity
        print(f"{self.get_name()} atnaujinti duomenys. Dabartinė temperatūra: {self.__current_temp}°C, Drėgmė: {self.__humidity}%")

    def get_status(self) -> dict:
        return {
        "pavadinimas": self.get_name(),
        "kambarys": self.get_room(),
        "tipas": "thermostat",
        "ar_ijungta": self.is_on(),
        "dabartine_temperatura": self.__current_temp,
        "norima_temperatura": self.__target_temp,
        "dregme": self.__humidity
    }