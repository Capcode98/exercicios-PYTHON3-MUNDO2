n1 = float(input('qual a primeira nota?'))
n2 = float(input('qual a segunda nota?'))
m = (n1 + n2) * (1/2)
if m < 5:
    print('reprovado!')
elif 5 <= m < 7:
    print('recuperação!')
elif m >= 7:
    print('aprovado!')
