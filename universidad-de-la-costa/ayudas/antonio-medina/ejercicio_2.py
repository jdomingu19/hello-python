# Ejercicio 1

# Cantidad de elementos:
cantidad_elementos = eval(input("Ingrese la cantidad de elementos: "))

# Definir listas:
a = []
b = []
c = []

# Llenar lista A:
i = 0
while i < cantidad_elementos:
    elemento = eval(input(f"Ingrese el elemento a[{i}]: "))
    a.append(elemento)
    i = i + 1

# Llenar lista B:
i = 0
while i < cantidad_elementos:
    elemento = eval(input(f"Ingrese el elemento b[{i}]: "))
    b.append(elemento)
    i = i + 1

# Sumar lista A + lista B:
i = 0
while i < cantidad_elementos:
    elemento = a[i] + b[i]
    c.append(elemento)
    i = i + 1

# Resultados:
print("Lista A =", a)
print("Lista B =", b)
print("Lista A + B =", c)