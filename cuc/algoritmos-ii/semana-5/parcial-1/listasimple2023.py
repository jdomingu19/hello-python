"""
Semana 5 | Parcial 1 | Jesús Alberto Domínguez Charris

Diseñe un método que indique si un dato ingresado 
por el usuario aparece repetido en la lista.
"""

# Creación de nodos
class NodoSimple:
    def __init__(self, dato) -> None:
        self.dato = dato
        self.siguiente = None

    def __str__(self) -> str:
        return self.dato
    

# Creación de listas
class ListaEnlazadaSimple:
    # Constructor
    def __init__(self) -> None:
        self.nodoInicial = None

    # Verificar si está vacía
    def estaVacia(self) -> bool:
        return self.nodoInicial == None

    # Adicionarl al inicio
    def adicionarAlInicio(self, dato_nuevo) -> None:
        nodoNuevo = NodoSimple(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoNuevo.siguiente = self.nodoInicial
            self.nodoInicial = nodoNuevo

    # Eliminar al inicio
    def eliminarAlInicio(self) -> (int | float | str | None):
        if self.estaVacia():
            return None
        else:
            dato = self.nodoInicial.dato
            self.nodoInicial = self.nodoInicial.siguiente
            return dato

    # Buscar un dato
    def buscarDato(self, dato_buscar) -> bool:
        if self.estaVacia():
            return False
        else:
            nodoActual = self.nodoInicial
            while nodoActual != None:
                if nodoActual.dato == dato_buscar:
                    return True
                nodoActual = nodoActual.siguiente
            return False
    
    # Imprimir datos
    def __str__(self) -> str:
        recorrido = ""
        nodoActual = self.nodoInicial
        while nodoActual != None:
            recorrido = recorrido + str(nodoActual.dato) + " "
            nodoActual = nodoActual.siguiente
        return recorrido
    
    # Eliminar dato (primer encontrado)
    def eliminarDato(self, dato_eliminar) -> bool:
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

    # Adicionar al final
    def adicionarAlFinal(self, dato_nuevo) -> None:
        nodoNuevo = NodoSimple(dato_nuevo)
        if self.estaVacia():
            self.nodoInicial = nodoNuevo
        else:
            nodoActual = self.nodoInicial
            while nodoActual.siguiente != None:
                nodoActual = nodoActual.siguiente
            nodoActual.siguiente = nodoNuevo
    
    # Eliminar al final
    def eliminarAlFinal(self) -> (int | float | str | None):
        if self.estaVacia():
            return None
        else:
            nodoPrevio = None
            nodoActual = self.nodoInicial
            while nodoActual.siguiente != None:
                nodoPrevio = nodoActual
                nodoActual = nodoActual.siguiente
            nodoPrevio.siguiente = None
            return nodoActual.dato

    # Repeticiones de un dato
    def repeticionesDato(self, dato_buscar) -> (int | None):
        if self.estaVacia():
            return None
        else:
            cont = 0
            nodoActual = self.nodoInicial
            while nodoActual != None:
                if nodoActual.dato == dato_buscar:
                    cont = cont + 1
                nodoActual = nodoActual.siguiente
            return cont

    # Elemento en posición dada
    def elementoEnPosicion(self, posicion) -> (int | float | str | None):
        if self.estaVacia() or posicion < 0:
            return None

        nodaActual = self.nodoInicial
        cont = 0
        while nodaActual != None and cont < posicion:
            nodaActual = nodaActual.siguiente
            cont = cont + 1

        if nodaActual is None:
            return None
        else:
            return nodaActual.dato

    # Último elemento   
    def ultimoElemento(self) -> (int | float | str | None):
        if self.estaVacia():
            return None

        if self.nodoInicial.siguiente == None:
            return self.nodoInicial.dato
        
        nodoActual = self.nodoInicial
        while nodoActual.siguiente != None:
            nodoActual = nodoActual.siguiente
        return nodoActual.dato

    # Eliminar en posición dada   
    def eliminarEnPosicion(self, posicion) -> (bool | None):
        if self.estaVacia() or posicion < 0 or posicion >= self.contarNodos():
            return None

        if posicion == 0:
            self.eliminarAlInicio()
            return True
        
        nodoPrevio = None
        nodoActual = self.nodoInicial
        cont = 0
        while nodoActual.siguiente != None and cont < posicion:
            nodoPrevio = nodoActual
            nodoActual = nodoActual.siguiente
            cont = cont + 1
        
        nodoPrevio.siguiente = nodoActual.siguiente
        return True
    
    # Cantidad de nodos
    def contarNodos(self) -> (int | None):
        if self.estaVacia():
            return None
        
        cont = 0
        nodoActual = self.nodoInicial
        while nodoActual != None:
            nodoActual = nodoActual.siguiente
            cont = cont + 1

        return cont
    
    # Obtener nodo en posición ingresada
    def obtenerNodo(self, posicion):
        if self.estaVacia():
            return None
            
        if posicion < 0 or posicion >= self.contarNodos():
            return None
        
        nodoActual = self.nodoInicial
        cont = 0
        while nodoActual != None and cont < posicion:
            nodoActual = nodoActual.siguiente
            cont += 1
        
        return nodoActual

    # Penúltimo elemento
    def penultimoElemento(self):
        if self.estaVacia():
            return None
        
        if self.nodoInicial.siguiente == None:
            return None
        
        nodoPrevio = None
        nodoActual = self.nodoInicial
        while nodoActual.siguiente != None:
            nodoPrevio = nodoActual
            nodoActual = nodoActual.siguiente
        
        return nodoPrevio.dato
    
    # Elemento entre dos posiciones
    def elementosEntrePosiciones(self, posInicial, posFinal):
        if self.estaVacia() or posInicial >= posFinal:
            return None
        
        nodoActual = self.nodoInicial
        cont = 0
        while nodoActual.siguiente != None and cont < posInicial:
            nodoActual = nodoActual.siguiente
            cont = cont + 1

        elementos = []
        while nodoActual.siguiente != None and cont <= posFinal:
            elementos.append(nodoActual.dato)
            nodoActual = nodoActual.siguiente
            cont = cont + 1

        return elementos

    # Eliminar apariciones de un dato
    def eliminarAparicionesDato(self, dato_buscar):
        if self.estaVacia():
            return None
        
        while self.nodoInicial.dato == dato_buscar:
            self.nodoInicial = self.nodoInicial.siguiente
            if self.nodoInicial is None:
                return True

        cont = 0
        nodoPrevio = None
        nodoActual = self.nodoInicial
        while nodoActual != None:
            if nodoActual.dato == dato_buscar:
                nodoPrevio.siguiente = nodoActual.siguiente
            else:
                nodoPrevio = nodoActual
            nodoActual = nodoActual.siguiente
        
        return True

    # INDICADOR PARCIAL
    def datoRepetido(self, dato_buscar) -> (bool | None):
        if self.estaVacia():
            return None
        
        cont = 0
        nodoActual = self.nodoInicial
        while nodoActual != None:
            if nodoActual.dato == dato_buscar:
                cont = cont + 1
            nodoActual = nodoActual.siguiente

        if cont > 1:
            return True
        elif cont == 0:
            return None
        else:
            return False        


# Clase comparadora de listas simples
class ComparadoraListasSimples:
    def __init__(self, lista1: ListaEnlazadaSimple, lista2: ListaEnlazadaSimple) -> None:
        self.listaSimple1 = lista1
        self.listaSimple2 = lista2

    # Indicar si dos listas son iguales (longitud)
    def compararLongitud(self) -> bool:
        longitud_lista1 = self.listaSimple1.contarNodos()
        longitud_lista2 = self.listaSimple2.contarNodos()
        if longitud_lista1 == longitud_lista2:
            return True
        else:
            return False
    
    # Indicar si dos listas son iguales (contenido)
    def compararContenido(self) -> bool:
        contenido_lista1 = self.listaSimple1.__str__()
        contenido_lista2 = self.listaSimple2.__str__()
        if contenido_lista1 == contenido_lista2:
            return True
        else:
            return False
        
    # Indicar si dos listas son iguales (longitud y contenido)
    def compararLongitudContenido(self) -> bool:
        if self.compararLongitud() and self.compararContenido():
            return True
        else:
            return False
