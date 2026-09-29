temps = []
dias_temp_max = []
dia_temp_mas_media = []

media = 0
temp_total = 0
temp_max = float('-inf')
temp_min = float('inf')

for i in range(1, 8):
    temp = float(input(f'Temperatura del día {i}: '))
    temps.append(temp)
    temp_total += temp
    
    if temp > temp_max:
        temp_max = temp
        dias_temp_max.append(i)
        
    if temp < temp_min:
        temp_min = temp
        
    if temp != temp_max:
        continue
    else:
        dias_temp_max.append(i)
    
    media = temp_total / 7

for i in temps:
    if i > media:
        dia_temp_mas_media.append(i)

print(f'Temperaturas registradas: {temps}')
print(f'Temperatura media de la semana: {media:.2f} C')
print(f'Temperatura máxima de la semana: {temp_max} C')
print(f'Temperatura mínima de la semana: {temp_min} C')
print(f'Temperatura superior a la media: {dia_temp_mas_media}')
print(f'Días con temperaturas máximas: {dias_temp_max}')