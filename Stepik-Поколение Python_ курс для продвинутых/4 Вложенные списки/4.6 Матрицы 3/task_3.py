'''
Заполнение 1
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n \times mn×m и заполняет её числами от 11 до n \cdot mn⋅m в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести матрицу в соответствии с образцом.

Примечание. Для вывода элементов матрицы как в примерах, отводите ровно 33 символа на каждый элемент. Для этого используйте строковый метод ljust(). Можно обойтись и без ljust(), система примет и такое решение 😇
'''

arr = [int(i) for i in input().split()]
n = arr[0]
m = arr[1]

matrix = [[0 for j in range(m)] for i in range(n)]

elem = 1
for i in range(n):
    for j in range(m):
        matrix[i][j] = elem
        elem += 1
        print(str(matrix[i][j]).ljust(3), end='')
    print()
