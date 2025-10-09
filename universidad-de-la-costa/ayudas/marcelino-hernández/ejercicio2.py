# ejercicio 2

# crear matriz
matriz = []

# leer valor m
m = int(input("Ingrese el valor de m: "))

# leer valor n
n = int(input("Ingrese el valor de n: "))

# llenar matriz
print("")
for i in range(m):
    matriz.append([])
    for j in range(n):
        x = int(input(f"Ingrese el elemento [{i}][{j}]: "))
        matriz[i].append(x)

# encontrar suma de índices pares
print("")

# matriz_nueva = matriz ERROR NO SE PUEDE HACER ESTO
matriz_nueva = []

for i in range(m):
    matriz_nueva.append([])
    for j in range(n):
        x = matriz[i][j]
        matriz_nueva[i].append(x)

for i in range(m):
    for j in range(n):
        sum_indices = i + j

        if sum_indices == 0:
            print(f"[{i}] + [{j}] = {sum_indices} CERO ")
            matriz_nueva[i][j] = "*"
        else:
            if sum_indices % 2 == 0:
                print(f"[{i}] + [{j}] = {sum_indices} PAR ")
                matriz_nueva[i][j] = matriz[i][j]

            if sum_indices % 2 != 0:
                print(f"[{i}] + [{j}] = {sum_indices} IMPAR ")
                matriz_nueva[i][j] = "*"
    
    print("")

# imprimir resultados
print("Matriz normal:")
print(matriz)
print("Matriz nueva:")
print(matriz_nueva)