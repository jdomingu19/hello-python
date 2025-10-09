class Persona:
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.identificacion = 0
        self.edad = 0
        self.correo = "None"

    def setNombre(self, x:str): 
        self.nombre = x

    def getNombre(self): 
        return self.nombre

    def setApellido(self, x:str):
        self.apellido = x

    def getApellido(self): 
        return self.apellido

    def setIdentificacion(self, x:int): 
        self.identificacion = x

    def getIdentificacion(self): 
        return self.identificacion

    def setEdad(self, x:int): 
        self.edad = x

    def getEdad(self): 
        return self.edad

    def setCorreo(self, x:str): 
        self.correo = x

    def getCorreo(self): 
        return self.correo

    def imprimirDatos(self):
        print(f"Nombre: {self.nombre} | Identificación: {self.identificacion} | Edad: {self.edad} | Correo: {self.correo}")

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.cargo = ""
        self.antiguedad = 0
        self.profesion = ""
    
    def setCargo(self, x:str): 
        self.cargo = x

    def getCargo(self): 
        return self.cargo

    def setAntiguedad(self, x:int): 
        self.antiguedad = x

    def getAntiguedad(self): 
        return self.antiguedad

    def setProfesion(self, x:str): 
        self.profesion = x

    def getProfesion(self): 
        return self.profesion

    def imprimirDatos(self):
        super().imprimirDatos()
        print(f"Cargo: {self.cargo} | Antiguedad: {self.antiguedad} | Profesión: {self.profesion}")

class TiempoCompleto(Empleado):
    def __init__(self):
        super().__init__()
        self.areaFormacion = ""
        self.horas = 0

    def setAreaFormacion(self, x:str): 
        self.areaFormacion = x

    def getAreaFormacion(self): 
        return self.areaFormacion

    def setHoras(self, x:int): 
        self.horas = x

    def getHoras(self): 
        return self.horas

    def imprimirDatos(self):
        super().imprimirDatos()
        print(f"Área formación: {self.areaFormacion} | Horas: {self.horas}")

class PorObraLabor(Empleado):
    def __init__(self):
        super().__init__()
        self.obra = ""
        self.fechaLimite = ""

    def setObra(self, x:str): 
        self.obra = x

    def getObra(self): 
        return self.obra

    def setFechaLimite(self, x:int): 
        self.fechaLimite = x

    def getFechaLimite(self): 
        return self.fechaLimite

    def imprimirDatos(self):
        super().imprimirDatos()
        print(f"Obra: {self.obra} | Fecha límite: {self.fechaLimite}")

class Estudiante(Persona):
    def __init__(self):
        super().__init__()
        self.lugar = ""
        self.profesorFavorito = ""

    def setLugar(self, x:str): 
        self.lugar = x

    def getLugar(self): 
        return self.lugar

    def setProfesorFavorito(self, x:str): 
        self.profesorFavorito = x

    def getProfesorFavorito(self): 
        return self.profesorFavorito

    def imprimirDatos(self):
        super().imprimirDatos()
        print(f"Lugar: {self.lugar} | Profesor favorito: {self.profesorFavorito}")

class Secundaria(Estudiante):
    def __init__(self):
        super().__init__()
        self.grupo = ""
        self.promocion = 0
    
    def setGrupo(self, x:str): 
        self.grupo = x

    def getGrupo(self): 
        return self.grupo

    def setPromocion(self, x:int): 
        self.promocion = x

    def getPromocion(self): 
        return self.promocion

    def imprimirDatos(self):
        super().imprimirDatos()
        print(f"Grupo: {self.grupo} | Promoción: {self.promocion}")

class Universitario(Estudiante):
    def __init__(self):
        super().__init__()
        self.programa = ""
        self.creditos = 0
        self.numSemestres = 0

    def setPrograma(self, x:str): 
        self.programa = x

    def getPrograma(self): 
        return self.programa

    def setCreditos(self, x:int): 
        self.creditos = x

    def getCreditos(self): 
        return self.creditos

    def setNumSemestres(self, x:int): 
        self.numSemestres = x

    def getNumSemestres(self): 
        return self.numSemestres

    def imprimirDatos(self):
        super().imprimirDatos()
        print(f"Programa: {self.programa} | Creditos: {self.creditos} | Número semestres: {self.numSemestres}")

