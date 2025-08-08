# Luis Gonzáles
import json
class SistemaVentas:
    # método para alamcenar clientes
    def almacenarClientes(self):
        dict_clientes = {}
        while True:
            identificacion = input("Digite identificacion del cliente: ")
            nombre = input("Digite nombre del cliente: ").capitalize()
            correo = input("Digite correo del cliente: ")
            telefono = input("Digite telefono del cliente: ")
            dict_clientes[identificacion] = {"IDENTIFICACION": identificacion, "NOMBRE": nombre, "CORREO": correo, "TELÉFONO": telefono}
            opc = input("¿Quiere seguir agregando dict_clientes? S/N: ").upper()
            if opc == "N": 
                break
        file = open("clientes_venta.txt", "w")
        json.dump(dict_clientes, file)
        file.close()

    # método para alamcenar productos
    def almacenarProductos(self):
        dict_productos = {}
        while True:
            referencia = input("Digite referencia del producto: ")
            nombre = input("Digite nombre del producto: ").capitalize()
            precio = input("Digite precio del producto: $")
            dict_productos[referencia] = {"NOMBRE": nombre, "REFERENCIA": referencia, "PRECIO": precio}
            opc = input("¿Quiere seguir agregando producto? S/N: ").upper()
            if opc == "N": 
                break
        file = open("productos_venta.txt", "w")
        json.dump(dict_productos, file)
        file.close()

    # método para alamcenar compras
    def almacenarCompra(self):
        dict_compras = {}
        while True:
            file = open("clientes_venta.txt", "r")
            dict_clientes = json.load(file)
            file.close()
            identificacion = input("Digite identificacion de un cliente existente: ")
            if identificacion in dict_clientes:
                referencia = input("Digite la referencia del producto: ")
                file = open("productos_venta.txt", "r")
                dict_productos = json.load(file)
                file.close()
                if referencia in dict_productos:
                    numero_factura = input("Digite número de compra: ")
                    cantidad = input("Digite cantidad del producto: ")
                    total = int(dict_productos[referencia]["PRECIO"]) * int(cantidad) 
                    dict_compras[numero_factura] = {"IDENTIFICACION": dict_clientes[identificacion]["IDENTIFICACION"], "CLIENTE": dict_clientes[identificacion]["NOMBRE"], "PRODUCTO": dict_productos[referencia]["NOMBRE"], "CANTIDAD": cantidad, "TOTAL": total}  
                    print("- - - -  - - - - -")
                    print(f"ID FACTURA : {numero_factura}")
                    print(f"CLIENTE: {dict_clientes[identificacion]['NOMBRE']}")
                    print(f"NOMBRE: {dict_productos[referencia]['NOMBRE']}")
                    print(f"CANTIDAD: {cantidad}")
                    print(f"PRECIO: ${dict_productos[referencia]['PRECIO']}")
                    print(f"TOTAL: ${total}") 
                    print("- - - -  - - - - -")                   
                    file = open("compras_venta.txt", "w")
                    json.dump(dict_compras, file)
                    file.close()
                    opc = input("¿Quiere seguir agregando compras? S/N: ").upper()
                    if opc == "N": 
                        break
                else:
                    print(f"dict_productos[{dict_productos}] no existe...")
            else:
                print(f"dict_clientes[{identificacion}] no existe...")

    # método para mostrar un listado de las facturas
    def listaFacturas(self):
        file = open("compras_venta.txt", "r")
        dict_compras = json.load(file)
        file.close()
        
        # mostrar datos en formato de tabla
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("| # | ID FACTURA | CLIENTE | PRODUCTO | CANTIDAD | TOTAL |")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        indice = 1
        for i in dict_compras:
            identificacion = dict_compras[i]["IDENTIFICACION"]
            cliente = dict_compras[i]["CLIENTE"]
            producto = dict_compras[i]["PRODUCTO"]
            cantidad = dict_compras[i]["CANTIDAD"]
            total = dict_compras[i]["TOTAL"]
            print("|{:^3}|{:^12}|{:^9}|{:^10}|{:^10}|{:^7}|".format(indice, identificacion, cliente, producto, cantidad, total))
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            indice = indice + 1

# método principal
def main():
    venta1 = SistemaVentas()
    while True:
        print("- - MENÚ - -")
        print("1. ALMACENAR CLIENTE")
        print("2. ALMACENAR PRODUCTO")
        print("3. ALMACENAR COMPRA")
        print("4. LISTA DE FACTURAS")
        print("5. SALIR")
        menu = input("¿Qué desea hacer?: ")
        if menu == "1": 
            venta1.almacenarClientes()
        elif menu == "2": 
            venta1.almacenarProductos()
        elif menu == "3": 
            venta1.almacenarCompra()
        elif menu == "4": 
            venta1.listaFacturas()
        elif menu == "5":
            print("Hasta luego") 
            break
        else: 
            print("Opción no válida")
            
# llamar método princial
main()