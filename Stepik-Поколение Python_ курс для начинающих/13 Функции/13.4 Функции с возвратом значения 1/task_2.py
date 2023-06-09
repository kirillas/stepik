'''
Количество дней
Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.

Примечание 1. Гарантируется, что передаваемый аргумент находится в диапазоне от 1 до 12.

Примечание 2. Считайте, что год является невисокосным.
'''


def get_days(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        result = 31
    elif month in [4, 6, 9, 11]:
        result = 30
    else:
        result = 28
    return result


print(get_days(1))
print(get_days(2))
print(get_days(9))
