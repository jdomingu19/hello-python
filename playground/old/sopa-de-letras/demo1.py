# 1. Tocas las combinaciones posibles de 'abc' en matriz

# Crear matriz (sopa de letra)
def crear_matriz():
    global matriz 
    matriz = []
    for i in range(3):
        matriz.append([])
        for j in range(3):
            matriz[i].append("x")

def mostrar_matriz():
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        print("[", end="")
        for j in range(columnas):
            if j != columnas - 1:
                print(f"{matriz[i][j]}", end=" ")
            else:
                print(f"{matriz[i][j]}", end="")
        print("]")

crear_matriz()
mostrar_matriz()

# Definir palabra ('abc')
palabra = "abc"
print("\n", palabra[0], palabra[1], palabra[2], "\n")

# Repartir 'abc' en matriz
print("Desde [0][0]")
for i in range(len(palabra)):
    # Desde [0][0] HORIZONTAL
    matriz[0][i] = palabra[i]

    # Desde [0][0] VERTICAL
    matriz[i][0] = palabra[i]

    # Desde [0][0] DIAGONAL
    matriz[i][i] = palabra[i]
mostrar_matriz()

crear_matriz()
print("Desde [0][-1]")
for i in range(len(palabra)):
    # Desde [0][-1] HORIZONTAL
    matriz[0][-1 - i] = palabra[i]

    # Desde [0][-1] VERTICAL
    matriz[i][-1] = palabra[i]

    # Desde [0][-1] DIAGONAL
    matriz[i][-1 - i] = palabra[i]
mostrar_matriz()

crear_matriz()
print("Desde [-1][-1]")
for i in range(len(palabra)):
    # Desde [-1][-1] HORIZONTAL
    matriz[-1][-1 - i] = palabra[i]

    # Desde [-1][-1] VERTICAL
    matriz[-1 - i][-1] = palabra[i]

    # Desde [-1][-1] DIAGONAL
    matriz[-1 - i][-1 - i] = palabra[i]
mostrar_matriz()

crear_matriz()
print("Desde [-1][0]")
for i in range(len(palabra)):
    # Desde [-1][0] HORIZONTAL
    matriz[-1][i] = palabra[i]

    # Desde [-1][0] VERTICAL
    matriz[-1 - i][0] = palabra[i]

    # Desde [-1][0] DIAGONAL
    matriz[-1 - i][i] = palabra[i]
mostrar_matriz()


crear_matriz()
print("Desde [0][1]")
for i in range(len(palabra)):
    # Desde [0][1] HORIZONTAL ERROR
    # Desde [0][1] VERTICAL
    matriz[i][1] = palabra[i]
    # Desde [0][1] DIAGONAL ERROR
mostrar_matriz()

crear_matriz()
print("Desde [1][2]")
for i in range(len(palabra)):
    # Desde [1][2] HORIZONTAL
    matriz[1][-1 - i] = palabra[i]
    # Desde [1][2] VERTICAL ERROR
    # Desde [1][2] DIAGONAL ERROR
mostrar_matriz()

crear_matriz()
print("Desde [-1][1]")
for i in range(len(palabra)):
    # Desde [-1][1] HORIZONTAL ERROR
    # Desde [-1][1] VERTICAL
    matriz[-1 - i][1] = palabra[i]
    # Desde [-1][1] DIAGONAL ERROR
mostrar_matriz()

crear_matriz()
print("Desde [1][0]")
for i in range(len(palabra)):
    # Desde [1][0] HORIZONTAL
    matriz[1][i] = palabra[i]
    # Desde [1][0] VERTICAL ERROR
    # Desde [1][0] DIAGONAL ERROR
mostrar_matriz()

crear_matriz()
print("Desde [1][1]")
for i in range(len(palabra)):
    # Desde [1][1] HORIZONTAL ERROR
    # Desde [1][1] VERTICAL ERROR
    # Desde [1][1] DIAGONAL ERROR
    matriz[1][1] = "a"
mostrar_matriz()