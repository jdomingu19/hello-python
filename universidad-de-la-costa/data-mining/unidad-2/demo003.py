# Outliers en 3 dimensiones
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Dimensión 1: edades
edades = np.array([22, 22, 23, 23, 23, 23, 26, 27, 27, 28, 30, 30, 30, 30, 31, 32, 33, 34, 80])
edad_unique, count = np.unique(edades, return_counts=True)

sizes = count * 100
colors = ['blue'] * len(edad_unique)

print("= = = Datos de Edades = = =")
print(f"{type(edad_unique)}, {edad_unique=}")
print(f"{type(count)}, {count=}")
print(f"{type(sizes)}, {sizes=}")
print(f"{type(colors)}, {colors=}")

# Dimesión 2: Salario anual (miles)
salario_anual_miles = np.array([16, 20, 15, 21, 19, 17, 33, 22, 31, 32, 56, 30, 22, 31, 30, 16, 2, 22, 23])
media = (salario_anual_miles).mean()
std_x = (salario_anual_miles).std() * 2
media_y = (edades).mean()
std_y = (edades).std() * 2

colors = ['blue'] * len(salario_anual_miles)
for index, x in enumerate(salario_anual_miles):
    if abs(x - media) > std_x:
        colors[index] = 'red'

for index, x in enumerate(edades):
    if abs(x - media_y) > std_y:
        colors[index] = 'red'

print("\n= = = Datos de Salario Anual (miles) = = =")
print(f"{type(media)}, {media=}")
print(f"{type(std_x)}, {std_x=}")
print(f"{type(media_y)}, {media_y=}")
print(f"{type(std_y)}, {std_y=}")
print(f"{type(colors)}, {colors=}")

# Dimesión 3: Compras mensuales
fig = plt.figure(figsize=(7, 7))
# ax = fig.gca(projection='3d') IT DOESN'T WORK
# ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(projection='3d')

compras_mes = np.array([1, 2, 1, 20, 1, 0, 3, 2, 3, 0, 5, 3, 2, 1, 0, 1, 2, 2, 2])
media_z = (compras_mes).mean()
std_z = (compras_mes).std() * 2

for index, x in enumerate(compras_mes):
    if abs(x - media_z) > std_z:
        colors[index] = 'red'

print("\n= = = Datos de Compras mensuales = = =")
print(f"{type(fig)}, {fig=}")
print(f"{type(ax)}, {ax=}")
print(f"{type(compras_mes)}, {compras_mes=}")
print(f"{type(media_z)}, {media_z=}")
print(f"{type(std_z)}, {std_z=}")

ax.scatter(edades, salario_anual_miles, compras_mes, s=20, c=colors)
plt.xlabel('Edad')
plt.ylabel('Salario Anual (miles)')
ax.set_zlabel('Compras mensuales')

plt.show()
