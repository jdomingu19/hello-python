# Detector de palabras 5.0

# Entrada:
print("- - Detector de palabras 5.0 (Python) - -")
mitexto = input("Ingrese una frase: ")

numPalabras = 1 # Valor por defecto
listaPalabras = mitexto.split() # Convertir a vectores

# Si no hay palabras:
if len(listaPalabras) == 0:
    numPalabras = 0
    # Salida:
    print("- - Resultados - -")
    print("Número de palabras: 0")
    print("Lista de palabras: N/A")

# Si hay palabras:
else:
    # Números de palabras = Números de vectores
    for x in listaPalabras:
        numPalabras = numPalabras + 1
        
    # Salida:
    print("- - Resultados - -")
    print("Número de palabras: ", numPalabras - 1)
    print("Lista de palabras: ")

    a = 0
    for x in listaPalabras:
        a = a + 1
        print(str(a) + ") ", x)