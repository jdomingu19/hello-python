# Contar y listar tipos de archivos
import os

# Directorio actual:
contenido = os.listdir()
archivos_py = []
directorios = []
pngs = []
for x in contenido:
    if os.path.isfile(x) and x.endswith('.py'):
        archivos_py.append(x)
    
    if os.path.isdir(x):
        directorios.append(x)

    if os.path.isfile(x) and x.endswith('.png'):
        pngs.append(x)

print('DIRECTORIO ACTUAL')
print(f'-> Número archivos .py: {len(archivos_py)}')
print(f'-> Número directorios: {len(directorios)}')
print(f'-> Número archivos .png: {len(pngs)}')
print(f'-> Lista archivos .py: {archivos_py}')
print(f'-> Lista directorios: {directorios}')
print(f'-> Lista archivos .png: {pngs}\n')

# Dir A:
contenido_a = os.listdir('./Dir A')
archivos_py = []
directorios = []
pngs = []
for x in contenido_a:
    if os.path.isfile(os.path.join('./Dir A', x)) and x.endswith('.py'):
        archivos_py.append(x)
    
    if os.path.isdir(os.path.join('./Dir A', x)):
        directorios.append(x)

    if os.path.isfile(os.path.join('./Dir A', x)) and x.endswith('.png'):
        pngs.append(x)

print('DIR A')
print(f'-> Número archivos .py: {len(archivos_py)}')
print(f'-> Número directorios: {len(directorios)}')
print(f'-> Número archivos .png: {len(pngs)}')
print(f'-> Lista archivos .py: {archivos_py}')
print(f'-> Lista directorios: {directorios}')
print(f'-> Lista archivos .png: {pngs}\n')

# Dir B:
contenido_b = os.listdir('./Dir B')
archivos_py = []
directorios = []
pngs = []
for x in contenido_b:
    if os.path.isfile(os.path.join('./Dir B', x)) and x.endswith('.py'):
        archivos_py.append(x)
    
    if os.path.isdir(os.path.join('./Dir B', x)):
        directorios.append(x)

    if os.path.isfile(os.path.join('./Dir B', x)) and x.endswith('.png'):
        pngs.append(x)

# Imprimir resultados
print('DIR B')
print(f'-> Número archivos .py: {len(archivos_py)}')
print(f'-> Número directorios: {len(directorios)}')
print(f'-> Número archivos .png: {len(pngs)}')
print(f'-> Lista archivos .py: {archivos_py}')
print(f'-> Lista directorios: {directorios}')
print(f'-> Lista archivos .png: {pngs}')
