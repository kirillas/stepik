"""
Напишите программу, которая вычисляет долю студентов, получивших оценку A.
Используется пятибальная система оценивания с оценками A, B, C, D, F.
Формат ввода:
Строка, в которой через пробел записаны оценки студентов. Оценок всегда не меньше одной.
Формат вывода:
Дробное число с ровно двумя знаками после запятой.
"""

str_score = input().split()
col = len(str_score)
A = str_score.count('A')
print("{0:.2f}".format(A / col))
