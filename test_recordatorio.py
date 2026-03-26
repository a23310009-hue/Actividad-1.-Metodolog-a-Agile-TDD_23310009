import unittest
from recordatorios import generar_recordatorio

class TestRecordatorio(unittest.TestCase):

    def test_generar_recordatorio_cita_medica(self):
        resultado = generar_recordatorio("María", "25/03/2026", "10:00 AM")
        self.assertEqual(
            resultado,
            "Recordatorio para María: cita médica el 25/03/2026 a las 10:00 AM"
        )

if __name__ == "__main__":
    unittest.main()
