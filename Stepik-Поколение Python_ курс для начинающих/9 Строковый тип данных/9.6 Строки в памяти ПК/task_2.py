'''
Простой шифр
На вход программе подается строка текста. Напишите программу, которая переводит каждый ее символ в соответствующий ему код из таблицы символов Unicode.
Формат входных данных
На вход программе подается строка текста.
Формат выходных данных
Программа должна вывести кодовые значения символов строки разделенных одним символом пробела.
'''

s = input()
for c in s:
    print(ord(c), end=' ')
