'''
19. Цена пирожка
  Представьте, что вы работаете на заводе (с программистами такое тоже случается) по производству пирожков. Вас попросили написать программу, которая принимает на вход цену одного пирожка в рублях и копейках, а затем количество пирожков — целое число. Вывести нужно итоговую стоимость пирожков в рублях и копейках через пробел.
'''
import math

rub = int(input())
kop = int(input())
count = int(input())

totalrub = count * rub
totalkop = count * kop

print(totalrub + totalkop // 100, totalkop % 100)
