# Calculadora fracciones

class Fraccionarios:
    def __init__(self):
        self.numerador = 0
        self.denominador = 0

    def set_numerador(self, x: int):
        self.numerador = x

    def get_numerador(self):
        return self.numerador
    
    def set_denominador(self, x: int):
        self.denominador = x

    def get_denominador(self):
        return self.denominador
    

class CalculadoraFraccionarios:
    def __init__(self):
        self.f1 = Fraccionarios()
        self.f2 = Fraccionarios()

    def set_f1(self, x: Fraccionarios):
        self.f1 = x

    def get_f1(self):
        return self.f1
    
    def set_f2(self, x: Fraccionarios):
        self.f2 = x

    def get_f2(self):
        return self.f2
    
    def suma_heterogenea(self):
        numerador = (self.f1.get_numerador() * self.f2.get_denominador()) + (self.f1.get_denominador() * self.f2.get_numerador())
        denominador = self.f1.get_denominador() * self.f2.get_denominador()
        print(f"Suma heterogénea: {numerador} / {denominador} = {numerador / denominador}")
    
    def suma_homogenea(self):
        numerador = self.f1.get_numerador() + self.f1.get_numerador()
        denominador = self.f1.get_denominador()
        print(f"Suma homogénea: {numerador} / {denominador} = {numerador / denominador}")

    def resta_heterogenea(self):
        numerador = (self.f1.get_numerador() * self.f2.get_denominador()) - (self.f1.get_denominador() * self.f2.get_numerador())
        denominador = self.f1.get_denominador() * self.f2.get_denominador()
        print(f"Resta heterogénea: {numerador} / {denominador} = {numerador / denominador}")
    
    def resta_homogenea(self):
        numerador = self.f1.get_numerador() - self.f2.get_numerador()
        denominador = self.f1.get_denominador()
        print(f"Resta heterogénea: {numerador} / {denominador} = {numerador / denominador}")

    def multiplicacion(self):
        numerador = self.f1.get_numerador() * self.f2.get_numerador()
        denominador = self.f1.get_denominador() * self.f2.get_denominador()
        print(f"Multiplicación: {numerador} / {denominador} = {numerador / denominador}")

    def division(self):
        numerador = self.f1.get_numerador() * self.f2.get_denominador()
        denominador = self.f1.get_denominador() * self.f2.get_numerador()
        print(f"División: {numerador} / {denominador} = {numerador / denominador}")


def main():
    f1 = Fraccionarios()
    f1.set_numerador(4)
    f1.set_denominador(9)

    f2 = Fraccionarios()
    f2.set_numerador(3)
    f2.set_denominador(7)

    calculo1 = CalculadoraFraccionarios()
    calculo1.set_f1(f1)
    calculo1.set_f2(f2)

    calculo1.suma_heterogenea()
    # calculo1.suma_homogenea()
    calculo1.resta_heterogenea()
    # calculo1.resta_homogenea()
    calculo1.multiplicacion()
    calculo1.division()

main()
