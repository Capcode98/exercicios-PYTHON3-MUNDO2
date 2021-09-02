from random import randint

print('''vamos jogar jokenpô!
escolha entre:
 [0] pedra 
 [1] papel 
 [2] tesoura
sabendo que:
pedra ganha da tesoura & perde para o papel 
tesoura ganha da papel & perde para o pedra
papel ganha da pedra & perde para o tesoura''')
e = int(input("escolha entre (pedra, papel ou tesoura) para jogar"))
op = int(randint(0, 2))
if e == op:
    print('empatou')
elif e == 0 and op == 2:
    print('voce ganhou')
elif e == 0 and op == 1:
    print('voce perdeu')
elif e == 2 and op == 1:
    print('voce ganhou')
elif e == 2 and op == 0:
    print('voce perdeu')
elif e == 1 and op == 0:
    print('voce ganhou')
elif e == 1 and op == 2:
    print('voce perdeu')
#from random import randint
itens = ('Pedra','Papel','Tesoura')
#computador = randint(0,2)
print('o computador escolheu {}'.format(itens[op]))
