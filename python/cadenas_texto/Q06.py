frase = input('Introduce una frase: ')

cont = 0
actual = ''
mas_larga = ''

for c in frase:
    if c != ' ':
         actual += c
    else:
        if actual != '':
            cont += 1
            if len(actual) > len(mas_larga):
                mas_larga = actual
            actual = ''

if actual != '':
    cont += 1
    if len(actual) > len(mas_larga):
        mas_larga = actual

print(f'Número de palabras: {cont}')
print(f'Palabra más larga: {mas_larga} ({len(mas_larga)} letras)')