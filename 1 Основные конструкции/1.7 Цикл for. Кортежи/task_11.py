'''
Коровы
  С клавиатуры вводится натуральное число n <= 100. Выведите n строк вида "На лугу n коров", склоняя слово "коров" в соответствии с числом n.
'''

num = int(input())
for i in range(1, num + 1):
    if 0 < i < 10 or 20 <= i <= 100:
        if i % 10 == 1:
            print('На лугу', i, 'корова')
        elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
            print('На лугу', i, 'коровы')
        else:
            print('На лугу', i, 'коров')
    else:
        print('На лугу', i, 'коров')
       