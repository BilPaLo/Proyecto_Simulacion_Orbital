import libreria_operaciones_tuplas


class Planeta:

    def __init__(self, nombre = "", MASA = 0, img = "", fijo = "", posicion = (0.0, 0.0), velocidad = (0, 0.0), acceleracion = (0.0, 0.0)):
        self.nombre = nombre
        self.MASA = MASA
        self.img = img
        self.fijo = fijo
        self.posicion = posicion
        self.velocidad = velocidad
        self.acceleracion = acceleracion

    def __str__(self):
        return ("Nombre: %s, Masa: %f, Imagen: %s, Coordenada x: %f, Coordenada y: %f, Fijo: %s , Velocidad x: %f, Velocidad y: %f" % (self.nombres, self.MASA, self.img, self.poscion[0], self.posicion[1], self.fijo, self.velocidad[0], self.velocidad[1]))


    # Calculo de la distancia entre dos objetos, usando sus coordenadas
    def distanciaf(self, posicion_2):
        valor = libreria_operaciones_tuplas.restar_tuplas(posicion_2, self.posicion)
        return valor

    # Calculo de la fuerza gravitatoria que un objeto ejerce sobre otro objeto
    def fuerzaf(self, CONSTANTE_GRAVITATION_UNIVERSAL, masa_2, distancia):
        magnitud = CONSTANTE_GRAVITATION_UNIVERSAL * ((self.MASA * masa_2) / ((libreria_operaciones_tuplas.modulo_vector(distancia))**2))
        normalizado = libreria_operaciones_tuplas.normalizar_vector(distancia)
        valor = libreria_operaciones_tuplas.producto_escalar(normalizado, magnitud)
        return valor

    # Calulo de la fuerza total que ejercen todos los cuerpos del sistema sobre un objeto
    def fuerza_totalf(self, fuerza_1, fuerza_2):
        valor = libreria_operaciones_tuplas.sumar_tuplas(fuerza_1, fuerza_2)
        return valor

    # Calculo de la acceleracion de un objeto a partir de la fuerza ejercida en el y de su masa
    def acceleracionf(self, fuerza):
        valor = libreria_operaciones_tuplas.producto_escalar(fuerza, (1 / self.MASA))
        return valor

    # Calculo de la varacion de la velocidad de un cuerpo a parir de el tiempo pasado y de la acceleracion en ese intervalo
    def variacion_velocidadf(self, tiempo_variacion):
        valor = libreria_operaciones_tuplas.producto_escalar(self.acceleracion, tiempo_variacion)
        return valor

    # Calculo de la velocidad actual de un objeto a partir de la varacion de su velocidad y de su velocidad anterior
    def velocidadf(self, variacion_velocidad):
        valor = libreria_operaciones_tuplas.sumar_tuplas(self.velocidad, variacion_velocidad)
        return valor

    # Calculo de la posicion actual de un objeto a partir de su posicion anterior, su velocidad y el intervalo de tiempo
    def posicionf(self, tiempo_variacion):
        producto = libreria_operaciones_tuplas.producto_escalar(self.velocidad, tiempo_variacion)
        valor = libreria_operaciones_tuplas.sumar_tuplas(self.posicion, producto)
        return valor
