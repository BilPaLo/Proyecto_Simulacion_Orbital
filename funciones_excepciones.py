def excepciones_int(texto_input):
    dato_valido = False

    while not dato_valido:
        try:
            # aqui ponemos los que puede fallar
            valor = int(input(texto_input))
            dato_valido = True
        except:
        # aqui ponemos el mensaje del error o lo que tiene que hacer si no funciona
            print("No has insertado un numero entero")
    return valor

def excepciones_int_rango(texto_input, numero_min,numero_max):
    dato_valido = False

    while not dato_valido:
        try:
            # aqui ponemos los que puede fallar
            valor = int(input(texto_input))
            if numero_min <= valor <= numero_max:
                dato_valido = True
            else:
                print("El valor no esta en el rango (%d, %d)" % (numero_min, numero_max))
        except:
        # aqui ponemos el mensaje del error o lo que tiene que hacer si no funciona
            print("No has insertado un numero entero")
    return valor

def excepciones_string(texto_input):
    dato_valido = False

    while not dato_valido:
        try:
            # aqui ponemos los que puede fallar
            valor = str(input(texto_input))
            dato_valido = True
        except:
        # aqui ponemos el mensaje del error o lo que tiene que hacer si no funciona
            print("No has insertado texto")
    return valor

def excepciones_float(texto_input):
    dato_valido = False

    while not dato_valido:
        try:
            # aqui ponemos los que puede fallar
            valor = float(input(texto_input))
            dato_valido = True
        except:
        # aqui ponemos el mensaje del error o lo que tiene que hacer si no funciona
            print("No has insertado un numero decimal")
    return valor

def excepciones_bool(texto_input):
    dato_valido = False

    while not dato_valido:
        try:
            # aqui ponemos los que puede fallar
            valor = bool(input(texto_input))
            dato_valido = True
        except:
        # aqui ponemos el mensaje del error o lo que tiene que hacer si no funciona
            print("No has insertado un booleano true/false")
    return valor
