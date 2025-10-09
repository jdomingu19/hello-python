class Padre:
    def __init__(self):
        self.nombre = None
        self.apellido = None

    def set_nombre(self, x:str):
        self.nombre = x

    def get_nombre(self):
        return self.nombre  

    def set_apellido(self, x:str):
        self.apellido = x

    def get_apellido(self):
        return self.apellido

    def saludar(self):
        print(f"¡Hola soy {self.get_nombre()} {self.get_apellido()}!")    

class Hijo(Padre):
    def __init__(self):
        super().__init__() # Hereda atributos del padre
        self.juguete = None # Atributos EXCLUSIVOS del hijo

    def set_juguete(self, x:str):
        self.juguete = x

    def get_juguete(self):
        return self.juguete

    def saludar(self):
        super().saludar() # SOBREESCRIBE el método saludar de padre
        print(f"Y mi juguete es: {self.get_juguete()}")

def main():
    padre_1 = Padre()
    padre_1.set_nombre("Deiner")
    padre_1.set_apellido("Domínguez")
    padre_1.saludar()

    print("\n")

    hijo_1 = Hijo()
    hijo_1.set_nombre("Jesús")
    hijo_1.set_apellido("Domínguez")
    hijo_1.set_juguete("Cubo de Rubik")
    hijo_1.saludar()

main()