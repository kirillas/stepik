'''
Удалите нечетные индексы
На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая создает из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.

Формат входных данных
На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести список в соответствии с условием задачи.

Примечание. Используйте оператор del.
'''

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

del arr[1::2]

print(arr)
