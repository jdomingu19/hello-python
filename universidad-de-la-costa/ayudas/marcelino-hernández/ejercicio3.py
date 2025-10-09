# ejercicio 3

# importar librería
import random as rd

# crear matriz
matriz = []

# leer valor de m
m = int(input("Ingrese el valor de m: "))

# leer valor de n
n = int(input("Ingrese el valor de n: "))

# llenar matriz
for i in range(m):
    matriz.append([])
    for j in range(n):
        x = rd.randint(0,100)
        matriz[i].append(x)

print("")      
pares = 0
impares = 0
ceros = 0
maximo = 0
minimo = 10101010
for i in range(m):
    for j in range(n):
        # ceros
        if matriz[i][j] == 0:
            ceros = ceros + 1
        else:
            # números pares
            if matriz[i][j] % 2 == 0:
                pares = pares + 1
            # números impares
            else:
                impares = impares + 1

        # máximo
        if matriz[i][j] > maximo:
            maximo = matriz[i][j]
        # mínimo
        if matriz[i][j] < minimo:
            minimo = matriz[i][j]
        
# imprimir resultados
print(matriz)
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Ceros: {ceros}")
print(f"Número máximo: {maximo}")
print(f"Número mínimo: {minimo}")