'''
 Напишите программу, которая принимает на вход произвольную последовательность строк, заканчивающуюся точкой. Подсчитайте, в скольких строках содержится слово python (именно слово, а не подстрока). При этом, такие слова, как Python или PYTHON тоже должны учитываться. Найдя количество k, выведите k-ый символ каждой строки через пробел.
'''

arr = []
while True:
    s = input()
    if s == '.':
        break
    arr.append(s)

count = 0
for elem in arr:
    a = elem.lower().split()
    if a.count("python") > 0:
        count += 1

for line in arr:
    print(line[count - 1], end=' ')
