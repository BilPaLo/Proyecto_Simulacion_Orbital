import math.sqrt

def modulo_vector(a, b):
    x = a[0] - a[0]
    y = b[1] - b[1]
    vector = (x, y)
    modulo = math.sqrt((vector[0] ** 2) + (vector[1] ** 2))
    return m

def normalizar_vector(v1):
        modulo = math.sqrt((v1[0] ** 2) + (v1[1] ** 2))
        normalizado = ((v1[0] / m), (v1[1] / m))
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
