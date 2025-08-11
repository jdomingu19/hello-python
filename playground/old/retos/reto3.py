# Elementos de un vector | Reto 3

# Crear vector:
mi_vector = []

# 1) Cantidad de elementos:
cantidad_elementos = eval(input("Ingrese la cantidad de elementos: "))

# Validar que cantidad_elementos sea mayor que cero
while cantidad_elementos <= 0:
    print("Datos no válidos")
    print("La cantidad de elementos debe ser mayor que cero...")
    cantidad_elementos = eval(input("Ingrese la cantidad de elementos: "))

# 2) Llenar vector:
i = 0
while i < cantidad_elementos:
    elemento = eval(input(f"Ingrese el elemento mi_vector[{i}]: "))
    # Validar que elemento sea positivo
    if elemento <= 0:
        print("Datos no válidos")
        print("Los elementos deben ser positivos...")
    else:
        mi_vector.append(elemento)
        i = i + 1

# 3) Promedio números pares:
sumatoria_pares = 0
cantidad_pares = 0

i = 0
while i < cantidad_elementos:
    # Pares
    if mi_vector[i] % 2 == 0:
        # Sumatoria pares
        sumatoria_pares = sumatoria_pares + mi_vector[i]
        # Cantidad pares
        cantidad_pares = cantidad_pares + 1
    i = i + 1

promedio_pares = round(sumatoria_pares / cantidad_pares,2)

# 4) Promedio números impares:
sumatoria_impares = 0
cantidad_impares = 0

i = 0
while i < cantidad_elementos:
    # impares
    if mi_vector[i] % 2 != 0:
        # Sumatoria impares
        sumatoria_impares = sumatoria_impares + mi_vector[i]
        # Cantidad impares
        cantidad_impares = cantidad_impares + 1
    i = i + 1

promedio_impares = round(sumatoria_impares / cantidad_impares,2)

# 5) Sumatoria elementos a la cantidad_elementos:
sumatoria_elementos = 0

i = 0
while i < cantidad_elementos:
    # Elemento a la cantidad_elementos
    x = mi_vector[i] ** cantidad_elementos
    # Sumatoria elementos
    sumatoria_elementos = sumatoria_elementos + x
    i = i + 1

# Resultados
print("- - RESULTADOS - -")
print(f"A) Promdedio pares: {promedio_pares}")
print(f"B) Promdedio impares: {promedio_impares}")
print(f"C) Sumatoria elementos a la cantidad de elementos: {sumatoria_elementos}")