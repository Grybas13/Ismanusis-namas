
# Išmaniojo Namo Valdymo Sistema

## 1. Įvadas

### Apie programą
Išmaniojo namo valdymo sistema — tai programa, leidžianti vartotojui 
valdyti namų įrenginius per paprastą sąsają. Sistemoje galima pridėti 
kambarius, juose esančius įrenginius (lempas, termostatus, kameras) 
bei juos valdyti. Programos paskirtis — supaprastinti įrenginių valdymą 
ir suteikti galimybę stebėti jų rodiklius realiuoju laiku.

### Kaip paleisti programą?
1. Atsisiųskite projektą iš GitHub arba išskleiskite `.zip` archyvą
2. Terminale pereikite į projekto aplanką: cd Ismanusis-namas
3. Paleiskite programą: python3 main.py

### Kaip naudoti programą?
Programa veikia demo režimu su CLI (komandinės eilutės) sąsaja. 
Paleidus programą, vartotojui pateikiamas meniu su šiais pasirinkimais:

| Pasirinkimas | Veiksmas |
|---|---|
| 1 | Rodyti namo būseną |
| 2 | Pridėti kambarį |
| 3 | Pridėti prietaisą į kambarį |
| 4 | Valdyti prietaisą (įjungti/išjungti) |
| 5 | Išsaugoti būseną į failą |
| 6 | Įkelti būseną iš failo |
| 0 | Išeiti |

Palaikomi prietaisų tipai: `light` (lempa), `thermostat` (termostatas), `camera` (kamera).


## 2. Analizė

### 4 OOP principai

#### Abstrakcija
Abstrakcija — tai būdas apibrėžti *ką* objektas turi daryti, 
nenurodant *kaip* tai bus daroma. Sistemoje abstrakcija įgyvendinta 
per `SmartDevice` abstrakčią bazinę klasę. Ji apibrėžia metodus 
kuriuos *privalo* turėti kiekvienas prietaisas, bet neįgyvendina jų.

```python
from abc import ABC, abstractmethod

class SmartDevice(ABC):

    def __init__(self, name: str, room: str):
        self.__name = name
        self.__room = room
        self.__is_on = False

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def get_status(self) -> dict:
        pass
```

#### Enkapsuliacija
Enkapsuliacija — tai kintamųjų apsauga nuo tiesioginio pasiekimo 
iš išorės. Sistemoje visi vidiniai kintamieji yra privatus (du 
pabraukimai `__`), o pasiekiami tik per metodus.

```python
class Light(SmartDevice):

    def __init__(self, name: str, room: str, brightness: int = 100):
        super().__init__(name, room)
        self.__brightness = brightness  # privatus kintamasis

    def get_brightness(self):
        return self.__brightness  # pasiekiamas tik per metodą

    def set_brightness(self, level: int):
        if 0 <= level <= 100:
            self.__brightness = level
```

#### Paveldėjimas
Paveldėjimas — tai mechanizmas leidžiantis klasei perimti kitos 
klasės savybes. `Light`, `Thermostat` ir `Camera` klasės paveldi 
`SmartDevice` klasę ir gauna visus jos metodus.

```python
class Light(SmartDevice):      # paveldi SmartDevice
    ...

class Thermostat(SmartDevice): # paveldi SmartDevice
    ...

class Camera(SmartDevice):     # paveldi SmartDevice
    ...
```

#### Polimorfizmas
Polimorfizmas — tai gebėjimas skirtingų klasių objektams reaguoti 
į tą patį metodą skirtingai. Visi prietaisai turi `turn_on()` metodą, 
bet kiekvienas jį įgyvendina skirtingai.

```python
# Lempos turn_on()
def turn_on(self):
    self._set_on(True)
    print(f"{self.get_name()} įjungta. Ryškumas: {self.__brightness}%")

# Termostato turn_on()
def turn_on(self):
    self._set_on(True)
    print(f"{self.get_name()} įjungtas. Temperatūra: {self.__current_temp}°C")

# Kameros turn_on()
def turn_on(self):
    self._set_on(True)
    print(f"{self.get_name()} įjungta. Rezoliucija: {self.__resolution}")
```

### Kompozicija ir Agregacija

Sistemoje naudojami abu principai:

