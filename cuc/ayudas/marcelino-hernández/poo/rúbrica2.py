# Ejercicio 2

class Libro():
    def __init__(self, ISBN, titulo, autor, numPaginas):
        self.__ISBN = ISBN
        self.__titulo = titulo
        self.__autor = autor
        self.__numPaginas = numPaginas

    def set_ISBN(self, ISBN):
        self.__ISBN = ISBN

    def get_ISBN(self):
        return self.__ISBN

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_titulo(self):
        return self.__titulo

    def set_autor(self, autor):
        self.__autor = autor

    def get_autor(self):
        return self.__autor

    def set_numPaginas(self, numPaginas):
        self.__numPaginas = numPaginas

    def get_numPaginas(self):
        return self.__numPaginas

    def mensaje(self):
        print(f"El libro con ISBN {self.get_ISBN()} creado por el autor {self.get_autor()} tiene {self.get_numPaginas()} páginas y su título es {self.get_titulo()}")


def main():
    libro1 = Libro("A123", "CIUDADANÍA", "JOSÉ MIGUEL", 45)
    libro1.mensaje()

    libro2 = Libro("B456", "ALGORITMOS", "MARÍA SOFÍA", 79)
    libro2.mensaje()

    if libro1.get_numPaginas() > libro2.get_numPaginas():
        print("El libro 1 tiene más páginas...")
    elif libro1.get_numPaginas() < libro2.get_numPaginas():
        print("El libro 2 tiene más páginas...")
    else:
        print("Ambos tienen misma cantidad de páginas...")
main()