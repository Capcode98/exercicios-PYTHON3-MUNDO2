s = 0
c = 0
while True:
    n = int(input('digite um numero inteiro diferente de 999: '))
    if n == 999:
        break
    c += +1
    s += n
print(f'a quantidade de entradas de valores foi: {c} e a soma deles foi: {s} ')
