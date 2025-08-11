"""
Dominó 1.0 | Jesús Alberto Domínguez Charris

Secuencial
Piezas
Repartir piezas Jugador - CPU
Ver piezas

Juego:
Empiza el doble mayor
Si no, empieza la pieza mayor

"""

import random

# 1. Piezas
piezas = [
    # Ceros
    [0, 0],
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [0, 5],
    [0, 6],
    # Unos
    [1, 1],
    [1, 2],
    [1, 3],
    [1, 4],
    [1, 5],
    [1, 6],
    # Doses
    [2, 2],
    [2, 3],
    [2, 4],
    [2, 5],
    [2, 6],
    # Treses
    [3, 3],
    [3, 4],
    [3, 5],
    [3, 6],
    # Cuatros
    [4, 4],
    [4, 5],
    [4, 6],
    # Cincos
    [5, 5],
    [5, 6],
    # Seises
    [6, 6]
]

# 2. Repartir piezas
piezas_jugador = []
i = 0
while i < 7:
    pieza = random.choice(piezas)
    if pieza not in piezas_jugador:
        piezas_jugador.append(pieza)
        i = i + 1

piezas_cpu = []
i = 0
while i < 7:
    pieza = random.choice(piezas)
    if pieza not in piezas_cpu and pieza not in piezas_jugador:
        piezas_cpu.append(pieza)
        i = i + 1

print(f"Piezas: {piezas}")
print(f"Piezas JUGADOR: {piezas_jugador}")
print(f"Piezas CPU: {piezas_cpu}\n")

# 3. Juego
dobles_jugador = []
for x in piezas_jugador:
    if x[0] == x[1]:
        dobles_jugador.append(x)

dobles_cpu = []
for x in piezas_cpu:
    if x[0] == x[1]:
        dobles_cpu.append(x)

print(f"Dobles JUGADOR: {dobles_jugador}")
print(f"Dobles CPU: {dobles_cpu}")

# Validar si hay dobles:
if len(dobles_jugador) != 0 and len(dobles_cpu) != 0:
    doble_mayor_jugador = [0, 0]
    for x in dobles_jugador:
        suma = x[0] + x[1]
        if suma > doble_mayor_jugador[0] + doble_mayor_jugador[1]:
            doble_mayor_jugador = x

    doble_mayor_cpu = [0, 0]
    for x in dobles_cpu:
        suma = x[0] + x[1]
        if suma > doble_mayor_cpu[0] + doble_mayor_cpu[1]:
            doble_mayor_cpu = x

    print(f"Doble mayor JUGADOR: {doble_mayor_jugador}")
    print(f"Doble mayor CPU: {doble_mayor_cpu}")

    if sum(doble_mayor_jugador) > sum(doble_mayor_cpu):
        print("¡Jugador empieza!")
    else:
        print("¡CPU empieza!")

elif len(dobles_jugador) != 0 and len(dobles_cpu) == 0:
    doble_mayor_jugador = [0, 0]
    for x in dobles_jugador:
        suma = x[0] + x[1]
        if suma > doble_mayor_jugador[0] + doble_mayor_jugador[1]:
            doble_mayor_jugador = x
    print(f"Doble mayor JUGADOR: {doble_mayor_jugador}")
    print("¡Jugador empieza!")

elif len(dobles_jugador) == 0 and len(dobles_cpu) != 0:
    doble_mayor_cpu = [0, 0]
    for x in dobles_cpu:
        suma = x[0] + x[1]
        if suma > doble_mayor_cpu[0] + doble_mayor_cpu[1]:
            doble_mayor_cpu = x
    print(f"Doble mayor CPU: {doble_mayor_cpu}")
    print("¡CPU empieza!")

# si ninguno tiene dobles:
else:
    mayor_jugador = [0, 0]
    for x in piezas_jugador:
        suma = x[0] + x[1]
        if suma > mayor_jugador[0] + mayor_jugador[1]:
            mayor_jugador = x

    mayor_cpu = [0, 0]
    for x in piezas_cpu:
        suma = x[0] + x[1]
        if suma > mayor_cpu[0] + mayor_cpu[1]:
            mayor_cpu = x

    if mayor_jugador > mayor_cpu:
        print("¡Empieza el jugador!")

