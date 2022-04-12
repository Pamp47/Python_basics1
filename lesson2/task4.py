#  Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например
# «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7
# копеек или 0 копеек (должно быть 07 коп или 00 коп). Вывести цены, отсортированные по возрастанию, новый список не
# создавать (доказать, что объект списка после сортировки остался тот же). Создать новый список, содержащий те же
# цены, но отсортированные по убыванию. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров
# по возрастанию, написав минимум кода?


price = [43.04, 11, 95.55, 12, 54.54, 87.89, 11.11, 98, 564, 1.01, 76, 99.9]
for i in price:
    i_rub = int(i)
    i_kop_round = round((i - i_rub) * 100)
    print(f'{i_rub} руб {i_kop_round:02} коп')

# Вывести цены, отсортированные по возрастанию, новый список не
# # создавать (доказать, что объект списка после сортировки остался тот же).

print(price, id(price))
price.sort()
print(price, id(price))

# Создать новый список, содержащий те же цены, но отсортированные по убыванию.

print(price, id(price))
price_copy = sorted(price, reverse=True)
print(price_copy, id(price_copy))


# Вывести цены пяти самых дорогих товаров
for i in price_copy[:5]:
    print(i)