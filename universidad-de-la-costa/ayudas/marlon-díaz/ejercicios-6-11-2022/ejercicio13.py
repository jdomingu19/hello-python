# Ejercicio 13
import random

numero_generado = random.randint(0, 100)

turno = 3
while turno > 0:
    numero = eval(input("Adivine el número generado: "))
    if numero == numero_generado:
        print("Felicidades, ha ganado")
    else:
        print("Incorrecto, le quedan", turno - 1, "turnos")
        turno = turno - 1