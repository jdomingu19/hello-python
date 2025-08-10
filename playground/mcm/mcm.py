# Python MCM (Mínimo Común Múltiplo)

# Clase MCM
class MCM:
    # Constructor
    def __init__(self) -> None:
        self.__cantidad_numeros = 0
        self.__numeros_usuario = []
        self.__cantidad_multiplos = 0
        self.__matriz_multiplos = []
        self.__multiplos_comunes = []
        self.__mcm = 0

    # Setters and getters
    def set_cantidad_numeros(self, x: int) -> None:
        self.__cantidad_numeros = x

    def get_cantidad_numeros(self) -> int:
        return self.__cantidad_numeros

    def set_numeros_usuario(self, x: list) -> None:
        self.__numeros_usuario = x

    def get_numeros_usuario(self) -> list:
        return self.__numeros_usuario
    
    def set_cantidad_multiplos(self, x: int) -> None:
        self.__cantidad_multiplos = x

    def get_cantidad_multiplos(self) -> int:
        return self.__cantidad_multiplos
    
    def set_matriz_multiplos(self, x: list) -> None:
        self.__matriz_multiplos = x

    def get_matriz_multiplos(self) -> list:
        return self.__matriz_multiplos

    def set_multiplos_comunes(self, x: list) -> None:
        self.__multiplos_comunes = x

    def get_multiplos_comunes(self) -> list:
        return self.__multiplos_comunes
    
    def set_mcm(self, x: int) -> None:
        self.__mcm = x

    def get_mcm(self) -> int:
        return self.__mcm
    
    # 1. Ingresar datos
    def ingresar_datos(self):
        cantidad_numeros = input("Ingrese cantidad de números: ")
        while not cantidad_numeros.isdigit():
            print(f"'{cantidad_numeros}' no es un formato válido...")
            cantidad_numeros = input("Ingrese cantidad de números: ")
        self.set_cantidad_numeros(int(cantidad_numeros))

        cantidad_multiplos = input("Ingrese cantidad de multiplos: ")
        while not cantidad_multiplos.isdigit():
            print(f"'{cantidad_multiplos}' no es un formato válido...")
            cantidad_multiplos = input("Ingrese cantidad de múltiplos: ")
        self.set_cantidad_multiplos(int(cantidad_multiplos))

        numeros_usuarios = []
        for x in range(int(cantidad_numeros)):
            number = input(f"Ingrese un número entero (#{x+1}): ")
            while not number.isdigit():
                print(f"'{number}' no es un formato válido...")
                number = input(f"Ingrese un número entero (#{x+1}): ")
            numeros_usuarios.append(int(number))
        self.set_numeros_usuario(numeros_usuarios)

        return True

    # 2. Calcular múltiplos
    def calcular_multiplos(self):
        matriz_multiplos = []
        i = 0
        while i < self.get_cantidad_numeros():
            multiplos = []
            j = 0
            while j < self.get_cantidad_multiplos():
                multiplo = self.get_numeros_usuario()[i] * (j + 1)
                multiplos.append(multiplo)
                j = j + 1
            matriz_multiplos.append(multiplos)
            i = i + 1

        self.set_matriz_multiplos(matriz_multiplos)

    # 3. Encontrar múltiplos comunes
    def encontar_multiplos_comunes(self):
        multiplos_comunes = []
        fila_matriz_primera = self.get_matriz_multiplos()[0]
        i = 0
        while i < len(fila_matriz_primera):
            j = 0
            while j < len(self.get_matriz_multiplos()):
                if fila_matriz_primera[i] in self.get_matriz_multiplos()[j]:
                    multiplos_comunes.append(fila_matriz_primera[i])
                j = j + 1
            i = i + 1
        
        set_multiplos = set(multiplos_comunes)
        for x in set_multiplos:
            if multiplos_comunes.count(x) == self.get_cantidad_numeros():
                self.get_multiplos_comunes().append(x)

    # 4. Encontrar el MCM
    def encontrar_mcm(self):
        if len(self.get_multiplos_comunes()) > 0:
            mcm = min(self.get_multiplos_comunes())
            self.set_mcm(mcm)
        else:
            self.set_mcm(0)

    # 5. Imprimir datos (consola)
    def imprimir_datos(self):
        print(f"Cantidad números usuario: {self.get_cantidad_numeros()}")
        print(f"Lista números usuario: {self.get_numeros_usuario()}")
        print(f"Matriz múltiplos usuario: {self.get_matriz_multiplos()}")
        print(f"Lista múltiplos comunes: {self.get_multiplos_comunes()}")
        print(f"MCM: {self.get_mcm()}")

# Función principal
def main():
    consulta01 = MCM()
    consulta01.ingresar_datos()
    consulta01.calcular_multiplos()
    consulta01.encontar_multiplos_comunes()
    consulta01.encontrar_mcm()
    consulta01.imprimir_datos()

# Llamar función principal
main()
