password = "9900"
password_incompleta = "990"

print("Adividar la contraseña".upper())
print("Adivine el último dígito de la contraseña")
print("O ingrese 'd' para opción de descifrado")
salir = False
while salir == False:
    x = input("Ingrese un número para completar la contraseña " + password_incompleta + "*: ").lower()

    if x == "d":
        for i in range(10):
            y = password_incompleta + str(i)
            if y == password:
                print("La contraseña era", password)
                salir = True

    elif password_incompleta + x == password:
        print("Felicidades, ha encontrado la contraseña (" + password + ")")
        salir = True

    else:
        print("Incorrecto...")