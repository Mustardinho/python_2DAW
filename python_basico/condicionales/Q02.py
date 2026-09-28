n1 = int(input('Introduce el primer número: '))
n2 = int(input('Ahora introduce el segundo número: '))

if n1 > n2:
    print(n1, 'es mayor que', n2)
elif n1 < n2:
    print(n2, 'es mayor que', n1)
else:
    print(n1, 'es igual que', n2)