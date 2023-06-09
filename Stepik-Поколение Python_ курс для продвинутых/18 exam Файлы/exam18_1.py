'''
Количество строк в файле
На вход программе подается строка текста с именем текстового файла. Напишите программу для вывода на экран количества строк данного файла.

Формат входных данных
На вход программе подается строка текста, содержащая имя существующего текстового файла.

Формат выходных данных
Программа должна вывести количество строк файла.

Примечание. Считайте, что исполняемая программа и указанный файл находятся в одной папке.
'''

filename = input()
with open(filename, encoding='utf-8') as file:
    content = file.readlines()
    count = len(content)
    print(count)
