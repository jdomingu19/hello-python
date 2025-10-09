# Ejercicio 9

# Entradas
tipoAlumno = eval(input("Ingrese tipo de alumno 1) Profesional 2) Preparatoria: "))
promedioAlumno = eval(input("Ingrese el promedio del alumno (1 al 10): "))
materiasRepobradas = eval(input("Ingrese cantidad materias reprobadas: "))

# Condiciones
if promedioAlumno >= 9.5 and tipoAlumno == 2:
    unidades = 55
    subTotal = unidades * 36 # 180 / 5
    descuento = subTotal * 0.25 # 25%
    total = subTotal - descuento
    print("El alumno pagará: $", total)

elif promedioAlumno >= 9 and promedioAlumno < 9.5 and tipoAlumno == 2:
    unidades = 50
    subTotal = unidades * 36 # 180 / 5
    descuento = subTotal * 0.10 # 10%
    total = subTotal - descuento
    print("El alumno pagará: $", total)

elif promedioAlumno > 7 and promedioAlumno < 9 and tipoAlumno == 2:
    unidades = 50
    subTotal = unidades * 36 # 180 / 5
    descuento = 0
    total = subTotal - descuento
    print("El alumno pagará: $", total)

elif promedioAlumno <= 7 and materiasRepobradas >= 0 and materiasRepobradas <= 3 and tipoAlumno == 2:
    unidades = 45
    subTotal = unidades * 36 # 180 / 5
    descuento = 0
    total = subTotal - descuento
    print("El alumno pagará: $", total)

elif promedioAlumno <= 7 and materiasRepobradas >= 4 and tipoAlumno == 2:
    unidades = 40
    subTotal = unidades * 36 # 180 / 5
    descuento = 0
    total = subTotal - descuento
    print("El alumno pagará: $", total)

elif promedioAlumno >= 9.5 and tipoAlumno == 1:
    unidades = 55
    subTotal = unidades * 36 # 180 / 5
    descuento = subTotal * 0.20 # 20%
    total = subTotal - descuento
    print("El alumno pagará: $", total)

elif promedioAlumno < 9.5 and tipoAlumno == 1:
    unidades = 55
    subTotal = unidades * 36 # 180 / 5
    descuento = 0
    total = subTotal - descuento
    print("El alumno pagará: $", total)