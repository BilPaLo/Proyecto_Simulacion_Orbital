def modulo_vector(v1):
    modulo = ((v1[0] ** 2) + (v1[1] ** 2))**(1/2)
    return modulo

def normalizar_vector(v1):
        modulo = ((v1[0] ** 2) + (v1[1] ** 2))**(1/2)
        normalizado = ((v1[0] / modulo), (v1[1] / modulo))
        return normalizado

def producto_escalar(v1, a):
    x = v1[0] * a
    y = v1[1] * a
    c = (x, y)
    return c

def sumar_tuplas(v1, v2):
    x = v1[0] + v2[0]
    y = v1[1] + v2[1]
    c = (x, y)
    return c

def restar_tuplas(v1, v2):

    x = v1[0] - v2[0]
    y = v1[1] - v2[1]
    c = (x, y)
    return c

def multiplicar_tuplas(v1, v2):
    x = v1[0] * v2[0]
    y = v1[1] * v2[1]
    c = (x, y)
    return c

def dividir_tuplas(v1, v2):
    x = v1[0] / v2[0]
    y = v1[1] / v2[1]
    c = (x, y)
    return c
