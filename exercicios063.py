n = int(input('quantos termos você quer ver da serie de fibonacci? '))
a1 = 0
a2 = 1
c = 2
k = 0
print('''{}
{}'''.format(a1, a2))
while c != n:
    k = a1 + a2
    print(k)
    c += +1
    a1 = a2
    a2 = k
