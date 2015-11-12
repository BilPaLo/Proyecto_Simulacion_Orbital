# Eliminar un cuerpo: Elimina el cuerpo seleccionado de la lista. El usuario debe introducir el nombre del cuerpo a eliminar.
#                     Debe existir la posibilidad de que el usuario vuelva al menú principal sin eliminar ningún cuerpo.
#                     Si el usuario no selecciona esta opción de volver, el programa se quedará en esta opción permitiendo al usuario borrar elementos
#                     hasta que ya no existan más. Si no existen elementos a borrar, el programa debe notificárselo al usuario y no permitirle seleccionar nada.
#
#Modificar los datos de un cuerpo. Se presenta al usuario la lista de cuerpos, el usuario selecciona un cuerpo de los existentes,
#                     se imprime la información del cuerpo seleccionado y se solicita indicar qué propiedad quiere ser modificada,
#                     pidiendo al usuario el nuevo valor. Al igual que en el caso anterior, el programa se queda en esta opción hasta que
#                     el usuario introduce la opción de Volver. Si no existen elementos a modificar el programa debe notificárselo al usuario y
#                     no permitirle seleccionar ningún elemento.


def eliminar(nombres):
    # se le pide que introduzca el nombre del cuerpo que quiere eliminar
    # en la misma pantalla se le tiene que ofrecer la opcion de volver atras, es decir, la opcion de no eliminar ningun cuerpo
    # si el cuerpo que escribe no existe se le notifica y se vuelve a mostrar la opcion de borrar
    # despues de borrar un cuerpo se comprueba si quedan mas cuerpos
    # si quedan mas cuerpos se le ofrece la opcion anterior de borrar otro
    # si no quedan mas cuerpos se le notifica y se vuelve al menu principal

def modificar_datos(nombres):

    # imprimir la lista de cuerpos y a cada cuerpo establecerle un numero
    # seleccion de un numero
    # abrir cuerpo correspondiente al numero
    # mostrar su informacion con un numero que hace referencia a cada elemento
    # el usuario determina el numero(el elemento quiere modificar)
    # si no existe ese elemento el programa lo notifica y le vuelve a mostrar la lista de elementos a elegir
    # el usuario modifica el valor y se le ofrece la opcion de salir
    # se le pregunta si quiere modificar otro dato: ->SI: se le muestra el menu de los cuerpos ->NO: se le lleva al menu principal
    # (si podemos mostrarle el menu de los elementos del dato seleccionado mejor)(SOLO SI NOS SOBRA TIEMPO)
