x = {
    "localidad 1" : 5000,
    "localidad 2" : 10000,
    "localidad 3" : 15000,
    "localidad 4" : 20000,
    "localidad 5" : 25000
}

kilos = eval(input("Ingrese número de kilos: "))

if kilos < 0:
    print("Datos incorrecto")
else:
    localidad = input("Ingrese la localidad: ")
    localidad = localidad.lower()

    if localidad not in x:
        print("Localidad ingresada no válida...")
    else:
        total = x[localidad] * kilos
        print(f"Total a pagar: ${total}")
