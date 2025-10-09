"""
Parcial Unidad 3 | Parte 1 | Jesús Alberto Domínguez Charris

Para un árbol binario de búsqueda, 
indicar los padres de los nodos con los tres valores más altos (Top 3).
"""

from ABB2023 import *

abb01 = ArbolesBinariosBusqueda()
abb01.insertarNodosAleatorios(10)
print(f"ABB 01:\n {abb01}")

listaNodos = abb01.nodoRaiz.verNodosArbol()
print(f"Lista nodos: {listaNodos}")
print(f"Ver nodo tres mayores: {abb01.verNodosTresMayores()}")
print(f"Ver padre tres mayores: {abb01.verPadresNodosTresMayores()}")
