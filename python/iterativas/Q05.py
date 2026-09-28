PRECIO = 135

print(f'El precio del producto es {PRECIO // 100},{PRECIO % 100:02d}€')

intr = 0

while intr < PRECIO:
    moneda = int(input('Introduce una monead en centimos (5, 10, 20, 50, 100, 200): '))

    if moneda == 5 or moneda == 10 or moneda == 20 or moneda == 50 or moneda == 100 or moneda == 200:
        intr = intr + moneda
        falta = PRECIO - intr
        if falta < 0:
            falta =0
        print(f'Introducido: {intr // 100},{intr % 100:02d}€ | '
              f'Falta: {falta // 100},{falta % 100:02d}€')
    else:
        print(f'Moneda de {moneda} rechazada: la máquina no la admite.')

cambio = intr - PRECIO

if cambio == 0:
    print('Importe exacto. No hay cambio.')
else:
    print(f"Su cambio es {cambio // 100},{cambio % 100:02d} €:")

    # 3) Descomponer de mayor a menor
    cantidad = cambio // 200
    if cantidad > 0:
        print(f"  {cantidad} x 2 €")
    cambio = cambio % 200

    cantidad = cambio // 100
    if cantidad > 0:
        print(f"  {cantidad} x 1 €")
    cambio = cambio % 100

    cantidad = cambio // 50
    if cantidad > 0:
        print(f"  {cantidad} x 50 céntimos")
    cambio = cambio % 50

    cantidad = cambio // 20
    if cantidad > 0:
        print(f"  {cantidad} x 20 céntimos")
    cambio = cambio % 20

    cantidad = cambio // 10
    if cantidad > 0:
        print(f"  {cantidad} x 10 céntimos")
    cambio = cambio % 10

    cantidad = cambio // 5
    if cantidad > 0:
        print(f"  {cantidad} x 5 céntimos")

print("Retire su producto. ¡Gracias!")