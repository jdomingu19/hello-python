# Ejercicio con una matriz | Reto 20

import random

vector_1 = []
vector_2 = []
vector_3 = []

n = eval(input("Ingrese valor de n: "))

while n <= 0:
    print("n debe ser entero positivo...")
    n = eval(input("Ingrese valor de n: "))

for i in range(n):
    x = random.randint(1,100)
    vector_1.append(x)

for i in range(n):
    x = random.randint(1,100)
    vector_2.append(x)

for i in range(n):
    x = random.randint(1,100)
    vector_3.append(x)

matriz = [vector_1, vector_2, vector_3]

print("- - RESULTADOS - -")
print(f"Vector 1: {vector_1}")
print(f"Vector 2: {vector_2}")
print(f"Vector 3: {vector_3}")
print(f"Matriz normal: {matriz}")

vector_1.sort()
vector_2.sort()
vector_3.sort()
matriz = [vector_1, vector_2, vector_3]
print(f"Matriz ordenada: {matriz}")