p = float(input("qual o seu peso ? (em kg)"))
a = float(input("qual a sua altura ? (em metros)"))
imc = (p / a ** 2)
if imc <= 18.5:
    print('abaixo do peso')
elif 18.5 < imc <= 25:
    print('peso ideal')
elif 25 < imc <= 30:
    print('sobrepeso')
elif 30 < imc <= 40:
    print('obesidade')
elif imc > 40:
    print('obesidade morbida')

print(imc)
