"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
"И": ["Иван", "Илья"], #random_dict["I"] = []
"М": ["Мария"],        #random_dict["I"].append('Ivan')
"П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется
сортировка по ключам? Можно ли использовать словарь в этом случае?
"""


def thesaurus(*args):
    result_dict = dict()
    for name in args:
        initial_letter = name[0]
        if initial_letter in result_dict:
            result_dict[initial_letter].append(name)
        else:
            result_dict[initial_letter] = [name]

    sort_dict = dict()
    for key in sorted(result_dict):
        sort_dict[key] = result_dict[key]

    return sort_dict


if __name__ == "__main__":
    print(thesaurus("Иван", "Мария", "Петр", "Илья", "Афанасий", 'Авдотья'))

# person_name = 'Маша', 'Петя', 'Вася', 'Женя', 'Анна', 'Дима'
# d1 = dict()
# for name1 in person_name:
#     # print(n1)
#     n1 = name1[0]
#     if name1 in n1:
#         d1[n1].append(name1)
#     else:
#         d1[n1] = [name1]
# print(d1)


