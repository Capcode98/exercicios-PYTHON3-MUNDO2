while True:
    v = int(input('digite o valor a ser sacado: '))
    n50 = v//50
    n20 = (v % 50)//20
    n10 = ((v % 50) % 20)//10
    n1 = (((v % 50) % 20) % 10)
    print(f'''o valor digitado foi:
          R$ {v}
          {n50} x cedulas de R$50
          {n20} x cedulas de R$20
          {n10} x cedulas de R$10
          {n1} x cedulas de R$1''')
    d = ''
    while d != 'S' and d != 'N':
        d = str(input('deseja parar: [S/N]')).strip().upper()
    if d == 'S':
        break
