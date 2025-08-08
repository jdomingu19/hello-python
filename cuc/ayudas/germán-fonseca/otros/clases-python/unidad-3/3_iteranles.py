"""
Iterable:
Objeto que se puede recorrer

Una cadena es un iterable
- hola
- germán

Un rango es un iterable
- range(1, 10)
- range(10)

Todas las estructuras de datos son iterables:
- listas
- tuplas
- sets
- diccionarios

Objetos NO iterables:
Los booleanos True False
Los números, int, float, complex
Las funciones
Las clases

"""

# Ejemplos cadenas
cadena = "Germán"
for i in cadena:
    print(i + " FORMA 1")

for i in "Germán":
    print(i + " FORMA 2")

# Ejemplos rangos
for i in range(5):
    print(f"Ciclo #{i} FORMA 1")

for i in range(0, 5):
    print(f"Ciclo #{i} FORMA 2")

for i in range(0, 10, 2):
    print(f"Ciclo #{i} FORMA 3")

# - - - - Ejemplos estructuras de datos - - - -

# Listas
for i in [2, 4, 8, 10]:
    print(f"{i} RECORRER LISTAS | FORMA 1")

pares = [2, 4, 8, 10]
for i in pares:
    print(f"{i} RECORRER LISTAS | FORMA 2")

# Tuplas
for i in (2, 4, 8, 10):
    print(f"{i} RECORRER TUPLAS | FORMA 1")

pares = (2, 4, 8, 10)
for i in pares:
    print(f"{i} RECORRER TUPLAS | FORMA 2")

# Sets
for i in {2, 4, 8, 10}:
    print(f"{i} RECORRER SETS | FORMA 1")

pares = {2, 4, 8, 10}
for i in pares:
    print(f"{i} RECORRER SETS | FORMA 2")

# Diccionarios
for i in {"red":"rojo", "green":"verde", "blue":"azul"}:
    print(f"{i} RECORRER DICCIONARIOS | FORMA 1")

pares = {"red":"rojo", "green":"verde", "blue":"azul"}
for i in pares:
    print(f"{i} RECORRER DICCIONARIOS | FORMA 2")

# - - - - ESTRUCTURAS DE DATOS ORDENADAS - - - -

# Forma manual acceder elementos de un iterables
nombre = "Germán"
print(nombre[0])
print(nombre[1])
print(nombre[2])
print(nombre[3])
print(nombre[4])
print(nombre[5])

# Forma 1 for 
nombre = input("Ingrese su nombre: ")
for i in nombre:
    print(i)

# Forma 2 for
nombre = input("Ingrese su nombre: ")
for i in range(len(nombre)):
    print(i, nombre[i])

# Forma única while
nombre = input("Ingrese su nombre: ")
i = 0
while i < len(nombre):
    print(i, nombre[i])
    i = i + 1
