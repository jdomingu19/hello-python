# Outliers en 1 dimensión
import matplotlib.pyplot as plt
import numpy as np

# Dimesión 1: Edades
edades = np.array([22, 22, 23, 23, 23, 23, 26, 27, 27, 28, 30, 30, 30, 30, 31, 32, 33, 34, 80])
edad_unique, count = np.unique(edades, return_counts=True)

sizes = count * 100
colors = ['blue'] * len(edad_unique)
colors[-1] = 'red'

print(f"{type(edad_unique)}, {edad_unique=}")
print(f"{type(count)}, {count=}")
print(f"{type(sizes)}, {sizes=}")
print(f"{type(colors)}, {colors=}")

plt.axhline(1, color='k', linestyle='--')
plt.scatter(edad_unique, np.ones(len(edad_unique)), s=sizes, color=colors)
plt.yticks([])
plt.show()
