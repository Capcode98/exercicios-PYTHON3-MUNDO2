from datetime import date
n = int(input('digite a quantidade de pessoas:'))
y = 0
for c in range(0, n):
    a = int(input('digite o ano que você nasceu'))
    #m = int(input('digite o mes que você nasceu'))
    #d = int(input('digite o dia que você nasceu'))
    k = date.today().year - a
    if k >= 21:
        y = y + 1
if y > 0:
    print('a quantidade de pessoas que atingiram a maioridade é {}'.format(y))