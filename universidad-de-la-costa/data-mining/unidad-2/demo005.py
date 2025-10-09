# Outliers usando PyOD
import numpy as np
import pandas as pd
from pyod.models.knn import KNN

edades = np.array([22, 22, 23, 23, 23, 23, 26, 27, 27, 28, 30, 30, 30, 30, 31, 32, 33, 34, 80])
salario_anual_miles = np.array([16, 20, 15, 21, 19, 17, 33, 22, 31, 32, 56, 30, 22, 31, 30, 16, 2, 22, 23])
compras_mes = np.array([1, 2, 1, 20, 1, 0, 3, 2, 3, 0, 5, 3, 2, 1, 0, 1, 2, 2, 2])

X = pd.DataFrame(data={'edad': edades, 'salario': salario_anual_miles, 'compras': compras_mes})

clf = KNN(contamination=0.18)
clf.fit(X)
y_pred = clf.predict(X)
X[y_pred == 1]

print(f"{type(clf)}, {clf=}")
print(f"{type(X)}")

print("\n= = = DATAFRAME X = = =", X, sep="\n")
print("\n= = = Outliers = = =", X[y_pred == 1], sep="\n")
