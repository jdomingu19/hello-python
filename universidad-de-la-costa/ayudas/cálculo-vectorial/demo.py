# Cálculo vectorial | CUC | Python

"""
- Un menú con los temas en orden
- Una función para cada tema
- Todo lo dado en clase si es posible
"""

# Funciones
def productoPunto():
    # Teoría
    print("- - - -")
    print("A = (a1, a2, a3 ... an) pertenece a R^n")
    print("B = (b1, b2, b3 ... bn) pertenece a R^n")
    print("entonces...")
    print("A • B = a1b1 + a2b2 + a3b3 + ... + anbn")
    print("")

    # Dimensión del vector
    r = input("Ingrese el valor de r: ") # str
    # Validar
    while not r.isnumeric():
        print("Datos ingresado no válidos...")
        r = input("Ingrese el valor de r: ") # str
    
    # Llenar vector A
    vector_A = []
    i = 1
    while i <= int(r):
        x = eval(input(f"Ingrese el componente vector_A[{i}]: "))
        vector_A.append(x)
        i = i + 1
    # Llenar vector B
    vector_B = []
    i = 1
    while i <= int(r):
        x = eval(input(f"Ingrese el componente vector_B[{i}]: "))
        vector_B.append(x)
        i = i + 1

    # Procedimiento
    acumulador = 0
    i = 0
    while i < int(r):
        x = vector_A[i] * vector_B[i]
        acumulador = acumulador + x
        i = i + 1

    # Imprimir resultados
    print(f"A = {vector_A}")
    print(f"B = {vector_B}")
    print("A • B =", end=" ")
    i = 0
    while i < int(r):
        if not i == int(r) - 1:
            print(f"({vector_A[i]})({vector_B[i]})", end=" + ")
        else:
            print(f"({vector_A[i]})({vector_B[i]})")
        i = i + 1

    print("A • B =", end=" ")
    i = 0
    while i < int(r):
        # Si no es el último número...
        if not i == int(r) - 1:
            # Si el número que está después...
            if vector_A[i + 1] * vector_B[i + 1] < 0:
                print(f"{abs(vector_A[i] * vector_B[i])}", end=" - ")
            else:
                print(f"{abs(vector_A[i] * vector_B[i])}", end=" + ")
        else:
            print(f"{abs(vector_A[i] * vector_B[i])}")
        i = i + 1

    print("A • B =", end=" ")
    print(acumulador)



def productoVectorial():
    print("Hola 2")

salir = False
while not salir:
    # Menú
    print("- - Menú - -")
    print("1) Producto punto")
    print("2) Producto vectorial")
    accion = input("¿Qué desea hacer?: ") # str

    # Validar accion
    while accion.isnumeric() == False:
        print("Datos ingresado no válidos...")
        accion = input("¿Qué desea hacer?: ") # str

    # Llamar funciones
    if accion == "1":
        productoPunto()
        # Salir...
        print("- - - -")
        x = input("¿Salir? 1) Sí 2) No: ")
        if x == "1":
            salir = True
        else:
            salir = False
    elif accion == "2":
        productoVectorial()
        # Salir...
        print("- - - -")
        x = input("¿Salir? 1) Sí 2) No: ")
        if x == "1":
            salir = True
        else:
            salir = False
    else:
        print("Datos ingresado no válidos...")

# Mensaje de despedida
print("- - - -")
print("Hasta luego...")