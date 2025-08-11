"""
Dominó 1.0 | Jesús Alberto Domínguez Charris

Secuencial
Piezas
Repartir piezas Jugador - CPU
Ver piezas
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
print(f"Piezas CPU: {piezas_cpu}")
