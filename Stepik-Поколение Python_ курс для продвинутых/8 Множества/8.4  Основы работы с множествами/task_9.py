'''
Три слова
На вход программе подается строка, состоящая из трех слов. Верно ли, что для записи всех трех слов был использован один и тот же набор букв?

Формат входных данных
На вход программе подается строка, состоящая из трех слов.

Формат выходных данных
Программа должна вывести YES, если для записи всех трех слов был использован один и тот же набор букв и NO в противном случае.
'''

arr = input().split()
if set(arr[0]) == set(arr[1]) == set(arr[2]):
    print('YES')
else:
    print('NO')
