# Madeleyne Ruiz ---------------- Ejercicio Herencia | CORTE 3.
class Personas:
    def __init__(self):
        self.name = ""
        self.apellido = ""
        self.identificacion = ""
        self.edad = ""
        self.correo = ""
    
    def set_name(self, name:str):
        self.name = name

    def get_name(self):
        return self.name

    def set_apellido(self, ap:str):
        self.apellido = ap

    def get_apellido(self):
        return self.apellido

    def set_identificacion(self, id:int):
        self.identificacion = id

    def get_identificacion(self):
        return self.identificacion

    def set_edad(self, edad:int):
        self.edad = edad

    def get_edad(self):
        return self.edad

    def set_correo(self, correo:str):
        self.correo = correo

    def get_correo(self):
        return self.correo

    def mostrar_datos(self):
        print(f"Nombre: {self.get_name()} {self.get_apellido()}")
        print(f"Identificacion: {self.get_identificacion()}")
        print(f"Edad: {self.get_edad()}")
        print(f"Correo: {self.get_correo()}")

class Empleados(Personas):
    def __init__(self):
        super().__init__()
        self.profesion = ""
        self.experiencia = ""
        self.cargo = ""

    def set_profesion(self, profesion:str):
        self.profesion = profesion

    def get_profesion(self):
        return self.profesion

    def set_expreriencia(self, exp:int):
        self.experiencia = exp

    def get_expreriencia(self):
        return self.experiencia

    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_cargo(self):
        return self.cargo

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Profesión: {self.get_profesion()}")
        print(f"Experiencia: {self.get_expreriencia()}")
        print(f"Cargo: {self.get_cargo()}")

class TiempoCompleto(Empleados):
    def __init__(self):
        super().__init__()   
        self.horas = ""
        self.campo = ""

    def set_horas(self, tiempo:int):
        self.horas = tiempo

    def get_horas(self):
        return self.horas

    def set_campo(self, x:str): # - Área de conocimiento del empleado -
        self.campo = x

    def get_campo(self):
        return self.campo

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Horas de trabajo: {self.get_horas()}")
        print(f"Área de conocimiento: {self.get_campo()}") # Área de Formación

class DeLabor(Empleados): # Labor de los empleados
    def __init__(self):
        super().__init__()
        self.labor = ""
        self.inicio = ""
        self.finalizacion = ""

    def set_labor(self, x:str):
        self.labor = x

    def get_labor(self):
        return self.labor

    def set_fecha_inicial(self, inicio:str):
        self.inicio = inicio

    def get_fecha_inicial(self):
        return self.inicio

    def set_fecha_final(self, fin:str):
        self.finalizacion = fin

    def get_fecha_final(self):
        return self.finalizacion

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Labor: {self.get_labor()}")
        print(f"Fecha de inicio: {self.get_fecha_inicial()}")
        print(f"Fecha final: {self.get_fecha_final()}")

class Estudiantes(Personas):
    def __init__(self):
        super().__init__()
        self.institucion = ""
        self.actividad_favorita = ""

    def set_institucion(self, x:str):
        self.institucion = x

    def get_institucion(self):
        return self.institucion

    def set_actividad(self, x:str):
        self.actividad_favorita = x

    def get_actividad(self):
        return self.actividad_favorita

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Institucion: {self.get_institucion()}")
        print(f"Actividad Favorita: {self.get_actividad()}")

class Secundaria(Estudiantes):
    def __init__(self):
        super().__init__()
        self.docente_asisgnado = ""
        self.año_cursado = ""

    def set_docente(self, x:str):
        self.docente_asisgnado = x

    def get_docente(self):
        return self.docente_asisgnado
    
    def set_grado(self, grado:int):
        self.año_cursado = grado

    def get_grado(self):
        return self.año_cursado

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Director de Grupo: {self.get_docente()}")
        print(f"Grado Cursado: {self.get_grado()}")

class Universitario(Estudiantes):
    def __init__(self):
        super().__init__()
        self.semestre = ""
        self.carrera = ""
        self.materia_principal = ""

    def set_semestre(self, x:int):
        self.semestre = x

    def get_semestre(self):
        return self.semestre

    def set_carrera(self, x:str):
        self.carrera = x

    def get_carrera(self):
        return self.carrera 

    def set_asignatura(self, materia:str):
        self.materia_principal = materia

    def get_asignatura(self):
        return self.materia_principal

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Semestre: {self.get_semestre()}")
        print(f"Carrera: {self.get_carrera()}")
        print(f"Asignatura Principal: {self.get_asignatura()}")

