# Ejercicio 2
n = eval(input("Ingrese valor de n: "))

sueldos = []
i = 1
while i <= n:
    sueldo = eval(input("Ingrese sueldo ($200 - $1000): "))
    sueldos.append(sueldo)
    i = i + 1

cont_1 = 0
cont_2 = 0
i = 0
while i < len(sueldos):
    if sueldos[i] >= 200 and sueldos[i] <= 500:
        cont_1 = cont_1 + 1
    if sueldos[i] > 500:
        cont_2 = cont_2 + 1
    i = i + 1

print("Sueldos entre $200 y $500:", cont_1)
print("Sueldos mayores que $500:", cont_2)