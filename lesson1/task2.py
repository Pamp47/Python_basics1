"""
Задание 2
* Создать список, состоящий из кубов нечётных чисел от 1 до 1000
  (куб X - третья степень числа X):
* Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
  Например, число «19 ^ 3 = 6859» будем включать в сумму,
  так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
* К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из
  этого списка, сумма цифр которых делится нацело на 7.
* Решить задачу под пунктом b, не создавая новый список.)
"""

my_list = []
for i in range(1, 1001, 2):
    my_list.append(i)
print(my_list)


def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""

    for j in range(1, 1001, 2):
        num1 = j ** 3 // 100000000
        num2 = j ** 3 // 10000000 % 10
        num3 = j ** 3 // 1000000 % 10
        num4 = j ** 3 // 100000 % 10
        num5 = j ** 3 // 10000 % 10
        num6 = j ** 3 // 1000 % 10
        num7 = j ** 3 // 100 % 10
        num8 = j ** 3 // 10 % 10
        num9 = j ** 3 % 10
        if num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 == 28:
            print(f'{j} ^ 3 = {j**3}')

    return 1


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка, 
        сумма цифр которых делится нацело на 7"""
    # место для написания кода
    return 1  # Верните значение полученной суммы


if __name__ == '__main__':
    my_list = []  # Соберите нужный список по заданию
    result_1 = sum_list_1(my_list)
    print(result_1)
    result_2 = sum_list_2(my_list)
    print(result_2)