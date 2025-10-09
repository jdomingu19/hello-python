class Personas:
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.apellido = ""
        self.edad = 0
        self.email = ""

    def set_Nombre(self, nombre:str): 
        self.nombre = nombre

    def get_Nombre(self): 
        return self.nombre

    def set_Apellido(self, apellido:str):
        self.apellido = apellido

    def get_Apellido(self): 
        return self.apellido

    def set_Id(self, id:int): 
        self.id = id

    def get_Id(self): 
        return self.id

    def set_Edad(self, edad:int): 
        self.edad = edad

    def get_Edad(self): 
        return self.edad

    def set_Email(self, email:str): 
        self.email = email

    def get_Email(self): 
        return self.email

    def imprimir(self):
        print("Id:", self.get_Id())
        print("Nombre:", self.get_Nombre(), self.get_Apellido())
        print("Edad:", self.get_Edad())
        print("Email:", self.get_Email())

class Empleados(Personas):
    def __init__(self):
        super().__init__()
        self.cargo = ""
        self.antiguedad = 0
        self.profesion = ""

    def set_Cargo(self, cargo:str):
        self.cargo = cargo

    def get_Cargo(self): 
        return self.cargo

    def set_Antiguedad(self, antiguedad:int):
        self.antiguedad = antiguedad

    def get_Antiguedad(self): 
        return self.antiguedad

    def set_Profesion(self, profesion:str):
        self.profesion = profesion

    def get_Profesion(self): 
        return self.profesion

    def imprimir(self):
        super().imprimir()
        print("Cargo:", self.get_Cargo())
        print("Antiguedad:", self.get_Antiguedad())
        print("Profesion:", self.get_Profesion())

class TiempoCompleto(Empleados):
    def __init__(self):
        super().__init__()
        self.horas = 0
        self.area = ""

    def set_Horas(self, horas:int):
        self.horas = horas

    def get_Horas(self): 
        return self.horas

    def set_Area(self, area:str):
        self.area = area

    def get_Area(self): 
        return self.area

    def imprimir(self):
        super().imprimir()
        print("Horas:", self.get_Horas())
        print("Área formación:", self.get_Area())

class PorObraLabor(Empleados):
    def __init__(self):
        super().__init__()  
        self.labor = ""
        self.inicio = ""
        self.final = ""

    def set_Labor(self, labor:str):
        self.labor = labor

    def get_Labor(self): 
        return self.labor

    def set_Inicio(self, inicio:str):
        self.inicio = inicio

    def get_Inicio(self): 
        return self.inicio
    
    def set_Final(self, final:str):
        self.final = final

    def get_Final(self): 
        return self.final

    def imprimir(self):
        super().imprimir()
        print("Labor:", self.get_Labor())
        print("Inicio labor:", self.get_Inicio())
        print("Final labor:", self.get_Final())

class Estudiantes(Personas):
    def __init__(self):
        super().__init__()
        self.sede = ""
        self.materias = 0

    def set_Sede(self, sede:str):
        self.sede = sede

    def get_Sede(self): 
        return self.sede

    def set_Materias(self, materias:int):
        self.materias = materias

    def get_Materias(self): 
        return self.materias

    def imprimir(self):
        super().imprimir()
        print("Sede:", self.get_Sede())
        print("Materias:", self.get_Materias())

class Secundaria(Estudiantes):
    def __init__(self):
        super().__init__()
        self.docente = ""
        self.curso = ""
    
    def set_Docente(self, docente:str):
        self.docente = docente

    def get_Docente(self): 
        return self.docente
    
    def set_Curso(self, curso:str):
        self.curso = curso

    def get_Curso(self): 
        return self.curso

    def imprimir(self):
        super().imprimir()
        print("Docente:", self.get_Docente())
        print("Grado:", self.get_Curso())

