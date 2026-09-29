nombre = input('Introduce el nombre del alumno/a: ')

norm = nombre.strip().title()
nom_mayus = nombre.strip().upper()
longitud = len(norm)

print(f'Nombre normalizado: {norm}')
print(f'Nombre en mayúsculas: {nom_mayus}')
print(f'Caracteres: {longitud}')
