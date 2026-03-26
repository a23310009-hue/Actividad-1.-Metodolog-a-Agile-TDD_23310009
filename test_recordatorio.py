import unittest
from recordatorios import generar_recordatorio

class TestRecordatorio(unittest.TestCase):

    def test_generar_recordatorio_cita_medica(self):
        resultado = generar_recordatorio("María", "25/03/2026", "10:00 AM")
        self.assertEqual(
            resultado,
            "Recordatorio para María: cita médica el 25/03/2026 a las 10:00 AM"
        )

    def test_recordatorio_vacio(self):
        resultado = generar_recordatorio("", "", "")
        self.assertEqual(
            resultado,
            "Error: datos incompletos"
        )

    def test_recordatorio_datos_incompletos(self):
        resultado = generar_recordatorio("María", "", "10:00 AM")
        self.assertEqual(
            resultado,
            "Error: datos incompletos"
        )

if __name__ == "__main__":
    unittest.main()
