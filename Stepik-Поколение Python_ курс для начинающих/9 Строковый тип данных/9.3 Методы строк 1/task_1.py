'''
Заглавные буквы
На вход программе подается строка состоящая из имени и фамилии человека, разделенных одним пробелом. Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.

Формат входных данных
На вход программе подается строка.

Формат выходных данных
Программа должна вывести «YES» если имя и фамилия начинаются с заглавной буквы и «NO» в противном случае.

Примечание. Строка содержит только буквы.
'''

s = input()
s1 = s.title()
if s == s1:
    print('YES')
else:
    print('NO')
