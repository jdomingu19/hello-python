# Ejercicio 2 | Asteriscos

# Ejercicio 1:

print("- - EJERCICIO 1 - -")

# Ciclo filas:
i = 1
while i <= 4:
    # Ciclo columnas:
    x = 1
    while x <= i:
        print("*", end=" ")
        x = x + 1
    # Siguiente fila:
    print("")
    i = i + 1

# Ejercicio 2:

print("- - EJERCICIO 2 - -")

# Ciclo filas:
i = 4
while i >= 1:
    # Columnas:
    x = "  " * (i - 1)
    y = "* " * (4 - i + 1)
    print(x + y)
    # Siguiente fila:
    i = i - 1

# Ejercicio 3:

print("- - EJERCICIO 3 - -")

# Ciclo filas:
i = 4
while i >= 1:
    # Columnas:
    x = "  " * (4 - i)
    y = "* " * i
    print(x + y)
    # Siguiente fila:
    i = i - 1
    
# Ejercicio 4:

print("- - EJERCICIO 4 - -")

# Ciclo filas:
i = 4
while i >= 1:
    # Columnas:
    print("* " * i, end="")
    # Siguiente fila:
    print("")
    i = i - 1

# Extra 1:

print("- - EXTRA 1 - -")

# Ciclo filas:
i = 4
while i >= 1:
    # Columnas:
    x = " " * (i - 1)
    y = "* " * (4 - i + 1)
    print(x + y)
    # Siguiente fila:
    i = i - 1

# Extra 2:

print("- - EXTRA 2 - -")

# Ciclo filas:
i = 4
while i >= 1:
    # Columnas:
    x = " " * (4 - i)
    y = "* " * i
    print(x + y)
    # Siguiente fila:
    i = i - 1