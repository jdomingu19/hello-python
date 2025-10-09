# KNN: K-Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np
import mplcursors

# 1. Definir las caracterísricas (peso y tamaño) y etiquetas (Manzana: 0, Naranja: 1)
X1 = np.array([[180, 7], [170, 8]]) # Características [peso, tamaño]
y = np.array([0, 0, 1, 1])          # Etiquetas (0: Manzana, 1: Naranja)

X2 = np.array([[150, 5], [140, 6]]) # Características [peso, tamaño]

X = np.vstack((X1, X2))

# 2. Crear el clasificador KNN con k=3
knn = KNeighborsClassifier(n_neighbors=3)

# 3. Entrenar el clasificador con nuestros datos
knn.fit(X, y)

# 4. Definir un nuevo punto de datos y predecir su clase
nuevo_punto = np.array([[160, 8], [150, 3], [180, 6], [170, 4], [190, 7], [200, 3]])
prediccion = knn.predict(nuevo_punto)

# 5. Mostrar la predicción
frutas = {0: "Manzana", 1: "Naranja"}
print(f"{type(nuevo_punto)} {nuevo_punto}")
print(f"{type(prediccion)} {prediccion}")
print(f"{type(frutas)} {frutas}")

for i in range(len(nuevo_punto)):
    print(f"(Fruta #{i+1}) Peso: {nuevo_punto[i, 0]} kg | Tamaño: {nuevo_punto[i, 1]} cm | Predicción KNN: {frutas[prediccion[i]]}")

# 6. Graficar los puntos de datos y la línea de decisión
plt.scatter(nuevo_punto[:, 0], nuevo_punto[:, 1], color='blue', label='Nuevo punto')
plt.scatter(X1[:, 0], X1[:, 1], color='red', label='Manzanas')      # Puntos de la clase 1
plt.scatter(X2[:, 0], X2[:, 1], color='orange', label='Naranjas')   # Puntos de la clase 2
plt.xlabel('Peso (kg)')
plt.ylabel('Tamaño (cm)')
plt.title('KNN')
plt.legend()
plt.grid(True)
cursor = mplcursors.cursor(hover=True)
plt.show()
