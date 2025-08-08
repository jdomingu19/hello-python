class MenuDelRestaurande():
    def __init__(self):
        self.__menu = []

    def set_registros(self, x:list):
        self.__menu = x

    def get_registros(self):
        return self.__menu

    def llenar_datos(self, filas:int):
        print("llenar datos")
        i = 0
        while i < filas:
            self.get_registros().append([])
            j = 0
            while j < 9:
                if j == 0:
                    id = int(input("Ingrese id de la comida: "))
                    self.get_registros()[i].append(id)
                if j == 1:
                    nombre = input("Ingrese nombre de la comida: ")
                    self.get_registros()[i].append(nombre)
                if j == 2:
                    ing_1 = input("Ingrese ingrediente 1 de la comida: ")
                    self.get_registros()[i].append(ing_1)
                if j == 3:
                    ing_2 = input("Ingrese ingrediente 2 de la comida: ")
                    self.get_registros()[i].append(ing_2)
                if j == 4:
                    ing_2 = input("Ingrese ingrediente 3 de la comida: ")
                    self.get_registros()[i].append(ing_2)
                if j == 5:
                    valor = int(input("Ingrese valor de la comida: "))
                    self.get_registros()[i].append(valor)
                if j == 6:
                    cantidad = int(input("Ingrese cantidad de la comida: "))
                    self.get_registros()[i].append(cantidad)
                if j == 7:
                    total = valor * cantidad
                    self.get_registros()[i].append(total)
                j = j + 1
            i = i + 1
            print("")
        
    
    def mostrar_datos(self):
        print("mostrar datos")
        i = 0
        while i < len(self.get_registros()):
            print(f"{i+1}. ID: {self.get_registros()[i][0]} | NOMBRE: {self.get_registros()[i][1]} | INGREDIENTE 1: {self.get_registros()[i][2]} | INGREDIENTE 2: {self.get_registros()[i][3]} | INGREDIENTE 3: {self.get_registros()[i][4]} | VALOR: ${self.get_registros()[i][5]} | CANTIDAD: {self.get_registros()[i][6]} | TOTAL: ${self.get_registros()[i][7]}")
            i = i + 1
        print("")

    def total_ventas(self):
        print("total ventas")
        total = 0
        i = 0
        while i < len(self.get_registros()):
            total = total + self.get_registros()[i][7]
            i = i + 1
        print(f"${total}")
        print("")

    def producto_mas_vendido(self):
        print("producto mas vendido")
        producto = []
        i = 0
        while i < len(self.get_registros()):
            if self.get_registros()[i][1] not in producto:
                producto.append(self.get_registros()[i][1])
            i = i + 1
        contadores_p = []
        cont = 0
        i = 0
        while i < len(producto):
            j = 0
            while j < len(self.get_registros()):
                if producto[i] == self.get_registros()[j][1]:
                    cont = cont + self.get_registros()[j][6]
                    j = j + 1
            contadores_p.append(cont)
            cont = 0
            i = i + 2
        
        print("lista de productos:")
        i = 0
        while i < len(producto):
            print(f"{producto[i]}, aparece {contadores_p[i]} veces")
            i = i + 1

        prod_mayor = contadores_p[0]
        nombre_prod = producto[0]
        i = 0
        while i < len(producto):
            if contadores_p[i] > prod_mayor:
                prod_mayor = contadores_p[i]
                nombre_prod = producto[i]
            i = i + 1

        cont = 0
        i = 0
        while i < len(contadores_p):
            if contadores_p[i] == prod_mayor:
                cont = cont + 1
            i = i + 1

        if cont != 1:
            print("Los más vendidos: ")
            i = 0
            while i < len(contadores_p):
                if contadores_p[i] == prod_mayor:
                    print(producto[i])
                i = i + 1
        else:
            print(f"Más vendido es {nombre_prod}")
        print("")
    
    def buscar_id(self):
        print("buscar id")
        id = int(input("Ingrese el id a buscar: "))
        encontrado = 0
        i = 0
        while i < len(self.get_registros()):
            if id == self.get_registros()[i][0]:
                encontrado = 1
                print(f"Producto: {self.get_registros()[i][1]}")
                break
            i = i + 1
        if encontrado == 0:
            print(f"id no encontrado")
        print("")

def main():
    menu = MenuDelRestaurande()
    menu.llenar_datos(3)
    menu.mostrar_datos()
    menu.total_ventas()
    menu.producto_mas_vendido()
    menu.buscar_id()
main()