#Clase Nodo Simple
class NodoSimple:
    #Constructor
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None        
    #Str
    def __str__(self) -> str:
        return str(self.dato)
    #Eq
    def __eq__(self, other):
        if not isinstance(other, NodoSimple):
            return False
        return self.dato == other.dato
    
#Clase ListaSimple
class ListaSimple:
    #Constructor
    def __init__(self) -> None:
        self.nodoInicial = None
    
    #Lista Vacia
    def estaVacia(self):
        return self.nodoInicial == None

    #Adicionar al inicio
    def adicionarAlInicio(self, dato_nuevo):
        nodoNuevo = NodoSimple(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoNuevo.siguiente = self.nodoInicial
            self.nodoInicial = nodoNuevo
    
    #Eliminar al inicio
    def eliminarAlInicio(self):
        if self.estaVacia():
            return None
        else:
            dato = self.nodoInicial.dato
            self.nodoInicial = self.nodoInicial.siguiente
            return dato
    
    #Buscar por dato
    def buscar(self, dato_buscar):
        if self.estaVacia():
            return False
        else:
            nodoActual = self.nodoInicial
            while nodoActual != None:
                if nodoActual.dato == dato_buscar:
                    return True
                nodoActual = nodoActual.siguiente
            return False
    
    #Recorrido (Str)
    def __str__(self):
        recorrido = ""
        nodoActual = self.nodoInicial
        while nodoActual != None:
            recorrido += str(nodoActual.dato) + " "
            nodoActual = nodoActual.siguiente
        return recorrido
    
    #Eliminar por información
    def eliminarInfo(self, dato_eliminar):
        if self.estaVacia():
            return False
        if self.nodoInicial.dato == dato_eliminar:
            self.eliminarAlInicio()
            return True
        nodoPrevio = None
        nodoActual = self.nodoInicial
        while nodoActual != None and nodoActual.dato != dato_eliminar:
            nodoPrevio = nodoActual
            nodoActual = nodoActual.siguiente
        if nodoActual == None:
            return False
        if nodoActual.siguiente == None:
            nodoPrevio.siguiente = None
        else:
            nodoPrevio.siguiente = nodoActual.siguiente
        return True
    
    #Comparar listas
    def comparar(self, lista02:"ListaSimple") -> bool:
        #Definir nodos de recorrido
        nodoActualLista1 = self.nodoInicial
        nodoActualLista2 = lista02.nodoInicial
        while nodoActualLista1 != None and nodoActualLista2 != None:
            if nodoActualLista1.dato != nodoActualLista2.dato:
                return False #Elementos distintos, listas distintas
            nodoActualLista1 = nodoActualLista1.siguiente
            nodoActualLista2 = nodoActualLista2.siguiente
        #Si los nodos son vacios, las listas son iguales
        if nodoActualLista1 == None and nodoActualLista2 == None:
            return True #Listas Iguales!
        else:
            return False #Listas no iguales por longitud
        
    def eliminarAparicionesDato(self, datoBuscar):
        if self.estaVacia():
            return False
        nodoPrevio = None
        nodoActual = self.nodoInicial
        primeraAparicion = True  # Para evitar eliminar la primera aparición
        while nodoActual is not None:
            if nodoActual.dato == datoBuscar:
                if primeraAparicion:
                    primeraAparicion = False
                else:
                    if nodoPrevio is not None:
                        nodoPrevio.siguiente = nodoActual.siguiente
                    else:
                        self.nodoInicial = nodoActual.siguiente
            else:
                nodoPrevio = nodoActual
            nodoActual = nodoActual.siguiente
        return True
    
