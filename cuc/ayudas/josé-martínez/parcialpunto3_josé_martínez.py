# Clase
class Ventas:
    # Constructor
    def __init__(self):
        self.id = []
        self.usuarios = []
        self.productos = []
        self.totales= []

    # Setters y getters
    # set = almacenar
    # get = devolver
    def setId(self, id:list):
        self.id = id

    def getId(self):
        return self.id

    def setUsuarios(self, usuarios:list):
        self.usuarios = usuarios

    def getUsuarios(self):
        return self.usuarios

    def setProductos(self, productos:list):
        self.productos = productos

    def getProductos(self):
        return self.productos

    def setTotales(self, totales:list):
        self.totales = totales

    def getTotales(self):
        return self.totales

    # llenar los vectores de la venta
    def almacenar(self):
        registros = int(input("Digite número de registros: "))
        for x in range(registros):
            id = int(input(f"Digite id venta {x+1}: "))
            usuario = input(f"Digite usuario venta {x+1}: ")
            prod = input(f"Digite producto venta {x+1} (computador, tablet, celular): ").lower()
            if prod == "computador": 
                total = 500000
            elif prod == "tablet": 
                total = 200000
            elif prod == "celular": 
                total = 100000
            else:
                total = 0
            self.getId().append(id)
            self.getUsuarios().append(usuario)
            self.getProductos().append(prod)
            self.getTotales().append(total)

    # imprimir vectores de la venta
    def imprimir(self):
        print("")
        print(f"ID Venta: {self.getId()}")
        print(f"USUARIOS Venta: {self.getUsuarios()}")
        print(f"PRODUCTOS Venta: {self.getProductos()}")
        print(f"TOTALES Venta: {self.getTotales()}")
    
    # 1. leer id y devolver su producto
    def idProducto(self):
        print("")
        registros = len(self.getId())
        buscar_id = int(input("Digite id a buscar: "))
        
        # verificar si ese id existe
        if buscar_id in self.getId():
            # buscar producto de id
            for x in range(registros):
                if buscar_id == self.getId()[x]:
                    # guardar en txt
                    print(f"El producto de ese ID es {self.getProductos()[x]}")
                    f = open("idProducto.txt", "w")
                    f.write(f"{self.getProductos()[x]}")
                    f.close()
                    break
        else:
            print(f"{buscar_id} no está en nuestra base de datos")

    # 2. leer usuario y devolver sus compras
    def compras(self):
        print("")
        num_usuarios = len(self.getUsuarios())
        buscar_usuario = input("Digite usuario a buscar: ")
        
        # verificar si ese usuario existe
        if buscar_usuario in self.getUsuarios():
            # buscar todas sus compras
            f = open("compras.txt", "w")
            cont = 1
            for x in range(num_usuarios):
                if buscar_usuario == self.getUsuarios()[x]:
                    # guardar en txt
                    print(f"{cont}. {self.getProductos()[x]} (${self.getTotales()[x]})")
                    f.write(f"{cont}. {self.getProductos()[x]} (${self.getTotales()[x]})" + "\n") 
                    cont = cont + 1
            f.close()
        else:
            print(f"{buscar_usuario} no está en nuestra base de datos")
            
    # 3. devolver el promedio de los totales
    def promedio(self):
        print("")
        # calcular promedio
        cantidad = len(self.getTotales())
        suma = 0
        for x in self.getTotales():
            suma = suma + x
        promedio = round(suma / cantidad, 3)
        # guardar en txt
        print(f"Promedio ventas: ${promedio}")
        f = open("promedio.txt", "w")
        f.write(f"Promedio ventas: ${promedio}")
        f.close()

    # 4. devolver producto más vendido
    def moda(self):
        print("")
        # saber cuántas veces aparece cada producto
        contadores = []
        cont = 0
        for x in self.getProductos():
            if x == "computador":
                cont = cont + 1
        contadores.append(cont)
            
        cont = 0
        for x in self.getProductos():
            if x == "tablet":
                cont = cont + 1
        contadores.append(cont)
            
        cont = 0
        for x in self.getProductos():
            if x == "celular":
                cont = cont + 1
        contadores.append(cont)

        # mostrar cantidades de productos
        print("Cantidades de productos:")
        prods = ["computador", "tablet", "celular"]
        for x in range(len(prods)):
            print(f"{prods[x]} {contadores[x]} veces")

        # calcular el producto más repetido
        moda = contadores[0]
        prod = prods[0]
        for x in range(len(contadores)):
            if contadores[x] > moda:
                moda = contadores[x]
                prod = prods[x]

        # verificar si hay más de una moda
        
        cont = 0
        for x in contadores: 
            if x == moda: 
                cont = cont + 1
        
        # cuando hay una moda hace esto   
        if cont > 1:
            f = open("moda.txt", "w")
            print("Los productos más vendidos fueron:")
            for x in range(len(contadores)):
                if contadores[x] == moda:
                    print(f"{prods[x]}")
                    f.write(f"{prods[x]}" + "\n")
            f.close()
        
        # cuando hay varias modas hace esto             
        if cont == 1:
            print(f"Producto más vendido: {prod}")
            f = open("moda.txt", "w")
            f.write(f"Producto mas vendido: {prod}")
            f.close()

    # 5. leer producto y devolver los usuarios que lo compraron
    def pro_usuarios(self):
        print("")
        num_productos = len(self.getProductos())
        buscar_prod = input("Digite producto a buscar: ")
        
        # verificar que producto existe
        if buscar_prod in self.getProductos():
            # buscar usuarios que lo compraron
            f = open("pro_usuarios.txt", "w")
            cont = 1
            for x in range(num_productos):
                if buscar_prod == self.getProductos()[x]:
                    print(f"{self.getUsuarios()[x]}")
                    f.write(f"{self.getUsuarios()[x]}" + "\n")
                    cont = cont + 1               
            f.close()
        else:
            print(f"{buscar_prod} no está en nuestra base de datos")

def main():
    joke = Ventas()
    joke.almacenar()
    joke.imprimir()
    joke.idProducto()
    joke.compras()
    joke.moda()
    joke.promedio()
    joke.pro_usuarios()
    
main()