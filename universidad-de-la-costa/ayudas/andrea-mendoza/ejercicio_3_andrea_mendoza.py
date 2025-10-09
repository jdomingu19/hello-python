# Ejercicio 3

# Entradas
numeradorFraccion1 = eval(input("Ingrese el numerador de la primera fracción: "))
denominadorFraccion1 = eval(input("Ingrese el denominador de la primera fracción: "))
numeradorFraccion2 = eval(input("Ingrese el numerador de la segunda fracción: "))
denominadorFraccion2 = eval(input("Ingrese el denominador de la segunda fracción: "))

# Condiciones
if denominadorFraccion1 == denominadorFraccion2: # homogeneas
    resultadoNumeradores = (numeradorFraccion1 + numeradorFraccion2)
    resultadoDenominadores = (denominadorFraccion1)
    print("Resultado: ", resultadoNumeradores, " / ", resultadoDenominadores)
    print("Fracción homogena")
else: # heterogeneas
    resultadoNumeradores = (numeradorFraccion1 * denominadorFraccion2) + (denominadorFraccion1 * numeradorFraccion2)  
    resultadoDenominadores = (denominadorFraccion1 * denominadorFraccion2)
    print("Resultado: ", resultadoNumeradores, " / ", resultadoDenominadores)
    print("Fracción heterogenea")