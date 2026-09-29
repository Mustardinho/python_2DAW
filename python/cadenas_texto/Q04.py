while True:
    pswd = input('Contraseña: ')
    
    pswd = pswd.strip()
    
    if len(pswd) < 8:
        print('La contraseña debe tener al menos 8 caracteres.')
        continue
    
    mayus = False
    minus = False
    digito = False
        
    for c in pswd:
        if c.isupper():
            mayus = True
                
    for c in pswd:
        if c.islower():
            minus = True
        
    for c in pswd:
        if c.isdigit():
            digito = True
    
    if mayus == True and minus == True and digito == True:
        print('Contraseña válida.')
        break
    else:
        print('Esta contraseña no es válida. Intentalo de nuevo.')
        continue