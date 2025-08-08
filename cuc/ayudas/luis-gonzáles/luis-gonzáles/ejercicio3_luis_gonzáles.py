# ejercicio 3 de Luis Gonzáles

# crear matriz
matriz = []

filas = 5
columnas = 6

# llenar matriz 5x6
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

# suma de los números almacendos
acumulador = 0
for i in range(filas):
    for j in range(columnas):
        acumulador = acumulador + matriz[i][j]
print(f"La suma de los números almacendos es: {acumulador}")