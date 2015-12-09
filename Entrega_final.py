import sys
import os.path
import time
import os
import libreria_operaciones_tuplas
import libreria_excepciones as ex



def os_usuario():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system('clear')

###############################################################################

#AQUI
def iniciar():
    os_usuario()
    lista_cuerpos = []

    nombre_fichero = ex.excepciones_exit("Escriba el nombre del fichero del que desea cargar datos de cuerpos espaciales: ")
    while nombre_fichero != -1:
        if nombre_fichero.find(".txt") == -1:
            nombre_fichero += ".txt"

        while os.path.isfile(nombre_fichero) == False:
            print("No existe ese fichero.\n")
            nombre_fichero = ex.excepciones_exit("Escriba que fichero desea leer: ")

        else:
            fichero = open(nombre_fichero, "r")

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
    os_usuario()
    print("Lista de cuerpos existentes: ")
    if len(nombres) == 0:
        print("No se ha encontrado ningun cuerpo en el fichero.\nSe volvera al menu principal.")
        time.sleep(2)
    else:
        contador = 0
        while contador < len(nombres):
            print("%d. %s" % (contador + 1, nombres[contador][0]))
            contador += 1
        opcion_detalles = ex.excepciones_string_si_no("Quieres ver la informacion detallada de uno de esos cuerpos? Si/No: ")
        if opcion_detalles == "Si":
            detalles_cuerpo(nombres)



def detalles_cuerpo(nombres):
    opcion_detalles_cuerpo = ex.excepciones_int_rango("\nNumero del cuerpo que quieres ver: ", 1, len(nombres))
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
    opcion_detalles_cuerpo_si_no = ex.excepciones_string_si_no("Quieres volver al menu principal? (Si) o quieres ver otro cuerpo? (No): ")
    if opcion_detalles_cuerpo_si_no == "No":
        mostrar_lista_cuerpos(nombres)



def anadir_cuerpo(nombres):
    os_usuario()
    nombre = ex.excepciones_string("\nNombre: ")
    contador = 0
    while contador < len(nombres):
        while nombre == (nombres[contador][0]):
            print("Error - Hay un cuerpo con ese nombre que ya existe. Por favor introduzca otro nombre:")
            nombre = str(input("Nombre: "))
            contador = 0
        contador += 1

    masa = ex.excepciones_float("\nMasa: ")
    while masa < 0:
        print("Error - Masa tiene que ser strictamente positiva. Por favor introduzca otra masa: ")
        masa = float(input("Masa: "))

    img = ex.excepciones_string("\nNombre de fichero de la imagen: ")
    # Comprobar que la imagen exista
    coordenada_x = ex.excepciones_float("\nCoordenada x del cuerpo: ")
    coordenada_y = ex.excepciones_float("\nCoordenada y del cuerpo: ")
    flag_fijo = ex.excepciones_string_si_no("\nEs fijo ese cuerpo? Si/No: ")
    velocidad_x = ex.excepciones_float("\nVelocidad x del cuerpo: ")
    velocidad_y = ex.excepciones_float("\nVelocidad y del cuerpo: ")
    nombres.append([nombre, masa, img, coordenada_x, coordenada_y, flag_fijo, velocidad_x, velocidad_y])
    return nombres

def eliminar_cuerpo(nombres):
    os_usuario()
    print("Lista de cuerpos existentes:\n")
    if len(nombres) == 0:
        print("No se ha encontrado ningun cuerpo en el fichero.\nSe volvera al menu principal.")
        time.sleep(2)
    else:
        contador = 0
        while contador < len(nombres):
            print("%d. %s" % (contador + 1, nombres[contador][0]))
            contador += 1
        opcion_eliminar = ex.excepciones_int_rango_exit("\nIntroduce el numero del cuerpo que quiere eliminar o q/Q para volver al menu principal: ", 1, len(nombres))
        if opcion_eliminar.isnumeric():
            del nombres[int(opcion_eliminar) - 1]
            print("El cuerpo se ha eliminado correctamente")
            opcion_eliminar_si_no = ex.excepciones_string_si_no("Quiere eliminar otro cuerpo? (Si/No): ")
            if opcion_eliminar_si_no == "Si":
                eliminar_cuerpo(nombres)
        return nombres


