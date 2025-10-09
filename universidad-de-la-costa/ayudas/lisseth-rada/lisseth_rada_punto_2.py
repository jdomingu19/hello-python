# 1. Importar módulo para arrays
import numpy as np

# 2. Leer la cantidad de elementos
n = int(input("-> Ingrese el valor de n: "))
while n <= 0:
    print("Datos incorrectos...")
    n = int(input("-> Ingrese el valor de n: "))

# 3. Llenar lista de números
lista_temporal = []
print(lista_temporal, type(lista_temporal))
for i in range(n):
    numero = eval(input("-> Ingrese un número: "))
    while numero < 0:
        print("Datos incorrectos...")
        numero = eval(input("-> Ingrese un número: "))
    lista_temporal.append(numero)

array_numeros = np.array(lista_temporal)
print(array_numeros, type(array_numeros))

# 4. Imprimir array números
print(f"<- {array_numeros}")

# a. promedio números pares
suma_pares = 0
cont_pares = 0
for i in array_numeros:
    if i % 2 == 0:
        suma_pares = suma_pares + i
        cont_pares = cont_pares + 1

if cont_pares == 0:
    print("<- Promedio pares: 0")
else:
    promedio_pares = suma_pares / cont_pares
    promedio_pares = round(promedio_pares, 2)
    print(f"<- Promedio pares: {promedio_pares}")

# b. promedio números impares
suma_impares = 0
cont_impares = 0
for i in array_numeros:
    if i % 2 != 0:
        suma_impares = suma_impares + i
        cont_impares = cont_impares + 1

if cont_impares == 0:
    print("<- Promedio impares: 0")
else:
    promedio_impares = suma_impares / cont_impares
    promedio_impares = round(promedio_impares, 2)
    print(f"<- Promedio impares: {promedio_impares}")

# c. sumatoria elementos a la n
sumatoria = 0
for i in array_numeros:
    sumatoria = sumatoria + (i**n)
print(f"<- Sumatoria elementos a la n: {sumatoria}")