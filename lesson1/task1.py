"""
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""


def naive_realisation(duration: int):
    # total_time = str(f'Дней: {day}, часов: {hour}, минут: {minutes}, секунд: {seconds}')
    """
    Решение задачи БЕЗ использования циклов.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужно формате
    """
    day = duration // 60 // 60 // 24
    hour = duration // 60 // 60 % 24
    minutes = duration // 60 % 60
    seconds = duration % 60

    total_time = str(f'{day} дн {hour} час {minutes} мин {seconds} сек')
    # print(type(total_time))
    return total_time


def one_cycle_realisation(duration):
    # total_time = str(f'Дней: {day}, часов: {hour}, минут: {minutes}, секунд: {seconds}')
    """
    Решение задачи с использования циклов.
    Можно два, но высший пилотаж через 1 цикл.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужно формате
    """
    while duration > 0:
        day = duration // 60 // 60 // 24
        hour = duration // 60 // 60 % 24
        minutes = duration // 60 % 60
        seconds = duration % 60
        total_time = str(f'{day} дн {hour} час {minutes} мин {seconds} сек')
        return total_time


if __name__ == '__main__':
    duration = 123532
    print(naive_realisation(duration))
    print(one_cycle_realisation(duration))
