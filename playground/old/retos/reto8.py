# Sistema de calificaciones | RETO 8

# Funciones
def mostrarTodo():
    # Validar e imprimir
    for i in range(len(ids)):
        if notas_finales[i] >= 3.5:        
            print(f"ID: {ids[i]} | NOMBRE: {nombres[i]} | PARCIAL 1: {parciales_1[i]} | PARCIAL 2: {parciales_2[i]} | PARCIAL 3: {parciales_3[i]} | NOTA FINAL: {notas_finales[i]} | ¡APROBÓ!")
        else:        
            print(f"ID: {ids[i]} | NOMBRE: {nombres[i]} | PARCIAL 1: {parciales_1[i]} | PARCIAL 2: {parciales_2[i]} | PARCIAL 3: {parciales_3[i]} | NOTA FINAL: {notas_finales[i]} | DESAPROBÓ...")

# D) Listas
ids = []
nombres = []
parciales_1 = []
parciales_2 = []
parciales_3 = []
notas_finales = []

# B) Menú
salir = False
while not salir:
    print("- - SISTEMA DE CALIFICACIONES - -")
    print("1. Ingresar notas")
    print("2. Mostrar notas")
    print("3. Salir")

    accion = input("¿Qué desea hacer?: ")
    # print(type(accion))

    # 1) Ingresar notas
    if accion == "1":
        print("- - INGRESAR NOTAS - -")

        # Número de estudiantes
        num_estudiantes = input("Ingrese números de estudiantes: ")
        # Validar
        while not num_estudiantes.isnumeric() or num_estudiantes == "0":
            print("Datos ingresados no válidos...")
            num_estudiantes = input("Ingrese números de estudiantes: ")
        
        # Si es primera vez
        if 1 not in ids:
            i = 0
            while i < int(num_estudiantes):
                # Nombre
                mi_nombre = input(f"Ingrese nombre del estudiante {i + 1}: ")
                while mi_nombre.isspace() or not mi_nombre.isalpha():
                    print("Datos ingresados no válidos...")
                    mi_nombre = input(f"Ingrese nombre del estudiante {i + 1}: ")
                # Parcial 1
                mi_parcial_1 = input(f"Ingrese nota parcial 1 del estudiante {i + 1} ({mi_nombre}): ")
                while mi_parcial_1.isspace() or not mi_parcial_1.isnumeric() or int(mi_parcial_1) > 5:
                    print("Datos ingresados no válidos...")
                    mi_parcial_1 = input(f"Ingrese nota parcial 1 del estudiante {i + 1} ({mi_nombre}): ")
                # Parcial 2
                mi_parcial_2 = input(f"Ingrese nota parcial 2 del estudiante {i + 1} ({mi_nombre}): ")
                while mi_parcial_2.isspace() or not mi_parcial_2.isnumeric() or int(mi_parcial_2) > 5:
                    print("Datos ingresados no válidos...")
                    mi_parcial_2 = input(f"Ingrese nota parcial 2 del estudiante {i + 1} ({mi_nombre}): ")
                # Parcial 3
                mi_parcial_3 = input(f"Ingrese nota parcial 3 del estudiante {i + 1} ({mi_nombre}): ")
                while mi_parcial_3.isspace() or not mi_parcial_3.isnumeric() or int(mi_parcial_3) > 5:
                    print("Datos ingresados no válidos...")
                    mi_parcial_3 = input(f"Ingrese nota parcial 3 del estudiante {i + 1}: ({mi_nombre}): ")
                # Nota final
                mi_nota_final = (int(mi_parcial_1) + int(mi_parcial_2) + int(mi_parcial_3)) / 3
                mi_nota_final = round(mi_nota_final, 2)

                # Añadir a listas
                ids.append(i + 1)
                nombres.append(mi_nombre)
                parciales_1.append(mi_parcial_1)
                parciales_2.append(mi_parcial_2)
                parciales_3.append(mi_parcial_3)
                notas_finales.append(mi_nota_final)
                i = i + 1
                print("- - - -")

        # Si no es primera vez
        else:
            x = ids[-1]
            i = 0
            while i < int(num_estudiantes):
                # Nombre
                mi_nombre = input(f"Ingrese nombre del estudiante {x + i + 1}: ")
                while mi_nombre.isspace() or not mi_nombre.isalpha():
                    print("Datos ingresados no válidos...")
                    mi_nombre = input(f"Ingrese nombre del estudiante {x + i + 1}: ")
                # Parcial 1
                mi_parcial_1 = input(f"Ingrese nota parcial 1 del estudiante {x + i + 1} ({mi_nombre}): ")
                while mi_parcial_1.isspace() or not mi_parcial_1.isnumeric() or int(mi_parcial_1) > 5:
                    print("Datos ingresados no válidos...")
                    mi_parcial_1 = input(f"Ingrese nota parcial 1 del estudiante {x + i + 1} ({mi_nombre}): ")
                # Parcial 2
                mi_parcial_2 = input(f"Ingrese nota parcial 2 del estudiante {x + i + 1} ({mi_nombre}): ")
                while mi_parcial_2.isspace() or not mi_parcial_2.isnumeric() or int(mi_parcial_2) > 5:
                    print("Datos ingresados no válidos...")
                    mi_parcial_2 = input(f"Ingrese nota parcial 2 del estudiante {x + i + 1} ({mi_nombre}): ")
                # Parcial 3
                mi_parcial_3 = input(f"Ingrese nota parcial 3 del estudiante {x + i + 1} ({mi_nombre}): ")
                while mi_parcial_3.isspace() or not mi_parcial_3.isnumeric() or int(mi_parcial_3) > 5:
                    print("Datos ingresados no válidos...")
                    mi_parcial_3 = input(f"Ingrese nota parcial 3 del estudiante {x + i + 1} ({mi_nombre}): ")
                # Nota final
                mi_nota_final = (int(mi_parcial_1) + int(mi_parcial_2) + int(mi_parcial_3)) / 3
                mi_nota_final = round(mi_nota_final, 2)

                # Añadir a listas
                ids.append(x + i + 1)
                nombres.append(mi_nombre)
                parciales_1.append(mi_parcial_1)
                parciales_2.append(mi_parcial_2)
                parciales_3.append(mi_parcial_3)
                notas_finales.append(mi_nota_final)
                i = i + 1
                print("- - - -")

        # ¿Continuar?
        continuar = input("¿Desea continuar? 1. Sí 2. No: ")
        # Validar
        while continuar != "1" and continuar != "2":
            print("Datos ingresados no válidos...")
            continuar = input("¿Desea continuar? 1. Sí 2. No: ")
        if continuar == "2":
            salir = True

    # 2) Mostrar notas
    elif accion == "2":
        print("- - MOSTRAR NOTAS - -")
        # Validar
        if 1 not in ids:
            print("Listas vacias...")
            print("- - - -")
        else:
            mostrarTodo()
            print("- - - -")

        # ¿Continuar?
        continuar = input("¿Desea continuar? 1. Sí 2. No: ")
        # Validar
        while continuar != "1" and continuar != "2":
            print("Datos ingresados no válidos...")
            continuar = input("¿Desea continuar? 1. Sí 2. No: ")
        if continuar == "2":
            salir = True

    # 3) Salir
    elif accion == "3":
        print("3. Salir")
        salir = True

    # 4) Secreto
    elif accion == "123":
        print("- - - -")
        print("¡Encontrastes el secreto oculto!")
        salir = True

    # 5) Validar
    else:
        print("Datos ingresados no válidos")