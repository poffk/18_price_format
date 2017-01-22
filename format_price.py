import argparse
from re import search


def parse_price():
    parser = argparse.ArgumentParser()
    parser.add_argument('price',
                        help='введите значение(цену) для форматирования')
    return parser.parse_args()


def make_price_beatiful(price):
    beatiful_price = '{0:,.2f}'.format(price).replace(',', ' ')
    if search(r'\d*[.]00', beatiful_price):
        beatiful_price = beatiful_price[:-3]
    return beatiful_price


def format_price(price):
    try:
        price = float(price)
    except ValueError:
        return None
    if price < 0:
        return None
    return make_price_beatiful(price)


if __name__ == '__main__':
    parser = parse_price()
    price = parser.price
    formatted_price = format_price(price)
    if formatted_price is None:
        print('Ошибка ввода')
    else:
        print('Отформатированная цена: {}'.format(formatted_price))
