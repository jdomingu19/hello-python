cadena = "Hola"
for i in cadena:
    print(i, "FOR 1")

cadena = "Hola"
for i in range(len(cadena)):
    print(i, "FOR 2")

cadena = "Hola"
for i in range(len(cadena)):
    print(f"{i} {cadena[i]}, FOR 3")
    # Primer ciclo i vale 0
    # Segundo ciclo i vale 1
    # Tercer ciclo i vale 2
    # Cuarto ciclo i vale 3
    # Y ya no tenemos que hacer así:
    # print(cadena[0])
    # print(cadena[1])
    # print(cadena[2])
    # print(cadena[3])
