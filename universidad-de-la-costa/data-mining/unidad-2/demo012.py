# Regresión logística

# 0. Importar librerías
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import mplcursors

# 1. Datos ficticios: horas de estudio y si aprueba (1) o no aprueba (0)
X = np.array([[1], [5], [3], [4], [2], [6], [7], [8], [9]]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])

# 2. Crear y entrenar el modelo de regresión logística
model = LogisticRegression()
model.fit(X, y)

# 3. Generar predicciones
x_test = np.linspace(0, 10, 100).reshape(-1, 1)
y_prob = model.predict_proba(x_test)[:, 1]  # Probabilidad de aprobar

horas = 4.8
z_prob = model.predict([[horas]])
print(f"Probabilidad de aprobar para {horas} horas de estudio: {z_prob[0]}")

# 4. Visualización del resultado
plt.scatter(X, y, color='blue', label='Datos Reales')  # Datos reales
plt.plot(x_test, y_prob, color='red', label='Curva Sigmoide')  # Curva sigmoide
plt.scatter(horas, z_prob, color='green', label="Predicción para horas")
plt.title("Regresión Logística: Predicción de Aprobación según Horas de Estudio")
plt.xlabel("Horas de Estudio")
plt.ylabel("Probabilidad de Aprobar")
plt.grid(True)
plt.legend()
cursor = mplcursors.cursor(hover=True)
plt.show()
