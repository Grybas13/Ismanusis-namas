# Išmaniojo Namo Valdymo Sistema

Objektinio programavimo kursuinis darbas — Python programa leidžianti 
valdyti išmaniojo namo įrenginius per komandinės eilutės sąsają.

## Funkcionalumas

- 🚪 Pridėti/šalinti kambarius
- 💡 Valdyti įrenginius (lempos, termostatai, kameros)
- 🔄 Įjungti/išjungti visus kambario įrenginius vienu metu
- 💾 Išsaugoti ir įkelti namo būseną iš CSV failo

## Projekto Struktūra

```
Ismanusis-namas/
├── main.py              # Pagrindinis paleidimo failas
├── devices/
│   ├── smart_device.py  # Abstrakti bazinė klasė
│   ├── light.py         # Lempa
│   ├── thermostat.py    # Termostatas
│   └── camera.py        # Kamera
├── home/
│   ├── room.py          # Kambario klasė
│   └── smart_home.py    # Namo klasė
├── factory/
│   └── device_factory.py # Factory Method šablonas
├── storage/
│   └── file_manager.py  # CSV skaitymas/rašymas
├── tests/
│   └── test_devices.py  # 43 unit testai
├── data/
│   └── home_state.csv   # Išsaugota namo būsena
└── report.md            # Kursuinio ataskaita
```

##Paleidimas

```bash
# 1. Klonuoti repozitoriją
git clone https://github.com/Grybas13/Ismanusis-namas.git

# 2. Pereiti į projekto aplanką
cd Ismanusis-namas

# 3. Paleisti programą
python3 main.py
```

## Testai

```bash
python3 -m unittest discover -s tests -v
```

Visi **43 testai** praeina sėkmingai.

## Naudojami Įrenginiai

| Tipas | Komanda | Papildomi nustatymai |
|---|---|---|
| Lempa | `light` | Ryškumas (0-100%) |
| Termostatas | `thermostat` | Temperatūra (5-35°C), Drėgmė |
| Kamera | `camera` | Rezoliucija, FOV |

## OOP Principai

| Principas | Įgyvendinimas |
|---|---|
| Abstrakcija | `SmartDevice` abstrakti bazinė klasė |
| Enkapsuliacija | Privatūs kintamieji su `__` |
| Paveldėjimas | `Light`, `Thermostat`, `Camera` paveldi `SmartDevice` |
| Polimorfizmas | Kiekvienas prietaisas turi savą `turn_on()` implementaciją |

## Dizaino Šablonas

**Factory Method** — `DeviceFactory` klasė sukuria tinkamą prietaiso 
objektą pagal nurodytą tipą.

## Technologijos

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

- Python 3
- `unittest` — testavimui
- `csv` — duomenų saugojimui
- `abc` — abstrakčioms klasėms