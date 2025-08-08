# Contar números repetidos WHILE

n = int(input("Ingrese cantidad elementos: "))

vector = []
i = 0
while i < n:
    x = eval(input(f"Ingrese elemento vector[{i}]: "))
    vector.append(x)
    i = i + 1

print(f"Vector: {vector}")

# Repetidos v2.0
numeros = []
i = 0
while i < len(vector):
    if vector[i] not in numeros:
        numeros.append(vector[i])
        cont = 0
        j = 0
        while j < len(vector):
            if vector[i] == vector[j]:
                cont = cont + 1
            j = j + 1
        print(f"Repeticiones de {vector[i]} : {cont}")
    i = i + 1
