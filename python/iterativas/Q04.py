imp_total = 0
num_ventas = 0
imp_alta = 0
imp_baja = 0
ventas_superior_100 = 0

print('=== ANALIZADOR DE VENTAS ===')

while True:
    imp = float(input('Introduce el importe de la venta (-1 para salir): '))

    if imp == -1:
        break
    if imp < 0 and imp != -1:
        print('Error, no se puede introducir una venta negativa, intentalo de nuevo')
        continue
    if imp == 0:
        continue

    imp_total += imp
    num_ventas += 1

    if imp > 100:
        ventas_superior_100 += 1
    if num_ventas == 1 or imp > imp_alta:
        imp_alta = imp
    if num_ventas == 1 or imp < imp_baja:
        imp_baja = imp

print('\n=== INFORME DE LA JORNADA ===')
if num_ventas == 0:
    print('No se ha registrado ninguna venta válida.')
else:
    imp_medio = imp_total / num_ventas
    print(f'Importe total recaudado: {imp_total:.2f}€')
    print(f'Número de ventas válidas: {num_ventas}')
    print(f'Importe medio: {imp_medio:.2f}€')
    print(f'Venta más alta: {imp_alta:.2f}€')
    print(f'Venta más baja: {imp_baja:.2f}€')
    print(f'Ventas superiores a 100€: {ventas_superior_100}')