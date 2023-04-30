'''Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и посчитать
число строк в нём.
Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому параметру, чтобы убрать
пробельные символы по краям).
После получения файла вы можете проверить результат, обратившись к полю text. Если результат работы скрипта не принимается,
проверьте поле url на правильность. Для подсчёта количества строк разбейте текст с помощью метода splitlines.
В поле ответа введите одно число или отправьте файл, содержащий одно число.'''

import requests

with open('request.txt', 'r') as file:
    url = file.readline().strip()
    r = requests.get(url)

    if len(r.text) > 0:
        lines = r.text.splitlines()
        print(len(lines))
    else:
        print(r.url)
