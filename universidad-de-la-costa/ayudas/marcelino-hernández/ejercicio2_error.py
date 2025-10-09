# ejercicio 2

# importar librería
import numpy as np

# leer valor m
m = int(input("Ingrese el valor de m: "))

# leer valor n
n = int(input("Ingrese el valor de n: "))

# crear matriz
"""
np.zeros(numero) = lista
np.zeros([filas, columnas]) = matriz
"""
matriz = np.zeros([m, n]) 

# llenar matriz
for i in range(m):
    for j in range(n):
        x = int(input(f"Ingrese el elemento [{i}][{j}]: "))
        matriz[i,j] = x

print(matriz)
# encontrar suma de índices pares
matriz_nueva = np.zeros([m, n])

for i in range(m):
    for j in range(n):
        # no empezar en [0][0]
        if i + j != 0:
            # sumar índices y ver si es par
            if i + j % 2 == 0:
                matriz_nueva[i][j] = matriz[i][j]
            # si no es par la suma
            else:
               matriz_nueva[i][j] = "*" 
        else:
            matriz_nueva[i][j] = "*"

# imprimir matriz
print("")
print(matriz)