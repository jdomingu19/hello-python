# Contar números repetidos FOR

n = int(input("Ingrese cantidad elementos: "))

vector = []
for i in range(n):
    x = eval(input(f"Ingrese elemento vector[{i}]: "))
    vector.append(x)
print(f"Vector: {vector}")

# Repetidos v3.0
numeros = []
for i in vector:
    if i not in numeros:
        numeros.append(i)
        cont = 0
        for j in vector:
            if i == j:
                cont = cont + 1
        print(f"Repeticiones de {i} : {cont}")