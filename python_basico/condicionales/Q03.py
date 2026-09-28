edad = int(input('Introduce tu edad: '))

if edad >= 0 and edad < 5:
    print('Entrada gratuita')
elif edad >= 5 and edad <= 12:
    print('Entrada por 5€')
elif edad >= 13 and edad <= 64:
    print('Entrada por 9€')
elif edad >= 65:
    print('Entrada por 6€')
else:
    print('Edad no válida')