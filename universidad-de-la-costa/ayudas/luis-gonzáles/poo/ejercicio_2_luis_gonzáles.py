# ejercicio 2 de Luis Gonzáles
import math as mt

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
        circunferencia = round(2 * mt.pi * self.get_area(), 3)
        return circunferencia

def main():
    print("CÍRCULO 1")
    a = Circulo(2)
    print(f"Radio: {a.get_radio()}")
    print(f"Área: {a.get_area()}")
    print(f"Circunferencia: {a.get_circunferencia()}")
    print("")

    print("CÍRCULO 2")
    b = Circulo(5)
    print(f"Radio: {b.get_radio()}")
    print(f"Área: {b.get_area()}")
    print(f"Circunferencia: {b.get_circunferencia()}")
    print("")

main()