"""
listas son una estructura de datos

podemos guardar diferentes valores 
en un mismo lugar o referencia

mi_lista = ["abc", True, 123, 3.14, 2j]

métodos básicos lista:
mi_lista.append(valor_agregar)

"""

import random

# append(valor_agregar ESTÁTICAMENTE
numeros = [1, 2, 3]
numeros.append(4)
numeros.append(5)
numeros.append(6)
print(numeros)

# append(valor_agregar) for DINÁMICAMENTE
numeros = [] # lista vacía
cantidad_numeros = int(input("Ingrese la cantidad número: ")) # múmero de números
for i in range(cantidad_numeros):
    num = eval(input(f"Ingrese elemento numeros[{i}]: ")) # preguntamos número
    numeros.append(num) # lo agregamos
print(f"Números dinámicamente FOR: {numeros}")

numeros = []
for i in range(random.randint(5, 10)):
    num = random.randint(1, 10)
    numeros.append(num)
print(f"Números dinámicamente FOR + RANDOM: {numeros}")

# append(valor_agregar) while DINÁMICAMENTE
numeros = []
i = 0
while i < 10:
    num = random.randint(1, 10)
    numeros.append(num)
    i = i + 1
print(f"Números dinámicamente WHILE + RANDOM: {numeros}")

# - - - Promedio estudiantes - - -
notas = []
n = int(input("Ingrese número de notas: "))
for i in range(n):
    nota = eval(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

print(f"Notas estudiante: {notas}")

promedio = sum(notas) / len(notas) # FORMA DIRÉCTA
promedio = round(promedio, 2)
print(f"Promedio DIRECTO: {promedio}")

# Manualmente
acumulador = 0
contador = 0
for i in notas:
    acumulador = acumulador + i
    # acumulador += i
    contador = contador + 1
    # contador += 1

promedio = acumulador / contador
promedio = round(promedio, 2)
print(f"Promedio MANUAL: {promedio}")

# par o impar
numeros = []
for i in range(10):
    num = random.randint(1, 10)
    numeros.append(num)

for i in numeros:
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")
