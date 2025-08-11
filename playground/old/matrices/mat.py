# Funciones matrices by: Deiner Domínguez

def reducir():
    pass

# 2. Suma A + B en C
def sumaMat(a: list, b: list, c: list):
    try:
        filas = len(a)
        columnas = len(a[0])
        for i in range(filas):
            for j in range(columnas):
                c[i][j] = a[i][j] + b[i][j]
        return c
    except:
        return 'Error suma A y B...'

# 3. Resta A - B en C
def restaMat(a: list, b: list, c: list):
    try:
        filas = len(a)
        columnas = len(a[0])
        for i in range(filas):
            for j in range(columnas):
                c[i][j] = a[i][j] - b[i][j]
        return c
    except:
        return 'Error resta A y B...'

# 4. Producto de A * B en C
def productoMat(a: list, b: list, c: list):
    try:
        numFilas = len(a)
        numColumnas = len(b[0])
        sumandos = len(a[0])
        for i in range(numFilas):
            for j in range(numColumnas):
                suma = 0
                for k in range(sumandos):
                    suma = suma + a[i][j] * b[i][j]
                c[i][j] = suma
        return c
    except:
        return 'Error producto A y B...'

# 5. Traspuesta de A
def traspuestaMat(a: list):
    try:
        numFilas = len(a)
        numColumnas = len(a[0])
        aux = []
        for i in range(numColumnas):
            aux.append([])
            for j in range(numFilas):
                aux[i].append(0)
        for i in range(numFilas):
            for j in range(numColumnas):
                aux[j][i] = a[i][j]
        traspuesta = aux
        return traspuesta
    except:
        return 'Error traspuesta de A...'

# 6. Adjunta de A
def adjuntaMat(a: list):
    try:
        numFilas = len(a)
        numColumnas = len(a[0])
        aux = a.copy()
        for i in range(numFilas):
            for j in range(numColumnas):
                aux[i][j] = cofactor(a, i, j)
        adjunta = aux
        return adjunta
    except:
        return 'Error adjunta de A...'

# 7. Cofactor de A
def cofactor(a: list, fila: int, col: int):
    if len(a) == 0:
        cofactor = 1
    # Forma lenta: signo = -1 ** (fila + col)
    # Forma rápida:
    if (fila + col) % 2 == 0:
        signo = 1
    else:
        signo = -1
    aux = reduceMat(a, fila, col)
    cofactor = signo * determinante(aux)
    return cofactor

# 8. Remueve fila y columna específica de A
def reduceMat(a: list, fila, col):
    n = len(a)
    aux = a

    obj = fila + 1
    i = obj
    for i in range(n):
        for j in range(n):
            aux[i - 1][j] = aux[i][j]

    obj = col + 1
    j = obj
    for j in range(n):
        for i in range(n):
            aux[i][j - 1] = aux[i][j]

    aux = reducir(aux)
    reducida = aux
    return reducida


def determinante():
    pass

def matxEscalar():
    pass

def inversaMat():
    pass

def numeroDeDim():
    pass

def gauss():
    pass
