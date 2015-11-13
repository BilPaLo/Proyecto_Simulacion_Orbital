import sys
import os.path
import time
import os



# Esa linea importa un programa de una libreria creado por nosotros que
# comprueba que el usuario ha entrado datos correctos (float o entero, y ningun otro tipo de datos)
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
        # aqui ponemos el mensaje del error o lo que tiene que hacer si no funciona
            print("Por favor introduce Si o No.\n")
    return valor

def excepciones_int_rango_exit(texto_input, numero_min,numero_max):
    dato_valido = False
    while not dato_valido:
        try:
            # aqui ponemos lo que puede fallar
            valor = str(input(texto_input))
            if valor.isdigit():
                if numero_min <= int(valor) <= numero_max:
                    dato_valido = True
            elif valor == "q":
                dato_valido = True
            elif valor == "Q":
                dato_valido = True
            else:
                print("El valor no esta en el rango (%d, %d) ni es q" % (numero_min, numero_max))
        except:
        # aqui ponemos el mensaje del error o lo que tiene que hacer si no funciona
            print("El valor no esta en el rango (%d, %d) ni es q" % (numero_min, numero_max))
    return valor

def excepciones_int_rango(texto_input, numero_min,numero_max):
    dato_valido = False
    while not dato_valido:
        try:
            # aqui ponemos lo que puede fallar
            valor = str(input(texto_input))
            if numero_min <= int(valor) <= numero_max:
                dato_valido = True
            else:
                print("El valor no esta en el rango (%d, %d)" % (numero_min, numero_max))
        except:
        # aqui ponemos el mensaje del error o lo que tiene que hacer si no funciona
            print("El valor no esta en el rango (%d, %d)" % (numero_min, numero_max))
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



def leer():
    os.system("cls")
    os.system('clear')
    lista_cuerpos = []

    #  preguntar el fichero
    nombre_fichero = excepciones_string("Escriba en que fichero desea leer: ")
    if nombre_fichero.find(".txt") == -1:
        nombre_fichero += ".txt"

    # comprobar que la ruta existe
    while os.path.isfile(nombre_fichero) == False:

        print("No existe ese fichero.\n")
        nombre_fichero = excepciones_string("Escriba que fichero desea leer: ")

    else:

        # abrir en formato leer
        fichero = open(nombre_fichero, "r")

        # leer linea a linea
        fin_fichero = False
        while not fin_fichero:
            linea = fichero.readline()
            if len(linea) == 0:
                fin_fichero = True
            else:
                if "nombre:" in linea:
                    datos_cuerpo_temp = linea.split(", ")
                    datos_cuerpo = []
                    contador = 0
                    while contador < len(datos_cuerpo_temp):
                        dato_temp = datos_cuerpo_temp[contador]
                        dato_temp = dato_temp.split(":")
                        dato_temp = dato_temp[1]
                        dato_temp = dato_temp.strip()
                        datos_cuerpo.append(dato_temp)
                        contador += 1
                    lista_cuerpos.append(datos_cuerpo)

        print("Se ha leido correctamente.")
        time.sleep(1)

    return lista_cuerpos



def mostrar_lista_cuerpos(nombres):
    os.system("cls")
    os.system('clear')
    print("Lista de cuerpos existentes: ")
    # 'nombres' siendo la clave para buscar los nombres de cuerpos en el fichero
    if len(nombres) == 0:
        print("No se ha encontrado ningun cuerpo en el fichero.")
        # Poner aqui un camino directo a anadir un cuerpo
    else:
        contador = 0
        while contador < len(nombres):
            print("%d. %s" % (contador + 1, nombres[contador][0]))
            contador += 1
        opcion_detalles = excepciones_string_si_no("Quieres ver la informacion detallada de uno de esos cuerpos? Si/No: ")
        if opcion_detalles == "Si":
            detalles_cuerpo(nombres)



