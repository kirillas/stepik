'''
Список делителей
На вход программе подается натуральное число nn. Напишите программу, которая создает список состоящий из делителей введенного числа.
Формат входных данных
На вход программе подается натуральное число nn.
Формат выходных данных
Программа должна вывести список, состоящий из делителей введенного числа.
'''

n = int(input())
arr = []
for i in range(1, n + 1):
    if n % i == 0:
        arr.append(i)
print(arr)
