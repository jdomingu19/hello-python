# Liseeth Rada

ids = []
nombres = []
parciales_1 = []
parciales_2 = []
parciales_3 = []
notas_finales = []
estados = []

while True:
    print("Menú")
    print("1. Ingresar notas")
    print("2. Mostrar notas")
    print("3. Salir")
    opc = input("-> ¿Qué desea hacer?: ")
    
    if opc == "1":
        n = int(input("-> Escriba el número de estudiantes: "))
        while n <= 0:
            print("Datos incorrectos...")
            n = int(input("-> Escriba el número de estudiantes: "))

        for i in range(n):
            id = int(input(f"-> Ingrese id estudiante {i+1}: "))
            nombre = input(f"-> Ingrese nombre estudiante {i+1}: ")

            parcial_1 = eval(input(f"-> Ingrese parcial_1 estudiante {i+1}: "))
            parcial_2 = eval(input(f"-> Ingrese parcial_2 estudiante {i+1}: "))
            parcial_3 = eval(input(f"-> Ingrese parcial_3 estudiante {i+1}: "))

            while parcial_1 < 0 or parcial_1 > 5:
                print("Nota parcial_1 incorrecta...")
                parcial_1 = eval(input(f"-> Ingrese parcial_1 estudiante {i+1}: "))

            while parcial_2 < 0 or parcial_2 > 5:
                print("Nota parcial_2 incorrecta...")
                parcial_2 = eval(input(f"-> Ingrese parcial_2 estudiante {i+1}: "))

            while parcial_3 < 0 or parcial_3 > 5:
                print("Nota parcial_3 incorrecta...")
                parcial_3 = eval(input(f"-> Ingrese parcial_3 estudiante {i+1}: "))

            nota_final = (parcial_1 + parcial_2 + parcial_3) / 3
            nota_final = round(nota_final, 2)

            if nota_final < 3.5:
                estado = "Reprobó"
            else:
                estado = "Aprobó"
            
            ids.append(id)
            nombres.append(nombre)
            parciales_1.append(parcial_1)
            parciales_2.append(parcial_2)
            parciales_3.append(parcial_3)
            notas_finales.append(nota_final)
            estados.append(estado)
            print("")

    elif opc == "2":
        for i in range(len(ids)):
            print(f"{i+1}. ID: {ids[i]} | NOMBRE: {nombres[i]} | PARCIAL 1: {parciales_1[i]} | PARCIAL 2: {parciales_2[i]} | PARCIAL 3: {parciales_3[i]} | NOTA FINAL: {notas_finales[i]} | ESTADO: {estados[i]}")
        print("")

    elif opc == "3":
        break

    else:
        print("Opción incorrecta")