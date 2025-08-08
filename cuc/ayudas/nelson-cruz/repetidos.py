# Contar números repetidos

n = int(input("Ingrese cantidad de elementos: "))

vector = []
i = 0
while i < n:
    x = eval(input(f"Ingrese el elemento vector[{i}]: "))
    vector.append(x)
    i = i + 1
    
print(f"Vector: {vector}")

# Vector sin repeticiones
sin_repetir = []
i = 0
while i < n:
    if vector[i] not in sin_repetir:
        sin_repetir.append(vector[i])
    i = i + 1
print(f"Vector sin repetir: {sin_repetir}")

# Comparar
i = 0
while i < len(sin_repetir):
    cont = 0
    j = 0
    while j < len(vector):
        if sin_repetir[i] == vector[j]:
            cont = cont + 1
        j = j + 1
    print(f"El {sin_repetir[i]} aparece {cont} vecez")
    i = i + 1
