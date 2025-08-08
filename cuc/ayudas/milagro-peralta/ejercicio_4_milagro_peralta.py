# Ejericio 4

# Entradas
num1 = eval(input("Ingrese número uno: "))
num2 = eval(input("Ingrese número dos: "))
num3 = eval(input("Ingrese número tres: "))

# Condiciones
if num1 > num2 and num1 > num3:
    print("El número mayor es: ", num1)
elif num2 > num1 and num2 > num3:
    print("El número mayor es: ", num2)
elif num3 > num1 and num3 > num2:
    print("El número mayor es: ", num3)
else:
    print("Error")