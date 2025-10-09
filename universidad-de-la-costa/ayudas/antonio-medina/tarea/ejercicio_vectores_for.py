# Ejercicio Vectores | For

# Cantidad de elementos:
cantidad = eval(input("Ingrese la cantidad de elementos: "))

# Definir listas:
a = [] # Usuario
b = [] # Usuario
c = [] # Sistema
d = [] # Usuario
e = [] # Sistema
f = [] # Usuario
g = [] # Sistema

# Llenar lista a:
for i in range(cantidad):
    elemento = eval(input(f"Ingrese el elemento a[{i}]: "))
    a.append(elemento)

# Llenar lista b:
for i in range(cantidad):
    elemento = eval(input(f"Ingrese el elemento b[{i}]: "))
    b.append(elemento)

# Llenar lista c:
for i in range(cantidad):
    # c = a + b
    elemento = a[i] + b[i]
    c.append(elemento)

# Llenar lista d:
for i in range(cantidad):
    elemento = eval(input(f"Ingrese el elemento d[{i}]: "))
    d.append(elemento)

# Llenar lista e:
for i in range(cantidad):
    # e = c + d invertida
    elemento = c[i] + d[cantidad - 1 - i]
    e.append(elemento)

# Llenar lista f:
for i in range(cantidad):
    elemento = eval(input(f"Ingrese el elemento f[{i}]: "))
    f.append(elemento)

# Llenar lista g:
for i in range(cantidad):
    # g = e ** f, invertir también
    elemento = e[cantidad - 1 - i] ** f[cantidad - 1 - i]
    g.append(elemento)

# Resultados:
print("- - RESULTADOS - -")
print("Lista a:", a)
print("Lista b:", b)
print("Lista c:", c)
print("Lista d:", d)
print("Lista e:", e)
print("Lista f:", f)
print("Lista g:", g)