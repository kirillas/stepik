'''
Старинная задача
Имеется 100100 рублей. Сколько быков, коров и телят можно купить на все эти деньги, если плата за быка – 1010 рублей, за корову – 55 рублей, за теленка – 0.50.5 рубля и надо купить 100100 голов скота?
Примечание. Используйте вложенный цикл for.
'''

price_b = 10
price_k = 5
price_t = 0.5

for b in range(1, 11):
    for k in range(1, 21):
        for t in range(1, 201):
            if b * price_b + k * price_k + t * price_t == 100 and b + k + t == 100:
                print(f"Быки={b} Коровы={k} Телята={t}")
