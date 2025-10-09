# ejercicio 1 de Luiz Gonzáles

# crear matriz
matriz = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1], [2], [3], [4], [5], [6], [7], [8], [9]]

# llenar matriz con multiplicaciones
for i in range(len(matriz)):
    # empezar desde la segunda fila
    if i != 0:
        for j in range(1, 10):
            # guardar en [i][2] en adelante
            x = matriz[i][0] * j
            matriz[i].append(x)

# imprimir matriz
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(f"{matriz[i][j]}", end=" ")
    print("")