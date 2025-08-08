# Ejercicio 2
import math

class Circulo():
    def __init__(self, radio):
        self.__radio = radio

    def set_radio(self, radio):
        self.__radio = radio

    def get_radio(self):
        return self.__radio

    def get_area(self):
        area = 2 * self.get_radio()
        return area

    def get_circunferencia(self):
        circunferencia = round(2 * math.pi * self.get_area(), 2)
        return circunferencia

def main():
    print("OBJETO 1")
    a = Circulo(3)
    print(f"Radio círculo: {a.get_radio()}")
    print(f"Área círculo: {a.get_area()}")
    print(f"Circunferencia círculo: {a.get_circunferencia()}")
    print("")

    print("OBJETO 2")
    b = Circulo(4)
    print(f"Radio círculo: {b.get_radio()}")
    print(f"Área círculo: {b.get_area()}")
    print(f"Circunferencia círculo: {b.get_circunferencia()}")
    print("")

main()