# Ejercicio 2

# Crear vector:
vector = []

# Cantidad de elementos del vector:
cantidad_elementos = eval(input("Ingrese la cantidad de elementos del vector: "))

# Llenar vector con for:
for i in range(cantidad_elementos):
    elemento = eval(input(f"Ingrese el elemento vector[{i}]: "))
    vector.append(elemento)

# A) Promedio números pares:
sumatoria_pares = 0
cantidad_pares = 0

for i in range(cantidad_elementos):
    # Números pares positivos
    if vector[i] > 0:    
        if vector[i] % 2 == 0:
            sumatoria_pares = sumatoria_pares + vector[i]
            cantidad_pares = cantidad_pares + 1
    # Número pares negativos
    if vector[i] < 0:
        x = vector[i] * - 1
        if x % 2 == 0:
            sumatoria_pares = sumatoria_pares + vector[i]
            cantidad_pares = cantidad_pares + 1
        
promedio_pares = round(sumatoria_pares / cantidad_pares, 2)

# B) Promedio números impares:
sumatoria_impares = 0
cantidad_impares = 0

for i in range(cantidad_elementos):
    # Números impares positivos
    if vector[i] > 0:    
        if vector[i] % 2 == 0:
            sumatoria_impares = sumatoria_impares + vector[i]
            cantidad_impares = cantidad_impares + 1
    # Número impares negativos
    if vector[i] < 0:
        x = vector[i] * - 1
        if x % 2 == 0:
            sumatoria_impares = sumatoria_impares + vector[i]
            cantidad_impares = cantidad_impares + 1
        
promedio_impares = round(sumatoria_impares / cantidad_impares, 2)

# C) Sumatoria de todos los elementos elevados a la N potencia
sumatoria_potencia = 0
for i in range(cantidad_elementos):
    sumatoria_potencia = sumatoria_potencia + (vector[i] ** cantidad_elementos)