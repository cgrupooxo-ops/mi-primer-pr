import unittest

from conversor import celsius_a_fahrenheit, fahrenheit_a_celsius


class TestConversor(unittest.TestCase):
    def test_celsius_a_fahrenheit(self):
        self.assertEqual(celsius_a_fahrenheit(0), 32)
        self.assertEqual(celsius_a_fahrenheit(100), 212)

    def test_fahrenheit_a_celsius(self):
        self.assertEqual(fahrenheit_a_celsius(32), 0)
        self.assertEqual(fahrenheit_a_celsius(212), 100)


if __name__ == "__main__":
    unittest.main()
