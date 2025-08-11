"""
Piedra, papel o tijéras 1.0 | Jesús Alberto Domínguez Charris
Secuencial
"""

from random import randint

x = ["piedra", "papel", "tijéras"]
print("Piedra, papel o tijéras 1.0")
user = input("Ingrese piedra = 0, papel = 1 o tijéras = 2: ")
user = x[int(user)]
cpu = x[randint(0, 2)]

print(f"User: {user}")
print(f"CPU: {cpu}")

if user == cpu:
    print("Empate")

elif user == "piedra":
    if cpu == "papel":
        print("Ganó CPU")
    if cpu == "tijéras":
        print("Ganó usuario")

elif user == "papel":
    if cpu == "piedra":
        print("Ganó usuario")
    if cpu == "tijéras":
        print("Ganó CPU")

elif user == "tijéras":
    if cpu == "piedra":
        print("Ganó CPU")
    if cpu == "papel":
        print("Ganó usuario")
