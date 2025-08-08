# Ejercicio 14

numeros = []
i = 0
while i < 20:
    numero = eval(input("Ingrese un número: "))
    numeros.append(numero)
    i = i + 1

numero_buscar = eval(input("Ingrese un número a buscar: "))
contador = 0
i = 0
while i < len(numeros):
    if numero_buscar == numeros[i]:
        contador = contador + 1
    i = i + 1
print(numero_buscar, "aparece", contador, "veces")