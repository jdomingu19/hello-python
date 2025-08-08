"""
r  -> Leer, si no existe error
r+ -> Leer y escribir, si no existe error
w  -> Escribir borra la información existente, si no existe lo crea
a  -> Añadir información sin borrar, si no existe lo crea
a+ -> Añadir y leer información sin borrar, si no existe lo crea

t  -> Modo texto
b  -> Modo binario
"""

# 1. Crear y escribir en un txt
mi_archivo = open("nombres.txt", "w")
mi_archivo.write("Madeleyne Ruiz" + "\n")
mi_archivo.write("Juan Sarmiento" + "\n")
mi_archivo.write("Juan Conde")
mi_archivo.close()

# 2. Añadir información nueva sin borrar la anterior
mi_archivo = open("nombres.txt", "a")
mi_archivo.write("\n" + "Noah" + "\n")
mi_archivo.write("Coifee")
mi_archivo.close()

# 3. Leer información de txt con READ
mi_archivo = open("nombres.txt", "r")
print(mi_archivo.read())
mi_archivo.close()

print("\n")

mi_archivo = open("nombres.txt", "r")
contenido = mi_archivo.read()
print(contenido)
mi_archivo.close()

print("\n")

# 4. Leer información de txt con ciclo for
mi_archivo = open("nombres.txt", "r")
for i in mi_archivo:
    print(i, end="")
mi_archivo.close()

print("\n")

# 5. Obtener una lista de las líneas de un txt
# FORMA 1
mi_archivo = open("nombres.txt", "r")
print(mi_archivo.readlines())
mi_archivo.close()

print("\n")

# FORMA 2
mi_archivo = open("nombres.txt", "r")
lineas = mi_archivo.readlines()
print(lineas)
mi_archivo.close()

print("\n")

# FORMA 3
mi_archivo = open("nombres.txt", "r")
lineas = [] 
for i in mi_archivo:
    lineas.append(i)
print(lineas)
mi_archivo.close()

print("\n")

# 6. Obtener una lista de líneas de un txt e imprimirlas con for
mi_archivo = open("nombres.txt", "r")
lineas = mi_archivo.readlines()
for i in lineas:
    print(i, end="")
mi_archivo.close()
