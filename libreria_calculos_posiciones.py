import libreria_operaciones_tuplas

# Calculo de la distancia entre dos objetos, usando sus coordenadas
def distanciaf(posicion_1, posicion_2):
    valor = libreria_operaciones_tuplas.restar_tuplas(posicion_2, posicion_1)
    return valor

# Calculo de la fuerza gravitatoria que un objeto ejerce sobre otro objeto
def fuerzaf(CONSTANTE_GRAVITATION_UNIVERSAL, masa_1, masa_2, distancia):
    magnitud = CONSTANTE_GRAVITATION_UNIVERSAL * ((masa_1 * masa_2) / ((libreria_operaciones_tuplas.modulo_vector(distancia))**2))
    normalizado = libreria_operaciones_tuplas.normalizar_vector(distancia)
    valor = libreria_operaciones_tuplas.producto_escalar(normalizado, magnitud)
    return valor

# Calulo de la fuerza total que ejercen todos los cuerpos del sistema sobre un objeto
def fuerza_totalf(fuerza_1, fuerza_2):
    valor = libreria_operaciones_tuplas.sumar_tuplas(fuerza_1, fuerza_2)
    return valor

# Calculo de la acceleracion de un objeto a partir de la fuerza ejercida en el y de su masa
def acceleracionf(fuerza, masa_1):
    valor = libreria_operaciones_tuplas.producto_escalar(fuerza, (1 / masa_1))
    return valor

# Calculo de la varacion de la velocidad de un cuerpo a parir de el tiempo pasado y de la acceleracion en ese intervalo
def variacion_velocidadf(acceleracion, tiempo_variacion):
    valor = libreria_operaciones_tuplas.producto_escalar(acceleracion, tiempo_variacion)
    return valor

# Calculo de la velocidad actual de un objeto a partir de la varacion de su velocidad y de su velocidad anterior
def velocidadf(velocidad_anterior, variacion_velocidad):
    valor = libreria_operaciones_tuplas.sumar_tuplas(velocidad_anterior, variacion_velocidad)
    return valor

# Calculo de la posicion actual de un objeto a partir de su posicion anterior, su velocidad y el intervalo de tiempo
def posicionf(posicion_anterior, velocidad, tiempo_variacion):
    producto = libreria_operaciones_tuplas.producto_escalar(velocidad, tiempo_variacion)
    valor = libreria_operaciones_tuplas.sumar_tuplas(posicion_anterior, producto)
    return valor
