'''
Цифры числа
    Напишите рекурсивную функцию digits(n), которая принимает натуральное число и возвращает строку с цифрами этого числа слева направо, разделяя их пробелами. Кроме функции ничего писать не нужно.
'''


def digits(n):
    if n < 10:
        return str(n)
    else:
        return digits(n // 10) + ' ' + str(n % 10)


n = int(input())
print(digits(n))
