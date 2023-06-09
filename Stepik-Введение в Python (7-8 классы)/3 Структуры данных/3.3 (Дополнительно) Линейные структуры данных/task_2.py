'''
TO-DO List
    Эффективный менеджер Иван пользуется карточками для управления временем. В течение рабочего дня он записывает на них задания и складывает в стопку. Выполняя задания, он постепенно убирает карточки из стопки. Напишите программу, которая анализирует его действия в течение рабочего дня и печатает список невыполненных дел.

    Формат ввода: число n — количество действий Ивана. Далее следуют n строк вида "Добавить: <задание>. <время>" или "Выполнить: <задание>. <время>". Обратите внимание, что действия передаются без привязки ко времени, то есть не являются последовательными.

    Формат вывода: список невыполненных дел через запятую, в порядке добавления карточек в стопку. Если список пуст, вывести "Все выполнено!"

    Гарантируется, что Иван выполняет только те задачи, которые уже находятся в стопке. Время принимает значение от 00:00 до 23:59.
'''

n = int(input())  # n — количество действий Ивана
tasks = []  # задачи
todo = {}  # структура вкл время
# {
# 10:27 : ['Добавить', ' поговорить о повышении']
# }


for i in range(n):
    str = input()
    cmd = str.split(":")[0]  # Добавить или Выполнить
    task_and_time = str.split(":", 1)[1]  # поговорить о повышении. 14:15
    task = task_and_time.split(".")[0]  # провести собеседование
    time = task_and_time.split(".")[1].strip()  # 12:59
    # заполняем структуру
    todo[time] = [cmd, task]

for key in sorted(todo):
    #print(key, ":", todo[key])
    if todo[key][0] == "Добавить":
        tasks.append(todo[key][1])
    elif todo[key][0] == "Выполнить" and todo[key][1] in tasks:
        tasks.remove(todo[key][1])

if len(tasks) == 0:
    print("Все выполнено!")
else:
    print(*tasks, sep=",")
