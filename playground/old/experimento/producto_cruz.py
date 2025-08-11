# Producto cruz | Versión 1.0 | @JesúsDomínguez

# Definir vectores:
vectorA = []
vectorB = []
vectorResultante = []

# Llenar vector A:
i = 0
while i <= 2:
    coeficiente = eval(input(f"Ingrese el coeficiente A[{i}]: "))
    vectorA.append(coeficiente)
    i = i + 1

# Llenar vector B:
i = 0
while i <= 2:
    coeficiente = eval(input(f"Ingrese el coeficiente B[{i}]: "))
    vectorB.append(coeficiente)
    i = i + 1

# Matriz de coeficientes:
print("- - Matriz de coeficientes - -")
print("|", end = " ")
print("i", end = " ")
print("j", end = " ")
print("k", end = " ")
print("|")

print("|", end = " ")
print(vectorA[0], end = " ")
print(vectorA[1], end = " ")
print(vectorA[2], end = " ")
print("|")

print("|", end = " ")
print(vectorB[0], end = " ")
print(vectorB[1], end = " ")
print(vectorB[2], end = " ")
print("|")

# Hallar i:
print("- - Hallar i - -")
print("|", end = " ")
print(vectorA[1], end = " ")
print(vectorA[2], end = " ")
print("|")

print("|", end = " ")
print(vectorB[1], end = " ")
print(vectorB[2], end = " ")
print("| i =", end = " ")

print("(", vectorA[1], " * ", vectorB[2],") - (", vectorB[1], " * ", vectorA[2], ") =", end = " ")
resultadoI = (vectorA[1] * vectorB[2]) - (vectorB[1] * vectorA[2])
print(str(resultadoI) + "i")
vectorResultante.append(resultadoI)

# Hallar j:
print("- - Hallar j - -")
print("|", end = " ")
print(vectorA[0], end = " ")
print(vectorA[2], end = " ")
print("|")

print("|", end = " ")
print(vectorB[0], end = " ")
print(vectorB[2], end = " ")
print("| j =", end = " ")

print("(", vectorA[0], " * ", vectorB[2],") - (", vectorB[0], " * ", vectorA[2], ") =", end = " ")
resultadoJ = (vectorA[0] * vectorB[2]) - (vectorB[0] * vectorA[2])
print(str(resultadoJ) + "j")
vectorResultante.append(resultadoJ)

# Hallar k:
print("- - Hallar k - -")
print("|", end = " ")
print(vectorA[0], end = " ")
print(vectorA[1], end = " ")
print("|")

print("|", end = " ")
print(vectorB[0], end = " ")
print(vectorB[1], end = " ")
print("| k =", end = " ")

print("(", vectorA[0], " * ", vectorB[1],") - (", vectorB[0], " * ", vectorA[1], ") =", end = " ")
resultadoK = (vectorA[0] * vectorB[1]) - (vectorB[0] * vectorA[1])
print(str(resultadoK) + "k")
vectorResultante.append(resultadoK)

# Resultado:
print("- - RESULTADOS - -")
print("A =", vectorA)
print("B =", vectorB)
print("A x B =", vectorResultante)