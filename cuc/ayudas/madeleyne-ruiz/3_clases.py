class Personas:
    # Constructor ESTÁTICO
    """def __init__(self, x, y, z):
        self.nombre = x
        self.apellido = y
        self.edad = z"""
    
    # Constructor DINÁMICO
    def __init__(self):
        self.__nombre = None
        self.__apellido = None
        self.__edad = None

    # sets
    def set_nombre(self, x):
        self.__nombre = x

    def set_apellido(self, x):
        self.__apellido = x

    def set_edad(self, x):
        self.__edad = x

    # gets
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_edad(self):
        return self.__edad

# Objeto 1
# persona_1 = Personas("Madeleyne", "Ruiz", 19) ESTÁTICO
persona_1 = Personas()
persona_1.set_nombre("Madeleyne")
persona_1.set_apellido("Ruiz")
persona_1.set_edad(19)

print("Nombre:", persona_1.get_nombre())
print("Apellido:", persona_1.get_apellido())
print("Edad:", persona_1.get_edad(), "\n")

# Objeto 2
persona_2 = Personas()

nombre = input("Ingrese nombre persona_2: ") # str
apellido = input("Ingrese apellido persona_2: ") # str
edad = int(input("Ingrese edad persona_2: ")) # str -> int

persona_2.set_nombre(nombre)
persona_2.set_apellido(apellido)
persona_2.set_edad(edad)

print("Nombre:", persona_2.get_nombre())
print("Apellido:", persona_2.get_apellido())
print("Edad:", persona_2.get_edad())