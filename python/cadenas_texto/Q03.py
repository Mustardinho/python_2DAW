texto = input('Introduce una frase: ')

a = texto.count('a')
e = texto.count('e')
i = texto.count('i')
o = texto.count('o')
u = texto.count('u')
total = a + e + i + o + u

print(f'A: {a}')
print(f'E: {e}')
print(f'I: {i}')
print(f'O: {o}')
print(f'U: {u}')
print(f'Total vocales: {total}')