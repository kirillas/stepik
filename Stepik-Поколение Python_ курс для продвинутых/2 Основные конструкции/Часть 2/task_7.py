'''
 Камень, ножницы, бумага
Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов". Для этого они решили сыграть в камень, ножницы и бумагу. Помогите ребятам бросить честный жребий и определить, кто будет делать очередной модуль нового курса.
Формат входных данных
На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага". На первой строке записан выбор Тимура, на второй – выбор Руслана.
Формат выходных данных
Программа должна вывести результат жеребьёвки, то есть кто победит Тимур, Руслан или они сыграют вничью.
'''
timur = input()
ruslan = input()

if timur == ruslan:
    print("ничья")
    exit(0)

if ((timur == 'ножницы' and ruslan == 'бумага') or
        (timur == 'бумага' and ruslan == 'камень') or
        (timur == 'камень' and ruslan == 'ножницы')):
    print('Тимур')
else:
    print('Руслан')
