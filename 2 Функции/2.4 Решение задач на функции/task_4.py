'''
Называем переменные правильно
    В языке Python есть некоторые ограничения на имена переменных. Имена переменных

могут состоять только из цифр, букв и знаков подчеркивания

не могут начинаться с цифры

    Программист вводит строки с именами переменных. Для каждой переменной нужно вывести "Можно использовать", если ее имя корректно, или "Нельзя использовать", если это не так. Определив все нужные переменные, программист заканчивает ввод строкой "Поработали, и хватит". Для проверки каждой строки используйте функцию check_variable(v). Для простоты будем считать, что программист использует только латинские буквы.
'''


def check_variable(v):
    if v[0].isdigit():
        print('Нельзя использовать')
        return
    for i in v:
        if i.isalnum() or i == '_':
            continue
        else:
            print('Нельзя использовать')
            return
    print('Можно использовать')


while True:
    s = input()
    if s == 'Поработали, и хватит':
        break
    check_variable(s)
