# Ejercicio 4
import random

# Variables:
primera_infancia_niños = 0
primera_infancia_niñas = 0
cantidad_niños = 0
cantidad_niñas = 0

# Preguntar la cantidad de personas:
cantidad_personas = random.randrange(2,21,1)

# Ciclo:
for i in range(cantidad_personas):
    # Sexo:
    sexo = random.randrange(1,3,1)
    # Edad:
    edad = random.randrange(1,18)

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
print("1) Porcentaje de niños (0 - 17 años): ", round(porcentajes_niños,2), "%")
print("2) Porcentaje de niñas (0 - 17 años): ", round(porcentajes_niñas,2), "%")
print("3) Porcentaje de niños primera infancia (0 - 7 años): ", round(porcentajes_primera_infancia_niños,2), "%")
print("4) Porcentaje de niñas primera infancia (0 - 7 años): ", round(porcentajes_primera_infancia_niñas,2), "%")

if porcentajes_niños > porcentajes_niñas:
    print("5) Hubo más niños que niñas...")
elif porcentajes_niños < porcentajes_niñas:
    print("5) Hubo más niñas que niños...")
else:
    print("5) Hubo la misma cantidad de niños y niñas...")