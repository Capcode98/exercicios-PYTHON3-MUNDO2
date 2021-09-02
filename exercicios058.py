from random import randint
k = int(randint(0, 10))
print('''vamos jogar!
eu vou pensar em um numero de 0 a 10, você precisa de quantas tentativas para acertar?''')
r = -1
z = 0
while r != k:
    z += + 1
    r = int(input('qual o numero que você acha eu pensei? '))
    if r == k:
        print('parabens vc acertou! o numero que eu escolhi foi: {}\n e você precisou de {} tentativas para acertar'.format(k, z))
print('Fim')
