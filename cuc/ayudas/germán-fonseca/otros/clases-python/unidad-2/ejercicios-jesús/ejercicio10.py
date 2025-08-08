# Ejercicio 10 | Unidad 2

# Leer peso
peso = eval(input("Ingrese el peso del paquete (kg): "))

# Validar peso
if peso <= 0 or peso > 20:
    print("Datos incorrectos...")

else:
    if peso < 5:
        print(f"El valor del paquete es $1500 ({peso} kg)")

    if peso >= 5 and peso <= 10:
        print(f"El valor del paquete es $2000 ({peso} kg)")
    
    if peso >= 11 and peso <= 20:
        print(f"El valor del paquete es $2500 ({peso} kg)")
