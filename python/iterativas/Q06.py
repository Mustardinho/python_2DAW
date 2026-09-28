capital = float(input('Capital inicial en €: '))
while capital < 0:
    print('Error, el capital inicial tiene que ser mayor a 0')
    capital = float(input('Capital inicial en €: '))

aportacion = float(input('Aportación mensual en €: '))
while capital < 0:
    print('Error, la aportación mensual tiene que ser mayor a 0')
    capital = float(input('Aportación mensual en €: '))

interes = float(input('Interés anual en %: '))
while interes < 0 or interes > 10:
    print('Error, el interés anual debe estar entre 0% y 10%')
    capital = float(input('Interés anual en %: '))

objetivo = float(input('Capital objetivo en €: '))
while objetivo <= 0:
    print('Error, el objetivo debe ser mayor a 0.')
    objetivo = float(input('Capital objetivo en €: '))

saldo = capital
interes_mensual = interes / 100 / 12
mes = 0
total_intereses = 0
total_aportado = 0

if saldo >= objetivo:
    print('El capital inicial ya alcanza el objetivo. No es necesario simular.')
elif aportacion == 0 and (interes == 0 or saldo == 0):
    print('El objetivo es inalcanzable con las condiciones indicadas.')
else:
    while saldo < objetivo:
        mes += 1
        interes = saldo * interes_mensual
        saldo += interes
        saldo += aportacion

        total_intereses += interes
        total_aportado += aportacion

        print(f'Mes {mes}: intereses {interes:.2f}€ | saldo {saldo:.2f}€')

    print(f'\nObjetivo alcanzado en {mes} meses.')
    print(f'Total aportado: {capital + total_aportado:.2f}€'
          f'(capital inicial {capital:.2f}€ + aportaciones {total_aportado:.2f}€)')
    print(f'Total obtenido por intereses: {total_intereses:.2f}€')