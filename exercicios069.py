ch = 0
mm20 = 0
pm18 = 0
while True:
    nome = str(input('Qual seu nome? ')).strip().lower().capitalize()
    idade = int(input('Qual sua idade? '))
    sexo = ''
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Qual seu sexo?[M/F] ')).strip().upper()
    if idade < 20 and sexo == 'F':
        mm20 += +1
    if sexo == 'M':
        ch += +1
    if idade > 18:
        pm18 += +1
    d = ''
    while d != 'S' and d != 'N':
        d = str(input('deseja para [S/N]: ')).strip().upper()
    if d == 'S':
        break
print(f'a quantidade de homens é: {ch} ,a quantidade de mulheres com menos de 20 anos é: {mm20},'
      f'a quantidade de pessoas com mais de 18 anos é: {pm18} ')
