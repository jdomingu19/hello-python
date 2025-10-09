# Regresión lineal

# 0. Importar librerías
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import mplcursors

# 1. Datos ficticios: altura (cm) y peso (kg)
X = np.array([[150], [160], [170], [190], [180]]).reshape(-1, 1)
y = np.array([50, 60, 70, 80, 90])

# 2. Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X, y)

# 3. Predicciones con el modelo
y_pred = model.predict(X)
print(f"Predicción peso (kg) usando X: {y_pred=}")

z_value = [[175], [184], [200], [179]]
z_pred = model.predict(z_value)
print(f"Predicción peso (kg) usando z_value: {z_pred=}")

# 4. Visualización del resultado
plt.scatter(X, y, color='blue', label='Datos Reales')  # Datos reales
plt.plot(X, y_pred, color='red', label='Línea de Regresión')  # Línea ajustada
plt.scatter(z_value, z_pred, color='green', label='Predicción')
plt.title("Regresión Lineal: Predicción de Peso según Altura")
plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")
plt.legend()
plt.grid(True)
cursor = mplcursors.cursor(hover=True)
plt.show()
