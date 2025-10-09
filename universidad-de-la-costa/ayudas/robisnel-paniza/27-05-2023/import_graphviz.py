class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None


class Arbol:
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def __agregar(self, nodo, nuevo_valor):
        if nuevo_valor < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(nuevo_valor)
            else:
                self.__agregar(nodo.izquierda, nuevo_valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(nuevo_valor)
            else:
                self.__agregar(nodo.derecha, nuevo_valor)

    def agregar(self, nuevo_valor):
        self.__agregar(self.raiz, nuevo_valor.capitalize())

    def __inorden(self, nodo):
        if nodo is not None:
            self.__inorden(nodo.izquierda)
            print(nodo.dato, end=" ")
            self.__inorden(nodo.derecha)

    def inorden(self):
        self.__inorden(self.raiz)

    def __buscar(self, nodo, valor):
        if nodo is None:
            return None
        if nodo.dato == valor:
            return nodo

        if valor < nodo.dato:
            return self.__buscar(nodo.izquierda, valor)
        else:
            return self.__buscar(nodo.derecha, valor)

    def buscar(self, valor):
        return self.__buscar(self.raiz, valor)


class JuegoAdivinanza:
    def __init__(self):
        self.arbol_animales = Arbol("Pájaro")
        self.arbol_personajes = Arbol("Mario")
        self.arbol_flores = Arbol("Rosa")
        self.arbol_actual = None
        self.categoria = None

    def obtenerCategoria(self):
        print("Juguemos a adivinar")
        print("1. Animales")
        print("2. Personajes")
        print("3. Flores")

        while True:
            opcion = input("Elige una categoría (1-3): ")
            if opcion in ("1", "2", "3"):
                break
            else:
                print("Opción inválida. Por favor, elige una categoría válida.")

        if opcion == "1":
            self.arbol_actual = self.arbol_animales
            self.categoria = "Animal"
        elif opcion == "2":
            self.arbol_actual = self.arbol_personajes
            self.categoria = "Personaje"
        elif opcion == "3":
            self.arbol_actual = self.arbol_flores
            self.categoria = "Flor"

    def jugar(self):
        print("Bienvenido al juego de adivinanzas")

        while True:
            nodo_actual = self.arbol_actual.raiz
            while True:
                respuesta = input("¿Es un(a) " + nodo_actual.dato + "? (si/no): ")
                if respuesta.lower() == "si":
                    if nodo_actual.izquierda is not None:
                        nodo_actual = nodo_actual.izquierda
                    else:
                        print("¡He adivinado!")
                        break
                elif respuesta.lower() == "no":
                    if nodo_actual.derecha is not None:
                        nodo_actual = nodo_actual.derecha
                    else:
                        nuevo_animal = input("¿Cuál es tu " + self.categoria + "?: ")
                        diferencia = input("¿Qué diferencia a " + nuevo_animal + " de " + nodo_actual.dato + "?: ")
                        respuesta = input("Para un(a) " + nuevo_animal + ", la respuesta es si/no: ")

                        while respuesta.lower() not in ("si", "no"):
                            print("Respuesta inválida. Por favor, responde 'si' o 'no'.")
                            respuesta = input("Para un(a) " + nuevo_animal + ", la respuesta es si/no: ")

                        # Actualizar árbol
                        nodo_actual.derecha = Nodo(nodo_actual.dato)
                        nodo_actual.dato = diferencia
                        nodo_actual.izquierda = Nodo(nuevo_animal)
                        nodo_actual.derecha.izquierda = Nodo(nodo_actual.derecha.dato)

                        break
                else:
                    print("Respuesta inválida. Por favor, responde 'si' o 'no'.")

            respuesta = input("¿Jugamos otra vez? (si/no): ")
            while respuesta.lower() not in ("si", "no"):
                print("Respuesta inválida. Por favor, responde 'si' o 'no'.")
                respuesta = input("¿Jugamos otra vez? (si/no): ")

            if respuesta.lower() == "no":
                break


juego = JuegoAdivinanza()
juego.obtenerCategoria()
juego.jugar()