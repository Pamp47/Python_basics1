from requests import get, utils


def currency_rates(url, currency_name):
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    capital_letter = content.find(currency_name.upper())  # Переводим переменную к заглавным буквам

    if capital_letter:
        # Каждое следующее значение мы ищем, начиная от предыдущего
        tag_open = content.find("<Value>", capital_letter)
        tag_close = content.find("</Value>", tag_open)
        tag_value_length = 7  # Длина тега <Value>
        currency = content[tag_open + tag_value_length: tag_close].replace(',', '.')
        return currency


if __name__ == '__main__':
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    currency_rates(url, "USD")
    print(currency_rates(url, "USD"))

    currency_rates(url, "EUR")
    print(currency_rates(url, "EUR"))
