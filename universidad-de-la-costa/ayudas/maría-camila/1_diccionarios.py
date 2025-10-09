# 1. Crear diccionario
datos = {}
print(type(datos), datos)

# 2. Menú
while True:
    print("1. Ingresar notas\n2. Mostrar notas\n3. Salir")
    menu = input("¿Qué desea hacer?: ")

    # 3. Ingresar notas
    if menu == "1":
        num_estudiantes = input("Ingrese número de estudiantes: ")
        while not num_estudiantes.isnumeric() or int(num_estudiantes) <= 0:
            print("Datos no válidos...")
            num_estudiantes = input("Ingrese número de estudiantes: ")

        for i in range(int(num_estudiantes)):
            id = i + 1
            nombre = input(f"Ingrese nombre estudiante {i + 1}: ")

            parcial_1 = input(f"Ingrese nota parcial 1 (0 - 5): ")
            while not parcial_1.isnumeric() or int(parcial_1) < 0 or int(parcial_1) > 5:
                print("Nota no válida...")
                parcial_1 = input(f"Ingrese nota parcial 1 (0 - 5): ")

            parcial_2 = input(f"Ingrese nota parcial 2 (0 - 5): ")
            while not parcial_2.isnumeric() or int(parcial_2) < 0 or int(parcial_2) > 5:
                print("Nota no válida...")
                parcial_2 = input(f"Ingrese nota parcial 2 (0 - 5): ")

            parcial_3 = input(f"Ingrese nota parcial 3 (0 - 5): ")
            while not parcial_3.isnumeric() or int(parcial_3) < 0 or int(parcial_3) > 5:
                print("Nota no válida...")
                parcial_3 = input(f"Ingrese nota parcial 3 (0 - 5): ")

            nota_final = round((int(parcial_1) + int(parcial_2) + int(parcial_3)) / 3, 2)

            if nota_final < 3.5:
                estado = "Desaprobó"
            else:
                estado = "Aprobó"

            datos[id] = {
                "Nombre": nombre,
                "Parcial 1": parcial_1,
                "Parcial 2": parcial_2,
                "Parcial 3": parcial_3,
                "Nota Final": nota_final,
                "Estado": estado
            }

    # 4. Mostrar notas
    elif menu == "2":
        # print(type(datos), datos)
        for i in datos:
            print(f"ID: {i} | NOMBRE: {datos[i]['Nombre']} | Parcial 1: {datos[i]['Parcial 1']} | Parcial 2: {datos[i]['Parcial 2']} | Parcial 3: {datos[i]['Parcial 3']} | Nota Final: {datos[i]['Nota Final']} | Estado: {datos[i]['Estado']}")


    # 5. Salir
    elif menu == "3":
        break

    else:
        print("Datos no válidos...")