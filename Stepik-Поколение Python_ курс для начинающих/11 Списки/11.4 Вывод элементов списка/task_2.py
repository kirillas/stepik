'''
Значение функции
На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая для каждого введенного числа xx выводит значение функции f(x) = x^2 + 2x + 1 каждое на отдельной строке.
Формат входных данных
На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести сначала введенные числа, затем пустую строку, а затем соответствующие значения функции.
'''

n = int(input())
arr = []
for _ in range(n):
    x = int(input())
    arr.append(x)

for x in arr:
    print(x)
print()
for x in arr:
    print(x ** 2 + 2 * x + 1)
