import unittest
from format_price import format_price


class TestFormattingPrice(unittest.TestCase):
    def test_int(self):
        formatted_price = format_price(4645)
        self.assertEqual(formatted_price, '4 645')

    def test_float(self):
        formatted_price = format_price(4645.0)
        self.assertEqual(formatted_price, '4 645')

    def test_string(self):
        formatted_price = format_price('4645.00')
        self.assertEqual(formatted_price, '4 645')

    def test_incorrect_input(self):
        formatted_price = format_price('4645abc')
        self.assertEqual(formatted_price, None)

    def test_negative_number(self):
        formatted_price = format_price(-4645)
        self.assertEqual(formatted_price, None)

    def test_wrong_delimiter(self):
        formatted_price = format_price('4645,0055')
        self.assertEqual(formatted_price, None)

    def test_high_accuracy(self):
        formatted_price = format_price(4645.005512341)
        self.assertEqual(formatted_price, '4 645.01')

    def test_decimal(self):
        formatted_price = format_price(4645.30000000000000426325641456060111522674560546875)
        self.assertEqual(formatted_price, '4 645.30')


if __name__ == '__main__':
    unittest.main()