def main():
    ejemplo1 = Persona()
    ejemplo1.setNombre("José")
    ejemplo1.setApellido("Martínez")
    ejemplo1.setIdentificacion("100235")
    ejemplo1.setEdad(18)
    ejemplo1.setCorreo("ejemplo1@gmail.com")
    ejemplo1.imprimirDatos()
    print("")

    ejemplo2 = Empleado()
    ejemplo2.setNombre("Juan")
    ejemplo2.setApellido("Mendoza")
    ejemplo2.setIdentificacion("200523")
    ejemplo2.setEdad(22)
    ejemplo2.setCorreo("ejemplo2@gmail.com")
    ejemplo2.setCargo("Limpieza de motores")
    ejemplo2.setAntiguedad(2002)
    ejemplo2.setProfesion("Ingeniero mecánico")
    ejemplo2.imprimirDatos()
    print("")

    ejemplo3 = TiempoCompleto()
    ejemplo3.setNombre("Sofía")
    ejemplo3.setApellido("Torres")
    ejemplo3.setIdentificacion("12453")
    ejemplo3.setEdad(19)
    ejemplo3.setCorreo("ejemplo3@gmail.com")
    ejemplo3.setCargo("Diseño de redes LAN")
    ejemplo3.setAntiguedad(2015)
    ejemplo3.setProfesion("Ingeniero de sistemas")
    ejemplo3.setAreaFormacion("Redes")
    ejemplo3.setHoras(7)
    ejemplo3.imprimirDatos()
    print("")

    ejemplo4 = PorObraLabor()
    ejemplo4.setNombre("María")
    ejemplo4.setApellido("Medina")
    ejemplo4.setIdentificacion("5436")
    ejemplo4.setEdad(132)
    ejemplo4.setCorreo("ejemplo4@gmail.com")
    ejemplo4.setCargo("Desarrolador de bases de datos")
    ejemplo4.setAntiguedad(2017)
    ejemplo4.setProfesion("Ingeniero de sistemas")
    ejemplo4.setObra("Crear base de datos SQL")
    ejemplo4.setFechaLimite("15-4-2023")
    ejemplo4.imprimirDatos()
    print("")

    ejemplo5 = Estudiante()
    ejemplo5.setNombre("Luis")
    ejemplo5.setApellido("Gonzáles")
    ejemplo5.setIdentificacion("78536")
    ejemplo5.setEdad(21)
    ejemplo5.setCorreo("ejemplo5@gmail.com")
    ejemplo5.setLugar("Colegio Sendero del Saber")
    ejemplo5.setProfesorFavorito("Juan Conde")
    ejemplo5.imprimirDatos()
    print("")

    ejemplo6 = Secundaria()
    ejemplo6.setNombre("Miguel")
    ejemplo6.setApellido("Torres")
    ejemplo6.setIdentificacion("78536")
    ejemplo6.setEdad(21)
    ejemplo6.setCorreo("ejemplo6@gmail.com")
    ejemplo6.setLugar("COLMETRO 2000")
    ejemplo6.setProfesorFavorito("Laura Ricardo")
    ejemplo6.setGrupo("11-04")
    ejemplo6.setPromocion(2019)
    ejemplo6.imprimirDatos()
    print("")

    ejemplo7 = Universitario()
    ejemplo7.setNombre("Santiago")
    ejemplo7.setApellido("Mendoza")
    ejemplo7.setIdentificacion("67426")
    ejemplo7.setEdad(19)
    ejemplo7.setCorreo("ejemplo7@gmail.com")
    ejemplo7.setLugar("Universidad de la Costa")
    ejemplo7.setProfesorFavorito("Fabio Mendoza")
    ejemplo7.setPrograma("Ingenería de sistemas")
    ejemplo7.setCreditos(160)
    ejemplo7.setNumSemestres(10)
    ejemplo7.imprimirDatos()

main()