class Room:
    def __init__(self, name: str):
        self.__name = name
        self.__devices = []  # Kambarys turi sąrašą įrenginių

    def add_device(self, device):
        self.__devices.append(device)  # Prideda įrenginį į kambario sąrašą

    def remove_device(self, device_name: str):
        self.__devices = [d for d in self.__devices if d.get_name() != device_name]  # paimk kiekvieną prietaisą d iš sąrašo, bet tik jei jo pavadinimas nėra tas kurį norim pašalinti"

    def turn_on_all(self):
        for device in self.__devices:
            device.turn_on()  # Įjungia visus įrenginius kambaryje

    def turn_off_all(self):
        for device in self.__devices:
            device.turn_off()  # Išjungia visus įrenginius kambaryje    

    def get_devices(self):
        return self.__devices  # Grąžina sąrašą įrenginių kambaryje 
    
    def get_name(self):
        return self.__name  # Grąžina kambario pavadinimą
    
    def get_status(self):
        return {
            "kambarys": self.get_name(),
            "irenginiai": [device.get_status() for device in self.__devices]  # Grąžina sąrašą įrenginių su jų statusais
        }
    
    def get_device(self, device_name: str):
        for device in self.__devices:
            if device.get_name() == device_name:
                return device
        return None