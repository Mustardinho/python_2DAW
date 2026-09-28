temp = int(input('Introduce una temperatura en grados C: '))

if temp < 0:
    print('Hace mucho frío')
elif temp >= 0 and temp <= 10:
    print('Hace frío')
elif temp >= 11 and temp <= 20:
    print('Temperatura suave')
elif temp >= 21 and temp <= 30:
    print('Hace calor')
else:
    print('Hace mucho calor')