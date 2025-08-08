"""
1. If
2. If Else
3. If Elif Else

Operadores de comparación
==
!=
>
<
>=
<=

Operadores lógicos:
and -> y
or  -> o
not -> no
in  -> en
"""

"""# and
a = 10
b = 5
c = 7

if a > b and b < c and a > c:
    print("Todas las expresiones son verdaderas!")

mascota_1 = "Gato"
mascota_2 = "Gato"

if mascota_1 == "Perro" and mascota_2 == "Gato":
    print("Quiero a los dos")

# or
a = 2
b = -5

if a > 0 or b > 0:
    print("Uno o los dos son verdaderos")

nombre = input("Ingrese el nombre de la mascota: ")

if nombre == "Noah" or nombre == "Coifee":
    print("¡Es mi mascota!")
else:
    print("No es mi mascota...")"""

# in   
frutas = ["Manzana", "Banana", "Uvas", "Peras"]

nombre = input("Ingrese nombre de una fruta: ")

if nombre in frutas:
    print(f"{nombre} sí está en la lista: {frutas}")
else:
    print(f"{nombre} no está en la lista: {frutas}")