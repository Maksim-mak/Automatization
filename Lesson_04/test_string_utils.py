import unittest
from string_utils import StringUtils
# Предполагаем, что класс находится в string_utils.py


class TestStringUtils(unittest.TestCase):

    def setUp(self):
        self.utils = StringUtils()

    # Позитивные тесты
    def test_capitalize(self):
        self.assertEqual(self.utils.capitalize("skypro"), "Skypro")
        self.assertEqual(self.utils.capitalize("hello"), "Hello")
        self.assertEqual(self.utils.capitalize(" python"), " Python")

    def test_trim(self):
        self.assertEqual(self.utils.trim("   skypro"), "skypro")
        self.assertEqual(self.utils.trim("      hello world  "),
                         "hello world  ")
        self.assertEqual(self.utils.trim("no leading spaces"),
                         "no leading spaces")

    def test_contains(self):
        self.assertTrue(self.utils.contains("SkyPro", "S"))
        self.assertTrue(self.utils.contains("hello", "h"))
        self.assertTrue(self.utils.contains("12345", "3"))

    def test_delete_symbol(self):
        self.assertEqual(self.utils.delete_symbol("SkyPro", "k"), "SyPro")
        self.assertEqual(self.utils.delete_symbol("Hello World", "o"),
                         "Hell Wrld")
        self.assertEqual(self.utils.delete_symbol("Hello", "x"), "Hello")

    # Негативные тесты
    def test_empty_string_capitalize(self):
        self.assertEqual(self.utils.capitalize(""), "")
        self.assertEqual(self.utils.capitalize(" "), " ")

    def test_trim_empty_string(self):
        self.assertEqual(self.utils.trim(""), "")
        self.assertEqual(self.utils.trim("     "), "")

    def test_contains_false(self):
        self.assertFalse(self.utils.contains("SkyPro", "U"))
        self.assertFalse(self.utils.contains("Python", "x"))

    def test_delete_symbol_nonexistent(self):
        self.assertEqual(self.utils.delete_symbol("SkyPro", "z"), "SkyPro")
        self.assertEqual(self.utils.delete_symbol("", "a"), "")
        self.assertEqual(self.utils.delete_symbol("   ", " "),
                         "   ")  # пробел остается


if __name__ == "__main__":
    unittest.main()
