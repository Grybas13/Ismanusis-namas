import unittest
from devices.light import Light
from devices.thermostat import Thermostat
from devices.camera import Camera
from factory.device_factory import DeviceFactory
from home.room import Room
from home.smart_home import SmartHome


# ===== LIGHT TESTAI =====
class TestLight(unittest.TestCase):

    def test_turn_on(self):
        # Įjungus lempą — is_on() turi būti True
        lempa = Light("Lempa", "Svetainė")
        lempa.turn_on()
        self.assertTrue(lempa.is_on())

    def test_turn_off(self):
        # Išjungus lempą — is_on() turi būti False
        lempa = Light("Lempa", "Svetainė")
        lempa.turn_on()
        lempa.turn_off()
        self.assertFalse(lempa.is_on())

    def test_default_brightness(self):
        # Numatytasis ryškumas turi būti 100
        lempa = Light("Lempa", "Svetainė")
        self.assertEqual(lempa.get_brightness(), 100)

    def test_set_brightness(self):
        # Ryškumas turi pasikeisti į 75
        lempa = Light("Lempa", "Svetainė")
        lempa.set_brightness(75)
        self.assertEqual(lempa.get_brightness(), 75)

    def test_invalid_brightness_too_high(self):
        # Ryškumas negali viršyti 100 — turi likti nepakitęs
        lempa = Light("Lempa", "Svetainė")
        lempa.set_brightness(150)
        self.assertEqual(lempa.get_brightness(), 100)

    def test_invalid_brightness_negative(self):
        # Neigiamas ryškumas — turi likti nepakitęs
        lempa = Light("Lempa", "Svetainė")
        lempa.set_brightness(-10)
        self.assertEqual(lempa.get_brightness(), 100)

    def test_status_keys(self):
        # get_status() turi turėti visus reikalingus raktus
        lempa = Light("Lempa", "Svetainė")
        status = lempa.get_status()
        self.assertIn("pavadinimas", status)
        self.assertIn("kambarys", status)
        self.assertIn("tipas", status)
        self.assertIn("ar_ijungta", status)
        self.assertIn("ryskumas", status)

    def test_status_type(self):
        # tipas turi būti "light"
        lempa = Light("Lempa", "Svetainė")
        self.assertEqual(lempa.get_status()["tipas"], "light")

    def test_initial_state_is_off(self):
        # Naujai sukurta lempa turi būti išjungta
        lempa = Light("Lempa", "Svetainė")
        self.assertFalse(lempa.is_on())


# ===== THERMOSTAT TESTAI =====
class TestThermostat(unittest.TestCase):

    def test_turn_on(self):
        t = Thermostat("Termostatas", "Miegamasis")
        t.turn_on()
        self.assertTrue(t.is_on())

    def test_turn_off(self):
        t = Thermostat("Termostatas", "Miegamasis")
        t.turn_on()
        t.turn_off()
        self.assertFalse(t.is_on())

    def test_set_valid_target_temp(self):
        # Teisinga temperatūra turi būti išsaugota
        t = Thermostat("Termostatas", "Miegamasis")
        t.set_target_temp(23.0)
        self.assertEqual(t.get_status()["norima_temperatura"], 23.0)

    def test_set_invalid_temp_too_high(self):
        # Per aukšta temperatūra — turi likti numatytoji
        t = Thermostat("Termostatas", "Miegamasis")
        t.set_target_temp(100.0)
        self.assertEqual(t.get_status()["norima_temperatura"], 21.0)

    def test_set_invalid_temp_too_low(self):
        # Per žema temperatūra — turi likti numatytoji
        t = Thermostat("Termostatas", "Miegamasis")
        t.set_target_temp(-10.0)
        self.assertEqual(t.get_status()["norima_temperatura"], 21.0)

    def test_default_humidity(self):
        # Numatytoji drėgmė turi būti 50
        t = Thermostat("Termostatas", "Miegamasis")
        self.assertEqual(t.get_humidity(), 50)

    def test_update_readings(self):
        # Atnaujinus rodmenis — turi pasikeisti temperatūra ir drėgmė
        t = Thermostat("Termostatas", "Miegamasis")
        t.update_readings(25.0, 60)
        status = t.get_status()
        self.assertEqual(status["dabartine_temperatura"], 25.0)
        self.assertEqual(status["dregme"], 60)

    def test_status_type(self):
        t = Thermostat("Termostatas", "Miegamasis")
        self.assertEqual(t.get_status()["tipas"], "thermostat")


