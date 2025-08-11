def noVacio(cadena):
    if cadena.isspace():
        print(True)
    else:
        print(False)

# Leer
mi_texto = input("Escriba algo: ")
# Validar pero con una función ¿ERROR?
noVacio(mi_texto)