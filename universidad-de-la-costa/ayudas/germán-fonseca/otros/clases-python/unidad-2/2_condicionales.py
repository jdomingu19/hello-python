"""
if

if
else

if
elif



"""

# 1. if
a = 5
b = 6
if a < b:
    print(f"{a} es menor que {b}")

# 2. if else
a = 5
b = 6
if a > b:
    print(f"{a} es mayor que {b}")
else:
    print(f"{a} es menor que {b}")

# 3. if elif
a = 5
b = 5
if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")

if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
elif a == b:
    print(f"{a} es igual a {b}")

# 4. Condicionales anidados
a = 5
b = 6
c = 7
if a < b:
    print(f"{a} es menor que {b}")
    if a < c:
        print(f"{a} es también menor a {c}")