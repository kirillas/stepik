'''
Решите уравнение в натуральных числах 28n + 30 k + 31 m = 36528n+30k+31m=365.

Примечание. Используйте вложенный цикл for. В первую очередь запишите решение с наименьшим значением nn.
'''

for n in range(1, 15):
    for k in range(1, 14):
        for m in range(1, 13):
            if 28 * n + 30 * k + 31 * m == 365:
                print(f"n={n} k={k} m={m}")
