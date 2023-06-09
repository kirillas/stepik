'''
Жаркий аукцион
    Перед началом торгов организаторы аукциона объявляют все предметы, участвующие в аукционе, а также начальную цену, с которой начинаются продажи всех предметов. Также перед началом аукциона все участники обязаны заявить об участии, указав свое имя. Когда начинаются торги, каждый участник имеет право объявить предмет, который он желает приобрести, и новую ставку. Если новая ставка больше предыдущей, она принимается организаторами. Незарегистрированные участники не могут предлагать ставку. Торги заканчиваются фразой организаторов "Аукцион закончен!". После этого необходимо вывести результаты аукциона: в каждой строчке необходимо указать предмет, имя покупателя, а также итоговую стоимость. Если предмет остался без покупателя, вместо этого выведите "Предложений не было".

    Формат ввода: в первой строке – список предметов через запятую; во второй – начальная стоимость всех предметов; в третьей – список имен участников через запятую; в последующих строках до строки "Аукцион закончен!" указываются название предмета, имя участника и новая ставка через пробел.

    Формат вывода: в каждой строчке находится название предмета, имя покупателя и итоговая стоимость, разделенные пробелом.
'''

arr_tovar = [tovar for tovar in input().split(', ')]
start_price = int(input())
arr_people = [people for people in input().split(', ')]

dict_sales = dict.fromkeys(arr_tovar, start_price)  # Apple II:500
dict_winner = {}  # Apple II : Alex

while True:
    s = input()
    if s == 'Аукцион закончен!':
        break
    question = s.split()
    name = question[0]
    tovar = ' '.join(question[1:-1])
    price = int(question[-1])

    if name in arr_people:  # если участник присутствует в списке участников
        if price > dict_sales[tovar]:
            dict_sales[tovar] = price  # меняем цену
            dict_winner[tovar] = name  # заносим победителя в словарь

for tovar, price in dict_sales.items():
    # выбрал ли участник данный товар
    name = dict_winner.get(tovar, "Предложений не было")
    f = lambda x: price if x != "Предложений не было" else ''
    print(tovar, name, f(name))
