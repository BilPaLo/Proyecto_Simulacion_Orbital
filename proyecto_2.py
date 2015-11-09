import sys
import os.path
import time



# Esa linea importa un programa de una libreria creado por nosotros que
# comprueba que el usuario ha entrado datos correctos (float o entero, y ningun otro tipo de datos)
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
                        dato = "".join(dato_temp[1].split())
                        datos_cuerpo.append(dato)
                        contador += 1
                    lista_cuerpos.append(datos_cuerpo)

        print("Se ha leido correctamente.")
        print(lista_cuerpos)
        time.sleep(1)

    return lista_cuerpos



def mostrar_lista_cuerpos(nombres):
    print("Lista de cuerpos existentes: ")
    # 'nombres' siendo la clave para buscar los nombres de cuerpos en el fichero
    if len(nombres) == 0:
        print("No se ha encontrado ningun cuerpo en el fichero.")
        # Poner aqui un camino directo a anadir un cuerpo
    else:
        contador = 1
        while contador <= len(nombres):
            print("%d. %s" % (contador,nombres[contador]))
            contador += 1
        opcion_detalles = excepciones_string_si_no("Quieres ver la informacion detallada de uno de esos cuerpos? Si/No: ")
        if opcion_detalles == "Si":
            detalles_cuerpo(nombres)
        else:
            menu_principal()



def detalles_cuerpo(nombres):
    opcion_detalles_cuerpo = excepciones_int_rango("Numero del cuerpo que quieres ver: ", 1, len(nombres))
    for e in nombres:
        print nombres[(opcion_detalles_cuerpo - 1)[e]]



def anadir_cuerpo():
    nombre = str(input("Nombre: "))
    while nombre is in nombres:
        print("Error - Hay un cuerpo con ese nombre que ya existe. Por favor introduzca otro nombre:")
        nombre = str(input("Nombre: "))
    masa = float(input("Masa: "))
    while masa is not > 0:
        print("Error - Masa tiene que ser strictamente positiva. Por favor introduzca otra masa:")
        masa = float(input("Masa: "))
    img = str(input("Nombre de fichero de la imagen: "))
    coordenada_x = float(input("Coordenada x del cuerpo: "))
    coordenada_y = float(input("Coordenada y del cuerpo: "))
    flag_fijo = str(input("Es fijo ese cuerpo? "))
    velocidad_x = float(input("Velocidad x del cuerpo: "))
    velocidad_y = float(input("Velocidad y del cuerpo: "))
    fichero.write("nombre: %s, masa: %f, img: %s, x: %f, y: %f, vx: %f, vy: %f")

def guardar(lista_cuerpos):
    os.system("cls")

    #  preguntar el fichero
    nombre_fichero = excepciones_string("Escriba en que fichero desea guardar la informacion: ")
    if nombre_fichero.find(".txt") == -1:
        nombre_fichero += ".txt"

    # comprobar que la ruta existe
    while os.path.isfile(nombre_fichero) == False:
        guardar_proceso(lista_cuerpos)
    else:
        guardar_sobreescribir = excepciones_string_si_no("Ya existe un archivo con ese nombre. Desea sobreescribir el archivo? (Si)\nO desea guardarlo como un nuevo archivo? (No): ")
        # abrir en formato leer
        if guardar_sobreescribir == "Si":
            guardar_proceso()
        else:
            guardar(lista_cuerpos)

def guardar_proceso(lista_cuerpos):
    fichero = open(nombre_fichero, "w")
    if lista_cuerpos is not []:
        for e in lista_cuerpos:
            fichero.write("nombre:%s, masa:%d, img: %s, x: %f, y: %f, fijo: %s, vx:%f, vy:%f" % (lista_cuerpos[e[0]], lista_cuerpos[e[1]], lista_cuerpos[e[2]], lista_cuerpos[e[3]], lista_cuerpos[e[4]], lista_cuerpos[e[5]], lista_cuerpos[e[6]], lista_cuerpos[e[7]]))
            print("Se ha guardado correctamente.")
    else:
        print("No hay informacion para guardar.")
    fichero.close()
    time.sleep(1)
    menu_principal()

# def del menu Principal

def menu_principal():
    lista_cuerpos = []
    os.system("cls")
    print("Menu Principal:\n\n1. Leer\n2. Mostrar\n3. Anadir un cuerpo nuevo\n4. Eliminar un cuerpo\n5. Modificar los datos de un cuerpo\n6. Guardar")
    opcion_menu_principal = excepciones_int_rango_exit("\nIntroduce que opcion desea realizar, pulsa q/Q para salir: ", 1, 6)

    if opcion_menu_principal == "1":
        lista_cuerpos = leer()
        menu_principal()
    elif opcion_menu_principal == "2":
        mostrar_lista_cuerpos(lista_cuerpos)
    elif opcion_menu_principal == "3":
        anadir_cuerpo()
    elif opcion_menu_principal == "4":
        eliminar_cuerpo()
    elif opcion_menu_principal == "5":
        modificar_datos_cuerpo()
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
        else:
            menu_principal()


# Definicion de la funcion main

def main():
    menu_principal()


# Programa - llamamos a la funcion main si estamos en esta programa

if __name__ == '__main__':
    main()
