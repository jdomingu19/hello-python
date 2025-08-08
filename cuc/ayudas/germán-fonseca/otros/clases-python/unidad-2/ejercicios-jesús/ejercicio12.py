# Ejercicio 12 | Unidad 2

# Leer fracción 1
numerador1 = eval(input("Ingrese numerador fracción 1: "))
denominador1 = eval(input("Ingrese denominador fracción 1: "))

# Leer fracción 2
numerador2 = eval(input("Ingrese numerador fracción 2: "))
denominador2 = eval(input("Ingrese denominador fracción 2: "))

# Validar denominadores
if denominador1 == 0 or denominador2 == 0:
    print("Datos incorrectos...")
else:
    # Homgéneas
    if denominador1 == denominador2:
        numerador_final = numerador1 + numerador2
        denominador_final = denominador1
        print(f"{numerador1} / {denominador1} = {round(numerador1 / denominador1, 2)}")
        print(f"{numerador2} / {denominador2} = {round(numerador2 / denominador2, 2)}")
        print(f"SUMA HOMOGÉNEA: {numerador_final} / {denominador_final} = {round(numerador_final / denominador_final, 2)}")

    # Heterogéneas
    else:
        numerador_final = (numerador1 * denominador2) + (denominador1 * numerador2)
        denominador_final = denominador1 * denominador2
        print(f"{numerador1} / {denominador1} = {round(numerador1 / denominador1, 2)}")
        print(f"{numerador2} / {denominador2} = {round(numerador2 / denominador2, 2)}")
        print(f"SUMA HETEROGÉNEA: {numerador_final} / {denominador_final} = {round(numerador_final / denominador_final, 2)}")
