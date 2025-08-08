# Ejercicio 2

"""
- Tres asignaturas
- Cada una con tres cortes
- Definamos tres notas por corte
"""

# - - - Asignatura 1 - - -

# Corte 1
print("ASIGNATURA 1")
nota_1 = eval(input("Ingrese nota 1 (corte 1): "))
nota_2 = eval(input("Ingrese nota 2 (corte 1): "))
nota_3 = eval(input("Ingrese nota 3 (corte 1): "))

nota_corte_1_a1 = (nota_1 + nota_2 + nota_3) / 3

# Corte 2
print("")
nota_1 = eval(input("Ingrese nota 1 (corte 2): "))
nota_2 = eval(input("Ingrese nota 2 (corte 2): "))
nota_3 = eval(input("Ingrese nota 3 (corte 2): "))

nota_corte_2_a1 = (nota_1 + nota_2 + nota_3) / 3

# Corte 3
print("")
nota_1 = eval(input("Ingrese nota 1 (corte 3): "))
nota_2 = eval(input("Ingrese nota 2 (corte 3): "))
nota_3 = eval(input("Ingrese nota 3 (corte 3): "))

nota_corte_3_a1 = (nota_1 + nota_2 + nota_3) / 3

# - - - Asignatura 2 - - -
print("")
print("ASIGNATURA 2")

# Corte 1
nota_1 = eval(input("Ingrese nota 1 (corte 1): "))
nota_2 = eval(input("Ingrese nota 2 (corte 1): "))
nota_3 = eval(input("Ingrese nota 3 (corte 1): "))

nota_corte_1_a2 = (nota_1 + nota_2 + nota_3) / 3

# Corte 2
print("")
nota_1 = eval(input("Ingrese nota 1 (corte 2): "))
nota_2 = eval(input("Ingrese nota 2 (corte 2): "))
nota_3 = eval(input("Ingrese nota 3 (corte 2): "))

nota_corte_2_a2 = (nota_1 + nota_2 + nota_3) / 3

# Corte 3
print("")
nota_1 = eval(input("Ingrese nota 1 (corte 3): "))
nota_2 = eval(input("Ingrese nota 2 (corte 3): "))
nota_3 = eval(input("Ingrese nota 3 (corte 3): "))

nota_corte_3_a2 = (nota_1 + nota_2 + nota_3) / 3

# - - - Asignatura 3 - - -
print("")
print("ASIGNATURA 3")

# Corte 1
nota_1 = eval(input("Ingrese nota 1 (corte 1): "))
nota_2 = eval(input("Ingrese nota 2 (corte 1): "))
nota_3 = eval(input("Ingrese nota 3 (corte 1): "))

nota_corte_1_a3 = (nota_1 + nota_2 + nota_3) / 3

# Corte 2
print("")
nota_1 = eval(input("Ingrese nota 1 (corte 2): "))
nota_2 = eval(input("Ingrese nota 2 (corte 2): "))
nota_3 = eval(input("Ingrese nota 3 (corte 2): "))

nota_corte_2_a3 = (nota_1 + nota_2 + nota_3) / 3

# Corte 3
print("")
nota_1 = eval(input("Ingrese nota 1 (corte 3): "))
nota_2 = eval(input("Ingrese nota 2 (corte 3): "))
nota_3 = eval(input("Ingrese nota 3 (corte 3): "))

nota_corte_3_a3 = (nota_1 + nota_2 + nota_3) / 3

# Mostrar sus resultados
print("")
print("RESULTADOS")

print("Asignatura 1 - Corte 1:", round(nota_corte_1_a1, 2))
print("Asignatura 1 - Corte 2:", round(nota_corte_2_a1, 2))
print("Asignatura 1 - Corte 3:", round(nota_corte_3_a1, 2))
nota_final_a1 = (nota_corte_1_a1 + nota_corte_2_a1 + nota_corte_3_a1) / 3

# Aprobó o desaprobó
if nota_final_a1 < 3:
    print("Nota final asignatura 1:", round(nota_final_a1, 2))
    print("El estudiante reprobó la asignatura 1...")
else:
    print("Nota final asignatura 1:", round(nota_final_a1, 2))
    print("¡El estudiante aprobó la asignatura 1!")

# Corte mayor
if nota_corte_1_a1 > nota_corte_2_a1 and nota_corte_1_a1 > nota_corte_3_a1:
    print("Su corte mayor fue el primero")
elif nota_corte_2_a1 > nota_corte_1_a2 and nota_corte_2_a1 > nota_corte_3_a1:
    print("Su corte mayor fue el segundo")
