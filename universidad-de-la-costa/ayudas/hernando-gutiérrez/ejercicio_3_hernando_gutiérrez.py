# Ejercicio 3

# Variables:
primera_infancia_niños = 0
primera_infancia_niñas = 0
cantidad_niños = 0
cantidad_niñas = 0

# Preguntar la cantidad de personas:
cantidad_personas = eval(input("Ingrese la cantidad de personas: "))

# Ciclo:
for i in range(cantidad_personas):
    # Sexo:
    sexo = eval(input(f"Ingrese el sexo de la persona número {i+1} (1 = Niño 2 = Niña): "))
    # Edad:
    edad = eval(input(f"Ingrese la edad de la persona número {i+1} (0 a 17 años): "))

    # Niños:
    if sexo == 1:
        if edad <= 7:
            primera_infancia_niños = primera_infancia_niños + 1
            cantidad_niños = cantidad_niños + 1
        else:
            cantidad_niños = cantidad_niños + 1

    # Niñas:
    if sexo == 2:
        if edad <= 7:
            primera_infancia_niñas = primera_infancia_niñas + 1
            cantidad_niñas = cantidad_niñas + 1
        else:
            cantidad_niñas = cantidad_niñas + 1

# Porcentajes:
porcentajes_niños = (cantidad_niños / cantidad_personas) * 100
porcentajes_niñas = (cantidad_niñas / cantidad_personas) * 100

porcentajes_primera_infancia_niños = (primera_infancia_niños / cantidad_personas) * 100
porcentajes_primera_infancia_niñas = (primera_infancia_niñas / cantidad_personas) * 100

# Salidas:
print("- - RESULTADOS - -")
print("1) Porcentaje de niños (0 - 17 años): ", porcentajes_niños, "%")
print("2) Porcentaje de niñas (0 - 17 años): ", porcentajes_niñas, "%")
print("3) Porcentaje de niños primera infancia (0 - 7 años): ", porcentajes_primera_infancia_niños, "%")
print("4) Porcentaje de niñas primera infancia (0 - 7 años): ", porcentajes_primera_infancia_niñas, "%")

if porcentajes_niños > porcentajes_niñas:
    print("5) Hubo más niños que niñas...")
elif porcentajes_niños < porcentajes_niñas:
    print("5) Hubo más niñas que niños...")
else:
    print("5) Hubo la misma cantidad de niños y niñas...")