class Universitario(Estudiantes):
    def __init__(self):
        super().__init__()
        self.carrera = ""
        self.creditos = 0

    def set_Programa(self, programa:str):
        self.carrera = programa

    def get_Programa(self): 
        return self.carrera

    def set_Creditos(self, creditos:int):
        self.creditos = creditos

    def get_Creditos(self): 
        return self.creditos

    def imprimir(self):
        super().imprimir()
        print("Programa:", self.get_Programa())
        print("Número créditos:", self.get_Creditos())

def main():
    ejemplo_1 = Personas()
    ejemplo_1.set_Nombre("Edgar")
    ejemplo_1.set_Apellido("Mercado")
    ejemplo_1.set_Id(34165)
    ejemplo_1.set_Edad(20)
    ejemplo_1.set_Email("edgar@cuc.edu.co")
    ejemplo_1.imprimir()
    print("\n")

    empleado_1 = Empleados()
    empleado_1.set_Nombre("Juan")
    empleado_1.set_Apellido("Conde")
    empleado_1.set_Id(745)
    empleado_1.set_Edad(22)
    empleado_1.set_Email("juan@cuc.edu.co")
    empleado_1.set_Cargo("Mantenimento de laptos")
    empleado_1.set_Antiguedad(2019)
    empleado_1.set_Profesion("tecnico en mantenimiento de computadoras")
    empleado_1.imprimir()
    print("\n")

    empleado_2 = TiempoCompleto()
    empleado_2.set_Nombre("Sofia")
    empleado_2.set_Apellido("Ruiz")
    empleado_2.set_Id(66354)
    empleado_2.set_Edad(30)
    empleado_2.set_Email("madeleyne@cuc.edu.co")
    empleado_2.set_Cargo("Diseño de pagina web")
    empleado_2.set_Antiguedad(2020)
    empleado_2.set_Profesion("Ingeniería de sistema")
    empleado_2.set_Horas(150)
    empleado_2.set_Area("Software")
    empleado_2.imprimir()
    print("\n")

    empleado_3 = PorObraLabor()
    empleado_3.set_Nombre("Julio")
    empleado_3.set_Apellido("Arellano")
    empleado_3.set_Id(15145)
    empleado_3.set_Edad(23)
    empleado_3.set_Email("julio@cuc.edu.co")
    empleado_3.set_Cargo("Diseño de bd")
    empleado_3.set_Antiguedad(2015)
    empleado_3.set_Profesion("Ingeniería de sistema")
    empleado_3.set_Labor("Crear una base de datos")
    empleado_3.set_Inicio("7-7-2022")
    empleado_3.set_Final("15-12-2022")
    empleado_3.imprimir()
    print("\n")

    estudiante_1 = Estudiantes()
    estudiante_1.set_Nombre("Ovier")
    estudiante_1.set_Apellido("Jiménez")
    estudiante_1.set_Id(9522)
    estudiante_1.set_Edad(19)
    estudiante_1.set_Email("ovier@cuc.edu.co")
    estudiante_1.set_Sede("indem")
    estudiante_1.set_Materias(6)
    estudiante_1.imprimir()
    print("\n")

    estudiante_2 = Secundaria()
    estudiante_2.set_Nombre("José")
    estudiante_2.set_Apellido("De la Hoz")
    estudiante_2.set_Id(5652)
    estudiante_2.set_Edad(15)
    estudiante_2.set_Email("jose@cuc.edu.co")
    estudiante_2.set_Sede("agropecuario")
    estudiante_2.set_Materias("artistica")
    estudiante_2.set_Docente("Rebeca López")
    estudiante_2.set_Curso("9-02")
    estudiante_2.imprimir()
    print("\n")

    estudiante_3 = Universitario()
    estudiante_3.set_Nombre("James")
    estudiante_3.set_Apellido("Torres")
    estudiante_3.set_Id(43466)
    estudiante_3.set_Edad(25)
    estudiante_3.set_Email("james@cuc.edu.co")
    estudiante_3.set_Sede("CUC")
    estudiante_3.set_Materias("algoritmos 1")
    estudiante_3.set_Programa("ingeniería de sistemas")
    estudiante_3.set_Creditos(160)
    estudiante_3.imprimir()

main()