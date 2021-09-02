casa = float(input('qual o valor da casa você pretende comprar? '))
salario = float(input('quanto você ganha por mes? '))
tempo = float(input('em quantos anos você pretende pagar? '))
prest = tempo * 12
vprest = casa * (1 / prest)
if vprest <= salario * 3/10:
    print('Meus Parabens! seu emprestimo foi aprovado!!')
else:
    print('infelizmente seu emprestimo foi recusado!')
