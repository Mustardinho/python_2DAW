total_grupos = 0
grupos_con_alumnos = 0
total_alumnos = 0
suma_global = 0
total_aprobados = 0
total_suspensos = 0
total_sobresalientes = 0

mejor_media = float('-inf')
grupo_mejor = ''
peor_media = float('inf')
grupo_peor = ''

while True:
    nomGrupo = input('Nombre del grupo (FIN para salir): ').strip()

    if nomGrupo.upper() == 'FIN':
        break

    total_grupos += 1

    alumnos = 0
    suma_notas = 0
    aprobados = 0
    suspensos = 0
    sobresalientes = 0
    nota_alta = float('-inf')
    nota_baja = float('inf')

    while True:
        nota = float(input('Nota (-1 para salir): '))

        if nota == -1:
            break

        if nota < 0 or nota > 10:
            print('La nota tiene que estar entre 0 y 10.')
            continue

        alumnos += 1
        suma_notas += nota

        if nota >= 5:
            aprobados += 1
        else:
            suspensos += 1

        if nota >= 9:
            sobresalientes += 1

        if nota > nota_alta:
            nota_alta = nota
        if nota < nota_baja:
            nota_baja = nota

    print(f'=== INFORME DEL GRUPO {nomGrupo} ===')

    if alumnos == 0:
        print('No se ha introducido ninguna nota en este grupo.')
    else:
        media = suma_notas / alumnos
        porcentaje = aprobados / alumnos * 100

        print(f'Alumnos evaluados: {alumnos}')
        print(f'Aprobados: {aprobados}')
        print(f'Suspensos: {suspensos}')
        print(f'Nota media: {media:.2f}')
        print(f'Nota más alta: {nota_alta:.2f}')
        print(f'Nota más baja: {nota_baja:.2f}')
        print(f'Porcentaje de aprobados: {porcentaje:.2f}%')
        print(f'Sobresalientes: {sobresalientes}')

        if media > mejor_media:
            mejor_media = media
            grupo_mejor = nomGrupo
        if media < peor_media:
            peor_media = media
            grupo_peor = nomGrupo

print('\n=== INFORME GLOBAL DEL CENTRO ===')
print(f'Grupos procesados: {total_grupos}')
print(f'Grupos con al menos un alumno evaluado: {grupos_con_alumnos}')

if total_alumnos == 0:
    print('No se ha evaluado a ningún alumno: no se pueden calcular medias ni porcentajes.')
else:
    media_global = suma_global / total_alumnos
    porcentaje_global = total_aprobados / total_alumnos * 100

    print(f'Alumnos evaluados: {total_alumnos}')
    print(f'Aprobados: {total_aprobados}')
    print(f'Suspensos: {total_suspensos}')
    print(f'Nota media global: {media_global:.2f}')
    print(f'Porcentaje global de aprobados: {porcentaje_global:.2f}%')
    print(f'Sobresalientes: {total_sobresalientes}')
    print(f'Grupo con la media más alta: {grupo_mejor} ({mejor_media:.2f})')
    print(f'Grupo con la media más baja: {grupo_peor} ({peor_media:.2f})')