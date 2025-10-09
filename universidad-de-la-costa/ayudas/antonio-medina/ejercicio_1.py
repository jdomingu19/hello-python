# Ejercicio 1

# Cantidad de elementos:
cantidad_elementos = eval(input("Ingrese la cantidad de elementos: "))

# Definir listas:
a = []
b = []
c = []

# Llenar lista A:
for i in range(cantidad_elementos):
    elemento = eval(input(f"Ingrese el elemento a[{i}]: "))
    a.append(elemento)

# Llenar lista B:
for i in range(cantidad_elementos):
    elemento = eval(input(f"Ingrese el elemento b[{i}]: "))
    b.append(elemento)

# Sumar lista A + lista B:
for i in range(cantidad_elementos):
    elemento = a[i] + b[i]
    c.S(elemento)

# Resultados:
print("Lista A =", a)
print("Lista B =", b)
print("Lista A + B =", c)