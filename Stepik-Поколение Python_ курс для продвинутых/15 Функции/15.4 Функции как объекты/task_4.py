'''
Сортируй как хочешь
Список athletes содержит сведения о спортсменах в виде кортежей: (имя, возраст, рост, вес).

Напишите программу сортировки списка спортсменов по указанному полю:

11: по имени;
22: по возрасту;
33: по росту;
44: по весу.
Формат входных данных
На вход программе подается натуральное число от 11 до 44 – номер поля по которому требуется отсортировать список.

Формат выходных данных
Программа должна вывести отсортированный по заданному полю список в соответствии с примерами.
'''

athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]


def sorted_by_param(n):
    def compare(item):
        return item[n - 1]

    return sorted(athletes, key=compare)


n = int(input())
for t in sorted_by_param(n):
    print(*t)
