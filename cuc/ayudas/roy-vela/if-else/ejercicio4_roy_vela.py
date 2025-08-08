# Algoritmo 4 if-else

# Captura de la información:
horas = eval(input("Ingrese horas que trabajó: "))

# Condiciones:
if horas <= 40:
    salario = horas * 16
    print("Salario de la semana: $", salario)
else:
    if horas > 40:
        horas_extras = horas - 40
        horas_normales = horas - horas_extras
        salario = (horas_normales * 16) + (horas_extras * 20)
        print("Salario de la semana: $", salario)