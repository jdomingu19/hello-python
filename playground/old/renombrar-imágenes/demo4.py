# Contar y listar tipos de archivos
import os


def contar_listar_archivos(contenido, nombre):
    ficheros = []
    directoreos = []
    for x in contenido:
        if os.path.isfile(x):
            ficheros.append(x)

        if os.path.isdir(x):
            directoreos.append(x)

    print(f"Cantidad ficheros '{nombre}': {len(ficheros)}")
    print(f"Cantidad directoreos '{nombre}': {len(directoreos)}")


contar_listar_archivos(os.listdir(), str(os.path.__name__))
contar_listar_archivos(os.listdir(), str(os.path.__name__))