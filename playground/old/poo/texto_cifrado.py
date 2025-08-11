# Texto cifrado | v1.0 | Jesús Alberto Domínguez Charris


"""
1.1 -> Cambiar m[i][j] por m[i] + índices
"""
# Clase Mensajes
class Mensajes():
    # Constructor
    def __init__(self):
        self.__texto = None # str
        self.__cifrado = None # list

    # Setters y getters
    def setTexto(self, x:str):
        self.__texto = x

    def getTexto(self):
        return self.__texto

    def setCifrado(self, x:list):
        self.__cifrado = x

    def getCifrado(self):
        return self.__cifrado

    def cifrarTexto(self):
        print("")
        x = [["a", "0"], 
             ["b", "1"],
             ["c", "2"],
             ["d", "3"],
             ["e", "4"],
             ["f", "5"],
             ["g", "6"],
             ["h", "7"],
             ["i", "8"],
             ["j", "9"],
             ["k", "10"],
             ["l", "11"],
             ["m", "12"],
             ["n", "13"],
             ["ñ", "14"],
             ["o", "15"],
             ["p", "16"],
             ["q", "17"],
             ["r", "18"],
             ["s", "19"],
             ["t", "20"],
             ["u", "21"],
             ["v", "22"],
             ["w", "23"],
             ["x", "24"],
             ["y", "25"],
             ["z", "26"],
             ["A", "27"], 
             ["B", "28"],
             ["C", "29"],
             ["D", "30"],
             ["E", "31"],
             ["F", "32"],
             ["G", "33"],
             ["H", "34"],
             ["I", "35"],
             ["J", "36"],
             ["K", "37"],
             ["L", "38"],
             ["M", "39"],
             ["N", "40"],
             ["Ñ", "41"],
             ["O", "42"],
             ["P", "43"],
             ["Q", "44"],
             ["R", "45"],
             ["S", "46"],
             ["T", "47"],
             ["U", "48"],
             ["V", "49"],
             ["W", "50"],
             ["X", "51"],
             ["Y", "52"],
             ["Z", "53"],
             ["0", "54"],
             ["1", "55"],
             ["2", "56"],
             ["3", "57"],
             ["4", "58"],
             ["5", "59"],
             ["6", "60"],
             ["7", "61"],
             ["8", "62"],
             ["9", "63"],
             [".", "61"],
             [":", "62"],
             [",", "63"],
             [";", "64"],
             ["¡", "65"],
             ["!", "66"],
             ["¿", "67"],
             ["?", "68"],
             ["(", "69"],
             [")", "70"],
             ["+", "71"],
             ["-", "72"],
             ["*", "73"],
             ["/", "74"],
             ["#", "75"],
             ["$", "76"],
             ["%", "77"],
             ["&", "78"],
             ["=", "79"],
             ["°", "80"],
             ["|", "81"],
             ["¬", "82"],
             ["'", "83"],
             ["_", "84"],
             ["[", "85"],
             ["]", "86"],
             ["{", "87"],
             ["}", "88"],
             ["^", "89"],
             ["~", "90"],
             ["<", "91"],
             [">", "92"],
             ["@", "93"],
             [" ", "94"],
             ["á", "95"],
             ["é", "96"],
             ["í", "97"],
             ["ó", "98"],
             ["ú", "99"],
             ["Á", "100"],
             ["É", "101"],
             ["I", "102"],
             ["Ó", "103"],
             ["Ú", "104"],
            ]       
        self.setCifrado([])
        texto = input("Ingrese texto a cifrar: ")
        for i in range(len(texto)): # Caracter en texto
            for j in range(len(x)): # Buscar en x
                if texto[i] == x[j][0]: # Si son iguales
                    self.getCifrado().append(x[j][1]) # Agregarlo
                    if i != len(texto) - 1: # Si i diferente del último
                        self.getCifrado().append("&") # Separador

        print("El texto cifrado es:")
        for i in range(len(self.getCifrado())):
            if i != len(self.getCifrado()) - 1:
                print(self.getCifrado()[i], end="")
            else:
                print(self.getCifrado()[i])

    def traducirCifrado(self):
        print("")
        x = [["a", "0"], 
             ["b", "1"],
             ["c", "2"],
             ["d", "3"],
             ["e", "4"],
             ["f", "5"],
             ["g", "6"],
             ["h", "7"],
             ["i", "8"],
             ["j", "9"],
             ["k", "10"],
             ["l", "11"],
             ["m", "12"],
             ["n", "13"],
             ["ñ", "14"],
             ["o", "15"],
             ["p", "16"],
             ["q", "17"],
             ["r", "18"],
             ["s", "19"],
             ["t", "20"],
             ["u", "21"],
             ["v", "22"],
             ["w", "23"],
             ["x", "24"],
             ["y", "25"],
             ["z", "26"],
             ["A", "27"], 
             ["B", "28"],
             ["C", "29"],
             ["D", "30"],
             ["E", "31"],
             ["F", "32"],
             ["G", "33"],
             ["H", "34"],
             ["I", "35"],
             ["J", "36"],
             ["K", "37"],
             ["L", "38"],
             ["M", "39"],
             ["N", "40"],
             ["Ñ", "41"],
             ["O", "42"],
             ["P", "43"],
             ["Q", "44"],
             ["R", "45"],
             ["S", "46"],
             ["T", "47"],
             ["U", "48"],
             ["V", "49"],
             ["W", "50"],
             ["X", "51"],
             ["Y", "52"],
             ["Z", "53"],
             ["0", "54"],
             ["1", "55"],
             ["2", "56"],
             ["3", "57"],
             ["4", "58"],
             ["5", "59"],
             ["6", "60"],
             ["7", "61"],
             ["8", "62"],
             ["9", "63"],
             [".", "61"],
             [":", "62"],
             [",", "63"],
             [";", "64"],
             ["¡", "65"],
             ["!", "66"],
             ["¿", "67"],
             ["?", "68"],
             ["(", "69"],
             [")", "70"],
             ["+", "71"],
             ["-", "72"],
             ["*", "73"],
             ["/", "74"],
             ["#", "75"],
             ["$", "76"],
             ["%", "77"],
             ["&", "78"],
             ["=", "79"],
             ["°", "80"],
             ["|", "81"],
             ["¬", "82"],
             ["'", "83"],
             ["_", "84"],
             ["[", "85"],
             ["]", "86"],
             ["{", "87"],
             ["}", "88"],
             ["^", "89"],
             ["~", "90"],
             ["<", "91"],
             [">", "92"],
             ["@", "93"],
             [" ", "94"],
             ["á", "95"],
             ["é", "96"],
             ["í", "97"],
             ["ó", "98"],
             ["ú", "99"],
             ["Á", "100"],
             ["É", "101"],
             ["I", "102"],
             ["Ó", "103"],
             ["Ú", "104"],
            ]
        self.setTexto("")
        cifrado = input("Ingrese cifrado a traducir: ")
        cifrado = cifrado.split("&")
        for i in range(len(cifrado)): # Código de cifrado
            for j in range(len(x)): # Buscar en x
                if cifrado[i] == x[j][1]: # Si son iguales
                    self.setTexto(self.getTexto() + x[j][0])  # Agregarlo

        print("La traducción del cifrado es:")
        print(self.getTexto())

    def menu(self):
        print("TEXTO CIFRADO 1.0")
        print("1. Texto a crifrado")
        print("2. Cifrado a texto")
        accion = input("¿Qué desea hacer?: ")
        while accion != "1" and accion != "2":
            print("Datos no válidos...")
            accion = input("¿Qué desea hacer?: ")
        if accion == "1":
            self.cifrarTexto()
        else:
            self.traducirCifrado()

# Método principal
def main():
    a = Mensajes()
    a.menu()

# Llamar método principal
main()