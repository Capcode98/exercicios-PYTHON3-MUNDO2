f = str(input('digite a frase que você quer testar:')).strip().upper().split()
junto = ''.join(f)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('a frese é {}, e o inverso é {}'.format(junto, inverso))
