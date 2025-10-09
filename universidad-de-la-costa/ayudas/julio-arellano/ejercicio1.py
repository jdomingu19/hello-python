# Calficaciones de notas

# Listas para trabajar
id = []
nombres = []
parciales_1 = []
parciales_2 = []
parciales_3 = []
notas_finales = []

num_estudiantes = 0
while num_estudiantes <= 0:
    # A) Número de estudiantes
    num_estudiantes = eval(input("Ingrese la cantidad de estudiantes: "))

    # C) PARTE 1 Validar estudiantes
    if num_estudiantes <= 0:
        print("Datos no válidos...")

accion = 0
while accion != 3:
    # B) Menú
    print("- - Menú - - ")
    print("1) Ingresar la nota")
    print("2) Mostrar las notas")
    print("3) Salir")
    accion = eval(input("¿Qué desea hacer?: "))

    # Ingresar notas
    if accion == 1:
        print("- - Ingresar notas - -")

        # Ciclo nombres estudiantes:
        i = 1
        while i <= num_estudiantes:
            nombre = input(f"Ingrese el nombre del estudiante {i}: ")
            nombres.append(nombre)
            id.append(i)
            i = i + 1            

        # Ciclo parciales 1 estudiantes:
        i = 1
        while i <= num_estudiantes:
            parcial_1 = eval(input(f"Ingrese nota parcial 1 del estudiante {i}: "))
            # C) PARTE 2 Validar notas
            if parcial_1 < 0 or parcial_1 > 5:
                print("Nota no válida... (0 - 5)")
            else:
                parciales_1.append(parcial_1)
                i = i + 1
            
        # Ciclo parciales 2 estudiantes:
        i = 1
        while i <= num_estudiantes:
            parcial_2 = eval(input(f"Ingrese nota parcial 2 del estudiante {i}: "))
            # C) PARTE 2 Validar notas
            if parcial_2 < 0 or parcial_2 > 5:
                print("Nota no válida... (0 - 5)")
            else:
                parciales_2.append(parcial_2)
                i = i + 1

        # Ciclo parciales 3 estudiantes:
        i = 1
        while i <= num_estudiantes:
            parcial_3 = eval(input(f"Ingrese nota parcial 3 del estudiante {i}: "))
            # C) PARTE 2 Validar notas
            if parcial_3 < 0 or parcial_3 > 5:
                print("Nota no válida... (0 - 5)")
            else:
                parciales_3.append(parcial_3)
                i = i + 1

        # Ciclo notas finales estudiantes:
        i = 0
        while i < num_estudiantes:
            elemento = (parciales_1[i] + parciales_2[i] + parciales_3[i]) / 3
            notas_finales.append(elemento)
            i = i + 1

    # Mostrar notas
    elif accion == 2:
        print("- - Mostrar notas - -")
        i = 0
        
        if len(id) == 0:
            print("ID:", id, "Nombre:", nombres, "Parcial 1:", parciales_1, "Parcial 2:", parciales_2, "Parcial 3:", parciales_3, "Notas finales:", notas_finales)
        else:
            while i < num_estudiantes:
                print("ID:", id[i], "Nombre:", nombres[i], "Parcial 1:", parciales_1[i], "Parcial 2:", parciales_2[i], "Parcial 3:", parciales_3[i], "Notas finales:", round(notas_finales[i],2))
                i = i + 1

            print("")

            print("Estudiantes que aprobaron:")
            i = 0
            while i < num_estudiantes:
                if notas_finales[i] > 3.5:
                    print(nombres[i], f"({round(notas_finales[i],2)})")
                i = i + 1

            print("")

            print("Estudiantes que desaprobaron:")
            i = 0
            while i < num_estudiantes:
                if notas_finales[i] < 3.5:
                    print(nombres[i], f"({round(notas_finales[i],2)})")
                i = i + 1

    elif accion != 1 and accion != 2 and accion != 3:
        print("Acción no valida...")

# Despedida
print("¡Gracias por usar nuestro programa!")