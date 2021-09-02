PN = float(input('qual o valor normal do produto (em reais) ?'))
print('''escolha a forma de pagamento da seguinte forma
digite:
(1) para (1x no cheque/dinheiro): 10% desconto 
(2) para (1x no cartao): 5% desconto
(3) para (2x no cartao): preço sem juros
(4) para (3x ou mais no cartao): 20% de juros''')
FP = int(input('qual a forma de pagamento?'))
if FP == 1:
    print((PN * 0.9))
if FP == 2:
    print((PN * 0.95))
if FP == 3:
    print(PN)
if FP == 4:
    print((PN + (PN * 0.2)))
