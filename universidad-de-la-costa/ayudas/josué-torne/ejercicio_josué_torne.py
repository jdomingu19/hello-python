# Algoritmo de Josué Torne

# 1) Cantidad de elementos
n = eval(input("Coloque la cantidad de elementos: "))

# 2) Crear las siete listas
a = []
b = []
c = []
d = []
e = []
f = []
g = []

# 3) Llenar a
i = 0
while i < n:
    x = eval(input("Coloque el elemento para a: "))
    a.append(x)
    i = i + 1

# 4) Llenar b
i = 0
while i < n:
    x = eval(input("Coloque el elemento para b: "))
    b.append(x)
    i = i + 1

# 5) Llenar c
i = 0
while i < n:
    # c = a + b
    x = a[i] + b[i]
    c.append(x)
    i = i + 1

# 6) Llenar d
i = 0
while i < n:
    x = eval(input("Coloque el elemento para d: "))
    d.append(x)
    i = i + 1

# 7) Llenar e
i = 0
while i < n:
    # e = c + d pero invertida
    x = c[i] + d[n - 1 - i]
    e.append(x)
    i = i + 1

# 8) Llenar f
i = 0
while i < n:
    x = eval(input("Coloque el elemento para f: "))
    f.append(x)
    i = i + 1

# 9) Llenar g
i = 0
while i < n:
    # g = e ** f
    # Imprimir resultados de derecha a izquierda
    x = e[n - 1 - i] ** f[n - 1 - i]
    g.append(x)
    i = i + 1

# 10) Imprimir los resultados:
print("RESULTADOS")
print("1) Lista a:", a)
print("2) Lista b:", b)
print("3) Lista c:", c)
print("4) Lista d:", d)
print("5) Lista e:", e)
print("6) Lista f:", f)
print("7) Lista g:", g)