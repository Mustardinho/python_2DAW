n1 = int(input('Introduce un número: '))
n2 = int(input('Introduce otro número: '))
op = input('Introduce una operación (+, -, * o /): ')

if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    if n2 == 0:
        print('No se puede dividir entre cero')
    else:
        print(round((n1 / n2), 2))
else:
    print('Operación inválida')