#Entrada
horas =eval(input("Ingrese la hora de trabajo que hizo: "))

#Condicionales
if horas <= 40:
    salario = horas * 16
    print("Horas laboradas: ", horas)
    print("Salario semanal: $", salario)
else: # Es decir, horas > 40
    horasExtras = horas - 40
    horasNormales = horas - horasExtras
    salario = (horasNormales * 16) + (horasExtras * 20)
    print("Horas extras laboradas: ", horasExtras)
    print("Horas normales laboradas: ", horasNormales)
    print("Salario semanal: $", salario)