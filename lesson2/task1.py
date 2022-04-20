# Выяснить тип результата выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2


def mathematical_operations():
    multiplication = type(15 * 3)
    division = type(15 / 3)
    integer_division = type(15 // 2)
    degree = type(15 ** 2)
    # print(multiplication, division, integer_division, degree)
    return multiplication, division, integer_division, degree


mathematical_operations()
# print(mathematical_operations())
