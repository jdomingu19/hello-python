# Robisnel Paniza

class NodosBinarios:
    def __init__(self, dato) -> None:
        self.dato = dato
        self.nodoIzquierdo = None
        self.nodoDerecho = None

    # nodo sin hijos...
    def esHoja(self):
        return self.nodoIzquierdo == None and self.nodoDerecho == None


class ArbolesBinarios:
    def __init__(self) -> None:
        self.nodoRaiz = None

    # arbol sin nodos...
    def estaVacio(self):
        return self.nodoRaiz == None

    # agregar nodos...
    def __agregarNodoRecursivo(self, nodoActual: NodosBinarios, valorNuevo):
        if self.nodoRaiz is None:
            self.nodoRaiz = NodosBinarios(valorNuevo)
            return

        if valorNuevo < nodoActual.dato:
            if nodoActual.nodoIzquierdo is None:
                nodoActual.nodoIzquierdo = NodosBinarios(valorNuevo)
            else:
                self.__agregarNodoRecursivo(nodoActual.nodoIzquierdo, valorNuevo)
        else:
            if nodoActual.nodoDerecho is None:
                nodoActual.nodoDerecho = NodosBinarios(valorNuevo)
            else:
                self.__agregarNodoRecursivo(nodoActual.nodoDerecho, valorNuevo)

    def agregarNodo(self, valorNuevo):
        self.__agregarNodoRecursivo(self.nodoRaiz, valorNuevo)

    # in orden...
    def __inOrdenRecursivo(self, nodoActual: NodosBinarios):
        if nodoActual is not None:
            self.__inOrdenRecursivo(nodoActual.nodoIzquierdo)
            print(nodoActual.dato, end=" ")
            self.__inOrdenRecursivo(nodoActual.nodoDerecho)

    def inOrden(self):
        self.__inOrdenRecursivo(self.nodoRaiz)

    # pre orden...
    def __preOrdenRecursivo(self, nodoActual: NodosBinarios):
        if nodoActual is not None:
            print(nodoActual.dato, end=" ")
            self.__preOrdenRecursivo(nodoActual.nodoIzquierdo)
            self.__preOrdenRecursivo(nodoActual.nodoDerecho)

    def preOrden(self):
        self.__preOrdenRecursivo(self.nodoRaiz)

    # pos orden...
    def __posOrdenRecursivo(self, nodoActual: NodosBinarios):
        if nodoActual is not None:
            self.__posOrdenRecursivo(nodoActual.nodoIzquierdo)
            self.__posOrdenRecursivo(nodoActual.nodoDerecho)
            print(nodoActual.dato, end=" ")

    def posOrden(self):
        self.__posOrdenRecursivo(self.nodoRaiz)

    # buscar...
    def __buscarRecursivo(self, nodoActual: NodosBinarios, valorBuscar):
        if nodoActual is None:
            return None
        
        if nodoActual.dato == valorBuscar:
            return nodoActual
        
        if valorBuscar < nodoActual.dato:
            return self.__buscarRecursivo(nodoActual.nodoIzquierdo, valorBuscar)
        else:
            return self.__buscarRecursivo(nodoActual.nodoDerecho, valorBuscar)

    def buscar(self, valorBuscar):
        return self.__buscarRecursivo(self.nodoRaiz, valorBuscar)


class JuegoRubrica:
    def __init__(self) -> None:
        self.arbolAnimales = ArbolesBinarios()
        self.arbolPersonajes = ArbolesBinarios()
        self.arbolFlores = ArbolesBinarios()
        self.arbolActual = None
        self.categoria = None

    def setCategoria(self):
        print(f"ÁRBOL DE ADIVINANZA\n1. Animales\n2. Personajes\n3. Flores\n") 
        while True:
            x = input("-> ")
            if x not in {"1", "2", "3"}:
                print("-> Incorrecto...")
            else:
                break
        if x == "1":
            self.arbolActual = self.arbolAnimales
            self.arbolActual.nodoRaiz = NodosBinarios("Pájaro")
            self.categoria = "Animal"
        elif x == "2":
            self.arbolActual = self.arbolPersonajes
            self.arbolActual.nodoRaiz = NodosBinarios("Superman")
            self.categoria = "Personaje"
        elif x == "3":
            self.arbolActual = self.arbolFlores
            self.arbolActual.nodoRaiz = NodosBinarios("Margarita")
            self.categoria = "Flor"

    def jugar(self):
        print("- - - - -")
        while True:
            nodoActual: NodosBinarios = self.arbolActual.nodoRaiz
            while True:
                y = input(f"-> ¿Es un(a) {nodoActual.dato}? si/no: ").lower()
                if y == "si":
                    if nodoActual.nodoIzquierdo is not None:
                        nodoActual = nodoActual.nodoIzquierdo
                    else:
                        print("¡Adiviné!")
                        break
                elif y == "no":
                    if nodoActual.nodoDerecho is not None:
                        nodoActual = nodoActual.nodoDerecho
                    else:
                        animalNuevo = input(f"-> ¿Cuál era tu {self.categoria}?: ").capitalize()
                        diferencia = input(f"-> ¿Diferencia entre {animalNuevo} y {nodoActual.dato}?: ").capitalize()
                        y = input(f"-> Para un(a) {animalNuevo} la respuesta es si/no: ").lower()
                        while y not in {"si", "no"}:
                            print(f"Incorrecto...")
                            y = input(f"-> Para un(a) {animalNuevo} la respuesta es si/no: ").lower()
                        nodoActual.nodoDerecho = NodosBinarios(nodoActual.dato)
                        nodoActual.dato = diferencia
                        nodoActual.nodoIzquierdo = NodosBinarios(animalNuevo)
                        nodoActual.nodoDerecho.nodoIzquierdo = NodosBinarios(nodoActual.nodoDerecho.dato)
                        break
                else:
                    print(f"Incorrecto...")
            y = input(f"-> ¿jugar otra vez? si/no: ").lower()
            while y not in {"si", "no"}:
                print(f"Incorrecto...")
                y = input(f"-> ¿jugar otra vez? si/no: ").lower()
            if y == "no":
                print("¡Chao!")
                break
            elif y == "si":
                print("")
                

# prueba...
juego01 = JuegoRubrica()
juego01.setCategoria()
juego01.jugar()
