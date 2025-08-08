# ejercicio 4 de Luis Gonzáles

# crear matriz
matriz = []

filas = 10
columnas = 10

# llenar matriz 10x10
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        x = int(input(f"Ingrese el elemento matriz[{i}][{j}]: "))
        matriz[i].append(x)

# imprimir matriz
print("RESULTADO")
for i in range(filas):
    for j in range(columnas):
        print(f"{matriz[i][j]}", end=" ")
    print("")

# número mayor
mayor = matriz[0][0]

for i in range(filas):
    for j in range(columnas):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            posicion = f"[{i}][{j}]"
print(f"El número mayor es {mayor}")
print(f"Y su posición es {posicion}")