# ===== CAMERA TESTAI =====
class TestCamera(unittest.TestCase):

    def test_turn_on(self):
        k = Camera("Kamera", "Prieškambaris")
        k.turn_on()
        self.assertTrue(k.is_on())

    def test_turn_off(self):
        k = Camera("Kamera", "Prieškambaris")
        k.turn_on()
        k.turn_off()
        self.assertFalse(k.is_on())

    def test_start_recording(self):
        # Įjungus kamerą ir pradėjus įrašymą — is_recording() turi būti True
        k = Camera("Kamera", "Prieškambaris")
        k.turn_on()
        k.start_recording()
        self.assertTrue(k.is_recording())

    def test_stop_recording(self):
        # Sustabdžius įrašymą — is_recording() turi būti False
        k = Camera("Kamera", "Prieškambaris")
        k.turn_on()
        k.start_recording()
        k.stop_recording()
        self.assertFalse(k.is_recording())

    def test_recording_without_turning_on(self):
        # Neįjungus kameros — įrašymas neturi prasidėti
        k = Camera("Kamera", "Prieškambaris")
        k.start_recording()
        self.assertFalse(k.is_recording())

    def test_default_resolution(self):
        k = Camera("Kamera", "Prieškambaris")
        self.assertEqual(k.get_status()["rezoliucija"], "2160p")

    def test_status_type(self):
        k = Camera("Kamera", "Prieškambaris")
        self.assertEqual(k.get_status()["tipas"], "camera")

    def test_initial_not_recording(self):
        # Naujai sukurta kamera neturi įrašinėti
        k = Camera("Kamera", "Prieškambaris")
        self.assertFalse(k.is_recording())


# ===== DEVICE FACTORY TESTAI =====
class TestDeviceFactory(unittest.TestCase):

    def test_create_light(self):
        p = DeviceFactory.create("light", "Lempa", "Svetainė")
        self.assertIsInstance(p, Light)

    def test_create_thermostat(self):
        p = DeviceFactory.create("thermostat", "Termostatas", "Miegamasis")
        self.assertIsInstance(p, Thermostat)

    def test_create_camera(self):
        p = DeviceFactory.create("camera", "Kamera", "Prieškambaris")
        self.assertIsInstance(p, Camera)

    def test_create_unknown(self):
        # Nežinomas tipas turi grąžinti None
        p = DeviceFactory.create("unknown", "X", "Y")
        self.assertIsNone(p)

    def test_created_device_name(self):
        # Sukurto prietaiso pavadinimas turi sutapti
        p = DeviceFactory.create("light", "Mano lempa", "Svetainė")
        self.assertEqual(p.get_name(), "Mano lempa")

    def test_created_device_room(self):
        # Sukurto prietaiso kambarys turi sutapti
        p = DeviceFactory.create("thermostat", "T", "Virtuvė")
        self.assertEqual(p.get_room(), "Virtuvė")


# ===== ROOM TESTAI =====
class TestRoom(unittest.TestCase):

    def test_add_device(self):
        kambarys = Room("Svetainė")
        lempa = Light("Lempa", "Svetainė")
        kambarys.add_device(lempa)
        self.assertEqual(len(kambarys.get_devices()), 1)

    def test_remove_device(self):
        kambarys = Room("Svetainė")
        lempa = Light("Lempa", "Svetainė")
        kambarys.add_device(lempa)
        kambarys.remove_device("Lempa")
        self.assertEqual(len(kambarys.get_devices()), 0)

    def test_remove_nonexistent_device(self):
        # Pašalinus neegzistuojantį prietaisą — sąrašas turi likti nepakitęs
        kambarys = Room("Svetainė")
        kambarys.remove_device("Neegzistuoja")
        self.assertEqual(len(kambarys.get_devices()), 0)

    def test_turn_on_all(self):
        kambarys = Room("Svetainė")
        kambarys.add_device(Light("Lempa1", "Svetainė"))
        kambarys.add_device(Light("Lempa2", "Svetainė"))
        kambarys.turn_on_all()
        for device in kambarys.get_devices():
            self.assertTrue(device.is_on())

    def test_turn_off_all(self):
        kambarys = Room("Svetainė")
        kambarys.add_device(Light("Lempa1", "Svetainė"))
        kambarys.add_device(Light("Lempa2", "Svetainė"))
        kambarys.turn_on_all()
        kambarys.turn_off_all()
        for device in kambarys.get_devices():
            self.assertFalse(device.is_on())

    def test_get_name(self):
        kambarys = Room("Virtuvė")
        self.assertEqual(kambarys.get_name(), "Virtuvė")

    def test_empty_room(self):
        # Tuščias kambarys turi turėti 0 prietaisų
        kambarys = Room("Svetainė")
        self.assertEqual(len(kambarys.get_devices()), 0)


# ===== SMART HOME TESTAI =====
class TestSmartHome(unittest.TestCase):

    def test_add_room(self):
        namas = SmartHome("Mano namai")
        namas.add_room(Room("Svetainė"))
        self.assertEqual(len(namas.get_rooms()), 1)

    def test_remove_room(self):
        namas = SmartHome("Mano namai")
        namas.add_room(Room("Svetainė"))
        namas.remove_room("Svetainė")
        self.assertEqual(len(namas.get_rooms()), 0)

    def test_get_room(self):
        namas = SmartHome("Mano namai")
        namas.add_room(Room("Svetainė"))
        kambarys = namas.get_room("Svetainė")
        self.assertIsNotNone(kambarys)
        self.assertEqual(kambarys.get_name(), "Svetainė")

    def test_get_nonexistent_room(self):
        namas = SmartHome("Mano namai")
        self.assertIsNone(namas.get_room("Neegzistuoja"))

    def test_turn_on_all(self):
        namas = SmartHome("Mano namai")
        svetaine = Room("Svetainė")
        svetaine.add_device(Light("Lempa", "Svetainė"))
        namas.add_room(svetaine)
        namas.turn_on_all()
        for room in namas.get_rooms():
            for device in room.get_devices():
                self.assertTrue(device.is_on())


if __name__ == "__main__":
    unittest.main()