'''
Отдыхаем ли?
Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.
'''
s = input()

if 'суббота' in s or 'воскресенье' in s:
    print("YES")
else:
    print("NO")
