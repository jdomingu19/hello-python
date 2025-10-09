# Ejercicio de vectores

# Cantidad de elementos
n = eval(input("Ingrese la cantidad de elementos: "))

# Crear listas:
a = []
b = []
d = []
f = []

# Llenar la lista a
i = 0
while i < n:
    elemento = eval(input(f"Ingrese el elemento a[{i}]: "))
    a.append(elemento)
    i = i + 1
    
# Llenar la lista b
i = 0
while i < n:
    elemento = eval(input(f"Ingrese el elemento b[{i}]: "))
    b.append(elemento)
    i = i + 1

# Llenar la lista d
i = 0
while i < n:
    elemento = eval(input(f"Ingrese el elemento d[{i}]: "))
    d.append(elemento)
    i = i + 1

# Llenar la lista f
i = 0
while i < n:
    elemento = eval(input(f"Ingrese el elemento f[{i}]: "))
    f.append(elemento)
    i = i + 1

# Lista c = a + b
c = []
i = 0
while i < n:
    elemento = a[i] + b[i]
    c.append(elemento)
    i = i + 1

# Lista e = c + d pero invertida
e = []
i = 0
while i < n:
    elemento = c[i] + d[len(d)- 1 - i]
    e.append(elemento)
    i = i + 1

# Lista g = e ^ f
g = []
i = 0
while i < n:
    elemento = pow(e[n - 1 - i], f[n - 1 - i])
    g.append(elemento)
    i = i + 1

# Resultados
print("- - RESULTADOS - -")
print("Lista a: ", a)
print("Lista b: ", b)
print("Lista c: ", c)
print("Lista d: ", d)
print("Lista e: ", e)
print("Lista f: ", f)
print("Lista g: ", g)