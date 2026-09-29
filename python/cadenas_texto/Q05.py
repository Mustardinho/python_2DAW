texto = input('Introduce un texto: ')

cifrado = ''

for c in texto:
    if c.isdigit() or c == ' ':
        cifrado += c
        continue
    else:
        c = (ord(c) + 1)
        c = chr(c)
        cifrado += c
        
print(cifrado)