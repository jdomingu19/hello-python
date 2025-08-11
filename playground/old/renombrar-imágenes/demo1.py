# Obtener lista de elementos directorio
import os

# 1. os.listdir() - lista directorio actual
contenido = os.listdir()
print(f"Directorio actual (sin ruta): {contenido}\n")

# 2. os.listdir('/ruta') - lista directorio ingresado
contenido = os.listdir("/Users/dell i3/OneDrive/Programación/Lenguajes/Python/Otros/Renombrar imágenes/")
print(f"Directorio actual (ruta): {contenido}\n")

# 3. os.listdir('./ruta') - lista directorio dentro directorio actual
contenido_a = os.listdir("./Dir A")
contenido_b = os.listdir("./Dir B")
print(f"Dir A: {contenido_a}\n")
print(f"Dir B: {contenido_b}")
