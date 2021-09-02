pessoas = {}
q = int(input('quantas pessoas serão cadastradas ? '))
mi = 0
hv = ''
ihv = 0
mm20 = 0
for c in range(1, q + 1):
    pessoas['nome {}'.format(c)] = str(input('Qual seu nome? ')).strip().lower().capitalize()
    pessoas['idade {}'.format(c)] = int(input('Qual sua idade? '))
    pessoas['sexo {}'.format(c)] = str(input('Qual seu sexo?[M/F] ')).strip().upper()
    i = pessoas['idade {}'.format(c)]
    mi = (mi + i)
    if pessoas['idade {}'.format(c)] < 20 and pessoas['sexo {}'.format(c)] == 'F':
        mm20 += 1
    if c == 1 and pessoas['sexo {}'.format(c)] == 'M':
        hv = pessoas['nome {}'.format(c)]
        ihv = pessoas['idade {}'.format(c)]
    else:
        if pessoas['idade {}'.format(c)] > ihv and pessoas['sexo {}'.format(c)] == 'M':
            hv = pessoas['nome {}'.format(c)]
            ihv = pessoas['idade {}'.format(c)]
print('o homem mais velho é: {}\n a idade dele é: {}\n  a quantidade de mulheres com menos de 20 anos é: {}'.format(hv, ihv, mm20))
print('a media da idade das pessoas cadastradas é {}'.format(mi / q))
