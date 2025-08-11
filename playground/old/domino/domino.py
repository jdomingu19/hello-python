# Domino | Versión 1
import random

# Todas las piezas:
piezas = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[2,2],[2,3],[2,4],[2,5],[2,6],[3,3],[3,4],[3,5],[3,6],[4,4],[4,5],[4,6],[5,5],[5,6],[6,6]]

# Repartir piezas CPU:
piezas_cpu = []
contador = 0

while contador < 7:
    # Generar un número aleatorio
    aleatorio = random.randint(0,27)
    # Validar no piezas repetidas para CPU
    if piezas[aleatorio] not in piezas_cpu:
        piezas_cpu.append(piezas[aleatorio])
        contador = contador + 1

print(piezas_cpu)

# Repartir piezas JUGADOR:
piezas_jugador = []
contador = 0

while contador < 7:
    # Generar un número aleatorio
    aleatorio = random.randint(0,27)
    # Validar no piezas utilizadas por CPU + Validar no piezas repetidas para JUGAGOR
    if piezas[aleatorio] not in piezas_cpu and piezas[aleatorio] not in piezas_jugador:
        piezas_jugador.append(piezas[aleatorio])
        contador = contador + 1

print(piezas_jugador)