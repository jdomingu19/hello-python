# Fracciones | POO | 1.0

# Importaciones necesarias
from random import randint

# Clase CREADORA de fracciones
class Fraciones():
    def __init__(self):
        self.__numerador = 0
        self.__denominador = 0
    
    def setNumerador(self, x:int):
        self.__numerador = x

    def getNumerador(self):
        return self.__numerador

    def setDenominador(self, x:int):
        self.__denominador = x

    def getDenominador(self):
        return self.__denominador

    def llenarAleatoriamente(self):
        numerador = randint(1, 20)
        denominador = randint(1, 20)
        self.setNumerador(numerador)
        self.setDenominador(denominador)
    
    def imprimirFraccion(self, indice):
        print(f"Fracción {indice}: {self.getNumerador()} / {self.getDenominador()}")

# Clase OPERADORA de fracciones
class OperadoraFracciones(Fraciones):
    def __init__(self):
        self.f1 = Fraciones()
        self.f2 = Fraciones()

    def setF1(self, x:Fraciones()):
        self.f1 = x

    def getF1(self):
        return self.f1

    def setF2(self, x:Fraciones()):
        self.f2 = x

    def getF2(self):
        return self.f2
      
    # Suma HETEROGÉNEA
    def sumaFraccionesHeterogeneas(self):
        numerador = (self.f1.getNumerador() * self.f2.getDenominador()) + (self.f1.getDenominador() * self.f2.getNumerador())
        denominador = self.f1.getDenominador() * self.f2.getDenominador()
        print(f"Suma heterogénea: {numerador} / {denominador} = {round(numerador / denominador, 2)}")

    # Suma HOMOGÉNEAS
    def sumaFraccionesHomogeneas(self):
        numerador = self.f1.getNumerador() + self.f2.getNumerador()
        denominador = self.f1.getDenominador()
        print(f"Suma homogénea: {numerador} / {denominador} = {round(numerador / denominador, 2)}")

    # Resta HETEROGÉNEA
    def restaFraccionesHeterogeneas(self):
        numerador = (self.f1.getNumerador() * self.f2.getDenominador()) - (self.f1.getDenominador() * self.f2.getNumerador())
        denominador = self.f1.getDenominador() * self.f2.getDenominador()
        print(f"Resta heterogénea: {numerador} / {denominador} = {round(numerador / denominador, 2)}")

    # Resta HOMOGÉNEAS
    def restaFraccionesHomogeneas(self):
        numerador = self.f1.getNumerador() - self.f2.getNumerador()
        denominador = self.f1.getDenominador()
        print(f"Resta homogénea: {numerador} / {denominador} = {round(numerador / denominador, 2)}")

    # Multiplicación
    def multiplicacionFracciones(self):
        numerador = self.f1.getNumerador() * self.f2.getNumerador()
        denominador = self.f1.getDenominador() * self.f2.getDenominador()
        print(f"Multiplicación: {numerador} / {denominador} = {round(numerador / denominador, 2)}")

    # División
    def divisionFracciones(self):
        numerador = self.f1.getNumerador() * self.f2.getDenominador()
        denominador = self.f1.getDenominador() * self.f2.getNumerador()
        print(f"División: {numerador} / {denominador} = {round(numerador / denominador, 2)}")

# Método principal de pruebas
def main():
    a = Fraciones()
    a.llenarAleatoriamente()
    a.imprimirFraccion(1)

    b = Fraciones()
    b.llenarAleatoriamente()
    b.imprimirFraccion(2)

    c = OperadoraFracciones()
    c.setF1(a)
    c.setF2(b)
    c.sumaFraccionesHeterogeneas()
    #c.sumaFraccionesHomogeneas()
    c.restaFraccionesHeterogeneas()
    #c.restaFraccionesHomogeneas()
    c.multiplicacionFracciones()
    c.divisionFracciones()
    
# Llamar método principal
main()