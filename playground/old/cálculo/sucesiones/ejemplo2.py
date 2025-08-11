# Ejemplo 2 | Sucesiones

# Sucesión
print("- - Sucesión - -")
print("     2n^2 + 1")
print("an = --------")
print("     3n^2 - n")

# Primero cinco términos For
print("- - For - -")
for n in range(1,6,1):
    numerador = 2 * (n ** n) + 1
    denominador = 3 * (n ** n) - n
    an = round(numerador / denominador, 2)
    print("a" + str(n), "=", an)

# Primero cinco términos While
print("- - While - -")
n = 1
while n <= 5:
    numerador = 2 * (n ** n) + 1
    denominador = 3 * (n ** n) - n
    an = round(numerador / denominador, 2)
    print("a" + str(n), "=", an)
    n = n + 1