class Vehiculos:
    def __init__(self):
        self.alto = 0
        self.ancho = 0
        self.color = ""
        self.motores = 0

    def set_alto(self, alto:eval):
        self.alto = alto

    def get_alto(self):
        return self.alto

    def set_ancho(self, ancho:eval):
        self.ancho = ancho

    def get_ancho(self):
        return self.ancho

    def set_color(self, color:str):
        self.color = color

    def get_color(self):
        return self.color

    def imprimir(self):
        print("alto vehiculo: " + str(self.get_alto()) + " m")
        print("ancho vehiculo: " + str(self.get_ancho()) + " m")
        print("color vehiculo: " + self.get_color())

class Autos(Vehiculos):
    def __init__(self):
        super().__init__()
        self.aire_acondicionado = False
        self.radio = False

    def set_aire_acondicionado(self, aire:bool):
        self.aire_acondicionado = aire

    def get_aire_acondicionado(self):
        return self.aire_acondicionado

    def set_radio(self, radio:bool):
        self.radio = radio

    def get_radio(self):
        return self.radio

    def imprimir(self):
        super().imprimir()
        print("Aire acondicionado auto: " + str(self.get_aire_acondicionado()))
        print("Radio auto: " + str(self.get_radio()))

class Motos(Vehiculos):
    def __init__(self):
        super().__init__()
        self.tiempos = 0

    def set_tiempos(self, tiempos:int):
        self.tiempos = tiempos

    def get_tiempos(self):
        return self.tiempos

    def imprimir(self):
        super().imprimir()
        print("numero tiempos moto: " + str(self.get_tiempos()))
        
def main():
    vehiculo_1 = Vehiculos()
    vehiculo_1.set_alto(2.5)
    vehiculo_1.set_ancho(3.0)
    vehiculo_1.set_color("azul")
    vehiculo_1.imprimir()
    print("")
    carro_1 = Autos()
    carro_1.set_alto(1.7)
    carro_1.set_ancho(2.6)
    carro_1.set_color("blanco")
    carro_1.set_aire_acondicionado(True)
    carro_1.set_radio(True)
    carro_1.imprimir()
    print("")
    moto_1 = Motos()
    moto_1.set_alto(1.7)
    moto_1.set_ancho(2.6)
    moto_1.set_color("blanco")
    moto_1.set_tiempos(4)
    moto_1.imprimir()
main()