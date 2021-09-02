a1 = int(input('qual o inicio da pa?'))
n = int(input('qual o ultimo termo da pa?'))
r = int(input('qual a razão da pa?'))
k = a1
c = 0
while k != (a1 + (n - 1)*r):
    if c == 0:
        k = a1
        c += +1
        print('o 1º termo é {}'.format(k))
    else:
        k += +r
        c += +1
        print('o {}º termo é {}'.format(c, k))
