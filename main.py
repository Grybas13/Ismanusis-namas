from home.smart_home import SmartHome
from home.room import Room
from factory.device_factory import DeviceFactory
from storage.file_manager import FileManager

def main():
    namas = SmartHome(input("Įveskite namo pavadinimą: "))

    while True:
        print("\n=== Išmanusis Namas ===")
        print("1. Rodyti namo būseną")
        print("2. Pridėti kambarį")
        print("3. Pridėti prietaisą")
        print("4. Valdyti prietaisą")
        print("5. Išsaugoti")
        print("6. Įkelti")
        print("0. Išeiti")

        pasirinkimas = input("\nPasirinkite: ")

        if pasirinkimas == "0":
            print("Viso gero!")
            break
        elif pasirinkimas == "1":
            # atspausdink namo būseną...
            print(namas.get_status())
        elif pasirinkimas == "2":
            # paprašyk kambario pavadinimo ir pridėk...
            kambario_pavadinimas = input("Įveskite kambario pavadinimą: ")
            namas.add_room(Room(kambario_pavadinimas))  
        elif pasirinkimas == "3":
            # paprašyk kambario, tipo, pavadinimo ir pridėk...
            kambario_pavadinimas = input("Įveskite kambario pavadinimą: ")
            tipo = input("Įveskite prietaiso tipą (light/thermostat/camera): ")
            pavadinimas = input("Įveskite prietaiso pavadinimą: ")
            prietaisas = DeviceFactory.create(tipo, pavadinimas, kambario_pavadinimas)
            if prietaisas:
                namas.get_room(kambario_pavadinimas).add_device(prietaisas)
        elif pasirinkimas == "4":
            # paprašyk kambario, prietaiso ir veiksmo...
            kambario_pavadinimas = input("Įveskite kambario pavadinimą: ")
            prietaiso_pavadinimas = input("Įveskite prietaiso pavadinimą: ")
            veiksmas = input("Įveskite veiksmo tipą (turn_on/turn_off): ")

            kambarys = namas.get_room(kambario_pavadinimas)
            if kambarys:
                prietaisas = kambarys.get_device(prietaiso_pavadinimas)
                if prietaisas:
                    if veiksmas == "turn_on":
                        prietaisas.turn_on()
                    elif veiksmas == "turn_off":
                        prietaisas.turn_off()
        elif pasirinkimas == "5":
            # išsaugok...
            FileManager.save(namas)
        elif pasirinkimas == "6":
            # įkelk...
            FileManager.load(namas)

if __name__ == "__main__":
    main()