# Prueba de AB interactivo | Jesús Domínguez

class Nodos:
    def __init__(self, pregunta=None, animal=None) -> None:
        self.pregunta = pregunta
        self.animal = animal
        self.si = None
        self.no = None


def jugar_adivinanza(nodo: Nodos):
    if nodo.animal:
        adivinanza = input("Ya sé, es un(a) {}. ¿Es correcto? (si/no): ".format(nodo.animal))
        if adivinanza.lower() == "si":
            print("¡He adivinado!")
        else:
            animal = input("¿Cuál es tu animal? ")
            diferencia = input("Qué diferencia a un(a) {} de un(a) {}? ".format(animal, nodo.animal))
            pregunta = input("Para un(a) {}, la respuesta es sí/no? ".format(animal))
            nuevo_animal = Nodos(animal=animal)
            nueva_pregunta = Nodos(pregunta=diferencia)
            if pregunta.lower() == "si":
                nueva_pregunta.si = nuevo_animal
                nueva_pregunta.no = nodo
            else:
                nueva_pregunta.si = nodo
                nueva_pregunta.no = nuevo_animal
            return nueva_pregunta
    else:
        respuesta = input(nodo.pregunta + " (si/no): ")
        if respuesta.lower() == "si":
            nodo.si = jugar_adivinanza(nodo.si)
        else:
            nodo.no = jugar_adivinanza(nodo.no)
    return nodo


def main():
    arbol = Nodos(pregunta="Juguemos a adivinar animales")
    arbol.si = Nodos(pregunta="¿Es mamífero?")
    arbol.no = Nodos(pregunta="¿Ladra?")
    arbol.si.si = Nodos(animal="Vaca")
    arbol.si.no = Nodos(pregunta="¿Maúlla?")
    arbol.si.no.si = Nodos(animal="Gato")
    arbol.si.no.no = Nodos(animal="Perro")
    arbol.no.si = Nodos(pregunta="¿Es acuático?")
    arbol.no.si.si = Nodos(animal="Ballena")

    jugar_adivinanza(arbol)

main()
