'''
Цифра 1
На вход программе подается одна строка состоящая из цифр. Напишите программу, которая считает сумму цифр данной строки.

Формат входных данных
На вход программе подается одна строка состоящая из цифр.

Формат выходных данных
Программа должна вывести сумму цифр данной строки.
'''

s = input()
summa = 0
for c in s:
    summa += int(c)
print(summa)
