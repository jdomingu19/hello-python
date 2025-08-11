# Ejercicio con lista | RETO 6

print("- - Ejercicio con lista | RETO 6 - -")

# Crear lista:
mi_lista = []

# Cantidad de elementos:
cantidad_elementos = eval(input("Ingrese la cantidad de elementos: "))

while cantidad_elementos <= 0:
    print("Datos no válidos...")
    cantidad_elementos = eval(input("Ingrese la cantidad de elementos: "))

# Llenar lista:
i = 0
while i < cantidad_elementos:
    elemento = eval(input(f"Ingrese el elemento mi_lista[{i}]: "))
    mi_lista.append(elemento)
    i = i + 1

# A) Elementos pares mayores que 10:
cantidad_pares = 0
a = []

i = 0
while i < cantidad_elementos:
    if mi_lista[i] > 10 and mi_lista[i] % 2 == 0:
        cantidad_pares = cantidad_pares + 1
        a.append(mi_lista[i])
    i = i + 1

# B) Promedio elementos:
sumatoria_elementos = 0

i = 0
while i < cantidad_elementos:
    sumatoria_elementos = sumatoria_elementos + mi_lista[i]
    i = i + 1 

promedio_elementos = sumatoria_elementos / cantidad_elementos

# Resultados:
print("- - RESULTADOS - -")
print(f"A) Elementos pares mayores que 10: {cantidad_pares}")
print(a)
print(f"B) Promedio elementos: {promedio_elementos}")