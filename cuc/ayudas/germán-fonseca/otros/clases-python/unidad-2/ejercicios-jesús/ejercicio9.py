# Ejercicio 9 | Unidad 2

# Leer datos estudiante
nombre = input("Ingrese nombre estudiante: ")
nota_unidad1 = eval(input(f"Ingrese nota unidad 1 de {nombre}: "))
nota_unidad2 = eval(input(f"Ingrese nota unidad 2 de {nombre}: "))
nota_unidad3 = eval(input(f"Ingrese nota unidad 3 de {nombre}: "))

# Validar notas
if nota_unidad1 < 0 or nota_unidad1 > 5:
    print("Nota unidad 1 incorrecta...")

elif nota_unidad2 < 0 or nota_unidad2 > 5:
    print("Nota unidad 2 incorrecta...")

elif nota_unidad3 < 0 or nota_unidad1 > 5:
    print("Nota unidad 3 incorrecta...")

else: # Todas están buenas
    promedio = (nota_unidad1 + nota_unidad2 + nota_unidad3) / 3
    promedio = round(promedio, 2)
    if promedio >= 3.3:
        print(f"¡{nombre} aprobó! Promedio: {promedio}")
    else:
        print(f"{nombre} desaprobó, promedio: {promedio}...")
