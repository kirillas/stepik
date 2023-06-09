'''
Самое длинное слово в файле
Вам доступен текстовый файл words.txt со словами, разделенными пробелом. Напишите программу, которая находит и выводит самые длинные слова этого файла, не меняя порядка их следования.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести самые длинные слова файла words.txt, каждое с новой строки, не меняя их порядка следования.

Примечание 1. Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. Словом считайте любую группу символов без пробелов, даже если она включает цифры или знаки препинания.
'''

with open('words.txt', encoding='utf-8') as file:
    content = file.read().split(' ')
    arr_length = [len(word) for word in content]
    m = max(arr_length)
    res = list(filter(lambda w: len(w) == m, content))
    print(*res, sep='\n')
