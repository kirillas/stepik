'''
Списочное выражение 1
На вход программе подается натуральное число nn. Напишите программу, использующую списочное выражение, которая создает список содержащий квадраты чисел от 11 до nn, а затем выводит его элементы построчно, то есть каждый на отдельной строке.
Формат входных данных
На вход программе подается натуральное число.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Примечание. Для вывода элементов списка используйте цикл for.
'''
n = int(input())

arr = [i ** 2 for i in range(1, n + 1)]

for elem in arr:
    print(elem)
