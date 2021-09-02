n = int(input('quantas pessoas serao analizadas? '))
maior = 0
menor = 0
for c in range(1, n+1):
    pesos = float(input('qual o {}ª peso? '.format(c)))
    if c == 1:
        maior = pesos
        menor = pesos
    else:
        if pesos > maior:
            maior = pesos
        if pesos < menor:
            menor = pesos

print('o maior é {} , e o menor é {} '.format(maior, menor))