# Método principal: 
def main():
    persona_1 = Personas()
    persona_1.set_name("Ibis")
    persona_1.set_apellido("Taborda")
    persona_1.set_identificacion(12345)
    persona_1.set_edad(3)
    persona_1.set_correo("Ibistaborda15@gmail.com")
    persona_1.mostrar_datos()

# Empleado ----- DATOS:
    empleado_1 = Empleados()
    empleado_1.set_name("Jaime")
    empleado_1.set_apellido("Alcaraz")
    empleado_1.set_identificacion(34224)
    empleado_1.set_edad(60)
    empleado_1.set_correo("Jaimealcaraz04@gmail.com")
    empleado_1.set_profesion("Electricista")
    empleado_1.set_cargo("Jefe de Obra")
    empleado_1.set_expreriencia(2001)
    empleado_1.mostrar_datos()

# Empleado de Tiempo Completo ----- DATOS:
    empleado_2 = TiempoCompleto()
    empleado_2.set_name("Javier")
    empleado_2.set_apellido("Ruiz")
    empleado_2.set_identificacion(722133)
    empleado_2.set_edad(45)
    empleado_2.set_correo("Berthjavi@gmail.com")
    empleado_2.set_profesion("Ingeniero de Sistemas")
    empleado_2.set_cargo("Jefe de Área")
    empleado_2.set_campo("Desarrollo de Software")
    empleado_2.set_expreriencia(2003)
    empleado_2.set_horas(200)
    empleado_2.mostrar_datos()

# Empleado de Labor ----- DATOS:
    empleado_3 = DeLabor()
    empleado_3.set_name("Yaneth")
    empleado_3.set_apellido("Alcaraz")
    empleado_3.set_identificacion(2223557)
    empleado_3.set_edad(46)
    empleado_3.set_correo("yanealc@gmail.com")
    empleado_3.set_profesion("Licenciada en Lenguaje")
    empleado_3.set_cargo("Directora de grupo")
    empleado_3.set_expreriencia(2015)
    empleado_3.set_labor("Docente de Primaria")
    empleado_3.set_fecha_inicial("enero 2018")
    empleado_3.set_fecha_final("diciembre 2030")
    empleado_3.mostrar_datos()

# Estudiante ----- DATOS:
    estudiante_1 = Estudiantes()
    estudiante_1.set_name("Camila")
    estudiante_1.set_apellido("Alcaraz")
    estudiante_1.set_identificacion(122402)
    estudiante_1.set_edad(14)
    estudiante_1.set_correo("Cam24alc@gmail.com")
    estudiante_1.set_institucion("Normal de Fátima")
    estudiante_1.set_actividad("Deportes - Voleibol")
    estudiante_1.mostrar_datos()

# Estudiante de Secundaria ----- DATOS:
    estudiante_2 = Secundaria()
    estudiante_2.set_name("Joshua")
    estudiante_2.set_apellido("Montoya")
    estudiante_2.set_identificacion(112445)
    estudiante_2.set_edad(16)
    estudiante_2.set_correo("Joshua04M@gmail.com")
    estudiante_2.set_institucion("Madre Marcelina")
    estudiante_2.set_grado(11)
    estudiante_2.set_actividad("Deportes - Voleibol")
    estudiante_2.set_docente("Adriana Alcaraz")
    estudiante_2.mostrar_datos()

# Estudiante Universitario ----- DATOS:
    estudiante_3 = Universitario()
    estudiante_3.set_name("Madeleyne")
    estudiante_3.set_apellido("Ruiz")
    estudiante_3.set_identificacion(144355)
    estudiante_3.set_edad(18)
    estudiante_3.set_correo("Madruiza@gmail.com")
    estudiante_3.set_institucion("Universidad de la Costa")
    estudiante_3.set_actividad("Deportes - Cheerleading - Voleibol")
    estudiante_3.set_semestre(3)
    estudiante_3.set_carrera("Ingeniería de Sistemas")
    estudiante_3.set_asignatura("Algoritmos")
    estudiante_3.mostrar_datos()

# Llamar al método principal
main()    

# - TERMINADO -