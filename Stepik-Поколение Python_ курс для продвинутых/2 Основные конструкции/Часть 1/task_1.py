'''
На easy
На вход программе подаются два целых числа aa и bb. Напишите программу, которая выводит:

сумму чисел aa и bb;
разность чисел aa и bb;
произведение чисел aa и bb;
частное чисел aa и bb;
целую часть от деления числа aa на bb;
остаток от деления числа aa на bb;
корень квадратный из суммы их 10-х степеней:
Формат входных данных
На вход программе подаются два целых числа a и b , каждое на отдельной строке.
'''
import math

a, b = int(input()), int(input())
# сумму чисел a и b;
print(a + b)
# разность чисел a и b;
print(a - b)
# произведение чисел a и b;
print(a * b)
# частное чисел a и b;
print(a / b)
# целую часть от деления числа a на b;
print(a // b)
# остаток от деления числа a на b;
print(a % b)
# корень квадратный из суммы их 10-х степеней:
print(math.sqrt(a ** 10 + b ** 10))
