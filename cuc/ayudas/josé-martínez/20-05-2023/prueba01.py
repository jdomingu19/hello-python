# Prueba de AB interactivo | Jesús Domínguez

class NodosBinarios:
    def __init__(self, pregunta) -> None:
        self.pregunta = pregunta
        self.si = None
        self.no = None

    
def construirArbol():
    raiz = NodosBinarios("¿Tiene pelo?")
    raiz.si = NodosBinarios("¿Es un mamífero?")
    raiz.no = NodosBinarios("¿Tiene trompa?")
    raiz.si.si = NodosBinarios("Es un perro")
    raiz.si.no = NodosBinarios("Es un elefante")
    raiz.no.si = NodosBinarios("Es un pez")
    raiz.no.no = NodosBinarios("Es un cocodrilo")
    return raiz


def hacerPregunta(nodo: NodosBinarios):
    respuesta = input(nodo.pregunta + " (s/n): ").lower()
    if respuesta == "s":
        if nodo.si:
            hacerPregunta(nodo.si)
        else:
            print("¡Adiviné!", nodo.pregunta)
    else:
        if nodo.no:
            hacerPregunta(nodo.no)
        else:
            print("¡Adiviné!", nodo.pregunta)



arbol = construirArbol()
hacerPregunta(arbol)
