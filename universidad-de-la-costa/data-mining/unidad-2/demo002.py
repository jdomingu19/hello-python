# Outliers en 2 dimensiones
import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Dimesión 1: Edades
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

plt.scatter(edades, salario_anual_miles, s=100, color=colors)
plt.axhline(media, color='k', linestyle='--')
plt.axvline(media_y, color='k', linestyle='--')

v = media       # y-position of the center
u = media_y     # x-position of the center
b = std_x       # radius on the y-axis
a = std_y       # radios on the x-axis

t = np.linspace(0, 2 * pi, 100)
plt.plot(u + a * np.cos(t), v + b * np.sin(t))

print("\n= = = Datos de Salario Anual (miles) = = =")
print(f"{type(media)}, {media=}")
print(f"{type(std_x)}, {std_x=}")
print(f"{type(media_y)}, {media_y=}")
print(f"{type(std_y)}, {std_y=}")
print(f"{type(colors)}, {colors=}")
print(f"{type(v)}, {v=}")
print(f"{type(u)}, {u=}")
print(f"{type(b)}, {b=}")
print(f"{type(a)}, {a=}")
print(f"{type(t)}, {t=}")

plt.xlabel('Edad')
plt.ylabel('Salario Anual (miles)')
plt.show()
