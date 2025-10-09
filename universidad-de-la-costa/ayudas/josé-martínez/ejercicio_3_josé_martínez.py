# Ejercicio 3

# Captura de datos
numerador1 = eval(input("Ingrese el numerador de la primera fracción: "))
denominador1 = eval(input("Ingrese el denominador de la primera fracción: "))
numerador2 = eval(input("Ingrese el numerador de la segunda fracción: "))
denominador2 = eval(input("Ingrese el denominador de la segunda fracción: "))

# Condiciones
if denominador1 == denominador2:
    resultado_numeradores = (numerador1 + numerador2)
    resultado_denominadores = (denominador1)
    print("Resultado de la operación: ", resultado_numeradores, " / ", resultado_denominadores)
    print("Es una fracción homogena...")
else:
    resultado_numeradores = (numerador1 * denominador2) + (denominador1 * numerador2)  
    resultado_denominadores = (denominador1 * denominador2)
    print("Resultado de la operación: ", resultado_numeradores, " / ", resultado_denominadores)
    print("Es una fracción heterogenea...")