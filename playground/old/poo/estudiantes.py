# Estudiantes | Versión 1.0

"""
estudiante.tipoDocumento
estudiante.id
estudiante.nombre
estudiante.apellido

estudiante.nota1
estudiante.nota2
estudiante.nota3
estudiante.notaFinal
"""

class Estudiantes():
    def __init__(self):
        self.__tipoDocumento = "N/A"
        self.__id = 0
        self.__nombre = "N/A" 
        self.__apellido = "N/A"

        self.__nota1 = 0
        self.__nota2 = 0
        self.__nota3 = 0
        self.__notaFinal = 0

    def setTipoDocumento(self, x:str):
        self.__tipoDocumento = x

    def getTipoDocumento(self):
        return self.__tipoDocumento

    def setId(self, x:int):
        self.__id = x

    def getId(self):
        return self.__id
    
    def setNombre(self, x:str):
        self.__nombre = x

    def getNombre(self):
        return self.__nombre

    def setApellido(self, x:str):
        self.__apellido = x

    def getApellido(self):
        return self.__apellido

    def setNota1(self, x:float):
        self.__nota1 = x

    def getNota1(self):
        return self.__nota1

    def setNota2(self, x:float):
        self.__nota2 = x

    def getNota2(self):
        return self.__nota2

    def setNota3(self, x:float):
        self.__nota3 = x

    def getNota3(self):
        return self.__nota3

    def getNotaFinal(self):
        return self.__notaFinal

    def calcularNotaFinal(self):
        notaFinal = round((self.getNota1() + self.getNota2() + self.getNota3()) / 3, 2)
        self.__notaFinal = notaFinal

    def registrar(self):
        print(f"{self.getTipoDocumento()} | {self.getId()} | {self.getNombre()} {self.getApellido()} | {self.getNota1()} | {self.getNota2()} | {self.getNota3()} | {self.getNotaFinal()}")

def main():
    estudiante1 = Estudiantes()
    estudiante1.setTipoDocumento("CC")
    estudiante1.setId(1044602481)
    estudiante1.setNombre("Jesús Alberto")
    estudiante1.setApellido("Domínguez Charris")
    estudiante1.setNota1(4.5)
    estudiante1.setNota2(4.6)
    estudiante1.setNota3(4.7)
    estudiante1.calcularNotaFinal()
    estudiante1.registrar()
    
    estudiante2 = Estudiantes()
    estudiante2.setTipoDocumento("CC")
    estudiante2.setId(8498220)
    estudiante2.setNombre("Deiner de Jesús")
    estudiante2.setApellido("Domínguez Bolaño")
    estudiante2.setNota1(4.8)
    estudiante2.setNota2(4.9)
    estudiante2.setNota3(5.0)
    estudiante2.calcularNotaFinal()
    estudiante2.registrar()

    estudiante3 = Estudiantes()
    estudiante3.setTipoDocumento("CC")
    estudiante3.setId(22712443)
    estudiante3.setNombre("Elvia Cristina")
    estudiante3.setApellido("Charris Rúa")
    estudiante3.setNota1(4.9)
    estudiante3.setNota2(5.0)
    estudiante3.setNota3(5.0)
    estudiante3.calcularNotaFinal()
    estudiante3.registrar()
    
    estudiante4 = Estudiantes()
    estudiante4.setTipoDocumento("TI")
    estudiante4.setId(1043563475)
    estudiante4.setNombre("Santiago Andrés")
    estudiante4.setApellido("Domínguez Charris")
    estudiante4.setNota1(5.0)
    estudiante4.setNota2(5.0)
    estudiante4.setNota3(5.0)
    estudiante4.calcularNotaFinal()
    estudiante4.registrar()

main()