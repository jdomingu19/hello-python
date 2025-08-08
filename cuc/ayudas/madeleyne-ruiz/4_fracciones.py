# Fracciones
class Fracciones:
    def __init__(self) -> None:
        self.__numerador = None
        self.__denominador = None

    def set_numerador(self, x:int):
        self.__numerador = x

    def get_numerador(self):
        return self.__numerador

    def set_denominador(self, x:int):
        self.__denominador = x

    def get_denominador(self):
        return self.__denominador

    def mostrar(self):
        x = round(self.get_numerador() / self.get_denominador(), 2)
        print(f"{self.get_numerador()} / {self.get_denominador()} = {x}")

def main():
    fraccion_1 = Fracciones()
    fraccion_1.set_numerador(10)
    fraccion_1.set_denominador(5)
    fraccion_1.mostrar()

main()