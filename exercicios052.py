n = int(input('digite um numero inteiro, que você queira saber se é primo:'))
p = 0
for c in range(n, 2, -1):
    k = float((n/(c-1))-(n//(c-1)))
    if k == 0:
        p = p + 1
if p == 0:
    print('esse valor {} é primo!'.format(n))
if p != 0:
    print('esse valor {} não é primo!'.format(n))
