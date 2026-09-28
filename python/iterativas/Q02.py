tmp_menos_10 = 0
tmp_mas_30 = 0
tmp_total = 0

for dia in range(1, 8):
    tmp = float(input(f'Indica la temperatura del día {dia}: '))
    if tmp < 10:
        tmp_menos_10 += 1
    if tmp > 30:
        tmp_mas_30 += 1

    tmp_total += tmp

tmp_media = tmp_total / 7
if tmp_media < 15:
    print('Fría')
elif tmp_media >= 15 and tmp_media < 25:
    print('Templada')
else:
    print('Cálida')

print(f'Temperatura media: {round(tmp_media, 2)}')