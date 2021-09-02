n = 0
s = 0
c = 0
while n != 999:
    n = int(input('digite um numero inteiro diferente de 999: '))
    s += n
    c += +1
    if n == 999:
        s += -999
        c += -1
print('a quantidade de entradas de valores foi: {} e a soma deles foi: {} '.format(c, s))
