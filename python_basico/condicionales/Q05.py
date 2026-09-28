imp = float(input('Importe de la compra: '))

if imp < 50:
    porc = 0
elif imp < 100:
    porc = 5
elif imp < 200:
    porc = 10
else:
    porc = 15

desc = imp * porc / 100
p_final = imp - desc

print(f'Descuento: {desc} €')
print(f'Precio final: {p_final} €')