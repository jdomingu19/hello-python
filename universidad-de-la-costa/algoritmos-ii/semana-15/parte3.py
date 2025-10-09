"""
Parcial Unidad 3 | Parte 3 | Jesús Alberto Domínguez Charris

Para un árbol binario de búsqueda, 
se desean manejar nodos con un valor numérico entero y un color asociado a cada nodo, 
para diseñar un método que obtenga la suma de los nodos de un color específico indicado por el usuario.
"""

from ABB2023 import *

abb01 = ArbolesBinariosBusqueda()
abb01.insertarNodoConColor(15, "azul")
abb01.insertarNodoConColor(17, "azul")
abb01.insertarNodoConColor(16, "azul")

abb01.insertarNodoConColor(25, "verde")
abb01.insertarNodoConColor(27, "verde")
abb01.insertarNodoConColor(26, "verde")

abb01.insertarNodoConColor(10, "rojo")
abb01.insertarNodoConColor(12, "rojo")
abb01.insertarNodoConColor(11, "rojo")

print(f"ABB 01:\n {abb01}")
print(f"Lista nodos: {abb01.nodoRaiz.verNodosArbol()}")

print(f"Suma nodos con color 'azul': {abb01.sumaNodosColorEspecifico('azul')}")
print(f"Suma nodos con color 'verde': {abb01.sumaNodosColorEspecifico('verde')}")
print(f"Suma nodos con color 'rojo': {abb01.sumaNodosColorEspecifico('rojo')}")
print(f"Suma nodos con color 'amarillo': {abb01.sumaNodosColorEspecifico('amarillo')}")
