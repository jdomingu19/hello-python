# ejercicio 4

# crear matriz
matriz = []

# [[nota1, nota2 ... , nota6], [nota1, nota2 ... , nota6], ...]

# leer cantidad de grupos
m = int(input("Ingrese la cantidad de grupos de estudiantes (m): "))

# llenar matriz
print("")
for i in range(m):
    matriz.append([])
    for j in range(6):
        x = eval(input(f"Ingrese la nota materia {j+1} del estudiante {i+1}: "))
        matriz[i].append(x)
    print("")

# a. la nota promedio de cada estudiante
sumatoria = 0
# cambiar estudiante
for i in range(m): 
    # recorrer sus notas
    for j in range(6): 
        # sumar sus notas
        sumatoria = sumatoria + matriz[i][j] 

    # calcular y mostrar 
    promedio = round(sumatoria / 6, 2)
    print(f"Nota promedio del estudiante {i+1}: {promedio}")

    # restablecer variables
    sumatoria = 0
    promedio = 0

# b. número de estudiantes que aprobaron cada materia
notas_materia_1 = []
notas_materia_2 = []
notas_materia_3 = []
notas_materia_4 = []
notas_materia_5 = []
notas_materia_6 = []

# cambiar estudiante
for i in range(m): 
    # recorrer sus notas
    for j in range(6):

        if j == 0:
            notas_materia_1.append(matriz[i][j])
        if j == 1:
            notas_materia_2.append(matriz[i][j])
        if j == 2:
            notas_materia_3.append(matriz[i][j])
        if j == 3:
            notas_materia_4.append(matriz[i][j])
        if j == 4:
            notas_materia_5.append(matriz[i][j])
        if j == 5:
            notas_materia_6.append(matriz[i][j])

# b. número estudiante que aprobaron cada materia
print("")
contador = 0
for i in range(len(notas_materia_1)):
    if notas_materia_1[i] >= 3:
        contador = contador + 1
print(f"Aprobados materia 1: {contador}")

contador = 0
for i in range(len(notas_materia_2)):
    if notas_materia_2[i] >= 3:
        contador = contador + 1
print(f"Aprobados materia 2: {contador}")

contador = 0
for i in range(len(notas_materia_3)):
    if notas_materia_3[i] >= 3:
        contador = contador + 1
print(f"Aprobados materia 3: {contador}")

contador = 0
for i in range(len(notas_materia_4)):
    if notas_materia_4[i] >= 3:
        contador = contador + 1
print(f"Aprobados materia 4: {contador}")

contador = 0
for i in range(len(notas_materia_5)):
    if notas_materia_5[i] >= 3:
        contador = contador + 1
print(f"Aprobados materia 5: {contador}")

contador = 0
for i in range(len(notas_materia_6)):
    if notas_materia_6[i] >= 3:
        contador = contador + 1
print(f"Aprobados materia 6: {contador}")

# c. número estudiante que desaprobaron cada materia
print("")
contador = 0
for i in range(len(notas_materia_1)):
    if notas_materia_1[i] < 3:
        contador = contador + 1
print(f"Desaprobados materia 1: {contador}")

contador = 0
for i in range(len(notas_materia_2)):
    if notas_materia_2[i] < 3:
        contador = contador + 1
print(f"Desaprobados materia 2: {contador}")

contador = 0
for i in range(len(notas_materia_3)):
    if notas_materia_3[i] < 3:
        contador = contador + 1
print(f"Desaprobados materia 3: {contador}")

contador = 0
for i in range(len(notas_materia_4)):
    if notas_materia_4[i] < 3:
        contador = contador + 1
print(f"Desaprobados materia 4: {contador}")

contador = 0
for i in range(len(notas_materia_5)):
    if notas_materia_5[i] < 3:
        contador = contador + 1
print(f"Desaprobados materia 5: {contador}")

contador = 0
for i in range(len(notas_materia_6)):
    if notas_materia_6[i] < 3:
        contador = contador + 1
print(f"Desaprobados materia 6: {contador}")

# d. nota promedio cada materia
print("")
suma = 0
for i in range(len(notas_materia_1)):
    suma = suma + notas_materia_1[i]
promedio = suma / len(notas_materia_1)
print(f"Promedio materia 1: {promedio}")

suma = 0
for i in range(len(notas_materia_2)):
    suma = suma + notas_materia_2[i]
promedio = suma / len(notas_materia_2)
print(f"Promedio materia 2: {promedio}")

suma = 0
for i in range(len(notas_materia_3)):
    suma = suma + notas_materia_3[i]
promedio = suma / len(notas_materia_3)
print(f"Promedio materia 3: {promedio}")

suma = 0
for i in range(len(notas_materia_4)):
    suma = suma + notas_materia_4[i]
promedio = suma / len(notas_materia_4)
print(f"Promedio materia 4: {promedio}")

suma = 0
for i in range(len(notas_materia_5)):
    suma = suma + notas_materia_5[i]
promedio = suma / len(notas_materia_5)
print(f"Promedio materia 5: {promedio}")

suma = 0
for i in range(len(notas_materia_6)):
    suma = suma + notas_materia_6[i]
promedio = suma / len(notas_materia_6)
print(f"Promedio materia 6: {promedio}")