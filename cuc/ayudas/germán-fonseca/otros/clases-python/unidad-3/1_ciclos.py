"""
Dos ciclos en Python:
- for
- while

for: recorrer iterables
while: recorrer iteables, menús infinitos
"""

# - - - - - for - - - - -
for _ in range(5):
    print("Hola mundo")

for x in range(5):
    print(f"Hola mundo {x} FOR")

for fruta in ["Mazana", "Banana", "Naranja"]:
    print(fruta + " DIRECTO")
    
frutas = ["Mazana", "Banana", "Naranja"]
for x in frutas:
    print(x + " INDIRECTO")


# - - - - - while - - - - -
i = 0
while i < 5:
    print(f"Hola mundo {i} WHILE")
    i = i + 1

nombre = "Germán"
i = 0
while i < len(nombre):
    print(i, nombre[i])
    i = i + 1

frutas = ["Mazana", "Banana", "Naranja"]
i = 0
while i < len(frutas):
    print(i, frutas[i])
    i = i + 1