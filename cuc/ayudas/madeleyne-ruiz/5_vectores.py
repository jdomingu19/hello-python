class Vectores:
    def __init__(self) -> None:
        self.vector = []

    def set_vector(self, x:list):
        self.vector = x

    def get_vector(self):
        return self.vector

    def llenar(self):
        n = int(input("Ingrese cantidad elementos: "))