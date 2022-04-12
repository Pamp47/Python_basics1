"""
Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
"""
percent = 1
while percent <= 100:
    if 10 <= percent <= 20:
        print(percent, 'процентов')
    elif percent == 1 or percent % 10 == 1:
        print(percent, 'процент')
    elif percent % 10 == 5 or percent % 10 == 6 or percent % 10 == 7 or percent % 10 == 8 or percent % 10 == 9 or percent % 10 == 0:
        print(percent, 'процентов')
    elif percent % 10 == 2 or percent % 10 == 3 or percent % 10 == 4:
        print(percent, 'процента')
    percent += 1


def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""

    # return 'верните отформатированную строку'

# if __name__ == '__main__':
#     for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
#         print(transform_string(n))
