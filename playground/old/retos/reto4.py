# Detector de diabetes | RETO 4

"""
Añadir info de términos y propósito
"""

print("- - DETECTOR DE DIABETES | RETO 4 - -")

# Crear vector categorías:
categorias = ["Hipoglusemia", "Sin diabetes", "Prediabetes", "Diabetes"]

# Cantidad de pacientes:
cantidad_pacientes = 10

# Contadores:
cantidad_hipoglusemia = 0
cantidad_sin_diabetes = 0
cantidad_prediabetes = 0
cantidad_diabetes = 0

# Ciclo:
i = 1
while i <= cantidad_pacientes:
    # 1) ¿En ayunas?
    en_ayunas = eval(input(f"¿El paciente {i} se encuentra en ayunas? 1) Sí 2) No: "))
   
    # Validaciones cuando paciente está en ayuno
    if en_ayunas == 1:

        # 2) Glucosa en sangre (mg/dl)
        nivel_glucosa = eval(input(f"Ingrese el nivel de glucosa del paciente {i} (mg/dl): "))

        if nivel_glucosa < 70:
            cantidad_hipoglusemia = cantidad_hipoglusemia + 1
            print(f"El paciente {i} es categorizado como: {categorias[0]}")
            print("- - - - - - -")
            i = i + 1

        elif nivel_glucosa >= 70 and nivel_glucosa < 100:
            cantidad_sin_diabetes = cantidad_sin_diabetes + 1
            print(f"El paciente {i} es categorizado como: {categorias[1]}")
            print("- - - - - - -")
            i = i + 1

        elif nivel_glucosa >= 100 and nivel_glucosa < 125:
            cantidad_prediabetes = cantidad_prediabetes + 1
            print(f"El paciente {i} es categorizado como: {categorias[2]}")
            print("- - - - - - -")
            i = i + 1

        else:
            cantidad_diabetes = cantidad_diabetes + 1
            print(f"El paciente {i} es categorizado como: {categorias[3]}")
            print("- - - - - - -")
            i = i + 1

    # Validaciones cuando paciente no está en ayuno
    elif en_ayunas == 2:
        
        # 2) Glucosa en sangre (mg/dl)
        nivel_glucosa = eval(input(f"Ingrese el nivel de glucosa del paciente {i} (mg/dl): "))


        if nivel_glucosa < 140:
            cantidad_sin_diabetes = cantidad_sin_diabetes + 1
            print(f"El paciente {i} es categorizado como: {categorias[1]}")
            print("- - - - - - -")
            i = i + 1

        elif nivel_glucosa >= 140 and nivel_glucosa < 200:
            cantidad_prediabetes = cantidad_prediabetes + 1
            print(f"El paciente {i} es categorizado como: {categorias[2]}")
            print("- - - - - - -")
            i = i + 1

        else:
            cantidad_diabetes = cantidad_diabetes + 1
            print(f"El paciente {i} es categorizado como: {categorias[3]}")
            print("- - - - - - -")
            i = i + 1

    # En caso de ingresar un estado de ayuno no válido
    else:
        print("Datos ingresados no válidos...")
        print("- - - - - - -")

# Mostrar resultados:
print("RESULTADOS")
print(f"Cantidad de pacientes con hipoglusemia: {cantidad_hipoglusemia}")
print(f"Cantidad de pacientes sin diabetes: {cantidad_sin_diabetes}")
print(f"Cantidad de pacientes con prediabetes: {cantidad_prediabetes}")
print(f"Cantidad de pacientes con diabetes: {cantidad_diabetes}")