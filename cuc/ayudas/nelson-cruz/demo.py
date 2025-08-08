# Ejercicio

codigo = input("Ingrese el código MMAAARR: ")
mes = int(codigo[0:2])
año = int(codigo[2:6])
region = codigo[6:8]

codigo = str(mes) + str(año) + str(region)
print("Usuario:", codigo)

if region == "CA":
    codigo = str(mes) + "-" + str(año) + "-" + "Caribe"
    print("El código ingresado es: ", codigo)

    año = año + 8
    if mes > 12:
        año = año + 1
        mes = mes - 13
        
    codigo = str(mes) + "-" + str(año) + "-" + "Caribe"
    print("Fecha vencimiento: ", codigo)
    

if region == "AN":
    codigo = str(mes) + "-" + str(año) + "-" + "Andina"
    print(codigo)

    año = año + 7
    mes = mes + 6
    if mes > 12:
        año = año + 1
        mes = mes - 13

    codigo = str(mes) + "-" + str(año) + "-" + "Andina"
    print("Fecha vencimiento: ", codigo)

if region == "PA":
    codigo = str(mes) + "-" + str(año) + "-" + "Pacífico"
    print(codigo)
    
    año = año + 8
    if mes > 12:
        año = año + 1
        mes = mes - 13

    codigo = str(mes) + "-" + str(año) + "-" + "Pacífico"
    print("Fecha vencimiento: ", codigo)

if region == "OR":
    codigo = str(mes) + "-" + str(año) + "-" + "Orinoquía"
    print(codigo)

    año = año + 6
    mes = mes + 6
    if mes > 12:
        año = año + 1
        mes = mes - 13

    codigo = str(mes) + "-" + str(año) + "-" + "Orinoquía"
    print("Fecha vencimiento: ", codigo)

if region == "AM":
    codigo = str(mes) + "-" + str(año) + "-" + "Amazonía"
    print(codigo)

    año = año + 7
    if mes > 12:
        año = año + 1
        mes = mes - 13

    codigo = str(mes) + "-" + str(año) + "-" + "Amazonía"
    print("Fecha vencimiento: ", codigo)