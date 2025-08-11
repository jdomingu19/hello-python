# Variables globales
nombre = ""


def saludar():
    global nombre
    nombre = input("Ingrese nombre: ")


saludar()
print(nombre)
