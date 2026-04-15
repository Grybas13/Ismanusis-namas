class SmartHome:
    def __init__(self, name: str):
        self.__name = name
        self.__rooms = []

    def add_room(self, room):
        self.__rooms.append(room)  # Prideda kambarį į namo sąrašą

    def remove_room(self, room_name: str):
        self.__rooms = [r for r in self.__rooms if r.get_name() != room_name]

    def get_room(self, room_name: str):
        for room in self.__rooms:
            if room.get_name() == room_name:
                return room
        return None
    
    def get_name(self):
        return self.__name  # Grąžina namo pavadinimą

    def get_all_rooms(self):
        return [room.get_status() for room in self.__rooms]  # Grąžina sąrašą kambarių su jų statusais
    
    def turn_on_all(self):
        for room in self.__rooms:
            room.turn_on_all()  # Įjungia visus įrenginius visuose kambariuose

    def turn_off_all(self):
        for room in self.__rooms:
            room.turn_off_all()  # Išjungia visus įrenginius visuose kambariuose    

    def get_status(self):
        return {
            "namas": self.__name,
            "kambariai": [room.get_status() for room in self.__rooms]  # Grąžina sąrašą kambarių su jų statusais
        }