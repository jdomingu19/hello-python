# ejercicio 1

# crear matriz
matriz = []

# leer valor de m
m = int(input("Ingrese el valor de m: "))

# llenar matriz
print("")
for i in range(m):
    matriz.append([])
    for j in range(m):
        x = int(input(f"Ingrese el elemento [{i}][{j}]: "))
        matriz[i].append(x)

# imprimir números diagonal principal
print("")
print("Números diagonal principal:")
for i in range(m):
    for j in range(m):
        if j == i:
            print(matriz[i][j])

# imprimir números diagonal principal mayor que 10
print("")
print("Números diagonal principal mayores que 10:")
encontrados = False
for i in range(m):
    for j in range(m):
        if j == i and matriz[i][j] > 10:
            print(matriz[i][j])
            encontrados = True

if encontrados == False:
    print("Ninguno cumple la condición...")