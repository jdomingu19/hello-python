"""
if

if
else

if
elif

Operadores comparativos:
a == b -> igual
a != b -> diferente
a > b  -> mayor
a < b  -> menor
a >= b -> mayor o igual
a <= b -> menor o igual

Operadores lógicos:
and -> y
or  -> o
in  -> en
not -> no
is  -> es
"""

# == igualdad
a = 5
b = 6
if a == b:
    print(f"{a} es igual a {b}")
else:
    print(f"{a} NO es igual a {b}")

# != diferente
a = 5
b = 6
if a != b:
    print(f"{a} NO es igual a {b}")
else:
    print(f"{a} es igual a {b}")

# > mayor
a = 5
b = 6
if a > b:
    print(f"{a} es mayor a {b}")
else:
    print(f"{a} NO es mayor a {b}")

# < menor
a = 5
b = 6
if a < b:
    print(f"{a} es menor a {b}")
else:
    print(f"{a} NO es menor a {b}")

# > mayor o igual
a = 5
b = 6
if a >= b:
    print(f"{a} es mayor o igual a {b}")
else:
    print(f"{a} NO es mayor o igual a {b}")

# <= menor o igual
a = 5
b = 6
if a <= b:
    print(f"{a} es menor o igual a {b}")
else:
    print(f"{a} NO es menor o igual a {b}")

# and -> y
a = 5
b = 6
c = 7
if a < b and a < c:
    print(f"{a} es el menor de todos\n")
elif b < a and b < c:
    print(f"{b} es el menor de todos\n")
elif c < a and c < b:
    print(f"{c} es el menor de todos\n")
else:
    print("Hay números iguales\n")

# or -> o
a, b, c = 5, 6, 2
if a < b or a < c:
    print(f"{a} es menor a todos o al menos un número\n")
else:
    print(f"{a} NO es menor a NINGÚN número\n")

# in -> en
palabra = "Germán"
if "r" in palabra:
    print(f"r está en la cadena {palabra}")

numero = "32"
if "2" in numero:
    print(f"2 está en {numero}")

frutas = ["Manzana", "Peras", "Uvas"]
if "Uvas" in frutas:
    print(f"Uvas está dentro de la lista frutas: {frutas}\n")

# not -> no
palabra = "Germán"
if "ñ" not in palabra:
    print(f"ñ NO está en {palabra}")

numero = "32"
if "5" not in numero:
    print(f"5 NO está en {numero}")

frutas = ["Manzana", "Peras", "Uvas"]
if "Piña" not in frutas:
    print(f"Piñas NO está dentro de la lista frutas: {frutas}")

x = False
if x == False:
    print(f"x == False")

if not x:
    print(f"x == False")

cadena = ""
if not cadena:
    print("Cadena vacía\n")

# is -> es
a = "Germán"
if a is "Germán":
    print(f"{a} es Germán")

a = "Germán"
if a is not "Jesús":
    print(f"{a} no es Jesús")
