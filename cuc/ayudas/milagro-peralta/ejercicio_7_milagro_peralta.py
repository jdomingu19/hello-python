# Ejericio 7

# Entradas
num1 = eval(input("Ingrese número uno: "))
num2 = eval(input("Ingrese número dos: "))
num3 = eval(input("Ingrese número tres: "))

# Condiciones
if type(num1) != int:
    print("El primer número no es entero, no es posible continuar...")
elif type(num2) != int:
    print("El segundo número no es entero, no es posible continuar...")
elif type(num3) != int:
    print("El tercer número no es entero, no es posible continuar...")
else: # Es decir, todos son enteros

    # num1 es el mayor
    if num1 > num2 and num1 > num3 and num2 != num3: 
        print("El primer número es el mayor (", num1 ,")")
        if num2 > num3: # num2 el del medio
            print("El segundo número es el del medio (", num2 ,")")
            print("El tercer número es el menor (", num3 ,")")
        else: # num3 el del medio
            print("El tercer número es el del medio (", num3 ,")")
            print("El segundo número es el menor (", num2 ,")")

    # num2 es el mayor
    elif num2 > num1 and num2 > num3 and num1 != num3: 
        print("El segundo número es el mayor (", num2 ,")")
        if num1 > num3: # num1 el del medio
            print("El primer número es el del medio (", num1 ,")")
            print("El tercer número es el menor (", num3 ,")")
        else: # num3 el del medio
            print("El tercer número es el del medio (", num3 ,")")
            print("El primer número es el menor (", num1 ,")")

    # num3 es el mayor
    elif num3 > num1 and num3 > num2 and num1 != num2:
        print("El tercer número es el mayor (", num3 ,")")
        if num1 > num2: # num1 el del medio
            print("El primer número es el del medio (", num1 ,")")
            print("El segundo número es el menor (", num2 ,")")
        else: # num2 el del medio
            print("El segundo número es el del medio (", num2 ,")")
            print("El primer número es el menor (", num1 ,")")
            
    # Hay números iguales
    else:
        print("Hay números que son iguales, no es posible continuar...")