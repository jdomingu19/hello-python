

class ArbolBinarioAnimales:
    def __init__(self, pregunta: str=None) -> None:
        self.pregunta = pregunta
        self.si = None
        self.no = None

    def empezar(self):
        nodoRaiz = ArbolBinarioAnimales(pregunta="¿Es vertebrado?")
        nodoRaiz.si = ArbolBinarioAnimales(pregunta="¿Es mamífero?")
        nodoRaiz.si.no = ArbolBinarioAnimales(pregunta="¿Es un ave?")
        nodoRaiz.si.no.no = ArbolBinarioAnimales(pregunta="¿Es un pez?")
        nodoRaiz.si.no.no.no = ArbolBinarioAnimales(pregunta="¿Es anfibio?")
        nodoRaiz.si.no.no.no.no = ArbolBinarioAnimales(pregunta="¿Es reptil?")

        return self.preguntar(nodoRaiz)

    def preguntar(self, nodo: "ArbolBinarioAnimales"):
        if nodo is not None:
            x = input(nodo.pregunta).lower()
            if x == "si":
                self.preguntar(nodo.si)
            else:
                self.preguntar(nodo.no)
        

a = ArbolBinarioAnimales()
a.empezar()


class ArbolBinarioPersonajes:
    pass


class ArbolBinarioFlores:
    pass