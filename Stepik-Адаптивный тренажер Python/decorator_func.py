"""
Имеется реализованная функция f(x)f(x), принимающая на вход целое число xx, которая вычисляет
некоторое целочисленое значение и возвращает его в качестве результата работы.
Функция вычисляется достаточно долго, ничего не выводит на экран, не пишет в файлы и зависит
только от переданного аргумента xx.
Напишите программу, которая вычисляет значение этой функции для nn чисел.
Для ускорения вычисления необходимо сохранять уже вычисленные значения функции при известных аргументах.
"""
def f(x):
    return x**2


n = int(input())
args = []
value_func = {}
while n > 0:
    k = input()
    args.append(k)
    n -= 1

for iter in args:
    if iter in value_func:
        print(value_func[iter])
    else:
        value_func[iter] = f(int(iter))
        print(value_func[iter])

