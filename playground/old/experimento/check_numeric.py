# Check numeric | Versión 1.0

# 1) Valores booleanos por defecto:
buscar_enteros = False
buscar_decimales = False
buscar_complejos = False

# 2) Definir mi función:
def checkNumeric(buscar_enteros, buscar_decimales, buscar_complejos):
    # Enteros
    if buscar_enteros == True:
        print("Buscar enteros")

    # Decimales
    if buscar_decimales == True:
        print("Buscar decimales")

    # Complejos
    if buscar_complejos == True:
        print("Buscar complejos")
    
# 3) Menú:
print("- - Check numeric 1.0 - -")
print("1) Enteros")
print("2) Decimales")
print("3) Complejos")

menu = input("¿Qué desea hacer?: ")

while menu != "1" and menu != "2" and menu != "3":
    print("Acción no válida...")
    menu = input("¿Qué desea hacer?: ")

if menu == "1":
    buscar_enteros == True
    buscar_decimales = False
    buscar_complejos = False
    checkNumeric(buscar_enteros, buscar_decimales, buscar_complejos)

elif menu == "2":
    buscar_enteros == False
    buscar_decimales = True
    buscar_complejos = False
    checkNumeric(buscar_enteros, buscar_decimales, buscar_complejos)

elif menu == "3":
    buscar_enteros == False
    buscar_decimales = False
    buscar_complejos = True
    checkNumeric(buscar_enteros, buscar_decimales, buscar_complejos)