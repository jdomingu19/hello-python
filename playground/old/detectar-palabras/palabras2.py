# Detector de palabras 2.0

# Entrada:
print("- - Detector de palabras 2.0 (Python) - -")
mitexto = input("Ingrese una frase: ")

numPalabras = 1

# Si no hay palabras:
if mitexto == "" or mitexto == " ":
    numPalabras = 0
# Si hay palabras:
else:
    if mitexto[0] == " ":
        # Un espacio al principio
        numPalabras = numPalabras - 1
    if mitexto[-1:] == " ":
        # Un espacio al final
        numPalabras = numPalabras - 1

    # Recorrer caracter por caracter:
    for x in str(mitexto):
        if x == " ":
            numPalabras = numPalabras + 1

# Salida:
print("- - Resultados - -")
print("Número de palabras: ", numPalabras)