elif nota_corte_3_a1 > nota_corte_1_a2 and nota_corte_3_a1 > nota_corte_2_a1:
    print("Su corte mayor fue el tercero")
else:
    print("No hay corte mayor")

# Corte menor
if nota_corte_1_a1 < nota_corte_2_a1 and nota_corte_1_a1 < nota_corte_3_a1:
    print("Su corte menor fue el primero")
elif nota_corte_2_a1 < nota_corte_1_a2 and nota_corte_2_a1 < nota_corte_3_a1:
    print("Su corte menor fue el segundo")
elif nota_corte_3_a1 < nota_corte_1_a2 and nota_corte_3_a1 < nota_corte_2_a1:
    print("Su corte menor fue el tercero")
else:
    print("No hay corte menor")

print("")

print("Asignatura 2 - Corte 1:", round(nota_corte_1_a2, 2))
print("Asignatura 2 - Corte 2:", round(nota_corte_2_a2, 2))
print("Asignatura 2 - Corte 3:", round(nota_corte_3_a2, 2))
nota_final_a2 = (nota_corte_1_a2 + nota_corte_2_a2 + nota_corte_3_a2) / 3

if nota_final_a2 < 3:
    print("Nota final asignatura 1:", round(nota_final_a2, 2))
    print("El estudiante reprobó la asignatura 2...")
else:
    print("Nota final asignatura 1:", round(nota_final_a2, 2))
    print("¡El estudiante aprobó la asignatura 1!")

# Corte mayor
if nota_corte_1_a2 > nota_corte_2_a2 and nota_corte_1_a2 > nota_corte_3_a2:
    print("Su corte mayor fue el primero")
elif nota_corte_2_a2 > nota_corte_1_a2 and nota_corte_2_a2 > nota_corte_3_a2:
    print("Su corte mayor fue el segundo")
elif nota_corte_3_a2 > nota_corte_1_a2 and nota_corte_3_a2 > nota_corte_2_a2:
    print("Su corte mayor fue el tercero")
else:
    print("No hay corte mayor")

# Corte menor
if nota_corte_1_a2 < nota_corte_2_a2 and nota_corte_1_a2 < nota_corte_3_a2:
    print("Su corte menor fue el primero")
elif nota_corte_2_a2 < nota_corte_1_a2 and nota_corte_2_a2 < nota_corte_3_a2:
    print("Su corte menor fue el segundo")
elif nota_corte_3_a2 < nota_corte_1_a2 and nota_corte_3_a2 < nota_corte_2_a2:
    print("Su corte menor fue el tercero")
else:
    print("No hay corte menor")

print("")

print("Asignatura 3 - Corte 1:", round(nota_corte_1_a3, 2))
print("Asignatura 3 - Corte 2:", round(nota_corte_2_a3, 2))
print("Asignatura 3 - Corte 3:", round(nota_corte_3_a3, 2))
nota_final_a3 = (nota_corte_1_a3 + nota_corte_2_a3 + nota_corte_3_a3) / 3

if nota_final_a3 < 3:
    print("Nota final asignatura 1:", round(nota_final_a3, 2))
    print("El estudiante reprobó la asignatura 2...")
else:
    print("Nota final asignatura 1:", round(nota_final_a3, 2))
    print("¡El estudiante aprobó la asignatura 1!")

# Corte mayor
if nota_corte_1_a3 > nota_corte_2_a3 and nota_corte_1_a3 > nota_corte_3_a3:
    print("Su corte mayor fue el primero")
elif nota_corte_2_a3 > nota_corte_1_a2 and nota_corte_2_a3 > nota_corte_3_a3:
    print("Su corte mayor fue el segundo")
elif nota_corte_3_a3 > nota_corte_1_a2 and nota_corte_3_a3 > nota_corte_2_a3:
    print("Su corte mayor fue el tercero")
else:
    print("No hay corte mayor")

# Corte menor
if nota_corte_1_a3 < nota_corte_2_a3 and nota_corte_1_a3 < nota_corte_3_a3:
    print("Su corte menor fue el primero")
elif nota_corte_2_a3 < nota_corte_1_a2 and nota_corte_2_a3 < nota_corte_3_a3:
    print("Su corte menor fue el segundo")
elif nota_corte_3_a3 < nota_corte_1_a2 and nota_corte_3_a3 < nota_corte_2_a3:
    print("Su corte menor fue el tercero")
else:
    print("No hay corte menor")