class Ventas:
    
    def __init__(self, codigos = [], usuarios = [], productos = [], total = []):
        self.codigos = codigos
        self.usuarios = usuarios
        self.productos = productos
        self.total = total
       
    def __str__(self):
        return f"Ventas:\ncodigos {self.codigos}\nusuarios {self.usuarios}\nproductos {self.productos}\ntotal {self.total}"

    def set_codigos(self, x:list):
        self.codigos = x

    def get_codigos(self):
        return self.codigos

    def set_usuarios(self, x:list):
        self.usuarios = x

    def get_usuarios(self):
        return self.usuarios

    def set_productos(self, x:list):
        self.productos = x

    def get_productos(self):
        return self.productos

    def set_total(self, x:list):
        self.total = x

    def get_total(self):
        return self.total
        
    def ingresarVenta(self, codigo, usuario, producto):
        self.get_codigos().append(codigo)
        self.get_usuarios().append(usuario)
        if producto == "Computador":
            self.get_productos().append(producto)
            self.get_total().append(500000)
        elif producto == "Tablet":
            self.get_productos().append(producto)
            self.get_total().append(200000)
        elif producto == "Celular":
            self.get_productos().append(producto)
            self.get_total().append(100000)
        else:
            print("El producto en cuestion no existe")
            
    def buscarPorCodigo(self, codigoBuscar):
        print("")
        contador = 0
        producto = ""  
        for codigo in self.get_codigos():
            if codigoBuscar == codigo:
                producto = self.get_productos()[contador]
                break
            else:
                contador += 1    

        if producto == "":
            return f"{codigoBuscar} no tiene producto asociado..." 
        else:
            # almacenar en txt
            file = open("busqueda_codigo.txt", "w")
            file.write(producto)
            file.close()
            return producto
    
    def comprasUsuario (self, usuarioBuscar):
        print("")
        contador = 0
        productosComprados = []
        cadenaAInsertar = ""
        indice = 1
        file = open("compras_usuarios.txt", "w")
        for usuario in self.get_usuarios():
            if usuarioBuscar == usuario:
                cadenaAInsertar += f"producto {indice}: {self.get_productos()[contador]}, precio: {self.get_total()[contador]}"
                productosComprados.append(cadenaAInsertar)
                cadenaAInsertar = ""
                indice += 1
                file.write(self.get_productos()[contador] + "\n")
            contador += 1
        file.close()    
        if len(productosComprados) == 0:
            return "Este usuario no ha hecho compras"
        
        return productosComprados
    
    def promedioVentas (self):
        print("")
        contador = 0
        acumulacionVentas = 0
        
        for producto in self.get_productos():
            acumulacionVentas += self.get_total()[contador]
            contador += 1

        # almacenar en txt
        file = open("promedio_ventas.txt", "w")
        file.write(f"${round(acumulacionVentas / contador, 2)}")
        file.close()  
        return f"El promedio de ventas es: ${round(acumulacionVentas / contador, 2)}"

    def productoMasVendido (self):
        contadorComputador = 0
        contadorTablet = 0
        contadorCelular = 0
        
        for producto in self.get_productos():
            if producto == "Computador":
                contadorComputador += 1
            elif producto == "Tablet":
                contadorTablet += 1
            elif producto == "Celular":
                contadorCelular += 1
                
        contadores = []
        contadores.append(contadorComputador)     
        contadores.append(contadorTablet) 
        contadores.append(contadorCelular) 

        prods = ["Computador", "Tablet", "Celular"]
        [2, 6, 6]
        mayor = contadores[0]
        nombre = prods[0]
        for i in range(len(contadores)):
            if contadores[i] > mayor:
                mayor = contadores[i]
                nombre = prods[i]

        veces = 0
        for i in contadores:
            if i == mayor:
                veces += 1

        if veces == 1:
            file = open("mas_vendido.txt", "w")
            file.write(f"El mas vendido es {nombre} y se vendió {mayor} veces...")
            file.close()
            return f"El mas vendido es {nombre} y se vendio {mayor} veces..."
        if veces != 1:
            file = open("mas_vendido.txt", "w")
            mas_vendidos = []
            cadena = ""
            for i in range(len(contadores)):
                if contadores[i] == mayor:
                    cadena += f"{prods[i]} se vendió {contadores[i]}"
                    mas_vendidos.append(cadena)
                    cadena = ""
                    file.write(f"{prods[i]} se vendió {contadores[i]}\n")
            file.close()
            return mas_vendidos
   
    def usuarioQueCompraron(self, productoComprado):
        if productoComprado == "Computador" or productoComprado == "Tablet" or productoComprado == "Celular":
            file = open("usuarios_que_compraron.txt", "w")
            contador = 0
            usuariosCompradores = []
            cadenaAInsertar = ""
            
            for producto in self.get_productos():
                if producto == productoComprado:
                    cadenaAInsertar += f"usuario {contador + 1}: {self.get_usuarios()[contador]}"
                    usuariosCompradores.append(cadenaAInsertar)
                    cadenaAInsertar = ""
                    file.write(f"usuario {contador + 1}: {self.get_usuarios()[contador]}\n")
                contador += 1
            file.close()
            return usuariosCompradores
        else:
            return "El producto no existe"
        
def main():
    factura = Ventas()

    numeroVentas = int(input("Ingrese el número de ventas a registrar: "))

    for i in range(numeroVentas):
        factura.ingresarVenta(int(input("Ingrese el codigo: ")), input("Ingrese el usuario: ").capitalize(), input("Ingrese el producto comprado: ").capitalize())

    print(factura)
    print(factura.buscarPorCodigo(int(input("Ingrese el codigo de la factura: "))))
    print(factura.comprasUsuario(input("Ingrese el usuario a buscar: ")))
    print(factura.promedioVentas())
    print(factura.productoMasVendido())
    print(factura.usuarioQueCompraron(input("Ingrese el producto a buscar: ").capitalize()))

main()