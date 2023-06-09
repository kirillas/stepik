'''
Отличники
Учитель Тимур проверял контрольные работы по математике в нескольких классах онлайн-школы BEEGEEK и решил убедиться, что в каждом классе есть хотя бы один отличник – ученик с оценкой 55 по контрольной работе. Напишите программу с использованием встроенных функций all(), any() для помощи Тимуру в проверке.

Формат входных данных
На вход программе подается натуральное число nn – количество классов. Затем для каждого класса вводится блок информации вида:

натуральное число kk – количество учеников в классе;
далее вводится kk строк вида: фамилия оценка.
Формат выходных данных
Программа должна вывести YES, если в каждом классе есть хотя бы один отличник, и NO в противном случае.
'''
lst = []
n = int(input())
for _ in range(n):
    k = int(input())
    arr_class = [input().split() for _ in range(k)]
    any(map(lambda x: x[1] == '5', arr_class))
    lst.append(any(map(lambda x: x[1] == '5', arr_class)))

result = all(lst)

if result:
    print('YES')
else:
    print('NO')
