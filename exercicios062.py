a1 = int(input('qual o inicio da pa? '))
n = int(input('quantos termos da pa você quer ver? '))
r = int(input('qual a razão da pa? '))
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
    if c == n:
        m = int(input('quantos termos a mais da pa você quer conhecer? '))
        n += + m
print('fim')
