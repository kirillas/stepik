'''
Без дубликатов
На вход программе подается натуральное число nn, а затем nn строк. Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.
Формат входных данных
На вход программе подаются натуральное число nn, а затем nn строк, каждая на отдельной строке.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''
n = int(input())
arr = []
for _ in range(n):
    s = input()
    if s not in arr:
        arr.append(s)

print(*arr, sep='\n')
