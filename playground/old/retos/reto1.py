# Imprimir todo en una linea | Reto 1

print("- - - -")
suma = 0

# Ciclo:
for i in range(2, 201, 2):

    if i < 200:
        print(i, end=" ")
        suma = suma + i
    else:
        print(i)
        suma = suma + i

# Resultado:
print("- - - -")
print("La suma de todo es: ", suma)