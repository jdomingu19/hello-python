"""
contador: variable que aumenta o disminuye constantemente
en un mismo número o valor
    contador = contador + 1
    contador = contador - 1
    contador += 1
    contador -= 1

acumulador: variable que aumenta o disminuye variablemente
con diferentes valores o números
    acumulador = acumulador + variable
    acumulador = acumulador - variable
    acumulador += variable
    acumulador -= variable
"""

import random

# contador con for
contador = 0
for i in range(10):
    contador = contador + 1
print(f"Contador for: {contador}")

contador = 0
for i in range(10):
    contador += 1
print(f"Contador for: {contador}")

# contador con while
i = 0
while i < 10:
    i = i + 1
print(f"Contador con while: {i}")

i = 0
while i < 10:
    i += 1
print(f"Contador con while: {i}")

# acumulador con for
acumulador = 0
for i in range(3):
    numero = random.randint(1, 10)
    acumulador = acumulador + numero
print(f"Acumulador for: {acumulador}")

acumulador = 0
for i in range(3):
    numero = random.randint(1, 10)
    acumulador += numero
print(f"Acumulador for: {acumulador}")

# acumulador con while
acumulador = 0
i = 0
while i < 3:
    numero = random.randint(1, 10)
    acumulador = acumulador + numero
    i = i + 1
print(f"Acumulador while: {acumulador}")

acumulador = 0
i = 0
while i < 3:
    numero = random.randint(1, 10)
    acumulador += numero
    i = i + 1
print(f"Acumulador while: {acumulador}")