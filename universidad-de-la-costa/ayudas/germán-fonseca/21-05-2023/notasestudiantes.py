"""
Un docente genera un archivo de texto desde su plataforma académica, 
con las notas de 30 estudiantes, el formato del archivo es el siguiente:

Nombre: NombreEstudiante
Identificación: IdEstudiante
Nota_1
Nota_2
Nota_3

Se requiere Sacar el promedio de las 3 notas para cada estudiante. 
El archivo de salida debe tener el siguiente formato:

Nombre: NombreEstudiante
Identificación: IdEstudiante
Nota_1
Nota_2
Nota_3
Promedio: PromedioNotas

"""

import random 
nombres = ["Lucas", "Sofía", "Mateo", "Valentina", "Santiago", 
           "Isabella", "Gabriel", "Emma", "Daniel", "Victoria", 
           "Matías", "Catalina", "Alejandro", "Camila", "Sebastián", 
           "Mia", "Nicolás", "Valeria", "Samuel", "Amelia", "Tomás", 
           "Olivia", "Andrés", "Isadora", "Juan", "Gabriela", 
           "Carlos", "Natalia", "Emilio", "Antonella"]

apellidos = ["García", "Rodríguez", "López", "Martínez", "González", 
             "Hernández", "Pérez", "Sánchez", "Ramírez", "Torres", 
             "Flores", "Vargas", "Ramos", "Romero", "Medina", 
             "Jiménez", "Ríos", "Cruz", "Morales", "Castro", 
             "Ortega", "Silva", "Mendoza", "Reyes", "Herrera", 
             "Gómez", "Díaz", "Aguilar", "Torres", "Figueroa"]


# Archivo profesor
with open("notasProfesor.txt", "w", encoding="utf-8") as file:
    for x in range(30):
        nombre = random.choice(nombres) + " " + random.choice(apellidos)
        id = x + 1
        nota_1 = random.randint(0, 5)
        nota_2 = random.randint(0, 5)
        nota_3 = random.randint(0, 5)
        file.write(f"NOMBRE: {nombre}\n")
        file.write(f"ID: {id}\n")
        file.write(f"NOTA 1: {nota_1}\n")
        file.write(f"NOTA 2: {nota_2}\n")
        file.write(f"NOTA 3: {nota_3}\n")
        file.write("\n")

# Calcular promedios
with open("notasProfesor.txt", "r", encoding="utf-8") as file:    
    contenido = file.readlines()
    cont = 0
    for x in contenido:
        if x == "\n":
            nota_1 = int(contenido[cont - 3][-2])
            nota_2 = int(contenido[cont - 2][-2])
            nota_3 = int(contenido[cont - 1][-2])
            promedio = (nota_1 + nota_2 + nota_3) / 3
            promedio = round(promedio, 2)
            contenido[cont] = f"PROMEDIO: {promedio}\n\n"
        cont = cont + 1

    # Crear archivo nuevo
    with open("notasPromedios.txt", "w", encoding="utf-8") as file:
        for x in contenido:
            file.write(x)
