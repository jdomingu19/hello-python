# Ejercicio 2

suma = 0

# Ciclo:
for i in range(1, 201, 1):
    
    if i % 2 == 0: # Si es par...
        suma = suma + i
        print(i, "es par...")
    else: # Si no es par...
        print(i, "es impar...")

# Suma de todos:
print("La suma de todos es: ", suma)