'''
Задача Иосифа Флавия 🌶️🌶️
nn человек, пронумерованных числами от 11 до nn, стоят в кругу. Они начинают считаться, каждый kk-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека. Напишите программу, определяющую номер человека, который останется в кругу последним.
Формат входных данных
На вход программе подаются два числа nn и kk, записанные на отдельных строках.
Формат выходных данных
Программа должна вывести одно число – номер человека, который останется в кругу последним.
'''

n, k = int(input()), int(input())

arr = [i for i in range(1, n + 1)]

while len(arr) > 1:  # цикл до оставшегося последнего человека
    for _ in range(k - 1):
        elem = arr.pop(0)
        arr.append(elem)
    del arr[0]

print(*arr)
