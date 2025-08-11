"""
Piedra, papel o tijéras 1.2 | Jesús Alberto Domínguez Charris
Secuencial
rondas
contadores
"""

from random import randint

print("Piedra, papel o tijéras 1.2")
x = ["piedra", "papel", "tijéras"]
victorias_user = 0
victorias_cpu = 0
empates = 0
rondas = int(input("Ingrese número de rondas: "))
for ronda in range(rondas):
    print(f"RONDA {ronda + 1}")
    user = input("Ingrese piedra = 0, papel = 1 o tijéras = 2: ")
    user = x[int(user)]
    cpu = x[randint(0, 2)]

    print(f"User: {user}")
    print(f"CPU: {cpu}")

    if user == cpu:
        print("¡Empate!")
        empates = empates + 1

    elif user == "piedra":
        if cpu == "papel":
            print("¡Ganó CPU!")
            victorias_cpu = victorias_cpu + 1
        if cpu == "tijéras":
            print("¡Ganó usuario!")
            victorias_user = victorias_user + 1

    elif user == "papel":
        if cpu == "piedra":
            print("¡Ganó usuario!")
            victorias_user = victorias_user + 1
        if cpu == "tijéras":
            print("¡Ganó CPU!")
            victorias_cpu = victorias_cpu + 1

    elif user == "tijéras":
        if cpu == "piedra":
            print("¡Ganó CPU!")
            victorias_cpu = victorias_cpu + 1
        if cpu == "papel":
            print("¡Ganó usuario!")
            victorias_user = victorias_user + 1
    print("")

print(f"Victorias usuario: {victorias_user}")
print(f"Victorias CPU: {victorias_cpu}")
print(f"Empates: {empates}")
