# 01. Lista enlazada simple
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.dato, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")

# Ejemplo de uso:
lista = ListaEnlazada()
lista.insertar_al_principio("Oscar")
lista.insertar_al_principio("Juan")
lista.insertar_al_principio("Pedro")
lista.mostrar()  # Output: 1 -> 2 -> 3 -> None
