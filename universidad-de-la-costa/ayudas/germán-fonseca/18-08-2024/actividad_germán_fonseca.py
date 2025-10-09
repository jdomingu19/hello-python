# 01 Actividad listas enlazadas

# clase credora de nodos
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# clase creadora de listas enlazadas
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # 1. insertar al principio
    def insertar_al_principio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    # 2. insertar al final
    def insertar_al_final(self, dato):
        # creación nodo nuevo
        nuevo_nodo = Nodo(dato)
        # si la lista está vacía
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
        # de lo contrario
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente != None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    # 3. eliminar nodo específico
    def eliminar_nodo_index(self, index: int):
        # si está vacía
        if self.cabeza == None:
            return None

        # si el index es negativo
        if index < 0:
            return None
        
        # si index no es entero:
        if type(index) is not int:
            return None

        # si es el primer nodo
        if index == 0:
            self.cabeza = self.cabeza.siguiente
            return True
        
        # de lo contrario
        nodo_anterior = None
        nodo_actual = self.cabeza
        cont = 0
        while nodo_actual.siguiente != None and cont < index:
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
            cont = cont + 1
        
        nodo_anterior.siguiente = nodo_actual.siguiente
        return True


    # 4. mostrar lista enlazada
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

lista.insertar_al_final("Germán")
lista.insertar_al_final("Jesús")
lista.insertar_al_final("Carlos")
lista.mostrar()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

lista.eliminar_nodo_index(5) # Eliminar "Carlos"
lista.eliminar_nodo_index(2) # Eliminar "Oscar"
lista.mostrar() # Output: 1 -> 2 -> 4 -> 5 -> None
