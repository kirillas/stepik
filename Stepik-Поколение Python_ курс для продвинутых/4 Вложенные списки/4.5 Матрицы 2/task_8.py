'''
Ходы коня
На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки, которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь, отметьте символами *, остальные клетки заполните точками.
'''

posstr = input()
chess = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = 8 - int(posstr[1])
y = chess.index(posstr[0])

matrix = [['.'] * 8 for _ in range(8)]
matrix[x][y] = 'N'

for i in range(8):
    for j in range(8):
        if abs((x - i) * (y - j)) == 2:
            matrix[i][j] = '*'
        print(matrix[i][j], end=' ')
    print()
