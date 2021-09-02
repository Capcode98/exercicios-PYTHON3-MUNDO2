n = int(input('digite um numero inteiro'))
print('''para qual base de conversão voçê pretende converter?
[ 1 ] BINARIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
op = int(input('sua opção'))
if op == 1:
    print('{} convertido para BINARIO fica {}'.format(n, bin(n)))
elif op == 2:
    print('{} convertido para OCTAL fica {}'.format(n, oct(n)))
elif op == 3:
    print('{} convertido para HEXADECIMAL fica {}'.format(n, hex(n)))
elif op != [1, 2 or 3]:
    print('''
    resposta invaila! 
    por favor recomece com um valor valido!''')
