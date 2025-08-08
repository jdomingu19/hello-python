"""
continue para pasar a la siguiente iteración
break para salirse del for o while
"""

# continue
cadena = "ABCÑ123"
for i in cadena:
    if i == "Ñ":
        print("I don't like ñ")
        continue
    print(i)

frutas = ["manzana", "banana", "carro", "naranja", 231, True, "YTENEDOR"]
for i in frutas:
    if i != "manzana" and i != "banana" and i != "naranja":
        # print(f"{i} NO ES UNA FRUTA, GO TO NEXT")
        continue
    print(i)

# break
nombre = input("Ingrese su nombre: ")
for i in nombre:
    print(i)
    if i == "ñ" or i == "Ñ":
        print("¡Su nombre tiene eñes!")
        break


# Ejemplo de validación de datos
numero = eval(input("Ingrese el número 32: "))
while numero != 32:
    if numero == 64:
        print("No es 32, pero te lo dejo pasar")
        break # Se sale

    print("Número incorrecto...")
    numero = eval(input("Ingrese el número 32 nuevamente: "))
