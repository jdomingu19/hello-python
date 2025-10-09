# Vectores - Hernando Gutiérrez

# Cantidad de elementos
n = eval(input("Ingrese la cantidad de elementos: "))

# Crear listas:
a = []
b = []
c = []
d = []
e = []
f = []
g = []

# Llenar lista a
i = 0
while i < n:
    x = eval(input(f"Ingrese el elemento a[{i}]: "))
    a.append(x)
    i = i + 1
    
# Llenar lista b
i = 0
while i < n:
    x = eval(input(f"Ingrese el elemento b[{i}]: "))
    b.append(x)
    i = i + 1

# Llenar lista d
i = 0
while i < n:
    x = eval(input(f"Ingrese el elemento d[{i}]: "))
    d.append(x)
    i = i + 1

# Llenar lista f
i = 0
while i < n:
    x = eval(input(f"Ingrese el elemento f[{i}]: "))
    f.append(x)
    i = i + 1

# Lista c = a + b
i = 0
while i < n:
    x = a[i] + b[i]
    c.append(x)
    i = i + 1

# Lista e = c + d invertida
i = 0
while i < n:
    x = c[i] + d[len(d)- 1 - i]
    e.append(x)
    i = i + 1

# Lista g = e ^ f
i = 0
while i < n:
    x = pow(e[n - 1 - i], f[n - 1 - i])
    g.append(x)
    i = i + 1

# Resultados
print("RESULTADOS")
print("Lista a: ", a)
print("Lista b: ", b)
print("Lista c: ", c)
print("Lista d: ", d)
print("Lista e: ", e)
print("Lista f: ", f)
print("Lista g: ", g)