**Kompozicija** — `SmartHome` ir `Room` negali egzistuoti vienas 
be kito. Kambarys priklauso namui ir be jo neturi prasmės.

**Agregacija** — `Room` ir `SmartDevice` gali egzistuoti 
nepriklausomai. Prietaisas gali egzistuoti be kambario.

```
SmartHome
└── Room (kompozicija — kambarys negali egzistuoti be namo)
    └── SmartDevice (agregacija — prietaisas gali egzistuoti atskirai)
```

```python
class SmartHome:
    def __init__(self, name: str):
        self.__rooms = []  # kompozicija — kambariai priklauso namui

    def add_room(self, room):
        self.__rooms.append(room)

class Room:
    def __init__(self, name: str):
        self.__devices = []  # agregacija — prietaisai gali egzistuoti atskirai

    def add_device(self, device):
        self.__devices.append(device)
```

### Dizaino Šablonas — Factory Method

Factory Method šablonas naudojamas kai reikia kurti skirtingų tipų 
objektus pagal vartotojo įvestį. `DeviceFactory` klasė sukuria 
tinkamą prietaiso objektą pagal nurodytą tipą.

**Kodėl Factory Method?** Be šio šablono kiekviename programos 
vietoje reikėtų rašyti `if/elif` grandinę. Su Factory — viena 
atsakinga vieta visam objektų kūrimui.

```python
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
            print(f"Nežinomas įrenginys: {device_type}")
            return None
```

### Skaitymas ir Rašymas į Failą

Namo būsena išsaugoma į CSV failą `data/home_state.csv`. 
`FileManager` klasė turi du metodus — `save()` ir `load()`.

CSV failo struktūra:
```
room,type,name,is_on,setting1,setting2
Svetainė,light,Lubų lempa,False,100,
Miegamasis,thermostat,Termostatas,False,21.0,50
```

```python
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
                    
```

### Testavimas

Programos funkcionalumas padengtas unit testais naudojant 
`unittest` biblioteką. Iš viso parašyti **43 testai** 
apimantys visus prietaisus, `DeviceFactory`, `Room` ir `SmartHome`.

```python
class TestLight(unittest.TestCase):

    def test_turn_on(self):
        lempa = Light("Lempa", "Svetainė")
        lempa.turn_on()
        self.assertTrue(lempa.is_on())

    def test_invalid_brightness(self):
        lempa = Light("Lempa", "Svetainė")
        lempa.set_brightness(150)
        self.assertEqual(lempa.get_brightness(), 100)
```

Testai paleidžiami:
```
python3 -m unittest discover -s tests -v
```

## 3. Rezultatai ir Išvados

### Rezultatai
- Sėkmingai įgyvendinta išmaniojo namo valdymo sistema su trimis 
  prietaisų tipais: lempa, termostatu ir kamera.
- Visi 4 OOP principai (abstrakcija, enkapsuliacija, paveldėjimas, 
  polimorfizmas) pritaikyti praktiškai ir veikia kartu.
- Parašyti 43 unit testai — visi praeina sėkmingai.
- Namo būsena sėkmingai išsaugoma ir įkeliama iš CSV failo.
- Kurso metu išmokta kurti klasių hierarchiją, naudoti dizaino 
  šablonus ir rašyti unit testus.

### Išvados
Šio darbo metu sukurta veikianti išmaniojo namo valdymo sistema 
pritaikant objektinio programavimo principus. Programa leidžia 
vartotojui valdyti įrenginius, stebėti jų būseną ir išsaugoti 
duomenis tarp paleidimų.

Kurso metu išmokta:
- Kurti abstrakčias klases ir jas paveldėti
- Taikyti enkapsuliacijos principą apsaugant vidinius duomenis
- Naudoti Factory Method dizaino šabloną
- Rašyti unit testus su `unittest` biblioteka
- Dirbti su Git ir GitHub

### Ateities planai
- Prijungti realų Home Assistant API kad sistema valdytų 
  tikrus įrenginius
- Sukurti grafinę sąsają su `tkinter`
- Pridėti daugiau prietaisų tipų (pvz. išmanusis spynos, 
  žaliuzės, garso sistema)
- Pridėti vartotojų valdymą — skirtingi vartotojai su 
  skirtingomis teisėmis