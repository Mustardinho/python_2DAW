year = int(input('Introduce un año: '))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f'{year} -> bisiesto')
else:
    print(f'{year} -> no bisiesto')