# Ejercicio 2 | Unidad 2

# Leer números
num1 = eval(input("Ingrese un número: "))
num2 = eval(input("Ingrese otro número: "))
num3 = eval(input("Ingrese otro número: "))

# Positivos
if num1 > 0:
    print(f"{num1} es positivo")

if num2 > 0:
    print(f"{num2} es positivo")

if num3 > 0:
    print(f"{num3} es positivo")

# Negativos
if num1 < 0:
    print(f"{num1} es negativo")

if num2 < 0:
    print(f"{num2} es negativo")

if num3 < 0:
    print(f"{num3} es negativo")

# Ceros
if num1 == 0:
    print(f"{num1} es un cero\n")

if num2 == 0:
    print(f"{num2} es un cero\n")

if num3 == 0:
    print(f"{num3} es un cero\n")

# Resultados
print(f"{num1 = }")
print(f"{num2 = }")
print(f"{num3 = }")
