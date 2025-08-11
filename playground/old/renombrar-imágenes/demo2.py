# Diferenciar ficheros y directorios
import os

contenido = os.listdir()

ficheros = []
directorios = []
for x in contenido:
    # os.path.isfile(ruta)
    if os.path.isfile(x):
        ficheros.append(x)

    # os.path.isdir(ruta)
    if os.path.isdir(x):
        directorios.append(x)

print(f"Ficheros: {ficheros}")
print(f"Directorios: {directorios}")
