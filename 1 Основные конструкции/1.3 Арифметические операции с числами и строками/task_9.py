'''
  9. Последние n цифр числа
  С клавиатуры вводится натуральное число, затем на другой строке число n <= длины числа. Выведите на экран последние n цифр числа.
'''

n = int(input())
k = int(input())
print(n % (10 ** k))
