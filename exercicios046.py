from time import sleep
a = int(input('digite a quantidade de tempo inicial (em segundos)'))
b = int(input('digite a quantidade de tempo final (em segundos)'))
s = str(input('digite (s) ou (n) para iniciar o programa')).lower().strip()
if s == "s":
    for c in range(a, b, -1):
        print(c)
        sleep(1)
print('kabum')