def detalles_cuerpo(nombres):
    opcion_detalles_cuerpo = excepciones_int_rango("\nNumero del cuerpo que quieres ver: ", 1, len(nombres))
    contador = 0
    for e in nombres[int(opcion_detalles_cuerpo) - 1]:
        if contador == 0:
            print("Nombre: ", end="")
        if contador == 1:
            print("Masa: ", end="")
        if contador == 2:
            print("Imagen: ", end="")
        if contador == 3:
            print("Coordenada x: ", end="")
        if contador == 4:
            print("Coordenada y: ", end="")
        if contador == 5:
            print("Fijo: ", end="")
        if contador == 6:
            print("Velocidad x: ", end="")
        if contador == 7:
            print("Velocidad y: ", end="")
        print(e)
        contador += 1
    opcion_detalles_cuerpo_si_no = excepciones_string_si_no("Quieres volver al menu principal? (Si) o quieres ver otro cuerpo? (No): ")
    if opcion_detalles_cuerpo_si_no == "No":
        mostrar_lista_cuerpos(nombres)



def anadir_cuerpo(nombres):
    os.system("cls")
    os.system('clear')
    nombre = excepciones_string("\nNombre: ")
    contador = 0
    while contador < len(nombres):
        while nombre == (nombres[contador][0]):
            print("Error - Hay un cuerpo con ese nombre que ya existe. Por favor introduzca otro nombre:")
            nombre = str(input("Nombre: "))
            contador = 0
        contador += 1

    masa = excepciones_float("\nMasa: ")
    while masa < 0:
        print("Error - Masa tiene que ser strictamente positiva. Por favor introduzca otra masa: ")
        masa = float(input("Masa: "))

    img = excepciones_string("\nNombre de fichero de la imagen: ")
    # Comprobar que la imagen exista
    coordenada_x = excepciones_float("\nCoordenada x del cuerpo: ")
    coordenada_y = excepciones_float("\nCoordenada y del cuerpo: ")
    flag_fijo = excepciones_string_si_no("\nEs fijo ese cuerpo? ")
    velocidad_x = excepciones_float("\nVelocidad x del cuerpo: ")
    velocidad_y = excepciones_float("\nVelocidad y del cuerpo: ")
    nombres.append([nombre, masa, img, coordenada_x, coordenada_y, flag_fijo, velocidad_x, velocidad_y])
    return nombres

def eliminar_cuerpo(nombres):
    os.system("cls")
    os.system('clear')
    print("Lista de cuerpos existentes: ")
    if len(nombres) == 0:
        print("No se ha encontrado ningun cuerpo en el fichero.")
    else:
        contador = 0
        while contador < len(nombres):
            print("%d. %s" % (contador + 1, nombres[contador][0]))
            contador += 1
        opcion_eliminar = excepciones_int_rango_exit("Introduce el numero del cuerpo que quiere eliminar o q/Q para volver al menu principal: ", 0, len(nombres) - 1)
        ####for e in nombres[int(opcion_eliminar) - 1]:
            if contador == 0:
                print("Nombre: ", end="")
            if contador == 1:
                print("Masa: ", end="")
            if contador == 2:
                print("Imagen: ", end="")
            if contador == 3:
                print("Coordenada x: ", end="")
            if contador == 4:
                print("Coordenada y: ", end="")
            if contador == 5:
                print("Fijo: ", end="")
            if contador == 6:
                print("Velocidad x: ", end="")
            if contador == 7:
                print("Velocidad y: ", end="")
            print(e)
            contador += 1
        # Ahora la parte dificil de eliminar un cuerpo



    # se le pide que introduzca el nombre del cuerpo que quiere eliminar
    # en la misma pantalla se le tiene que ofrecer la opcion de volver atras, es decir, la opcion de no eliminar ningun cuerpo
    # si el cuerpo que escribe no existe se le notifica y se vuelve a mostrar la opcion de borrar
    # despues de borrar un cuerpo se comprueba si quedan mas cuerpos
    # si quedan mas cuerpos se le ofrece la opcion anterior de borrar otro
    # si no quedan mas cuerpos se le notifica y se vuelve al menu principal

