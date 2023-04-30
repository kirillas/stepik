'''
Сумма дробей 2
На вход программе подается натуральное число nn. Напишите программу, которая вычисляет и выводит рациональное число, равное значению выражения
Формат входных данных
На вход программе подается натуральное число nn.

Формат выходных данных
Программа должна вывести ответ на задачу.

Примечание 1. Результирующая дробь должна быть несократимой.

Примечание 2. Для вычисления факториала можно использовать функцию factorial из модуля math.
'''

from fractions import Fraction
import math

n = int(input())
summa = 0
for i in range(1, n + 1):
    summa += Fraction(1, math.factorial(i))

print(summa)
