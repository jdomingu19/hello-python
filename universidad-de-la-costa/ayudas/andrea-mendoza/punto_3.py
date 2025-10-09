# Módulos
import numpy as np
import random as rd

# Valor de n
n = int(input("Ingrese el valor de n: "))

# Vector 1
vector_1 = []
for i in range(n):
    elemento = rd.randint(1, 100)
    vector_1.append(elemento)
vector_1 = np.array(vector_1)

# Vector 2
vector_2 = []
for i in range(n):
    elemento = rd.randint(1, 100)
    vector_2.append(elemento)
vector_2 = np.array(vector_2)

# Vector 3
vector_3 = []
for i in range(n):
    elemento = rd.randint(1, 100)
    vector_3.append(elemento)
vector_3 = np.array(vector_3)

print(f"Vector 1: {type(vector_1)} {vector_1}")
print(f"Vector 2: {type(vector_2)} {vector_2}")
print(f"Vector 3: {type(vector_3)} {vector_3}")

# Matriz 3 x n
print("")
matriz = []
for i in range(3): # 3 filas
    matriz.append([])
    for j in range(n): # n columnas
        elemento = rd.randint(1, 100)
        matriz[i].append(elemento)
print(f"Matriz 3 x n: {type(matriz)} {matriz}")

# Matriz 3 x n + elementos vectores
print("")
for i in list(vector_1):
    matriz[0].append(i)

for i in list(vector_2):
    matriz[1].append(i)

for i in list(vector_3):
    matriz[2].append(i)

matriz = np.matrix(matriz)
print("Matriz 3 x n + elementos vectores:")
print(type(matriz))
print(matriz)
