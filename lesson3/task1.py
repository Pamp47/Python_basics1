"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на
русский язык. Например:
# >>> num_translate("one")
"один"
# >>> num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить
информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или
снаружи.
"""


def num_translate(number: str):
    translation = {'one': 'один',
                   'two': 'два',
                   'three': 'три',
                   'four': 'четыре',
                   'пять': 'пять',
                   'six': 'шесть',
                   'seven': 'семь',
                   'eight': 'восемь',
                   'nine': 'девять',
                   'ten': 'десять'
                   }
    return translation.get(number)


num_translate('two')

if __name__ == "__main__":
    print(num_translate('one'))
    print(num_translate('six'))
