# Punto 1

# Crear lista:
mi_lista = []

# Cantidad de elementos:
cantidad_elementos = eval(input("Ingrese la cantidad de elementos: "))

# Llenar lista con while:
i = 0
while i < cantidad_elementos:
    elemento = eval(input(f"Ingrese el elemento mi_lista[{i}]: "))
    mi_lista.append(elemento)
    i = i + 1

# Saber elemento mayor y menor en mi lista:
elemento_mayor = mi_lista[0]
elemento_menor = mi_lista[0]

i = 0
while i < cantidad_elementos:
    # Mayor
    if mi_lista[i] > elemento_mayor:
        elemento_mayor = mi_lista[i]
    # Menor
    else:
        elemento_menor = mi_lista[i]

    i = i + 1

# Resultados
print("Mi lista:", mi_lista)
print("Elemento mayor:", elemento_mayor)
print("Elemento menor:", elemento_menor)