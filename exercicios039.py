d = input('em qual dia vc nasceu?')
m = input('em qual mes vc nasceu?')
a = int(input('em qual ano vc nasceu?'))
if a < 2002:
    print('voce ja deveria ter se alistado a {} anos'.format(((a-2002) ** 2) ** (1/2)))
elif a > 2002:
    print('voce vai ter que se alistar daqui a {} anos'.format(((a-2002) ** 2) ** (1/2)))
elif a == 2002:
    print('voce vai ter q se alistar esse ano!')
