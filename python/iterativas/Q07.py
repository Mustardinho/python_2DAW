tabla_ini = int(input('Primera tabla: '))
while tabla_ini < 1 or tabla_ini > 20:
    print('Las tablas tendrán que ser entre el 1 y el 20')
    tabla_ini = int(input('Primera tabla: '))
tabla_fin = int(input('Última tabla: '))
while (tabla_fin < 1 or tabla_fin > 20) or tabla_fin < tabla_ini:
    print('Las tablas tendrán que ser entre el 1 y el 20 o ser mayor que la primera tabla')
    tabla_fin = int(input('Última tabla: '))
mult_max = int(input('Multiplicador máximo: '))
while mult_max < 1 or mult_max > 15:
    print('El multiplicador máximo debe ester entre el 1 y el 15')
    mult_max = int(input('Multiplicador máximo: '))

total_multiplicaciones = 0
suma_global = 0

for i in range(tabla_ini, tabla_fin + 1):
    print(f'==== TABLA DEL {i} ====')
    suma_tabla = 0

    for j in range(1, mult_max + 1):
        producto = i * j
        print(f'{i} x {j} = {producto}')
        suma_tabla += producto
        total_multiplicaciones += 1

    print(f'Suma de productos: {suma_tabla}')
    suma_global += suma_tabla

print('\n--- RESUMEN ---')
print(f'Tablas generadas: {tabla_fin - tabla_ini +1}')
print(f'Multiplicaciones realizadas: {total_multiplicaciones}')
print(f'Suma global de productos: {suma_global}')