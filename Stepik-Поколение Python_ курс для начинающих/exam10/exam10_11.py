'''
Переворот
На вход программе подается строка текста в которой буква «h» встречается как минимум два раза. Напишите программу, которая возвращает исходную строку и переворачивает последовательность символов, заключенную между первым и последним вхождением буквы «h».
Формат входных данных
На вход программе подается строка текста.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''

s = input()
ind_1 = s.find('h')
ind_2 = s.rfind('h')
rev_s = s[ind_2:ind_1:-1]
print(s[:ind_1] + rev_s + s[ind_2:])
