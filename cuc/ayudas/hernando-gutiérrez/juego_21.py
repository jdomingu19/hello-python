# 6 jugadores
# cada uno recibe tres numeros aleatorios entre 1 y 14

# rondas infinitas hasta un ganador
# jugador eliminado si puntaje menor dos rondas

# puntaje es suma de los tres números
# solo se almacena si: es mayor o igual a 16

# si es 21 se duplica el puntaje
# si > que 21 puntaje = 0

# puntos por cada ronda
# al final, clasificación

import random

puntaje_j1 = []
puntaje_j2 = []
puntaje_j3 = []
puntaje_j4 = []
puntaje_j5 = []
puntaje_j6 = []

juego_j1 = True
juego_j2 = True
juego_j3 = True
juego_j4 = True
juego_j5 = True
juego_j6 = True

vidas_j1 = 2
vidas_j2 = 2
vidas_j3 = 2
vidas_j4 = 2
vidas_j5 = 2
vidas_j6 = 2

jugadores = 6
ronda = 0
while jugadores > 1:
    # validar quien es eliminado
    if vidas_j1 == 0:
        juego_j1 = False
        jugadores = jugadores - 1
    
    if vidas_j2 == 0:
        juego_j2 = False
        jugadores = jugadores - 1

    if vidas_j3 == 0:
        juego_j3 = False
        jugadores = jugadores - 1

    if vidas_j4 == 0:
        juego_j4 = False
        jugadores = jugadores - 1

    if vidas_j5 == 0:
        juego_j5 = False
        jugadores = jugadores - 1

    if vidas_j6 == 0:
        juego_j6 = False
        jugadores = jugadores - 1
        
    # obtener numeros de ronda 
    if juego_j1 == True:
        num1_j1 = random.randint(1, 14)
        num2_j1 = random.randint(1, 14)
        num3_j1 = random.randint(1, 14)
        suma_j1 = num1_j1 + num2_j1 + num3_j1
        if suma_j1 >= 16 and suma_j1 <= 21:
            if suma_j1 == 21:
                puntos_j1 = suma_j1 * 2
                puntaje_j1.append(puntos_j1)
            else:
                puntos_j1 = suma_j1
                puntaje_j1.append(puntos_j1)
        else:
            puntos_j1 = 0
            puntaje_j1.append(puntos_j1)

    if juego_j2 == True:
        num1_j2 = random.randint(1, 14)
        num2_j2 = random.randint(1, 14)
        num3_j2 = random.randint(1, 14)
        suma_j2 = num1_j2 + num2_j2 + num3_j2
        if suma_j2 >= 16 and suma_j2 <= 21:
            if suma_j2 == 21:
                puntos_j2 = suma_j2 * 2
                puntaje_j2.append(puntos_j2)
            else:
                puntos_j2 = suma_j2
                puntaje_j2.append(puntos_j2)
        else:
            puntos_j2 = 0
            puntaje_j2.append(puntos_j2)

    if juego_j3 == True:
        num1_j3 = random.randint(1, 14)
        num2_j3 = random.randint(1, 14)
        num3_j3 = random.randint(1, 14)
        suma_j3 = num1_j3 + num2_j3 + num3_j3
        if suma_j3 >= 16 and suma_j3 <= 21:
            if suma_j3 == 21:
                puntos_j3 = suma_j3 * 2
                puntaje_j3.append(puntos_j3)
            else:
                puntos_j3 = suma_j3
                puntaje_j3.append(puntos_j3)
        else:
            puntos_j3 = 0
            puntaje_j3.append(puntos_j3)

    if juego_j4 == True:
        num1_j4 = random.randint(1, 14)
        num2_j4 = random.randint(1, 14)
        num3_j4 = random.randint(1, 14)
        suma_j4 = num1_j4 + num2_j4 + num3_j4
        if suma_j4 >= 16 and suma_j4 <= 21:
            if suma_j4 == 21:
                puntos_j4 = suma_j4 * 2
                puntaje_j4.append(puntos_j4)
            else:
                puntos_j4 = suma_j4
                puntaje_j4.append(puntos_j4)
        else:
            puntos_j4 = 0
            puntaje_j4.append(puntos_j4)

    if juego_j5 == True:
        num1_j5 = random.randint(1, 14)
        num2_j5 = random.randint(1, 14)
        num3_j5 = random.randint(1, 14)
        suma_j5 = num1_j5 + num2_j5 + num3_j5
        if suma_j5 >= 16 and suma_j5 <= 21:
            if suma_j5 == 21:
                puntos_j5 = suma_j5 * 2
                puntaje_j5.append(puntos_j5)
            else:
                puntos_j5 = suma_j5
                puntaje_j5.append(puntos_j5)
        else:
            puntos_j5 = 0
            puntaje_j5.append(puntos_j5)

    if juego_j6 == True:
        num1_j6 = random.randint(1, 14)
        num2_j6 = random.randint(1, 14)
        num3_j6 = random.randint(1, 14)
        suma_j6 = num1_j6 + num2_j6 + num3_j6
        if suma_j6 >= 16 and suma_j6 <= 21:
            if suma_j6 == 21:
                puntos_j6 = suma_j6 * 2
                puntaje_j6.append(puntos_j6)
            else:
                puntos_j6 = suma_j6
                puntaje_j6.append(puntos_j6)
        else:
            puntos_j6 = 0
            puntaje_j6.append(puntos_j6)

    # Puntos por ronda
    print("Puntos ronda", ronda+1)
    print("j1:", puntos_j1)
    print("j2:", puntos_j2)
    print("j3:", puntos_j3)
    print("j4:", puntos_j4)
    print("j5:", puntos_j5)
    print("j6:", puntos_j6)

    # puntaje menor
    if puntos_j1 < puntos_j2 and puntos_j1 < puntos_j3 and puntos_j1 < puntos_j4 and puntos_j1 < puntos_j5 and puntos_j1 < puntos_j6:
        vidas_j1 = vidas_j1 - 1

    if puntos_j2 < puntos_j1 and puntos_j2 < puntos_j3 and puntos_j2 < puntos_j4 and puntos_j2 < puntos_j5 and puntos_j2 < puntos_j6:
        vidas_j2 = vidas_j2 - 1
    
    if puntos_j3 < puntos_j1 and puntos_j3 < puntos_j2 and puntos_j3 < puntos_j4 and puntos_j3 < puntos_j5 and puntos_j3 < puntos_j6:
        vidas_j3 = vidas_j3 - 1

    if puntos_j4 < puntos_j1 and puntos_j4 < puntos_j2 and puntos_j4 < puntos_j3 and puntos_j4 < puntos_j5 and puntos_j4 < puntos_j6:
        vidas_j4 = vidas_j4 - 1

    if puntos_j5 < puntos_j1 and puntos_j5 < puntos_j2 and puntos_j5 < puntos_j3 and puntos_j5 < puntos_j4 and puntos_j5 < puntos_j6:
        vidas_j5 = vidas_j5 - 1

    if puntos_j6 < puntos_j1 and puntos_j6 < puntos_j2 and puntos_j6 < puntos_j3 and puntos_j6 < puntos_j4 and puntos_j6 < puntos_j5:
        vidas_j6 = vidas_j6 - 1

    
    print("")
    ronda = ronda + 1

# Resultados
print("Puntaje j1:", puntaje_j1)
print("Puntaje j2:", puntaje_j2)
print("Puntaje j3:", puntaje_j3)
print("Puntaje j4:", puntaje_j4)
print("Puntaje j5:", puntaje_j5)
print("Puntaje j6:", puntaje_j6)

# Clasificados
