# Punto 2

# Crear lista
lista = []

# Cantidad de elementos
cantidad_elementos = eval(input("Ingrese la cantidad de elementos: "))

# Llenar lista
i = 0
while i < cantidad_elementos:
    elemento = eval(input(f"Ingrese el elemento lista[{i}]: "))
    lista.append(elemento)
    i = i + 1

# 1) Números pares mayores que 10
contador_pares = 0
i = 0
while i < cantidad_elementos:

    if lista[i] %  2 == 0 and lista[i] > 10:
        contador_pares = contador_pares + 1

    i = i + 1

# 2) Promedio elementos
acumulador_suma = 0
i = 0
while i < cantidad_elementos:
    acumulador_suma = acumulador_suma + lista[i]
    i = i + 1

promedio = acumulador_suma / len(lista)

# Resultados
print("- - Resultados - -")
print("Mi lista:", lista)
print("Elementos pares mayores que 10:", contador_pares)
print("Promedio de elementos:", promedio)