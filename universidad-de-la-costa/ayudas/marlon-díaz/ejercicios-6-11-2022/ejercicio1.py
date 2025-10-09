# Ejercicio 1
n = eval(input("Ingrese valor de n: "))

alturas = []
i = 1
while i <= n:
    altura = eval(input("Ingrese la altura (metros): "))
    alturas.append(altura)
    i = i + 1

acumulador = 0
i = 0
while i < len(alturas):
    acumulador = acumulador + alturas[i]
    i = i + 1
promedio = acumulador / len(alturas)

mas_alta = alturas[0]
mas_baja = alturas[0]
i = 0
while i < len(alturas):
    if alturas[i] > mas_alta:
        mas_alta = alturas[i]
    if alturas[i] < mas_baja:
        mas_baja = alturas[i]
    i = i + 1

print("Promedio:", promedio)
print("Más alta:", mas_alta)
print("Más baja:", mas_baja)