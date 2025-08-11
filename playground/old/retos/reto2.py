# Resolver tres ecuaciones | Reto 2

# - - Ecuación A - -
print("- - Ecuación A - -")
n = eval(input("Ingrese el valor de n: "))
m = eval(input("Ingrese el valor de m: "))

numerador_a = 0

for k in range(2,11):
    numerador_a = numerador_a + (k + m)

denominador_a = 0

for i in range(1,n + 1):
    for j in range(1,n + 1):
        denominador_a = denominador_a + (i * j)

a = numerador_a / denominador_a

print(f"Ecuación A: {numerador_a}/{denominador_a} = {a}")

# - - Ecuación B - -
print("- - Ecuación B - -")
h = eval(input("Ingrese el valor de h: "))

numerador_b = 0
x = 0

for i in range(1,21):
    for j in range(1,51):
        x = x + ((j * h) + 1)
        numerador_b = numerador_b + (i * x)

denominador_b = 0

for k in range(1,21):
    denominador_b = denominador_b + (k + 2)

b = numerador_b / denominador_b

print(f"Ecuación B: {numerador_b}/{denominador_b} = {b}")

# - - Ecuación C - -
print("- - Ecuación C - -")
n = eval(input("Ingrese el valor de n: "))
k = eval(input("Ingrese el valor de k: "))

c = 0

for i in range(1,n + 1):
    for j in range(2,9):
        c = c + (k + i)

print(f"Ecuación C: {c}")