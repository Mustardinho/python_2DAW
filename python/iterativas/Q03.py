saldo = 1000
n_ingresos = 0
n_retiradas = 0
total_ingresado = 0
total_retirado = 0

while True:
    print('====== CAJERO AUTOMÁTICO ======')
    print('1. Consultar saldo')
    print('2. Ingresar dinero')
    print('3. Retirar dinero')
    print('4. Salir')
    opc = int(input('Introduce una opción: '))

    if opc == 1:
        print(f'Saldo actual: {round(saldo, 2)} €')

    elif opc == 2:
        cant = float(input('Introduce la cantidad a ingresar: '))
        if cant <= 0:
            print('La cantidad debe ser mayor que 0.')
        else:
            saldo += cant
            n_ingresos += 1
            total_ingresado += cant
            print('Ingreso realizado correctamente.')

    elif opc == 3:
        cant = float(input('Introduce la cantidad a retirar: '))
        if cant <= 0:
            print('La cantidad debe ser mayor que 0.')
        elif cant > saldo:
            print('Saldo insuficiente.')
        else:
            saldo -= cant
            n_retiradas += 1
            total_retirado += cant
            print('Retirada realizada correctamente.')

    elif opc == 4:
        break

    else:
        print('Opción no válida.')

print('====== RESUMEN ======')
print(f'Saldo final: {round(saldo, 2)} €')
print(f'Ingresos realizados: {n_ingresos} (total: {round(total_ingresado, 2)} €)')
print(f'Retiradas realizadas: {n_retiradas} (total: {round(total_retirado, 2)} €)')