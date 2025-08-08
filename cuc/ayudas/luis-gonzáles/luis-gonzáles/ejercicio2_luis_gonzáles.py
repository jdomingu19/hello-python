# ejercicio 2 de Luiz Gonzáles

# crear matriz
matriz = []

# cantidad de filas
filas = int(input("Ingrese la cantidad de filas para la matriz: "))

# llenar columna 1 y 2
for i in range(filas):
    matriz.append([])
    for j in range(2):
        x = int(input(f"Ingrese el elemento fila {i} columna {j}: "))
        matriz[i].append(x)

# calcular tercera fila
for i in range(filas):
    x = matriz[i][0] + matriz[i][1]
    matriz[i].append(x)

# imprimir matriz
print("RESULTADO")
for i in range(filas):
    for j in range(len(matriz[0])):
        print(f"{matriz[i][j]}", end=" ")
    print("")