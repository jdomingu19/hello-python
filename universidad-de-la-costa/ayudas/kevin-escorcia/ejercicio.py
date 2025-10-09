# Kevin Escorcia

# Captura de datos:
num1 = eval(input("Ingrese número 1: "))
num2 = eval(input("Ingrese número 2: "))
num3 = eval(input("Ingrese número 3: "))
num4 = eval(input("Ingrese número 4: "))
num5 = eval(input("Ingrese número 5: "))
num6 = eval(input("Ingrese número 6: "))
num7 = eval(input("Ingrese número 7: "))
num8 = eval(input("Ingrese número 8: "))
num9 = eval(input("Ingrese número 9: "))
num10 = -99

# Condiciones
if num1 == 0 or num2 == 0 or num3 == 0 or num4 == 0 or num5 == 0 or num6 == 0 or num7 == 0 or num8 == 0 or num9 == 0 or num10 == 0:
    print("Datos no validos...")
    print("Deben ser números diferentes de 0...")
else:
    # Número mayor
    if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5 and num1 > num6 and num1 > num7 and num1 > num8 and num1 > num9 and num1 > num10:
        print("El número mayor es: ", num1)
    elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5 and num2 > num6 and num2 > num7 and num2 > num8 and num2 > num9 and num2 > num10:
        print("El número mayor es: ", num2)
    elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5 and num3 > num6 and num3 > num7 and num3 > num8 and num3 > num9 and num3 > num10:
        print("El número mayor es: ", num3)
    elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5 and num4 > num6 and num4 > num7 and num4 > num8 and num4 > num9 and num4 > num10:
        print("El número mayor es: ", num4)
    elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4 and num5 > num6 and num5 > num7 and num5 > num8 and num5 > num9 and num5 > num10:
        print("El número mayor es: ", num5)
    elif num6 > num1 and num6 > num2 and num6 > num3 and num6 > num4 and num6 > num5 and num6 > num7 and num6 > num8 and num6 > num9 and num6 > num10:
        print("El número mayor es: ", num6)
    elif num7 > num1 and num7 > num2 and num7 > num3 and num7 > num4 and num7 > num5 and num7 > num6 and num7 > num8 and num7 > num9 and num7 > num10:
        print("El número mayor es: ", num7)
    elif num8 > num1 and num8 > num2 and num8 > num3 and num8 > num4 and num8 > num5 and num8 > num6 and num8 > num7 and num8 > num9 and num8 > num10:
        print("El número mayor es: ", num8)
    elif num9 > num1 and num9 > num2 and num9 > num3 and num9 > num4 and num9 > num5 and num9 > num6 and num9 > num7 and num9 > num8 and num9 > num10:
        print("El número mayor es: ", num9)
    elif num10 > num1 and num10 > num2 and num10 > num3 and num10 > num4 and num10 > num5 and num10 > num6 and num10 > num7 and num10 > num8 and num10 > num9:
        print("El número mayor es: ", num10)
    
    # Números pares
    print("")
    sumaNumPares = 0
    cantidadNumPares = 0

    if abs(num1) % 2 == 0:
        print(num1, " es un número par")
        sumaNumPares = sumaNumPares + num1
        cantidadNumPares = cantidadNumPares + 1
    if abs(num2) % 2 == 0:
        print(num2, " es un número par")
        sumaNumPares = sumaNumPares + num2
        cantidadNumPares = cantidadNumPares + 1
    if abs(num3) % 2 == 0:
        print(num3, " es un número par")
        sumaNumPares = sumaNumPares + num3
        cantidadNumPares = cantidadNumPares + 1
    if abs(num4) % 2 == 0:
        print(num4, " es un número par")
        sumaNumPares = sumaNumPares + num4
        cantidadNumPares = cantidadNumPares + 1
    if abs(num5) % 2 == 0:
        print(num5, " es un número par")
        sumaNumPares = sumaNumPares + num5
        cantidadNumPares = cantidadNumPares + 1
    if abs(num6) % 2 == 0:
        print(num6, " es un número par")
        sumaNumPares = sumaNumPares + num6
        cantidadNumPares = cantidadNumPares + 1
    if abs(num7) % 2 == 0:
        print(num7, " es un número par")
        sumaNumPares = sumaNumPares + num7
        cantidadNumPares = cantidadNumPares + 1
    if abs(num8) % 2 == 0:
        print(num8, " es un número par")
        sumaNumPares = sumaNumPares + num8
        cantidadNumPares = cantidadNumPares + 1
    if abs(num9) % 2 == 0:
        print(num9, " es un número par")
        sumaNumPares = sumaNumPares + num9
        cantidadNumPares = cantidadNumPares + 1
    if abs(num10) % 2 == 0:
        print(num10, " es un número par")
        sumaNumPares = sumaNumPares + num10
        cantidadNumPares = cantidadNumPares + 1

    # Números impares
    print("")
    sumaNumImpares = 0
    cantidadNumImpares = 0

    if abs(num1) % 2 != 0:
        print(num1, " es un número impar")
        sumaNumImpares = sumaNumImpares + num1
        cantidadNumImpares = cantidadNumImpares + 1
    if abs(num2) % 2 != 0:
        print(num2, " es un número impar")
        sumaNumImpares = sumaNumImpares + num2
        cantidadNumImpares = cantidadNumImpares + 1
    if abs(num3) % 2 != 0:
        print(num3, " es un número impar")
        sumaNumImpares = sumaNumImpares + num3
        cantidadNumImpares = cantidadNumImpares + 1
    if abs(num4) % 2 != 0:
        print(num4, " es un número impar")
        sumaNumImpares = sumaNumImpares + num4
        cantidadNumImpares = cantidadNumImpares + 1
    if abs(num5) % 2 != 0:
        print(num5, " es un número impar")
        sumaNumImpares = sumaNumImpares + num5
        cantidadNumImpares = cantidadNumImpares + 1
    if abs(num6) % 2 != 0:
        print(num6, " es un número impar")
        sumaNumImpares = sumaNumImpares + num6
        cantidadNumImpares = cantidadNumImpares + 1
    if abs(num7) % 2 != 0:
        print(num7, " es un número impar")
        sumaNumImpares = sumaNumImpares + num7
        cantidadNumImpares = cantidadNumImpares + 1
    if abs(num8) % 2 != 0:
        print(num8, " es un número impar")
        sumaNumImpares = sumaNumImpares + num8
        cantidadNumImpares = cantidadNumImpares + 1
    if abs(num9) % 2 != 0:
        print(num9, " es un número impar")
        sumaNumImpares = sumaNumImpares + num9
        cantidadNumImpares = cantidadNumImpares + 1
    if abs(num10) % 2 != 0:
        print(num10, " es un número impar")
        sumaNumImpares = sumaNumImpares + num10
        cantidadNumImpares = cantidadNumImpares + 1

    # Suma de números pares
    print("")
    print("Suma de números pares: ", sumaNumPares)

    # Suma de números impares
    print("Suma de números impares: ", sumaNumImpares)

    # Promedio número pares
    if cantidadNumPares == 0:
        print("Promedio números pares: 0")
    else:
        promedioNumPares = round(sumaNumPares / cantidadNumPares, 2)
        print("Promedio números pares: ", promedioNumPares)

    # Promedio número impares
    if cantidadNumImpares == 0:
        print("Promedio números impares: 0")
    else:
        promedioNumImpares = round(sumaNumImpares / cantidadNumImpares,2)
        print("Promedio números impares: ", promedioNumImpares)