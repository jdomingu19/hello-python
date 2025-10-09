# Algoritmo de Josué Torne

n = eval(input("Coloque la cantidad de elementos: "))

a = []
b = []
c = []
d = []
e = []
f = []
g = []

i = 0
while i < n:
    x = eval(input("Coloque el elemento para a: "))
    a.append(x)
    i = i + 1

i = 0
while i < n:
    x = eval(input("Coloque el elemento para b: "))
    b.append(x)
    i = i + 1

i = 0
while i < n:
    x = a[i] + b[i]
    c.append(x)
    i = i + 1

i = 0
while i < n:
    x = eval(input("Coloque el elemento para d: "))
    d.append(x)
    i = i + 1

i = 0
while i < n:
    x = c[i] + d[n - 1 - i]
    e.append(x)
    i = i + 1

i = 0
while i < n:
    x = eval(input("Coloque el elemento para f: "))
    f.append(x)
    i = i + 1

i = 0
while i < n:
    x = e[n - 1 - i] ** f[n - 1 - i]
    g.append(x)
    i = i + 1

print("RESULTADOS")
print("1) Lista a:", a)
print("2) Lista b:", b)
print("3) Lista c:", c)
print("4) Lista d:", d)
print("5) Lista e:", e)
print("6) Lista f:", f)
print("7) Lista g:", g)