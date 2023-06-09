'''Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое
 слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически
  первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.
Sample Input:
abc a bCd bC AbC BC BCD bcd ABC

Sample Output:
abc 3
'''
with open('sample_input2.txt', 'r') as file:
    str = file.read()
    lst = str.lower().split()  # перевели строки в список
    lst_one = list(set(lst))

    d = {}  # формируем словарь в котором будут храниться кол-во повторяющихся строк  'abc':12

    for i in lst_one:
        count = lst.count(i)
        d[i] = count

    temp = max(zip(d.values(), d.keys()))
    print(temp)
