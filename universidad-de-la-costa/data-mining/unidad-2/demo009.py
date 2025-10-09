# Importar librerías
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np
import mplcursors

# 1. Definir las características (horas de estudio y promedio) y etiquetas (0: Regular, 1: Bueno, 2: Sobresaliente)
X = np.array([[10, 70], [15, 75], [20, 85], [25, 90]])  # Características [horas de estudio, promedio]
y = np.array([0, 1, 2, 2])  # Etiquetas (0: Regular, 1: Bueno, 2: Sobresaliente)

# 2. Crear el clasificador KNN con k=3
knn = KNeighborsClassifier(n_neighbors=3, weights='distance')

# 3. Entrenar el clasificador con nuestros datos
knn.fit(X, y)

# 4. Definir un nuevo punto de datos y predecir su clase
nuevo_estudiante = np.array([[12, 65], [18, 80], [22, 88], [17, 70], [20, 82], [5, 55]])
prediccion = knn.predict(nuevo_estudiante)

# 5. Mostrar la predicción
rendimiento = {0: "Regular", 1: "Bueno", 2: "Sobresaliente"}
for i in range(len(nuevo_estudiante)):
    print(f"(Estudiante #{i+1}) Horas de estudio: {nuevo_estudiante[i, 0]} | Promedio: {nuevo_estudiante[i, 1]} | Predicción KNN: {rendimiento[prediccion[i]]}")

# 6. Separar los puntos de datos en tres categorías según las etiquetas
sobresalientes = X[y == 2]
buenos = X[y == 1]
regulares = X[y == 0]

# 7. Graficar los puntos de datos con colores distintos para cada categoría
plt.scatter(nuevo_estudiante[:, 0], nuevo_estudiante[:, 1], color='blue', label='Nuevo estudiante')
plt.scatter(sobresalientes[:, 0], sobresalientes[:, 1], color='green', label='Sobresaliente')   # Sobresaliente en verde
plt.scatter(buenos[:, 0], buenos[:, 1], color='orange', label='Bueno')                          # Bueno en naranja
plt.scatter(regulares[:, 0], regulares[:, 1], color='red', label='Regular')                     # Regular en rojo
plt.xlabel('Horas de estudio por semana')
plt.ylabel('Promedio de calificaciones')
plt.title('KNN Clasificación de Rendimiento Académico')
plt.legend()
plt.grid(True)
cursor = mplcursors.cursor(hover=True)
plt.show()
