# Corazones 1.0 | Jesús Domínguez

# Importar módulo
import random as rd

# Lista de corazones
corazones = ["❤️","🧡","💛","💚","💙","💜","🤍"]

# Imprimir 100 corazones
for i in range(100):
    x = rd.randint(0, len(corazones) - 1)
    print(corazones[x], end=" ")