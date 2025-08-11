# Ejemplo 1 | Sucesiones

# Sucesión
print("- - Sucesión - -")
print("     n + 1")
print("an = ------")
print("     2n - 1")

# Primero cinco términos For
print("- - For - -")
for n in range(1,6,1):
    numerador = n + 1
    denominador = (2 * n) - 1
    an = round(numerador / denominador, 2)
    print("a" + str(n), "=", an)

# Primero cinco términos While
print("- - While - -")
n = 1
while n <= 5:
    numerador = n + 1
    denominador = (2 * n) - 1
    an = round(numerador / denominador, 2)
    print("a" + str(n), "=", an)
    n = n + 1