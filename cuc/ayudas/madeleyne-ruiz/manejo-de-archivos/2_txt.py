"""
nombre = input("Ingrese su nombre: ")
print(f"Usted se llama: {nombre}")
"""

# Leer varios txt manualmente
ubicacion_1 = "Secretos/notas1.txt"

mi_archivo = open(ubicacion_1, "r")
contenido = mi_archivo.read()
print("Contenido de notas1:")
print(contenido)
mi_archivo.close()

print("\n")

ubicacion_2 = "Secretos/notas2.txt"

mi_archivo = open(ubicacion_2, "r")
contenido = mi_archivo.read()
print("Contenido de notas2:")
print(contenido)
mi_archivo.close()

print("\n")

# 2. Leer varios txt con un ciclo for
ubicaciones = ["Secretos/notas1.txt", "Secretos/notas2.txt"]

for i in ubicaciones:
    archivo = open(i, "r")
    contenido = archivo.read()
    print(f"Contenido de: {i}")
    print(contenido)
    archivo.close()
    print("")

# 3. Ir cambiando archivos de una misma carpeta
path = "Mascotas/"
nombres_archivos = ["gatos.txt", "perros.txt"]

for i in nombres_archivos:
    ubicacion = path + i
    archivo = open(ubicacion, "r")
    print(f"Contenido de: {ubicacion}")
    print(archivo.read())
    archivo.close()
    print("")

# 4. Ir cambiando de carpetas y sus archivos internos CON MISMO NOMBRES
carpetas = ["Mascotas/", "Secretos/"]
nombres_archivos = ["gatos.txt", "perros.txt"]

for i in carpetas:
    for j in nombres_archivos:
        archivo = open(i + j, "r")
        print(f"Contenido de: {i + j}")
        contenido = archivo.read()
        print(contenido)
        archivo.close()
        print("")