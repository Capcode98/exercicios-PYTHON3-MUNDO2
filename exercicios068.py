from random import randint
print('VAMOS JOGAR PAR OU IMPAR, SE A SOMA DOS VALORES PENSADOS POR VOCE E POR MIM FOREM PAR E VOCE O TENHA ESCOLHIDO'
      ', VOCE GANHA, O MESMO VALE PARA O IMPAR! ')

while True:
    n = int(input('digite um numero inteiro: '))
    c = ''
    while c != 'P' and c != 'I':
        c = str(input('(vou te dar essa colher de chá) pode escolher... digite [P/I]: ')).strip().upper()
    k = int(randint(0, 10))
    s = k + n
    if s % 2 != 0 and c == 'I':
        # quer dizer que a soma é impar
        print(f'PARABENS VOCÊ ACERTOU! VOCÊ ESCOLHEU {n} E PAR E A SOMA DEU {s} IMPAR')
        print(f'E EU PENSEI EM {k}')
    if s % 2 == 0 and c == 'P':
        # quer dizer que a soma é par
        print(f'PARABENS VOCÊ ACERTOU! VOCÊ ESCOLHEU {n} E PAR E A SOMA DEU {s} PAR')
        print(f'E EU PENSEI EM {k}')
    if s % 2 != 0 and c == 'P':
        # quer dizer que a soma é impar
        print(f'VOCÊ ERROU! VOCÊ ESCOLHEU {n} E PAR E A SOMA DEU {s} IMPAR')
        print(f'E EU PENSEI EM {k}')
        break
    if s % 2 == 0 and c == 'I':
        # quer dizer que a soma é par
        print(f'VOCÊ ERROU! VOCÊ ESCOLHEU {n} E IMPAR E A SOMA DEU {s} PAR')
        print(f'E EU PENSEI EM {k}')
        break
print('FIM... CANSEI DE GANHAR...')
