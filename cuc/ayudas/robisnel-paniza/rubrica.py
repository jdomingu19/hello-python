import json
class almacenamiento:
    def cliente(self):
        cliente = {}
        while True:
            identificacion=input("Ingrese la identificacion del cliente: ").upper()
            nombre=input("Ingrese el nombre del cliente:  ").upper()
            correo=input("Ingrese el correo del cliente: ").upper()
            telefono=input("Ingrese el telefono del cliente: ")
            cliente[identificacion] = {
                "IDENTIFICACION":identificacion, "NOMBRE":nombre, "CORREO": correo, "TELEFONO":telefono
            }
            opc = input("Desea agregar otro cliente S/N:").upper()
            if opc == "N":
                break
        archivo = open("cliente.txt","a")
        json.dump(cliente, archivo)
        archivo.close()
    
    def producto(self):
        producto = {}
        while True:
            nombre = input("Ingrese el nombre del producto: ").upper()
            referencia = input("Ingrese la referencia del producto: ").upper()
            precio = input("Ingrese el precio del producto: ").upper()
            producto[referencia] = {
                "NOMBRE":nombre,
                "REFERENCIA":referencia,
                "PRECIO": precio
                }
            opcion = input("Desea agregar otro producto? S/N: ").upper()
            if opcion == "N":
                break
        archivo = open("producto.txt","a")
        json.dump(producto, archivo)
        archivo.close()
    
    def factura(self):
        factura={}
        while True:
            with open("cliente.txt","r") as f:
                cliente = json.load(f)
            if identificacion in cliente:
                referencia=input("Ingrese la referencia del producto: ")
                with open("producto.txt","r") as f:
                    producto = json.load(f)
                if referencia in producto:
                    nfactura=input("Ingrese el numero de la factura: ")
                    cantidad=input("Ingrese la cantidad de producto a llevar: ")
                    total=int(producto[referencia]["PRECIO"])*int(cantidad)
                    print("Cliente: ", cliente[identificacion]["NOMBRE"])
                    print("Nombre: ", producto[referencia]["NOMBRE"])
                    print("Cantidad", cantidad)
                    print("Precio: ", producto[referencia]["PRECIO"])
                    print("Total: ", total)
                    factura[nfactura] = {
                        "IDENTIFICACION":cliente[identificacion]["IDENTIFICACION"],
                        "CLIENTE":cliente[identificacion]["NOMBRE"],
                        "PRODUCTO":producto[referencia]["NOMBRE"],
                        "CANTIDAD":cantidad,
                        "TOTAL":total
                    }
                    archivo = open("factura.txt","a")
                    json.dump(factura, archivo)
                    archivo.close()
                opcion = input("Desea agregar otro producto a la compra? S/N: ").upper()
                if opcion == "N":
                    break                
                else:
                    print("Producto no existe")  
            else:
                print("Cliente no existe")
    def lista(self):
        with open("factura.txt","r") as f: 
            factura = json.load(f)  
        print("+--------------------+----------+----------+----------+----------+")
        print("|Identificacion      |Cliente   |Producto  |Cantidad  |Total     |")
        print("+--------------------+----------+----------+----------+----------+")
        for x in factura:
            identificacion = factura[x]["IDENTIFICACION"]
            cliente = factura[x]["CLIENTE"]
            producto = factura[x]["PRODUCTO"]
            cantidad = factura[x]["CANTIDAD"]
            total = factura[x]["TOTAL"]
            cadena = "|{:<20}|{:>10}|{:>10}|{:>10}|{:>10}|".format(identificacion, cliente, producto, cantidad, total)
            print(cadena)
            print("+--------------------+----------+----------+----------+----------+")
                
tienda=almacenamiento()
while True:
    print("Menú de Inventario")
    print("1. AGREGAR CLIENTE")
    print("2. AGREGAR PRODUCTO")
    print("3. FACTURA")
    print("4. LISTAR")
    print("5. SALIR")

    menu = input("Digite opcion del menu: ")
    if menu == "1": 
        tienda.cliente()
    elif menu == "2": 
        tienda.producto()
    elif menu == "3":
        identificacion=input("Ingrese la identificacion del cliente: ")
        tienda.factura()
    elif menu == "4":
        tienda.lista()
    elif menu == "5":
        break
