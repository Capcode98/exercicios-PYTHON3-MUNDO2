s = 0
for c in range(0, 6+1):
    print('os seis numeros inteiros são{}'.format(c))
    k = float((c/2)-(c//2))
    if k == 0.0:
        s = s + c
print('as somas dos numeros inteiros pares são{}'.format(s))
