# Cadenas | 1.0 | Jesús Domínguez
from time import sleep

"""
Barra de progreso
try except
operaciones
guardar horizontalmente
guerdar verticalmente
"""
# Método principal
class Cadenas:
    # Constructor
    def __init__(self, indice:int) -> None:
        self.__indice = indice
        self.__cadena = None
        self.__longitud = None
        self.__vector = None
        self.__diccionario = None

    # Mostrar objeto
    def __str__(self) -> str:
        return f"OBJETO      : {self.__indice}\nLONGITUD    : {self.__longitud}\nVECTOR      : {self.__vector}\nCADENA      : {self.__cadena}\nDICCIONARIO : {self.__diccionario}"

    # Setters and getters
    def set_indice(self, x:int):
        self.__indice = x
    
    def get_indice(self):
        return self.__indice

    def set_cadena(self, x:str):
        self.__cadena = x
    
    def get_cadena(self):
        return self.__cadena

    def set_longitud(self, x:int):
        self.__longitud = x
    
    def get_longitud(self):
        return self.__longitud

    def set_vector(self, x:list):
        self.__vector = x
    
    def get_vector(self):
        return self.__vector

    def set_diccionario(self, x:dict):
        self.__diccionario = x
    
    def get_diccionario(self):
        return self.__diccionario

    # Comportamientos
    def establecer(self, cadena:str, longitud:int, vector:list, diccionario:dict):
        self.set_cadena(cadena)
        self.set_longitud(longitud)
        self.set_vector(vector)
        self.set_diccionario(diccionario)
        
    def menu(self):
        while True:# ¿REPETIR?
            x = """POO | CADENAS | 1.0\n1. Leer cadena\n2. Leer vector\n3. Leer diccionario\n4. Leer txt\n5. Guardar en txt\n6. Mostrar objeto\n7. Operaciones Comming Soon...\n8. Salir"""
            print(x)
            accion = input(">>> ")

            while not accion.isnumeric() or int(accion) <= 0 or int(accion) > 8:
                print("Datos incorrectos")
                accion = input(">>> ")
        
            if accion == "1": self.leer_cadena()
            if accion == "2": self.leer_vector()
            if accion == "3": self.leer_diccionario()
            if accion == "4": self.leer_txt()
            if accion == "5": self.guardar_txt()
            if accion == "6": print(self)
            if accion == "7": pass
            if accion == "8": 
                print("¡Hasta pronto!")
                return False
            
            print("")
            for i in range(3):
                print(3 - i, end="\r")
                sleep(1)
            

    def leer_cadena(self):
        cadena = input("Ingrese cadena: ")
        print(type(cadena))

        lista = []
        for i in cadena:
            lista.append(i)
        
        self.establecer(cadena, len(cadena), lista, {"Cadena":cadena, "Longitud":len(cadena), "Vector":lista})

    def leer_vector(self):
        lista = input("Ingrese la lista: ")
        print(type(lista))
        lista = lista.replace("[", "")
        lista = lista.replace("]", "")
        lista = lista.replace("'", "")
        print(lista)
        lista = lista.split(",")
        print(lista, type(lista))
        
        cadena = ""
        for i in lista:
            cadena = cadena + i
        print(cadena, type(cadena))

        self.establecer(cadena, len(cadena), lista, {"Cadena":cadena, "Longitud":len(cadena), "Vector":lista})
        
    def leer_diccionario(self):
        pass

    def leer_txt(self):
        pass

    def guardar_txt(self):
        pass

    def palindromos(self):
        pass
    
# Método principal
def main():
    a = Cadenas(0)
    a.menu()

# Llamar método principal
main()