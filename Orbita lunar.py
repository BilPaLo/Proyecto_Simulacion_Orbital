### Programa que calcula la posición de la Luna durante su órbita alrededor de la Tierra.
### Saul, Lorite y Laurene

# Esa linea importa un programa de una libreria creado por nosotros que
# comprueba que el usuario ha entrado datos correctos (float o entero, y ningun otro tipo de datos)
from funciones_excepciones import excepciones_float
# Aqui importamos una libreria entera de operaciones de tuplas
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


# Definicion de la funcion main que calcula la posicion de la luna cada segundo y lo imprime cada dia

def main():
    CONSTANTE_GRAVITATION_UNIVERSAL = 6.67384e-11
    MASA_TIERRA = 5.9722e24
    MASA_LUNA = 7.348e22
    fuerza_gravitatoria_total = 0.0
    posicion_tierra = (0.0, 0.0)
    posicion_luna = (0.0, 384402e3)
    distancia_tierra_luna = (0.0, 0.0)
    fuerza_tierra_luna = (0.0, 0.0)
    tiempo_total = 86400 * tiempo_variacion * numeros_de_dias_a_simular
    acceleracion_luna = (0.0, 0.0)
    velocidad_luna = (1023.055, 0.0)
    velocidad_tierra = (0.0, 0.0)
    contador_1 = 0
    fichero_datos = open("datos.txt", "w")
    fichero_datos.write("t (s)\t\tt (d)\t\t\tF (N)\t\t\t\t(x, y) (m)\t\t\tR (m)\n")
    fichero_datos = open("datos.txt", "a")
    fichero_datos.write("--------------------------------------------------------------------------------------------------------------------\n")
    while contador_1 <= tiempo_total:
        distancia_tierra_luna = distanciaf(posicion_luna, posicion_tierra)
        fuerza_tierra_luna = fuerzaf(CONSTANTE_GRAVITATION_UNIVERSAL, MASA_TIERRA, MASA_LUNA, distancia_tierra_luna)
        fuerza_gravitatoria_total = fuerza_totalf(fuerza_tierra_luna, (0.0, 0.0))
        acceleracion_luna = acceleracionf(fuerza_tierra_luna, MASA_LUNA)
        variacion_velocidad = variacion_velocidadf(acceleracion_luna, tiempo_variacion)
        velocidad_luna = velocidadf(velocidad_luna, variacion_velocidad)
        if contador_1 % 86400 == 0:
            #print("%8.2f\t%.2f\t\t(%.5e, %.5e)\t(%.5e, %.5e)\t\t%.5e" % (contador_1, contador_1 / 86400, fuerza_gravitatoria_total[0], fuerza_gravitatoria_total[1], posicion_luna[0], posicion_luna[1], libreria_operaciones_tuplas.modulo_vector(distancia_tierra_luna)))
            # imprimir en un fichero
            fichero_datos = open("datos.txt", "a")
            fichero_datos.write("%8.2f\t%.2f\t\t(%.5e, %.5e)\t(%.5e, %.5e)\t\t%.5e\n" % (contador_1, contador_1 / 86400, fuerza_gravitatoria_total[0], fuerza_gravitatoria_total[1], posicion_luna[0], posicion_luna[1], libreria_operaciones_tuplas.modulo_vector(distancia_tierra_luna)))
            fichero_datos.close()
        posicion_luna = posicionf(posicion_luna, velocidad_luna, tiempo_variacion)
        contador_1 += tiempo_variacion



# Inputs pedidos al usuario

numeros_de_dias_a_simular = excepciones_float("Introduce el tiempo final de simulacion (dias): ")

tiempo_variacion = excepciones_float("Introduce el incremento de cada paso de tiempo (s): ")

numeros_de_dias_a_simular /= tiempo_variacion

# Programa - llamamos a la funcion main si estamos en esta programa

if __name__ == '__main__':
    main()
