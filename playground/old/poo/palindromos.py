def menu():
    x = "PALÍNDROMOS | 1.0\n1. Sencible\n2. No sencible"
    print(x)
    accion = input(">>>")
    while not accion.isnumeric() or int(accion) < 1 or int(accion) > 2:
        print("Datos incorrectos")
        accion = input(">>>")

    if accion == "1":
        cadena = input("Ingrese la cadena: ")
        if cadena == cadena[::-1]:
            print(f"{cadena} es una cadena palíndroma")
            print(f"{cadena} = {cadena[::-1]}")
        else:
            print(f"{cadena} no es una cadena palíndromo")
            print(f"{cadena} != {cadena[::-1]}")
    if accion == "2":
        cadena = input("Ingrese la cadena: ")
        cadena = cadena.lower()
        if cadena == cadena[::-1]:
            print(f"{cadena} es una cadena palíndroma")
            print(f"{cadena} = {cadena[::-1]}")
            print(f"{cadena.upper()} = {cadena.upper()[::-1]}")          
        else:
            print(f"{cadena} no es una cadena palíndromo")
            print(f"{cadena} != {cadena[::-1]}")
            print(f"{cadena.upper()} !=S {cadena.upper()[::-1]}")

menu()