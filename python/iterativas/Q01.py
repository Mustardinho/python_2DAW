adm = 0
rech = 0

while True:
    edad = int(input('Introduce la edad (-1 para terminar): '))

    if edad == -1:
        break
    if edad < 0:
        print('Error, la edad no puede ser negativa')

    altura = float(input('Ahora introduce la alturaen cm: '))
    while altura <= 0:
        print('Error: la altura debe ser mayor a 0')
        altura = float(input('Introduce la altura en cm: '))

    if edad >= 12 and altura >= 140:
        print('Acceso permitido.')
        adm += 1
    else:
        print('Acceso denegado.')
        rech += 1

print(f'Visitantes totales: {adm + rech}')
print(f'Visitantes admitidos: {adm}')
print(f'Visitantes rechazados: {rech}')