'''
Сознательный шоппинг
  Петя ходит в магазин со списком покупок из трех товаров, которые ему нужно купить. Далее он смотрит в каталог и ищет нужные ему товары. Выведите "YES", если он может найти все нужные товары в каталоге, и "NO" иначе.

  Формат ввода: три строки с товарами, а затем каталог товаров через запятую.

  Формат вывода: строка "YES" или "NO".
'''

x, y, z = input(), input(), input()
lst = input()

if x in lst and y in lst and z in lst:
    print("YES")
else:
    print("NO")
