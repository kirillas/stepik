'''
Звездный треугольник
На вход программе подается натуральное число n \, (n \ge 2)n(n≥2) – катет прямоугольного равнобедренного треугольника.

Напишите программу, которая выводит звездный треугольник в соответствии с примером.

Формат входных данных
На вход программе подается одно натуральное число n \, (n \ge 2)n(n≥2).

Формат выходных данных
Программа должна вывести треугольник в соответствии с условием задачи.
'''

n = int(input())
k = n
for i in range(n):
    print("*" * k)
    k -= 1
