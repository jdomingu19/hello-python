# Ejercicio 1

class Persona():
    def __init__(self, nombre, edad, numDocumento, sexo, peso, altura):
        self.__nombre = nombre
        self.__edad = edad
        self.__numDocumento = numDocumento
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre
    
    def set_edad(self, edad):
        self.__edad = edad

    def get_edad(self):
        return self.__edad

    def set_numDocumento(self, numDocumento):
        self.__numDocumento = numDocumento

    def get_numDocumento(self):
        return self.__numDocumento
    
    def set_sexo(self, sexo):
        self.__sexo = sexo

    def get_sexo(self):
        return self.__sexo

    def set_peso(self, peso):
        self.__peso = peso

    def get_peso(self):
        return self.__peso
    
    def set_altura(self, altura):
        self.__altura = altura

    def get_altura(self):
        return self.__altura

    def calcularIMC(self):
        imc = round(self.get_peso() / (self.get_altura() ** 2), 2)
        if imc < 20:
            return f"{imc}, Por debajo del peso"
        elif imc >= 20 and imc <= 25:
            return f"{imc}, Peso normal"
        else:
            return f"{imc}, Sobrepeso"

    def esMayorEdad(self):
        if self.get_edad() >= 18:
            return True
        else:
            return False

    def comprobarSexo(self):
        if self.get_sexo() != "H" and self.get_sexo() != "M":
            self.set_sexo("H")
            return "H"
        else:
            return self.get_sexo()

def main():
    persona1 = Persona("Marcelino", 19, 123, "H", 70, 1.78)
    print(f"IMC: {persona1.calcularIMC()}")
    print(f"MAYOR DE EDAD: {persona1.esMayorEdad()}")
    print(f"COMPROBAR SEXO: {persona1.comprobarSexo()}")
main()