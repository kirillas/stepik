'''
Список кубов
На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая создает из указанных чисел список их кубов.

Формат входных данных
На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести список, состоящий из кубов указанных чисел.
'''

n = int(input())
arr = []
for _ in range(n):
    m = int(input())
    arr.append(m ** 3)
print(arr)
