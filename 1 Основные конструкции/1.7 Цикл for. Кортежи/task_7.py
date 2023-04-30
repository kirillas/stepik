'''
Цвета радуги
﻿   Пятилетний Петя учит цвета радуги. Напишите программу, которая принимает на вход натуральное число n и печатает первые n цветов радуги с большой буквы. При этом, если n > 7, программа должна ответить "Радуга состоит только из семи цветов".
'''

n = int(input())
arr = ['Красный', 'Оранжевый', 'Желтый', 'Зеленый', 'Голубой', 'Синий', 'Фиолетовый']
if n > 7:
    print("Радуга состоит только из семи цветов")
else:
    print(*arr[0:n], sep='\n')
