
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

##