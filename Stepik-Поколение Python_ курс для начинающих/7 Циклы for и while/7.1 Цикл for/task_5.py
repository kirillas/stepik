'''
Повторяй за мной 2
Напишите программу, которая считывает одну строку текста и выводит 10 строк, пронумерованных от 0 до 9, каждая с указанной строкой текста.

Формат входных данных
На вход программе подается одна строка текста.

Формат выходных данных
Программа должна вывести десять строк в соответствии с условием задачи.
'''

s = input()

for i in range(10):
    print(i, s)
