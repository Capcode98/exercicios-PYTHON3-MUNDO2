id = int(input('qual o ano q vc nasceu?'))
idade = 2020 - id
if idade <= 9:
    print('vc pertence a categoria mirim')
if idade <= 14 and idade > 9:
    print('vc pertence a categoria infantil')
if idade <= 19 and idade > 14:
    print('vc pertence a categoria junior')
if idade <= 20 and idade > 19:
    print('vc pertence a categoria senior')
if idade > 20:
    print('vc pertence a categoria master')
