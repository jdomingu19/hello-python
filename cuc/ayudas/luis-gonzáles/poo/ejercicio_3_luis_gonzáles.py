# ejercicio 3 Luis Gonzáles

class Figura():
    def __init__(self, color, nombre):
        self.__color = color
        self.__nombre = nombre

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

class Rectangulo(Figura):
    def __init__(self, largo, ancho):
        self.__largo = largo
        self.__ancho = ancho

    def get_largo(self):
        return self.__largo

    def get_ancho(self):
        return self.__ancho

    def calcular_area(self):
        area = self.get_largo() * self.get_ancho()
        return area

    def calcular_perimetro(self):
        perimetro = 2 * (self.get_largo() + self.get_ancho())
        return perimetro

class Triangulo(Figura):
    def __init__(self, altura, base, lado1, lado2, lado3):
        self.__altura = altura
        self.__base = base
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    def get_altura(self):
        return self.__altura

    def get_base(self):
        return self.__base

    def get_lado1(self):
        return self.__lado1
    
    def get_lado2(self):
        return self.__lado2
    
    def get_lado3(self):
        return self.__lado3

    def calcular_area(self):
        area = (self.get_base() * self.get_altura()) / 2
        return area

    def calcular_perimetro(self):
        perimetro = self.get_lado1() + self.get_lado2() + self.get_lado3()
        return perimetro

def main():
    print("FIGURA 1")
    a = Rectangulo(1,2)
    a.set_color("Azul")
    a.set_nombre("Rectángulo")
    print(f"Nombre: {a.get_nombre()}")
    print(f"Color: {a.get_color()}")
    print(f"Largo: {a.get_largo()}")
    print(f"Ancho: {a.get_ancho()}")
    print(f"Área: {a.calcular_area()}")
    print(f"Perímetro: {a.calcular_perimetro()}")
    print("")

    print("FIGURA 2")
    b = Triangulo(3,4,2,4,5)
    b.set_color("Rojo")
    b.set_nombre("Triángulo")
    print(f"Nombre: {b.get_nombre()}")
    print(f"Color: {b.get_color()}")
    print(f"Altura: {b.get_altura()}")
    print(f"Base: {b.get_base()}")
    print(f"Lado 1: {b.get_lado1()}")
    print(f"Lado 2: {b.get_lado2()}")
    print(f"Lado 3: {b.get_lado3()}")
    print(f"Área: {b.calcular_area()}")
    print(f"Perímetro: {b.calcular_perimetro()}")
main()