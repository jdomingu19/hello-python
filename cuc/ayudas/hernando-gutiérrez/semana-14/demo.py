# Semana 14

cantidad_elementos = eval(input("Ingrese la cantidad de elementos: "))

a = []
b = []

# Llenar lista A con For:
for i in range(cantidad_elementos):
    x = eval(input(f"Ingrese el elemento a[{i}]: "))
    a.append(x)

# Llenar lista B con While:
i = 0
while i < cantidad_elementos:
    x = eval(input(f"Ingrese el elemento b[{i}]: "))
    b.append(x)

# Determinar el elemento mayor en cada lista:
mayor_a = a[0]
mayor_b = b[0]

i = 0
while i < len(a):
    if a[i] > mayor_a:
        mayor_a = a[i]
    i = i + 1
print("El elemento mayor de a[] es: ", mayor_a)

i = 0
while i < len(b):
    if b[i] > mayor_b:
        mayor_b = b[i]
    i = i + 1
print("El elemento mayor de b[] es: ", mayor_b)