def modificar_datos(nombres):
    os.system("cls")
    os.system('clear')
    # imprimir la lista de cuerpos y a cada cuerpo establecerle un numero
    # seleccion de un numero
    # abrir cuerpo correspondiente al numero
    # mostrar su informacion con un numero que hace referencia a cada elemento
    # el usuario determina el numero(el elemento quiere modificar)
    # si no existe ese elemento el programa lo notifica y le vuelve a mostrar la lista de elementos a elegir
    # el usuario modifica el valor y se le ofrece la opcion de salir
    # se le pregunta si quiere modificar otro dato: ->SI: se le muestra el menu de los cuerpos ->NO: se le lleva al menu principal
    # (si podemos mostrarle el menu de los elementos del dato seleccionado mejor)(SOLO SI NOS SOBRA TIEMPO)


def guardar(lista_cuerpos):
    os.system("cls")
    os.system('clear')

    #  preguntar el fichero
    nombre_fichero = excepciones_string("Escriba en que fichero desea guardar la informacion: ")
    if nombre_fichero.find(".txt") == -1:
        nombre_fichero += ".txt"

    # comprobar que la ruta existe
    while os.path.isfile(nombre_fichero) == False:
        guardar_proceso(lista_cuerpos, nombre_fichero)
    else:
        guardar_sobreescribir = excepciones_string_si_no("Ya existe un archivo con ese nombre. Desea sobreescribir el archivo? (Si)\nO desea guardarlo como un nuevo archivo? (No): ")
        # abrir en formato leer
        if guardar_sobreescribir == "Si":
            guardar_proceso(lista_cuerpos, nombre_fichero)
        else:
            guardar(lista_cuerpos)

def guardar_proceso(lista_cuerpos, fichero):
    fichero = open(fichero, "w")
    if lista_cuerpos != []:
        for e in lista_cuerpos:
            fichero.write("nombre:%s, masa:%f, img: %s, x: %f, y: %f, fijo: %s, vx:%f, vy:%f\n" % (e[0], float(e[1]), e[2], float(e[3]), float(e[4]), e[5], float(e[6]), float(e[7])))
        print("Se ha guardado correctamente.")
    else:
        print("No hay informacion para guardar.")
    fichero.close()
    time.sleep(1)
    menu_principal()

# def del menu Principal

def menu_principal():
    lista_cuerpos = []
    verdadero = True
    while verdadero:
        os.system("cls")
        os.system('clear')
        print("Menu Principal:\n\n1. Leer\n2. Mostrar\n3. Anadir un cuerpo nuevo\n4. Eliminar un cuerpo\n5. Modificar los datos de un cuerpo\n6. Guardar")
        opcion_menu_principal = excepciones_int_rango_exit("\nIntroduce que opcion desea realizar, pulsa q/Q para salir: ", 1, 6)
        if opcion_menu_principal == "1":
            lista_cuerpos = leer()
        elif opcion_menu_principal == "2":
            mostrar_lista_cuerpos(lista_cuerpos)
        elif opcion_menu_principal == "3":
            lista_cuerpos = anadir_cuerpo(lista_cuerpos)
        elif opcion_menu_principal == "4":
            lista_cuerpos = eliminar_cuerpo(lista_cuerpos)
        elif opcion_menu_principal == "5":
            lista_cuerpos = modificar_datos(lista_cuerpos)
        elif opcion_menu_principal == "6":
            guardar(lista_cuerpos)
        elif opcion_menu_principal == "q" or opcion_menu_principal == "Q":
            opcion_salir = excepciones_string_si_no("Estas seguro de que quieres salir? Si/No: ")
            if opcion_salir == "Si":
                opcion_salir_guardar = excepciones_string_si_no("Quieres guardar el archivo antes de salir? Si/No: ")
                if opcion_salir_guardar == "Si":
                    guardar(lista_cuerpos)
                print("Gracias por utilizar nuestro programa.\nPara cualquier problema enviar un email a alejandrolorite@opendeusto.es")
                time.sleep(2)
                sys.exit(0)


# Definicion de la funcion main

def main():
    lista_cuerpos = []
    menu_principal()


# Programa - llamamos a la funcion main si estamos en esta programa

if __name__ == '__main__':
    main()
