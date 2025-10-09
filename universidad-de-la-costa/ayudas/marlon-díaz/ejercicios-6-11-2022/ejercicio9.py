# Ejercicio 9

sumatoria = 0
contador = 0
i = 1
while i <= 100:
    if i % 2 != 0:
        print(i)
        sumatoria = sumatoria + i
        contador = contador + 1
    i = i + 1

promedio = sumatoria / contador
print("Sumatoria impares:", sumatoria)
print("Promedio impares:", promedio)