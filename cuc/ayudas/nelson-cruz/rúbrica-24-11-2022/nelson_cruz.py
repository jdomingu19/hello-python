# 10 rondas
# indicar ganador de cada ronda
# un jugador gana con tres rondas ganadas seguidas

# una palabra por turno
# palabra con len mayor 15 puntos
# palabra con mayor num vocales 10 puntos
# palabra con todas las vocales 5 puntos

# informar puntos cada ronda
# decir ganador

print("ESCRIBA SU PALABRA - NELSON CRUZ")
victoria_consecutiva = False
puntaje_j1 = []
palabras_j1 = []
victorias_j1 = []

puntaje_j2 = []
palabras_j2 = []
victorias_j2 = []
# 10 rondas
for ronda in range(10):
    # Cada jugador tendrá la oportunidad de escribir una palabra en su turno
    puntos_j1 = 0
    puntos_j2 = 0
    print("RONDA", ronda + 1)
    palabra_j1 = input("Palabra jugador 1: ")
    palabra_j2 = input("Palabra jugador 2: ")

    # Palabra con más caracteres
    if len(palabra_j1) > len(palabra_j2):
        puntos_j1 = puntos_j1 + 15
        puntos_j2 = puntos_j2 + 0

    if len(palabra_j1) < len(palabra_j2):
        puntos_j1 = puntos_j1 + 0
        puntos_j2 = puntos_j2 + 15

    if len(palabra_j1) == len(palabra_j2):
        puntos_j1 = puntos_j1 + 15
        puntos_j2 = puntos_j2 +15

    # Palabra con mayor número de vocales
    vocales_j1 = 0
    for letra in palabra_j1:
        if letra == "a" or letra == "A":
            vocales_j1 = vocales_j1 + 1
        if letra == "e" or letra == "E":
            vocales_j1 = vocales_j1 + 1
        if letra == "i" or letra == "I":
            vocales_j1 = vocales_j1 + 1
        if letra == "o" or letra == "O":
            vocales_j1 = vocales_j1 + 1
        if letra == "u" or letra == "U":
            vocales_j1 = vocales_j1 + 1

    vocales_j2 = 0
    for letra in palabra_j2:
        if letra == "a" or letra == "A":
            vocales_j2 = vocales_j2 + 1
        if letra == "e" or letra == "E":
            vocales_j2 = vocales_j2 + 1
        if letra == "i" or letra == "I":
            vocales_j2 = vocales_j2 + 1
        if letra == "o" or letra == "O":
            vocales_j2 = vocales_j2 + 1
        if letra == "u" or letra == "U":
            vocales_j2 = vocales_j2 + 1
    
    if vocales_j1 > vocales_j2:
        puntos_j1 = puntos_j1 + 10
        puntos_j2 = puntos_j2 + 0

    if vocales_j1 < vocales_j2:
        puntos_j1 = puntos_j1 + 0
        puntos_j2 = puntos_j2 + 10

    if vocales_j1 == vocales_j2:
        puntos_j1 = puntos_j1 + 10
        puntos_j2 = puntos_j2 + 10
    
    # Palabra con todas las vocales
    a = False
    e = False
    i = False
    o = False
    u = False
    for letra in palabra_j1:
        if letra == "a" or letra == "A":
            a = True
                        
        if letra == "e" or letra == "E":
            e = True
                        
        if letra == "i" or letra == "I":
            i = True
                        
        if letra == "o" or letra == "O":
            o = True
            
        if letra == "u" or letra == "U":
            u = True                 
    if a == True and e == True and i == True and o == True and u == True:
        puntos_j1 = puntos_j1 + 5

    a = False
    e = False
    i = False
    o = False
    u = False
    for letra in palabra_j2:
        if letra == "a" or letra == "A":
            a = True
            continue
        if letra == "e" or letra == "E":
            e = True
            continue
        if letra == "i" or letra == "I":
            i = True
            continue
        if letra == "o" or letra == "O":
            o = True
            continue
        if letra == "u" or letra == "U":
            u = True
            continue
    if a == True and e == True and i == True and o == True and u == True:
        puntos_j2 = puntos_j2 + 5

    # Resultado ronda
    print("Puntos jugador 1 ronda", ronda + 1, ":", puntos_j1)
    print("Puntos jugador 2 ronda", ronda + 1, ":", puntos_j2)

    if puntos_j1 > puntos_j2:
        print("¡El jugador 1 ganó esta ronda!")
        victorias_j1.append("ganó")
        victorias_j2.append("perdió")
    
    if puntos_j1 < puntos_j2:
        print("¡El jugador 2 ganó esta ronda!")
        victorias_j1.append("perdió")
        victorias_j2.append("ganó")

    if puntos_j1 == puntos_j2:
        print("¡Empate en esta ronda!")
        victorias_j1.append("empate")
        victorias_j2.append("empate")

    puntaje_j1.append(puntos_j1)
    puntaje_j2.append(puntos_j2)

    palabras_j1.append(palabra_j1)
    palabras_j2.append(palabra_j2)

    # Validar si un jugador ya ganó tres veces seguidas
    if ronda >= 2:
        if victorias_j1[ronda] == "ganó" and victorias_j1[ronda-1] == "ganó" and victorias_j1[ronda-2] == "ganó":
            print("El jugador 1 ganó el juego por 3 victorias seguidas")
            victoria_consecutiva = True
            print("")
            break

        if victorias_j2[ronda] == "ganó" and victorias_j2[ronda-1] == "ganó" and victorias_j2[ronda-2] == "ganó":
            print("El jugador 2 ganó el juego por 3 victorias seguidas")
            victoria_consecutiva = True
            print("")
            break

# Resultados finales
if victoria_consecutiva == True:
    print("RESULTADO FINAL")
    suma_1 = 0
    for puntos in puntaje_j1:
        suma_1 = suma_1 + puntos

    suma_2 = 0
    for puntos in puntaje_j2:
        suma_2 = suma_2 + puntos

    print("Puntos acumulados jugador 1:", suma_1)
    print("Puntos acumulados jugador 2:", suma_2)
    print("Palabras jugador 1:", palabras_j1)
    print("Palabras jugador 2:", palabras_j2)
else:
    print("")
    print("RESULTADO FINAL")
    suma_1 = 0
    for puntos in puntaje_j1:
        suma_1 = suma_1 + puntos

    suma_2 = 0
    for puntos in puntaje_j2:
        suma_2 = suma_2 + puntos

    print("Puntos acumulados jugador 1:", suma_1)
    print("Puntos acumulados jugador 2:", suma_2)
    print("Palabras jugador 1:", palabras_j1)
    print("Palabras jugador 2:", palabras_j2)

    if puntos_j1 > puntos_j2:
        print("¡El jugador 1 ganó ESCRIBA SU PALABRA!")
    
    if puntos_j1 < puntos_j2:
        print("¡El jugador 2 ganó ESCRIBA SU PALABRA!")

    if puntos_j1 == puntos_j2:
        print("¡Empate juego ESCRIBA SU PALABRA!")