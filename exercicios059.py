print('''=========MENU=========
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
M = 0
rm = 0
while rm != 5:
    n1 = float(input('digite o primeiro numero: '))
    n2 = float(input('digite o segundo numero: '))
    rm = int(input('oque você deseja fazer? '))
    if rm == 4:
        while rm == 4:
            n1 = float(input('digite o primeiro numero: '))
            n2 = float(input('digite o segundo numero: '))
            rm = int(input('oque você deseja fazer? '))

    print(rm)
    s = n1 + n2
    m = n1 * n2
    if n1 > n2:
        M = n1
    elif n1 == n2:
        M = n1
    elif n1 < n2:
        M = n2
    if rm == 1:
        print('a soma dos numeros {} e {}, deu : {}'.format(n1, n2, s))
    if rm == 2:
        print('a multiplicação dos numeros {} e {}, deu : {}'.format(n1, n2, m))
    if rm == 3:
        print('o maior numero entre {} e {}, é : {}'.format(n1, n2, M))
