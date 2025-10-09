# Ejercicio A
n = int(input("Ingrese el valor de n: "))
m = int(input("Ingrese el valor de m: "))

numerador = 0
for k in range(2,11):
    numerador = numerador + k + 3

denominador = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        denominador = denominador + i + j

x = numerador / denominador

print("Numerador:", numerador)
print("Denominador:", denominador)
print("x:", x)