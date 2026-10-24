import unittest

from calculator import konversi_berat


class CalculatorTests(unittest.TestCase):
    def test_konversi_berat_menolak_tipe_input_tidak_valid(self):
        with self.assertRaises(ValueError):
            konversi_berat(80, 80, "salah")

    def test_konversi_berat_menerima_tipe_input_valid(self):
        self.assertEqual(konversi_berat(100, 80, "kotor"), (100, 80.0))
        self.assertEqual(konversi_berat(80, 80, "bersih"), (100.0, 80))


if __name__ == "__main__":
    unittest.main()