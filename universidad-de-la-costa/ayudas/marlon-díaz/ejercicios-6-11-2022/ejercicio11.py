# Ejercicio 11

num1 = eval(input("Ingrese num1: "))
num2 = eval(input("Ingrese num2: "))

if num1 > num2:
    print("num2 debe ser mayor que num1")

i = num1
while i <= num2:
    if i % 2 == 0:
        print(i)
    i = i + 1