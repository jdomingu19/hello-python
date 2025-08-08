"""
CALCULADORA DE FRACCIONES
Ronald Clavijo

- Suma heterogénea
- Resta heterogénea
- Suma homogénea
- Resta homogénea
- Multiplicación
- División

"""

class Fracciones:
    def __init__(self):
        self.numerador = 0
        self.denominador = 0

    def setNumerador(self, x: int):
        self.numerador = x

    def getNumerador(self):
        return self.numerador
    
    def setDenominador(self, x: int):
        self.denominador = x

    def getDenominador(self):
        return self.denominador
    
    def verFraccion(self):
        print(self.getNumerador(), "/", self.getDenominador())
    

class CalculadoraFracciones:
    def __init__(self):
        self.f1 = Fracciones()
        self.f2 = Fracciones()

    def setF1(self, x: Fracciones):
        self.f1 = x

    def getF1(self):
        return self.f1
    
    def setF2(self, x: Fracciones):
        self.f2 = x

    def getF2(self):
        return self.f2
    
    def sumaHeterogenea(self):
        numerador = (self.getF1().getNumerador() * self.getF2().getDenominador()) + (self.getF1().getDenominador() * self.getF2().getNumerador())
        denominador = self.getF1().getDenominador() * self.getF2().getDenominador()
        resultado = numerador / denominador
        resultado = round(resultado, 2) # Redondear resultado a dos decimales
        print("Suma heterogénea =", numerador, "/", denominador, "=", resultado)
    
    def sumaHomogenea(self):
        numerador = self.getF1().getNumerador() + self.getF1().getNumerador()
        denominador = self.getF1().getDenominador()
        resultado = numerador / denominador
        resultado = round(resultado, 2) # Redondear resultado a dos decimales
        print("Suma homogénea =", numerador, "/", denominador, "=", resultado)

    def restaHeterogenea(self):
        numerador = (self.getF1().getNumerador() * self.getF2().getDenominador()) - (self.getF1().getDenominador() * self.getF2().getNumerador())
        denominador = self.getF1().getDenominador() * self.getF2().getDenominador()
        resultado = numerador / denominador
        resultado = round(resultado, 2) # Redondear resultado a dos decimales
        print("Resta heterogénea =", numerador, "/", denominador, "=", resultado)
    
    def restaHomogenea(self):
        numerador = self.getF1().getNumerador() - self.getF2().getNumerador()
        denominador = self.getF1().getDenominador()
        resultado = numerador / denominador
        resultado = round(resultado, 2) # Redondear resultado a dos decimales
        print("Resta homogénea =", numerador, "/", denominador, "=", resultado)

    def multiplicacion(self):
        numerador = self.getF1().getNumerador() * self.getF2().getNumerador()
        denominador = self.getF1().getDenominador() * self.getF2().getDenominador()
        resultado = numerador / denominador
        resultado = round(resultado, 2) # Redondear resultado a dos decimales
        print("Multiplicación =", numerador, "/", denominador, "=", resultado)

    def division(self):
        numerador = self.getF1().getNumerador() * self.getF2().getDenominador()
        denominador = self.getF1().getDenominador() * self.getF2().getNumerador()
        resultado = numerador / denominador
        resultado = round(resultado, 2) # Redondear resultado a dos decimales
        print("División =", numerador, "/", denominador, "=", resultado)


def main():
    # Prueba de fracciones heterogéneas
    print("- - - - FRACCIONES HETEROGÉNEAS - - - -")
    f1 = Fracciones()
    f1.setNumerador(2)
    f1.setDenominador(3)
    f1.verFraccion()

    f2 = Fracciones()
    f2.setNumerador(1)
    f2.setDenominador(5)
    f2.verFraccion()

    calculo1 = CalculadoraFracciones()
    calculo1.setF1(f1)
    calculo1.setF2(f2)

    calculo1.sumaHeterogenea()
    calculo1.restaHeterogenea()
    calculo1.multiplicacion()
    calculo1.division()

    # Prueba de fracciones homogéneas
    print("- - - - FRACCIONES HOMOGÉNEAS - - - -")
    f3 = Fracciones()
    f3.setNumerador(3)
    f3.setDenominador(7)
    f3.verFraccion()

    f4 = Fracciones()
    f4.setNumerador(4)
    f4.setDenominador(7)
    f4.verFraccion()

    calculo1 = CalculadoraFracciones()
    calculo1.setF1(f3)
    calculo1.setF2(f4)

    calculo1.sumaHomogenea()
    calculo1.restaHomogenea()
    calculo1.multiplicacion()
    calculo1.division()
    
main()
