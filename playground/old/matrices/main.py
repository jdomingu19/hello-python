# Aquí probaremos las funciones

import Mat
import random

def llenar_matrices(a: list, b: list, c: list):
    filas = random.randint(2, 5)
    columnas = random.randint(2, 5)
    for i in range(filas):
        a.append([])
        b.append([])
        c.append([])
        for j in range(columnas): 
            a[i].append(random.randint(0, 9))
            b[i].append(random.randint(0, 9))
            c[i].append(0)

def imprimir_matrices(a: list, b: list, c: list):
    print(f"Matriz A: {a}")
    print(f"Matriz B: {b}")
    print(f"Matriz C: {c}\n")

# 2. Suma A y B en C
a, b, c = [], [], []
llenar_matrices(a, b, c)
imprimir_matrices(a, b, Mat.sumaMat(a, b, c))

# 3. Resta A y B en C
a, b, c = [], [], []
llenar_matrices(a, b, c)
imprimir_matrices(a, b, Mat.restaMat(a, b, c))

# 4. Resta A y B en C
a, b, c = [], [], []
llenar_matrices(a, b, c)
imprimir_matrices(a, b, Mat.productoMat(a, b, c))

# 5. Transpuesta de A
print(f"Matriz A: {a}")
print(f"Transpuesta de A: {Mat.traspuestaMat(a)}\n")

# 6. Adjunta de A
print(f"Matriz A: {a}")
print(f"Adjunta de A: {Mat.adjuntaMat(a)}\n")

# 7. Cofactor de A
print(f"Matriz A: {a}")
print(f"Cofactor de A: {Mat.cofactor(a)}\n")
