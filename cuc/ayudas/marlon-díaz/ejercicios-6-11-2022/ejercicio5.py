# Ejercicio 5
numero = input("Ingrese un número entre 1 y 10000: ")

if int(numero) < 0 or int(numero) > 10000:
    print("Número incorrecto...")
else:
    i = 0
    while i < len(numero):
        i = i + 1
    print(numero, "tiene", i, "dígitos")