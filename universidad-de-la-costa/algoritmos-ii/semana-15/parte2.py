"""
Parcial Unidad 3 | Parte 2 | Jesús Alberto Domínguez Charris

Para un árbol binario de búsqueda, 
indicar el número de nodos a visitar desde la raíz para llegar a cada nodo hoja.
"""

from ABB2023 import *

abb01 = ArbolesBinariosBusqueda()
abb01.insertarNodosAleatorios(10)
print(f"ABB 01:\n {abb01}")

abb01.nodoRaiz.verNodosArbol()
print(f"Lista nodos: {abb01.nodoRaiz.verNodosArbol()}")
print(f"Lista nodos hojas: {abb01.nodoRaiz.verHojasArbol()}")
print(f"Contar nodos hasta cada hoja: {abb01.contarNodosHastaCadaHoja()}")
