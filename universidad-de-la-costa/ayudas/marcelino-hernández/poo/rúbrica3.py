# Ejercicio 3

class Item():
    def __init__(self, title, description):
        self.__title = title
        self.__description = description

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.__description

    def viewDescriptionITEM(self):
        print(f"Title: {self.get_title()}, Description: {self.get_description()}")

class Book(Item):
    def __init__(self, author, isbn):
        self.__author = author
        self.__isbn = isbn

    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn

    def viewDescriptionBOOK(self):
        print(f"Author: {self.get_author()}, ISBN: {self.get_isbn()}")

class DVD(Item):
    def __init__(self, director, certificate):
        self.__director = director
        self.__certificate = certificate

    def set_director(self, director):
        self.__director = director

    def get_director(self):
        return self.__director

    def set_certificate(self, certificate):
        self.__certificate = certificate

    def get_certificate(self):
        return self.__certificate

    def viewDescriptionDVD(self):
        print(f"Director: {self.get_director()}, Certificate: {self.get_certificate()}")

class CD(Item):
    def __init__(self, artist, genre, numberOfTracks):
        self.__artist = artist
        self.__genre = genre
        self.__numberOfTracks = numberOfTracks

    def set_artist(self, artist):
        self.__artist = artist

    def get_artist(self):
        return self.__artist

    def set_genre(self, genre):
        self.__genre = genre

    def get_genre(self):
        return self.__genre

    def set_numberOfTracks(self, numberOfTracks):
        self.__numberOfTracks = numberOfTracks

    def get_numberOfTracks(self):
        return self.__numberOfTracks

    def viewDescriptionCD(self):
        print(f"Artist: {self.get_artist()}, Genre: {self.get_genre()}, Number Of Tracks: {self.get_numberOfTracks()}")

def main():
    print("ITEM 1")
    item1 = Book("SANTIAGO ANDRÉS", "A123")
    item1.set_title("LIBRO EDUCATIVO")
    item1.set_description("PARA FAMILIAS")
    item1.viewDescriptionITEM()
    item1.viewDescriptionBOOK()

    print("")

    print("ITEM 2")
    item2 = DVD("JOSÉ ÁNGEL", "EFECTOS VISUALES")
    item2.set_title("FOTOGRAMA ANIMALES")
    item2.set_description("UNA VISTA ESPECIAL A LOS ANIMALES")
    item2.viewDescriptionITEM()
    item2.viewDescriptionDVD()

    print("")

    print("ITEM 3")
    item2 = CD("JOSÉ JOSÉ", "ROMÁNTICO", 79)
    item2.set_title("AMAR Y QUERER")
    item2.set_description("UNA CANCIÓN SOBRE EL AMOR Y LOS DESEOS")
    item2.viewDescriptionITEM()
    item2.viewDescriptionCD()

main()