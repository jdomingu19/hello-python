import time

# Forma 1
while True:
    print("Menú 1".center(16, "="))
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    opc = input("¿Qué desea hacer?: ")

    if opc == "1":
        num1 = eval(input("Num1: "))
        num2 = eval(input("Num2: "))
        print(f"{num1} + {num2} = {num1 + num2}")

    elif opc == "2":
        num1 = eval(input("Num1: "))
        num2 = eval(input("Num2: "))
        print(f"{num1} - {num2} = {num1 - num2}")

    elif opc == "3":
        break

    else:
        print("Opción incorrecta...")

    time.sleep(3)

# Forma 2
salir = False
while salir == False:
    print("Menú 2".center(16, "="), "\n1. Sumar\n2. Restar\n3. Salir")
    opc = input("¿Qué desea hacer?: ")

    if opc == "1":
        num1 = eval(input("Num1: "))
        num2 = eval(input("Num2: "))
        print(f"{num1} + {num2} = {num1 + num2}")

    elif opc == "2":
        num1 = eval(input("Num1: "))
        num2 = eval(input("Num2: "))
        print(f"{num1} - {num2} = {num1 - num2}")

    elif opc == "3":
        salir = True

    else:
        print("Opción incorrecta...")

    time.sleep(3)