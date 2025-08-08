notas_estudiantes = []

for i in range(10):
    nota = eval(input(f"Ingrese nota del estudiante {i + 1}: "))
    notas_estudiantes.append(nota)

print(notas_estudiantes)
notas_estudiantes.sort()
print(notas_estudiantes)