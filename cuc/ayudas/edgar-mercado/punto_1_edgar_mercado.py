class Vehiculos:
    def __init__(self):
        self.altura = 0
        self.anchura = 0
        self.color = ""

    def setAltura(self, x:eval):
        self.altura = x

    def getAltura(self):
        return self.altura

    def setAnchura(self, x:eval):
        self.anchura = x

    def getAnchura(self):
        return self.anchura

    def setColor(self, x:str):
        self.color = x

    def getColor(self):
        return self.color

    def informacion(self):
        print(f"Altura: {self.altura} metros")
        print(f"Anchura: {self.anchura} metros")
        print(f"Color: {self.color}")

class Carros(Vehiculos):
    def __init__(self):
        super().__init__()
        self.ruedas = 0

    def setRuedas(self, x:eval):
        self.ruedas = x

    def getRuedas(self):
        return self.ruedas

    def informacion(self):
        super().informacion()
        print(f"Ruedas: {self.ruedas}")

def main():
    vehiculo1 = Vehiculos()
    vehiculo1.setAltura(1.7)
    vehiculo1.setAnchura(2.6)
    vehiculo1.setColor("negro")
    vehiculo1.informacion()

    print("")

    carro1 = Carros()
    carro1.setAltura(1.7)
    carro1.setAnchura(2.6)
    carro1.setColor("blanco")
    carro1.setRuedas(4)
    carro1.informacion()

main()