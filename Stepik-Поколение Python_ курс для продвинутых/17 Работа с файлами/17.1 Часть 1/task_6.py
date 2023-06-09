'''
Общая стоимость
Вам доступен текстовый файл prices.txt с информацией о заказе из интернет магазина. В нем каждая строка с помощью символа табуляции (\t) разделена на три колонки:

наименование товара;
количество товара (целое число);
цена (в рублях) товара за 11 шт (целое число).
Напишите программу, выводящую на экран общую стоимость заказа.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести общую стоимость заказа.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Не забудьте закрыть файл 🙂.

Примечание 3. Указанный файл можно скачать по ссылке.
'''

file = open('prices.txt', encoding='utf-8')
lines = list(map(str.strip, file.readlines()))
arr = [a.split() for a in lines]
summary = 0
for elem in arr:
    summary += int(elem[1]) * int(elem[2])
print(summary)
file.close()
