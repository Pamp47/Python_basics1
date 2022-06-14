class CheckZeroDivision(ZeroDivisionError): pass


def divide(num, denom):
    try:
        return num / denom
    except ZeroDivisionError:
        raise CheckZeroDivision(f"Деление {num} на {denom} невозможно")


try:
    print(divide(19, 2))
    print(divide(14, 0))
except CheckZeroDivision as err:
    print(err)