def modificar_datos(nombres):
    os_usuario()
    print("Lista de cuerpos existentes: ")
    if len(nombres) == 0:
        print("No se ha encontrado ningun cuerpo en el fichero.\nSe volvera al menu principal.")
        time.sleep(2)
    else:
        contador1 = 0
        contador2 = 0
        while contador1 < len(nombres):
            print("%d. %s" % (contador1 + 1, nombres[contador1][0]))
            contador1 += 1
        opcion_modificar_cuerpo = ex.excepciones_int_rango_exit("Introduce el numero del cuerpo que quiere modificar o q/Q para volver al menu principal: ", 1, len(nombres))
        if opcion_modificar_cuerpo.isnumeric():
            opcion_modificar_cuerpo = int(opcion_modificar_cuerpo)
            for e in nombres[opcion_modificar_cuerpo - 1]:
                if contador2 == 0:
                    print("\n1. Nombre: ", end="")
                if contador2 == 1:
                    print("2. Masa: ", end="")
                if contador2 == 2:
                    print("3. Imagen: ", end="")
                if contador2 == 3:
                    print("4. Coordenada x: ", end="")
                if contador2 == 4:
                    print("5. Coordenada y: ", end="")
                if contador2 == 5:
                    print("6. Fijo: ", end="")
                if contador2 == 6:
                    print("7. Velocidad x: ", end="")
                if contador2 == 7:
                    print("8. Velocidad y: ", end="")
                print(e)
                contador2 += 1
            opcion_modificar_dato = ex.excepciones_int_rango_exit("\nIntroduce el numero del dato que quieres modificar o pulsa q/Q para volver a selecionar un cuerpo: ", 1, len(nombres[int(opcion_modificar_cuerpo) - 1]))
            if opcion_modificar_dato.isnumeric():
                opcion_modificar_dato = int(opcion_modificar_dato)
                if opcion_modificar_dato == 1:
                    nombre = ex.excepciones_string("\nNombre: ")
                    contador = 0
                    while contador < len(nombres):
                        while nombre == (nombres[contador][0]):
                            print("Error - Hay un cuerpo con ese nombre que ya existe. Por favor introduzca otro nombre:")
                            nombre = str(input("Nombre: "))
                            contador = 0
                        contador += 1
                    nombres[opcion_modificar_cuerpo - 1][0] = nombre
                elif opcion_modificar_dato == 2:
                    masa = ex.excepciones_float("\nMasa: ")
                    while masa < 0:
                        print("Error - Masa tiene que ser strictamente positiva. Por favor introduzca otra masa: ")
                        masa = float(input("Masa: "))
                    nombres[opcion_modificar_cuerpo - 1][1] = masa

                elif opcion_modificar_dato == 3:
                    img = ex.excepciones_string("\nNombre de fichero de la imagen: ")
                    nombres[opcion_modificar_cuerpo - 1][2] = img
                elif opcion_modificar_dato == 4:
                    coordenada_x = ex.excepciones_float("\nCoordenada x del cuerpo: ")
                    nombres[opcion_modificar_cuerpo - 1][3] = coordenada_x
                elif opcion_modificar_dato == 5:
                    coordenada_y = ex.excepciones_float("\nCoordenada y del cuerpo: ")
                    nombres[opcion_modificar_cuerpo - 1][4] = coordenada_y
                elif opcion_modificar_dato == 6:
                    flag_fijo = ex.excepciones_string_si_no("\nEs fijo ese cuerpo? Si/No: ")
                    nombres[opcion_modificar_cuerpo - 1][5] = flag_fijo
                elif opcion_modificar_dato == 7:
                    velocidad_x = ex.excepciones_float("\nVelocidad x del cuerpo: ")
                    nombres[opcion_modificar_cuerpo - 1][6] = velocidad_x
                elif opcion_modificar_dato == 8:
                    velocidad_y = ex.excepciones_float("\nVelocidad y del cuerpo: ")
                    nombres[opcion_modificar_cuerpo - 1][7] = velocidad_y
            else:
                modificar_datos()

        return nombres

def guardar(lista_cuerpos):
    os_usuario()
    nombre_fichero = ex.excepciones_string("Escriba en que fichero desea guardar la informacion: ")
    if nombre_fichero.find(".txt") == -1:
        nombre_fichero += ".txt"

    while os.path.isfile(nombre_fichero) == False:
        guardar_proceso(lista_cuerpos, nombre_fichero)
    else:
        guardar_sobreescribir = ex.excepciones_string_si_no("Ya existe un archivo con ese nombre. Desea sobreescribir el archivo? (Si)\nO desea guardarlo como un nuevo archivo? (No): ")
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

##############################################################################

def dibujar(lista_cuerpos):
    #AQUI todo lo de pygame, dibujar la pantalla, la generalisacion de calculos...
    pass

##############################################################################

def menu_principal(lista_cuerpos):
    verdadero = True
    while verdadero:
        os_usuario()
        print("Menu Principal:\n\n1. Mostrar\n2. Anadir un cuerpo nuevo\n3. Eliminar un cuerpo\n4. Modificar los datos de un cuerpo\n5. Guardar\n6. Lanzar simulacion grafica")
        opcion_menu_principal = ex.excepciones_int_rango_exit("\nIntroduce que opcion desea realizar, pulsa q/Q para salir: ", 1, 6)
        if opcion_menu_principal == "1":
            mostrar_lista_cuerpos(lista_cuerpos)
        elif opcion_menu_principal == "2":
            lista_cuerpos = anadir_cuerpo(lista_cuerpos)
        elif opcion_menu_principal == "3":
            lista_cuerpos = eliminar_cuerpo(lista_cuerpos)
        elif opcion_menu_principal == "4":
            lista_cuerpos = modificar_datos(lista_cuerpos)
        elif opcion_menu_principal == "5":
            guardar(lista_cuerpos)
        elif opcion_menu_principal == "6":
            dibujar(lista_cuerpos)
        elif opcion_menu_principal == "q" or opcion_menu_principal == "Q":
            opcion_salir = ex.excepciones_string_si_no("Estas seguro de que quieres salir? Si/No: ")
            if opcion_salir == "Si":
                opcion_salir_guardar = ex.excepciones_string_si_no("Quieres guardar el archivo antes de salir? Si/No: ")
                if opcion_salir_guardar == "Si":
                    guardar(lista_cuerpos)
                print("Gracias por utilizar nuestro programa.\nPara cualquier problema enviar un email a innovadeusto@soporte.es")
                time.sleep(2)
                sys.exit(0)


##############################################################################

def main():
    os_usuario()
    lista_cuerpos = iniciar()
    menu_principal(lista_cuerpos)


##############################################################################

if __name__ == '__main__':
    main()
