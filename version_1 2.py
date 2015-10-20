### Programa que calcula la posición de la Luna durante su órbita alrededor de la Tierra.
### Saul, Lorite y Laurene


from funciones_excepciones import excepciones_float
import libreria_operaciones_tuplas

def distanciaf(posicion_1, posicion_2):
    valor = libreria_operaciones_tuplas.restar_tuplas(posicion_2, posicion_1)
    return valor

def fuerzaf(CONSTANTE_GRAVITATION_UNIVERSAL, masa_1, masa_2, distancia):
    magnitud = CONSTANTE_GRAVITATION_UNIVERSAL * ((masa_1 * masa_2) / ((libreria_operaciones_tuplas.modulo_vector(distancia)) * (libreria_operaciones_tuplas.modulo_vector(distancia))))
    normalizado = libreria_operaciones_tuplas.normalizar_vector(distancia)
    valor = libreria_operaciones_tuplas.producto_escalar(normalizado, magnitud)
    return valor

def fuerza_totalf(fuerza_1, fuerza_2):
    valor = libreria_operaciones_tuplas.sumar_tuplas(fuerza_1, fuerza_2)
    return valor

def acceleracionf(fuerza, masa_1):
    valor = libreria_operaciones_tuplas.producto_escalar(fuerza, (1 / masa_1))
    return valor

def variacion_velocidadf(acceleracion, tiempo_variacion):
    valor = libreria_operaciones_tuplas.producto_escalar(acceleracion, tiempo_variacion)
    return valor

def velocidadf(velocidad_anterior, variacion_velocidad):
    valor = libreria_operaciones_tuplas.sumar_tuplas(velocidad_anterior, variacion_velocidad)
    return valor

def posicionf(posicion_anterior, velocidad, tiempo_variacion):
    producto = libreria_operaciones_tuplas.producto_escalar(velocidad, tiempo_variacion)
    valor = libreria_operaciones_tuplas.sumar_tuplas(posicion_anterior, producto)
    return valor


# Def main

def main():
    print("t (s)\t\tt (d)\t\tF (N)\t\t(x, y) (m)\t\tR (m)")
    for e in range(int(numeros_de_dias_a_simular) + 1):
        distancia_tierra_luna = distanciaf(posicion_tierra, posicion_luna)
        fuerza_tierra_luna = fuerzaf(CONSTANTE_GRAVITATION_UNIVERSAL, MASA_TIERRA, MASA_LUNA, distancia_tierra_luna)
        fuerza_gravitatoria_total = fuerza_totalf(fuerza_tierra_luna, (0.0, 0.0))
        acceleracion_luna = acceleracionf(fuerza_tierra_luna, MASA_TIERRA)
        variacion_velocidad = variacion_velocidadf(acceleracion_luna, tiempo_variacion)
        global velocidad_luna
        velocidad_luna = velocidadf(velocidad_luna, variacion_velocidad)
        global posicion_luna
        posicion_luna = posicionf(posicion_luna, velocidad_luna, tiempo_variacion)
        print("%.2f\t\t%.2f\t%s\t%s\t\t%s" % (tiempo_total, tiempo_total / 86400, fuerza_gravitatoria_total, posicion_luna, distancia_tierra_luna))
        global tiempo_total
        tiempo_total += (tiempo_variacion * 86400)
    print ("End simulacion")


### Variables

CONSTANTE_GRAVITATION_UNIVERSAL = 6.67e-11
MASA_TIERRA = 5.9722e24
MASA_LUNA = 7.348e22
fuerza_gravitatoria_total = 0.0
posicion_tierra = (0.0, 0.0)
posicion_luna = (0.0, 384402e3)
distancia_tierra_luna = (1.0, 1.0)
fuerza_tierra_luna = (0.0, 0.0)
tiempo_total = 0.0
acceleracion_luna = (0.0, 0.0)
velocidad_luna = (1023.055, 0.0)

## Inputs

numeros_de_dias_a_simular = excepciones_float("Introduce el tiempo final de simulacion (dias): ")

tiempo_variacion = excepciones_float("Introduce el incremento de cada paso de tiempo (s): ")

# Programa

if __name__ == '__main__':
    main()
