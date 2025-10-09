# 1. Importar paquetes necesarios
from random import randint

# 2. Crear matriz
matriz = []

# 3. Llenar matriz 4x4 con enteros aleatorios
filas = 4
columnas = 4
i = 0
while i < filas:
    matriz.append([])
    j = 0
    while j < columnas:
        numero = randint(0, 10)
        matriz[i].append(numero)
        j = j + 1
    i = i + 1

print(f"Matriz: {matriz}")
print(f"Filas: {filas}")
print(f"Columnas: {columnas}")

# 4. Sumar una fila que pida el usuario
fila = input("Ingrese fila a sumar: ")
while int(fila) < 0 or int(fila) > filas - 1:
    print("Datos incorrectos...")
    fila = input("Ingrese fila a sumar: ")

suma = 0
j = 0
while j < columnas:
    suma = suma + matriz[int(fila)][j]
    j = j + 1
print(f"Suma fila usuario: {suma}")

# 5. Suma diagonal inversa
suma_di = 0
i = 0
while i < filas:
    suma_di = suma_di + matriz[i][columnas - 1 - i]
    i = i + 1
print(f"Suma diagonal inversa: {suma_di}")