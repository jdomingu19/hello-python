# Ejercicio 2 | Prática | While

# Definir lista b:
b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "-"]
c = [11, 15, 27, 11, 15, 6, 18, 4]
d = [0, 11, 6, 15, 18, 8, 20, 12, 15, 19]

# Mensaje secreto 1:
mensaje1 = ""
for i in range(len(c)):
    letra = b[c[i]]
    mensaje1 = mensaje1 + letra

# Mensaje secreto 2:
mensaje2 = ""
for i in range(len(d)):
    letra = b[d[i]]
    mensaje2 = mensaje2 + letra

# Resultados:
print("- - RESULTADOS - -")
print("Lista b =", b)
print("Lista c =", c)
print("Lista d =", d)
print("Mensaje secreto 1:", mensaje1)
print("Mensaje secreto 2:", mensaje2)