def excepciones_float(texto_input):
    dato_valido = False

    while not dato_valido:
        try:
            valor = float(input(texto_input))
            dato_valido = True
        except:
            print("No has insertado un numero decimal")
    return valor

def excepciones_string_si_no(texto_input):
    dato_valido = False
    while not dato_valido:
        try:
            valor = str(input(texto_input))
            if valor == "Si" or valor == "No":
                dato_valido = True
            else:
                print("Por favor introduce Si o No.\n")
        except:
            print("Por favor introduce Si o No.\n")
    return valor

def excepciones_int_rango_exit(texto_input, numero_min,numero_max):
    dato_valido = False
    while not dato_valido:
        try:
            valor = str(input(texto_input))
            if valor.isdigit() and numero_min <= int(valor) <= numero_max:
                dato_valido = True
            elif valor == "q":
                dato_valido = True
            elif valor == "Q":
                dato_valido = True
            else:
                print("El valor no esta en el rango (%d, %d) ni es q" % (numero_min, numero_max))
        except:
            print("El valor no esta en el rango (%d, %d) ni es q" % (numero_min, numero_max))
    return valor

def excepciones_int_rango(texto_input, numero_min,numero_max):
    dato_valido = False
    while not dato_valido:
        try:
            valor = str(input(texto_input))
            if numero_min <= int(valor) <= numero_max:
                dato_valido = True
            else:
                print("El valor no esta en el rango (%d, %d)" % (numero_min, numero_max))
        except:
            print("El valor no esta en el rango (%d, %d)" % (numero_min, numero_max))
    return valor

def excepciones_string(texto_input):
    dato_valido = False
    while not dato_valido:
        try:
            valor = str(input(texto_input))
            dato_valido = True
        except:
            print("No has insertado texto")
    return valor

def excepciones_exit(texto_input):
    dato_valido = False
    while not dato_valido:
        valor = input(texto_input)
        if valor == "q" or valor == "Q":
            dato_valido = True
            return -1
        else:
            dato_valido = True
            return valor
