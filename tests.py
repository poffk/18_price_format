import unittest
from format_price import format_price


class TestFormattingPrice(unittest.TestCase):
    def test_int(self):
        price = format_price(4645)
        self.assertEqual(price, '4 645')

    def test_float(self):
        price = format_price(4645.0)
        self.assertEqual(price, '4 645')

    def test_string(self):
        price = format_price('4645.00')
        self.assertEqual(price, '4 645')

    def test_incorrect_input(self):
        formatted_price = format_price('4645abc')
        self.assertEqual(formatted_price, None)

    def test_negative_number(self):
        formatted_price = format_price(-4645)
        self.assertEqual(formatted_price, None)


if __name__ == '__main__':
    unittest.main()
