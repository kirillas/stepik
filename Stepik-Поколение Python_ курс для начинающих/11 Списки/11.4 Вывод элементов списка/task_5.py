'''
Google search - 1
На вход программе подается натуральное число nn, затем nn строк, затем еще одна строка — поисковый запрос. Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
Формат входных данных
На вход программе подаются натуральное число nn — количество строк, затем сами строки в указанном количестве, затем один поисковый запрос.
Формат выходных данных
Программа должна вывести все введенные строки, в которых встречается поисковый запрос.
Примечание. Поиск не должен быть чувствителен к регистру символов.
'''

n = int(input())
arr = []
for _ in range(n):
    s = input()
    arr.append(s)

query = input()

for s in arr:
    if s.lower().find(query.lower()) != -1:
        print(s)
