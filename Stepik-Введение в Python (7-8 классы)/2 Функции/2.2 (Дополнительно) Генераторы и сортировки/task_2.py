'''
Вокруг света за 80 итераций
        Путешественник Фредерик Фортран устал от всяких пари и приехал в Италию отдохнуть. Он купил туристический справочник в ближайшей лавке, но не может решить, какие из многочисленных мест посетить. Известно, что путешественник хочет посетить места, наиболее близкие к его текущему местоположению. На каждой странице справочника представлены три места, из которых он выбирает наилучшее. Помогите Фортрану и спланируйте для него список мест.

        Формат ввода: на первой строке — количество страниц в справочнике n, в следующих строках — характеристики трех мест. Характеристики разделены запятой и состоят из названия места и удаленности от города, где остановился путешественник. Эти параметры разделены пробелом.

        Формат вывода: список названий мест, которые стоит посетить Фортрану, разделены запятой.
'''

n = int(input())
arr = []
for _ in range(n):
    a1 = [i.split() for i in input().split(', ')]
    a2 = list(map(lambda t: (t[0], int(t[1])), a1))
    out = sorted(a2, key=lambda item: item[1])
    arr.append(out[0][0])

print(*arr, sep=', ')
