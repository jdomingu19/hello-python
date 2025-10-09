# Ejercicio 2 | Unidad 2

# Leer números
num1 = eval(input("Ingrese un número: "))
num2 = eval(input("Ingrese otro número: "))
num3 = eval(input("Ingrese otro número: "))

# El mayor
if num1 > num2 and num1 > num3:
    mayor = num1
elif num2 > num1 and num2 > num3:
    mayor = num2
elif num3 > num1 and num3 > num2:
    mayor = num3
else:
    mayor = "Ninguno"

# El menor
if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
elif num3 < num1 and num3 < num2:
    menor = num3
else:
    menor = "Ninguno"

# Resultados
print(f"\nNúmero mayor: {mayor}")
print(f"Número menor: {menor}")
