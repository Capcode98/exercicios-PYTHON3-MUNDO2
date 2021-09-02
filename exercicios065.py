n = 0
s = 0
c = 0
m = 0
M = 0
p = ''
while p != 'S':
    n = int(input('digite um numero inteiro : '))
    while p != 'S' and p != 'N':
        p = str(input('quer parar [S/N]? ')).strip().upper()
    if p == 'N':
        p = ''
    if c == 0:
        m = n
        M = n
        c = +1
        s = n
    elif c != 0:
        s += n
        c += +1
        if n > M:
            M = n
        if n < m:
            m = n
Media = s/c
print('a quantidade de vezes foi {}, a soma foi {}, a media dos numeros foram {},o maior numero digitado foi {} e o menor numero digitado foi {}'.format(c, s, Media, M, m))
