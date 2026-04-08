from abc import ABC, abstractmethod


class SmartDevice(ABC): # ABC (Abstract Base Class) yra bazinė klasė, kuri negali būti instancijuojama ir skirta būti paveldėta kitų klasių. Ji gali turėti abstrakčius metodus, kurie turi būti įgyvendinti paveldinčiose klasėse.

    def __init__(self, name: str, room: str):
        self.__name = name
        self.__room = room
        self.__is_on = False

    @abstractmethod  # sis dekoratorius nurodo, kad metodas yra abstraktus ir turi būti įgyvendintas klasėse, kurios paveldi šią bazinę klasę
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def get_status(self) -> dict:
        pass

    def get_name(self):
        return self.__name  # __name ir __room yra privatūs atributai, kurie negali būti pasiekiami tiesiogiai is isores.

    def get_room(self):
        return self.__room

    def is_on(self):
        return self.__is_on

    def _set_on(self, value: bool):  # _set_on metodas yra apsaugotas metodas, kuris leidžia paveldinčioms klasėms nustatyti įrenginio būseną (įjungta ar išjungta)
        self.__is_on = value