class Personas:
    def __init__(self):
        self.__id = 0
        self.__nombre = ""
        self.__apellido = ""
        self.__edad = 0
        self.__email = ""

    def setNombre(self, nombre:str): 
        self.__nombre = nombre

    def getNombre(self): 
        return self.__nombre

    def setApellido(self, apellido:str):
        self.__apellido = apellido

    def getApellido(self): 
        return self.__apellido

    def setId(self, id:int): 
        self.__id = id

    def getId(self): 
        return self.__id

    def setEdad(self, edad:int): 
        self.__edad = edad

    def getEdad(self): 
        return self.__edad

    def setEmail(self, email:str): 
        self.__email = email

    def getEmail(self): 
        return self.__email

    def mostrarDatos(self):
        print(f"id persona: {self.getId()}")
        print(f"nombre persona: {self.getNombre()} {self.getApellido()}")
        print(f"edad persona: {self.getEdad()}")
        print(f"email persona: {self.getEmail()}")

class Empleados(Personas):
    def __init__(self):
        super().__init__()
        self.__cargo = ""
        self.__antiguedad = 0
        self.__profesion = ""

    def setCargo(self, cargo:str):
        self.__cargo = cargo

    def getCargo(self): 
        return self.__cargo

    def setAntiguedad(self, antiguedad:int):
        self.__antiguedad = antiguedad

    def getAntiguedad(self): 
        return self.__antiguedad

    def setProfesion(self, profesion:str):
        self.__profesion = profesion

    def getProfesion(self): 
        return self.__profesion

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"cargo empleado: {self.getCargo()}")
        print(f"antiguedad empleado: {self.getAntiguedad()}")
        print(f"profesion empleado: {self.getProfesion()}")

class TiempoCompleto(Empleados):
    def __init__(self):
        super().__init__()
        self.__horas = 0
        self.__area = ""

    def setHoras(self, horas:int):
        self.__horas = horas

    def getHoras(self): 
        return self.__horas

    def setArea(self, area:str):
        self.__area = area

    def getArea(self): 
        return self.__area

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"horas tiempo completo: {self.getHoras()}")
        print(f"area tiempo completo: {self.getArea()}")

class PorObraLabor(Empleados):
    def __init__(self):
        super().__init__()  
        self.__labor = ""
        self.__inicio = ""
        self.__final = ""

    def setLabor(self, labor:str):
        self.__labor = labor

    def getLabor(self): 
        return self.__labor

    def setInicio(self, inicio:str):
        self.__inicio = inicio

    def getInicio(self): 
        return self.__inicio
    
    def setFinal(self, final:str):
        self.__final = final

    def getFinal(self): 
        return self.__final

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"labor empleado: {self.getLabor()}")
        print(f"inicio labor: {self.getInicio()}")
        print(f"final labor: {self.getFinal()}")

class Estudiantes(Personas):
    def __init__(self):
        super().__init__()
        self.__sede = ""
        self.__materias = 0

    def setSede(self, sede:str):
        self.__sede = sede

    def getSede(self): 
        return self.__sede

    def setMaterias(self, materias:int):
        self.__materias = materias

    def getMaterias(self): 
        return self.__materias

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"sede estudiante: {self.getSede()}")
        print(f"numero materias: {self.getMaterias()}")

class Secundaria(Estudiantes):
    def __init__(self):
        super().__init__()
        self.__docente = ""
        self.__curso = ""
    
    def setDocente(self, docente:str):
        self.__docente = docente

    def getDocente(self): 
        return self.__docente
    
    def setCurso(self, curso:str):
        self.__curso = curso

    def getCurso(self): 
        return self.__curso

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"docente secundaria: {self.getDocente()}")
        print(f"grado secundaria: {self.getCurso()}")

class Universitario(Estudiantes):
    def __init__(self):
        super().__init__()
        self.__carrera = ""
        self.__creditos = 0

    def setPrograma(self, programa:str):
        self.__carrera = programa

    def getPrograma(self): 
        return self.__carrera

    def setCreditos(self, creditos:int):
        self.__creditos = creditos

    def getCreditos(self): 
        return self.__creditos

    def mostrarDatos(self):
        super().mostrarDatos()
        print(f"programa universitario: {self.getPrograma()}")
        print(f"numero creditos universitario: {self.getCreditos()}")

def main():
    persona1 = Personas()
    persona1.setNombre("Edgar")
    persona1.setApellido("Mercado")
    persona1.setId(34165)
    persona1.setEdad(20)
    persona1.setEmail("edgar@cuc.edu.co")
    persona1.mostrarDatos()
    print("\n")

    empleado1 = Empleados()
    empleado1.setNombre("Juan")
    empleado1.setApellido("Conde")
    empleado1.setId(745)
    empleado1.setEdad(22)
    empleado1.setEmail("juan@cuc.edu.co")
    empleado1.setCargo("Mantenimento de laptos")
    empleado1.setAntiguedad(2019)
    empleado1.setProfesion("tecnico en mantenimiento de computadoras")
    empleado1.mostrarDatos()
    print("\n")

    empleado2 = TiempoCompleto()
    empleado2.setNombre("Sofia")
    empleado2.setApellido("Ruiz")
    empleado2.setId(66354)
    empleado2.setEdad(30)
    empleado2.setEmail("madeleyne@cuc.edu.co")
    empleado2.setCargo("Diseño de pagina web")
    empleado2.setAntiguedad(2020)
    empleado2.setProfesion("Ingeniería de sistema")
    empleado2.setHoras(150)
    empleado2.setArea("Software")
    empleado2.mostrarDatos()
    print("\n")

    empleado3 = PorObraLabor()
    empleado3.setNombre("Julio")
    empleado3.setApellido("Arellano")
    empleado3.setId(15145)
    empleado3.setEdad(23)
    empleado3.setEmail("julio@cuc.edu.co")
    empleado3.setCargo("Diseño de bd")
    empleado3.setAntiguedad(2015)
    empleado3.setProfesion("Ingeniería de sistema")
    empleado3.setLabor("Crear una base de datos")
    empleado3.setInicio("7-7-2022")
    empleado3.setFinal("15-12-2022")
    empleado3.mostrarDatos()
    print("\n")

    estudiante1 = Estudiantes()
    estudiante1.setNombre("Ovier")
    estudiante1.setApellido("Jiménez")
    estudiante1.setId(9522)
    estudiante1.setEdad(19)
    estudiante1.setEmail("ovier@cuc.edu.co")
    estudiante1.setSede("indem")
    estudiante1.setMaterias(6)
    estudiante1.mostrarDatos()
    print("\n")

    estudiante2 = Secundaria()
    estudiante2.setNombre("José")
    estudiante2.setApellido("De la Hoz")
    estudiante2.setId(5652)
    estudiante2.setEdad(15)
    estudiante2.setEmail("jose@cuc.edu.co")
    estudiante2.setSede("agropecuario")
    estudiante2.setMaterias("artistica")
    estudiante2.setDocente("Rebeca López")
    estudiante2.setCurso("9-02")
    estudiante2.mostrarDatos()
    print("\n")

    estudiante3 = Universitario()
    estudiante3.setNombre("James")
    estudiante3.setApellido("Torres")
    estudiante3.setId(43466)
    estudiante3.setEdad(25)
    estudiante3.setEmail("james@cuc.edu.co")
    estudiante3.setSede("CUC")
    estudiante3.setMaterias("algoritmos 1")
    estudiante3.setPrograma("ingeniería de sistemas")
    estudiante3.setCreditos(160)
    estudiante3.mostrarDatos()

main()