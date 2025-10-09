# SVM: Support Vector Machines
import numpy as np
import matplotlib.pyplot as plt
import sklearn.svm

# 1. Crear datos de ejemplo
X1 = np.array([[2, 3], [3, 4], [4, 5], [1, 2], [2, 2]])         # Clase 1
y1 = [0, 0, 0, 0, 0]                                            # Etiqueta 0 para clase 1

X2 = np.array([[6, 8], [7, 9], [8, 10], [7, 7], [8, 8]])        # Clase 2

X = np.vstack((X1, X2))                                         # Combinar datos de ambas clases
y = [0] * len(X1) + [1] * len(X2)                               # Etiqueta 1 para clase 2

# 2. Crear el clasificador SVM
clf = sklearn.svm.SVC(kernel='linear')
clf.fit(X, y)                                                   # Entrenar el modelo con los datos

# 3. Graficar los puntos de datos y la línea de decisión
plt.scatter(X1[:, 0], X1[:, 1], color='red', label='Clase 0')   # Puntos de la clase 1
plt.scatter(X2[:, 0], X2[:, 1], color='blue', label='Clase 1')  # Puntos de la clase 2

# 4. Trazar la línea de decisión
w = clf.coef_[0]
a = -w[0] / w[1]                                                # Pendiente de la línea
xx = np.linspace(0, 10)                                         # Rango de valores de x
yy = a * xx - (clf.intercept_[0] / w[1])                        # Calcular los valores de y en la línea de decisión
plt.plot(xx, yy, 'k-', label='Línea de decisión (SVM)')

# 5. Nueva coordenada para predecir
new_point = np.array([[5, 6]])                                  # Coordenada para predecir diferentes puntos
predicted_class = clf.predict(new_point)                        # Realizar predicción
print(f"La nueva coordenada {new_point} pertenece a la clase {predicted_class[0]}")

# 6. Graficar la nueva coordenada en el gráfico
plt.scatter(new_point[0, 0], new_point[0, 1], color='green', marker='x', s=100, label='Nuevo Punto')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Clasificación con SVM y nueva predicción')
plt.legend()
plt.grid(True)
plt.show()
