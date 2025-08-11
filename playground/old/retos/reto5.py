# Ejercicio con lista | RETO 5

print("- - Ejercicio con lista | RETO 5 - -")

# 1) Crear lista:
mi_lista = []

# 2) Cantidad de elementos:
cantidad_elementos = eval(input("Ingrese la cantidad de elementos: "))

while cantidad_elementos <= 0:
    print("Datos no válidos...")
    cantidad_elementos = eval(input("Ingrese la cantidad de elementos: "))

# 3) Llenar lista:
i = 0
while i < cantidad_elementos:
    elemento = eval(input(f"Ingrese el elemento mi_lista[{i}]: "))
    mi_lista.append(elemento)
    i = i + 1

# 4) Elemento mayor y elemento menor:
elemento_mayor = mi_lista[0]
elemento_menor = mi_lista[0]

i = 0
while i < cantidad_elementos:
    if mi_lista[i] > elemento_mayor:
        elemento_mayor = mi_lista[i]

    if mi_lista[i] < elemento_menor:
        elemento_menor = mi_lista[i]

    i = i + 1

# 5) Resultados
print("- - RESULTADOS - -")
print(f"Elemento mayor: {elemento_mayor}")
print(f"Elemento menor: {elemento_menor}")