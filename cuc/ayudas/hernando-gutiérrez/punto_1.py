# llenar notas
notas_estudiantes = []
for i in range(15):
    nota_definitiva = eval(input("Ingrese la nota definitiva estudiante: " ))
    notas_estudiantes.append(nota_definitiva)

# promedio
suma = 0
for i in notas_estudiantes:
    suma = suma + i
if suma == 0:
    promedio = 0
else:
    promedio = suma / len(notas_estudiantes)

# cuántos ganaron
aprobaron = 0
desaprobaron = 0
for i in notas_estudiantes:
    if i >= 3.0:
        aprobaron = aprobaron + 1
    else:
        desaprobaron = desaprobaron + 1

# resultados
print("El promedio es:", promedio)
print("Estudiantes que aprobaron:", aprobaron)
print("Estudiantes que desaprobaron:", desaprobaron)
