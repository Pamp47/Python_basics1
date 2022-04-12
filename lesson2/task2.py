# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и
# кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов: ['в', '"',
# '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для
# чисел со знаком? Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его
# реализации позже. Главное: дополнить числа до двух разрядов нулём!

list_basic = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list1_new = []
for i in list_basic:
    num1 = i.isdigit()
    num2 = (i[0] == '+' or i[0] == '-') and i[1:].isdigit()
    if num1 or num2:
        if len(i) == 1:
            i = f'0{i}'
        elif num2 and len(i[1:]) == 1:
            i = f'{i[0]}0{i[1:]}'
        list1_new.append('"')
        list1_new.append(i)
        list1_new.append('"')
    else:
        list1_new.append(i)
print(list1_new)
