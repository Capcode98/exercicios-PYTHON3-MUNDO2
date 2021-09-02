print('para descobrir se é possivel formar um triangulo com 3 retas quaisquer digite o tamanho delas a seguir! ')
r1 = float(input('qual o tamanho da primeira reta? '))
r2 = float(input('qual o tamanho da segunda reta? '))
r3 = float(input('qual o tamanho da terceira reta? '))
if ((r1 - r2) ** 2) ** (1 / 2) < r3 < (r1 + r2):
    if ((r1 - r3) ** 2) ** (1 / 2) < r2 < (r1 + r3):
        if ((r3 - r2) ** 2) ** (1 / 2) < r1 < (r3 + r2):
            print('é possivel formar um triangulo!')
        else:
            print('não é possivel formar!')
    else:
        print('não é possivel formar!')
else:
    print('não é possivel formar!')
if r1 == r2 and r1 == r3:
    print('É equilátero')
elif r3 != r1 == r2 or r2 != r1 == r3 or r1 != r2 == r3:
    print('É isóceles')
elif r1 != r2 != r3 and r3 != r1:
    print('É escaleno')
