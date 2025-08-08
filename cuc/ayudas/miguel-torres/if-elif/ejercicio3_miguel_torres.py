# Nombre: Miguel Angel Torres Salgado, Universidad De La Costa

# Entradas:
num1 = eval(input("Ingrese un primer número: "))
num2 = eval(input("Ingrese un segundo número: "))
num3 = eval(input("Ingrese un tercer número: "))
num4 = eval(input("Ingrese un cuarto número: "))
num5 = eval(input("Ingrese un quinto número: "))

# Condiciones:
if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
    print("El primer número es el número mayor: ", num1)
elif num2 > num3 and num2 > num4 and num2 > num5:  
    print("El segundo número es el número mayor: ", num2)
elif num3 > num4 and num3 > num5:
    print("El tercero número es el número mayor: ", num3)
elif num4 > num5:
    print("El cuarto es el número número mayor: ", num4) 
else:
    print("El quinto número es el número mayor: ", num5)