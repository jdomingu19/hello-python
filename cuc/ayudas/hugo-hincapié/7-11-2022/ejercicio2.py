asignaturas = ["Algoritmos", "Informática", "Desarrollo web"]
notas = []

for i in asignaturas:
    nota = eval(input(f"Ingrese la nota de {i}: "))
    notas.append(nota)

for i in range(len(notas)): 
    print(f"En {asignaturas[i]} sacó {notas[i]}")

for i in range(len(notas)):
    if notas[i] >= 3: 
        asignaturas[i] = ""

for i in asignaturas:
    if i == "": 
        asignaturas.remove(i)

if asignaturas[0] == "":
    print("¡No debe repetir ninguna!")
else: 
    for i in asignaturas:
        print(f"Debe repetir {i}")

        