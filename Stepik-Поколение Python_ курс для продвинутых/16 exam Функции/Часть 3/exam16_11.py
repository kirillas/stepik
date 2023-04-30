'''
Сортировка IP-адресов
IP-адрес – уникальный числовой идентификатор устройства в компьютерной сети, работающий по протоколу TCP/IP.

В 44-й версии IP-адрес представляет собой 3232-битное число. Адрес записывается в виде четырёх десятичных чисел (октетов) со значением от 00 до 255255, разделённых точками, например, 192.168.1.2192.168.1.2.

Напишите программу, которая считывает IP-адреса и выводит их в порядке возрастания в соответствии с десятичным представлением.

Формат входных данных
На вход программе подается число n \, (n \ge 1)n (n≥1) – количество IP-адресов. Затем nn строк с корректными IP-адресами.

Формат выходных данных
Программа должна вывести IP-адреса в порядке возрастания в соответствии с десятичным представлением.
'''


def ip_to_number(ip):
    arr = [int(i) for i in ip.split('.')]
    return arr[0] * 256 ** 3 + arr[1] * 256 ** 2 + arr[2] * 256 + arr[3]


n = int(input())
arr_ip = [input().strip() for _ in range(n)]
print(*sorted(arr_ip, key=ip_to_number), sep='\n')
