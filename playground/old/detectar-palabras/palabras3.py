# Detector de palabras 3.0

# Entrada:
print("- - Detector de palabras 3.0 (Python) - -")
mitexto = input("Ingrese una frase: ")

numPalabras = 1

# Si no hay palabras:
if mitexto == "" or mitexto == " ":
    numPalabras = 0
# Si hay palabras:
else:
    # Eliminar espacios al principio o al final
    textoNuevo = mitexto.strip()
    
    # Recorrer caracter por caracter:
    for x in textoNuevo:
        if x == " ":
            numPalabras = numPalabras + 1

# Salida:
print("- - Resultados - -")
print("Número de palabras: ", numPalabras)