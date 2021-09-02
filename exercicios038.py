n1 = float(input('digite o primeiro numero'))
n2 = float(input('degite o segundo numero'))
D = n1 - n2
if D == 0:
    print('nao existe valor maior, ambos sao iguais !')
elif n1 < n2:
    print('o segundo numero é maior que o primeiro !')
elif n1 > n2:
    print('o primeiro numero é maior que o segundo !')
