# Algortimo número 1 (if)

# Captura de información:
num1 = eval(input("Ingrese un primer número: "))
num2 = eval(input("Ingrese un segundo número: "))
num3 = eval(input("Ingrese un tercer número: "))
num4 = eval(input("Ingrese un cuarto número: "))
num5 = eval(input("Ingrese un quinto número: "))

# Condiciones:
if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print("El primer número es el mayor: ", num1)
    
if num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print("El segundo número es el mayor: ", num2)

if num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
    print("El tercero número es el mayor: ", num3)

if num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
    print("El cuarto número es el mayor: ", num4) 

if num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
    print("El quinto número es el mayor: ", num5)