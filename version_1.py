from funciones_excepciones import excepciones_float
import libreria_operaciones_tuplas

def distancia(posicion_1, posicion_2):
    valor = restar_tuplas(posicion_2, posicion_1)
    return valor

def fuerza(CONSTANTE_GRAVITATION_UNIVERSAL, masa_1, masa_2, distancia):
    magnitud = CONSTANTE_GRAVITATION_UNIVERSAL * ((masa_1 * masa_2) / ((modulo_vector(distancia)) * (modulo_vector(distancia)))
    normalizado = normalizar_vector(distancia_tierra_luna)
    valor = producto_escalar(normalizado, magnitud)
    return valor

def fuerza_total(fuerza_1, fuerza_2):
    valor = fuerza_1
    valor += fuerza_2
    return valor

def acceleracion(fuerza, masa_1):
    valor = fuerza / masa_1
    return valor

def variacion_velocidad(acceleracion, tiempo_variacion):
    valor = acceleracion * tiempo_variacion
    return valor

def velocidad(velocidad_anterior, variacion_velocidad):
    valor = sumar_tuplas(velocidad_anterior, variacion_velocidad)
    return valor

def posicion(posicion_anterior, velocidad, tiempo_variacion):
    valor = sumar_tuplas(posicion_anterior, (velocidad * tiempo_variacion))
    return valor


# Def main

def main():
    print("t (s)\tt (d)\tF (N)\t(x, y) (m)\tR (m)")
    for e in range(int(numeros_de_dias_a_simular) + 1):
        distancia_tierra_luna = distancia(posicion_tierra, posicion_luna)
        fuerza_tierra_luna = fuerza(CONSTANTE_GRAVITATION_UNIVERSAL, MASA_TIERRA, MASA_LUNA, distancia_tierra_luna)
        fuerza_gravitatoria_total = fuerza_total(fuerza_tierra_luna, 0)
        acceleracion_luna = acceleracion(fuerza_tierra_luna, MASA_TIERRA)
        variacion_velocidad = variacion_velocidad(acceleracion_luna, tiempo_variacion)
        velocidad_luna = velocidad(velocidad_luna, variacion_velocidad)
        posicion_luna = posicion(posicion_luna, velocidad_luna, tiempo_variacion)
        print("%f\t%f\t%f\t%f\t%f\t" % (tiempo_total, tiempo_total / 86400, fuerza_gravitatoria_total, posicion_luna, distancia_tierra_luna))
    print ("End simulacion")


### Variables

CONSTANTE_GRAVITATION_UNIVERSAL = 6.67e-11
MASA_TIERRA = 5.9722e24
MASA_LUNA = 7.348e22
fuerza_gravitatoria_total = 0.0
posicion_tierra = (0.0, 0.0)
posicion_luna = (0.0, 384402e3)
distancia_tierra_luna = (0.0, 0.0)
fuerza_tierra_luna = 0.0
tiempo_total = 0.0
acceleracion_luna = (0.0, 0.0)
velocidad_luna = (1023.055, 0.0)

## Inputs

numeros_de_dias_a_simular = excepciones_float("Introduce el tiempo final de simulacion (dias): ")

tiempo_variacion = excepciones_float("Introduce el incremento de cada paso de tiempo (s): ")

# Programa

if __name__ == '__main__':
    main()
