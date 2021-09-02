print('Mercados Inter:')
#Total gasto
t = 0
#Quantos produtos custam mais de 1000
m1000 = 0
#Qual o nome do produto mais barato
pmb = ''
Pmb = 0
#Contador de vezes
c = 0
while True:
    n = str(input('digite o nome do produto: ')).strip().upper()
    p = int(input('digite o preço do produto: '))
    d = ''
    if c == 0:
        pmb = n
        t = p
        c = 1
    else:
        if p < t:
            pmb = n
        c += +1
        t += +p
    if p > 1000:
        m1000 += +1
    while d != 'S' and d != 'N':
        d = str(input('deseja cadastrar mais produtos? [S/N]')).upper().strip()
    if d == 'N':
        break
print(f'o total foi: {t} \no nome do produto com menor preço foi: {pmb}'
      f' e a quantidade de produtos por mais de 1000 foi: {m1000}')
