def sumar_tuplas():
    a = ((float(input("Ax: "))), (float(input("Ay: "))))
    b = ((float(input("Bx: "))), (float(input("By: "))))
    x = a[0] + b[0]
    y = a[1] + b[1]
    c = (x, y)
    return c

def restar_tuplas():
    a = ((float(input("Ax: "))), (float(input("Ay: "))))
    b = ((float(input("Bx: "))), (float(input("By: "))))
    x = a[0] - b[0]
    y = a[1] - b[1]
    c = (x, y)
    return c

def multiplicar_tuplas():
    a = ((float(input("Ax: "))), (float(input("Ay: "))))
    b = ((float(input("Bx: "))), (float(input("By: "))))
    x = a[0] * b[0]
    y = a[1] * b[1]
    c = (x, y)
    return c

def dividir_tuplas():
    a = ((float(input("Ax: "))), (float(input("Ay: "))))
    b = ((float(input("Bx: "))), (float(input("By: "))))
    x = a[0] / b[0]
    y = a[1] / b[1]
    c = (x, y)
    return c
