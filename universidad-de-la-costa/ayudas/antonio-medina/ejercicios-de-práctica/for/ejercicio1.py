# Ejercicio 1 | Prática | While

# Definir lista a:
a = []

# Cantidad de elementos en lista a:
cantidad = eval(input("Ingrese la cantidad de elementos en lista a: "))

# Llenar lista a:
for i in range(cantidad):
    elemento = eval(input(f"Ingrese el elemento a[{i}]: "))
    a.append(elemento)
    
# 1) Mayor elemento de lista a:
elemento_mayor = a[0]

for i in range(cantidad):
    if a[i] > elemento_mayor:
        elemento_mayor = a[i]

# 2) Menor elemento de lista a:
elemento_menor = a[0]

for i in range(cantidad):
    if a[i] < elemento_menor:
        elemento_menor = a[i]

# 3) Promedio elementos de lista a:
sumatoria_elementos = 0

for i in range(cantidad):
    sumatoria_elementos = sumatoria_elementos + a[i]
promedio_elementos = sumatoria_elementos / len(a)

# 4) Sumatoria elementos de lista a:
sumatoria_elementos = 0

for i in range(cantidad):
    sumatoria_elementos = sumatoria_elementos + a[i]

# 5) Elementos pares e impares de lista a:
elementos_pares = 0
elementos_impares = 0

for i in range(cantidad):
    if a[i] % 2 == 0:
        elementos_pares = elementos_pares + 1
    else:
        elementos_impares = elementos_impares + 1

# 6) Sumatoria elementos pares e impares de lista a:
sumatoria_elementos_pares = 0
sumatoria_elementos_impares = 0

for i in range(cantidad):
    if a[i] % 2 == 0:
        sumatoria_elementos_pares = sumatoria_elementos_pares + a[i]
    else:
        sumatoria_elementos_impares = sumatoria_elementos_impares + a[i]

# 7) Elementos positivos e impares de lista a:
elementos_positivos = 0
elementos_negativos = 0

for i in range(cantidad):
    if a[i] > 0:
        elementos_positivos = elementos_positivos + 1
    else:
        elementos_negativos = elementos_negativos + 1

# Resultados:
print("- - RESULTADOS - -")
print("Vector a =", a)
print("Elemento mayor:", elemento_mayor)
print("Elemento menor:", elemento_menor)
print("Promedio de elementos:", promedio_elementos)
print("Sumatoria de elementos:", sumatoria_elementos)
print("Elementos pares:", elementos_pares)
print("Elementos impares:", elementos_impares)
print("Sumatoria de elementos pares:", sumatoria_elementos_pares)
print("Sumatoria de elementos impares:", sumatoria_elementos_impares)
print("Elementos positivos:", elementos_positivos)
print("Elementos negativos:", elementos_negativos)