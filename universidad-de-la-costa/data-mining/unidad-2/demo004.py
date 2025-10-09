# Outliers usando Boxplots
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Dimensión 1: Edades
edades = np.array([22, 22, 23, 23, 23, 23, 26, 27, 27, 28, 30, 30, 30, 30, 31, 32, 33, 34, 80])

green_diamond = dict(markerfacecolor='g', marker='D')
fig, ax = plt.subplots()
ax.set_title('Boxplot por Edades')
ax.boxplot(edades, flierprops=green_diamond, labels=["Edad"])

print("= = = Datos de Edades = = =")
print(f"{type(edades)}, {edades=}")
print(f"{type(green_diamond)}, {green_diamond=}")
print(f"{type(fig)}, {fig=}")
print(f"{type(ax)}, {ax=}")

plt.show()
