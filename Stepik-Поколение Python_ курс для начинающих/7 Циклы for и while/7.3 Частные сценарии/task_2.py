'''
Сумма чисел
На вход программе подается натуральное число nn, а затем nn целых чисел, каждое на отдельной строке. Напишите программу, которая подсчитывает сумму введенных чисел.

Формат входных данных
На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести сумму данных чисел.
'''
n = int(input())
summary = 0
for i in range(n):
    num = int(input())
    summary += num
print(summary)
