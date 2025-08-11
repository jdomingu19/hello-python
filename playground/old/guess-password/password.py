password = "0021"

salir = False
while not salir:
    x = input("Adivine la contraseña de 4 dígitos (S/s = salir): ")


    if x == "s" or x =="S":
        salir = True
        break

    if len(x) > 4 or not x.isnumeric():
        print("Datos incorrectos...")
    else:
        if x == password:
            print("¡Felicidades! Ha encontrado la contraseña")
            salir = True
        else:
            contador = 0
            caracteres_usados = []
            for i in x:
                # print(i, caracteres_usados)
                if i not in caracteres_usados and i in password:
                    caracteres_usados.append(i)
                    contador = contador + 1

            caracteres_usados.clear()
            print(f"Digítos acertados: {contador}")