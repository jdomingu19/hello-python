# Ejercicio 8 | Unidad 2

# Leer datos persona
nombre = input("Ingrese nombre persona: ")
edad = int(input(f"Ingrese la edad de {nombre}: "))
genero = int(input(f"Ingrese la genero de {nombre} 1 = Hombre, 2 = Mujer: "))

# Hombres
if genero == 1 and edad >= 18:
    print(f"¡{nombre} puede votar! HOMBRE")

# Mujeres
elif genero == 2 and edad >= 21:
    print(f"¡{nombre} puede votar! MUJER")

# Validar
else:
    print(f"{nombre} no puede votar...")
