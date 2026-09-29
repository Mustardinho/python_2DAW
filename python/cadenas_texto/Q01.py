nombre = input('Introduce tu nombre: ')
apellido_1 = input('Introduce tu primer apellido: ')
apellido_2 = input('Introduce tu segundo apellido: ')

usuario = nombre[:3] + apellido_1[:3] + apellido_2[:2]

print(f'Tu nombre de usuario es: {usuario.lower()}')