# Ejercicio 1

# Cantidad de elementos
n = eval(input("Ingrese la cantidad de elementos: "))

# Crear lista
lista = []

# Contadores
pares = 0
impares = 0

# Llenar lista con for
for i in range(n):
    elemento = eval(input(f"Ingrese el elemento lista[{i}]: "))
    lista.append(elemento)

    # Cuántos son pares e impares
    if lista[i] % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("Lista:", lista)
print("Elementos pares:", pares)
print("Elementos pares:", impares)