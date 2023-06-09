'''
Шахматная парти﻿я питонистов
  Программисты тоже любят играть в шахматы (в основном, на компьютере), и нередко за них это делают программы. Напишите программу, которая принимает на вход четыре числа: сначала координаты начального положения короля на шахматной доске, затем координаты клетки, куда игрок хочет походить. Вам необходимо вывести "YES", если игрок может походить королем из клетки в клетку за один ход, и "NO" иначе. Гарантируется, что изначально король находится на доске. Нумерация рядов и столбцов доски начинается с 1.
'''

x0, y0 = int(input()), int(input())
x1, y1 = int(input()), int(input())

if abs(x1 - x0) <= 1 and abs(y1 - y0) <= 1 and (x0 != x1 or y0 != y1) and 1 <= x1 <= 8 and 1 <= y1 <= 8:
    print("YES")
else:
    print("NO")
