# Algortimo 1 if-else

# Captura de información
peso = eval(input("Ingrese valor del peso en kg: "))
altura = eval(input("Ingrese valor de la altura en metros: "))

# Desarrollo
imc = peso / pow(altura,2)
print("El IMC de la persona = ", round(imc,2))

# Condiciones
if imc < 16:
    print("Criterio de ingreso en hospital")
else:
    if imc >= 16 and imc < 17:
        print("Infrapeso")
    else:
        if imc >= 17 and imc < 18:
            print("Bajo peso")
        else:
            if imc >= 18 and imc < 25:
                print("Peso normal (Saludable)")
            else:
                if imc >= 25 and imc < 30:
                    print("Sobre peso (Obesidad Grado I)")
                else:
                    if imc >= 30 and imc < 35:
                        print("Sobre peso crónico (Obesidad Grado II)")
                    else:
                        if imc >= 35 and imc < 40:
                            print("Obesidad premórbida (Obesidad Grado III)")
                        else:
                            if imc > 40:
                                print("Obesidad mórbida (Obesidad Grado IV)")