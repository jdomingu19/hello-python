# Sistema de ventas | Reto 7

# Crear listas:
codigos = []
usuarios = []
productos = []
totales = []

# Cantidad de registros:
cantidad_registros = eval(input("Ingrese la cantidad de registros: "))

while cantidad_registros <= 0:
    print("Datos no válidos...")
    cantidad_registros = eval(input("Ingrese la cantidad de registros: "))

# Llenar listas:
i = 0
while i < cantidad_registros:
    # Nombre y producto del usuario
    usuario = input("Ingrese nombre del usuario: ")
    producto = eval(input("Ingrese el producto 1) Computador 2) Tablet 3) Celular: "))

    # Validar producto
    while producto != 1 and producto != 2 and producto != 3:
        producto("Datos no válidos...")
        producto = eval(input("Ingrese el producto 1) Computador 2) Tablet 3) Celular: "))

    # Llenar listas
    if producto == 1:
        codigos.append(i + 1)
        usuarios.append(usuario)
        productos.append("Computador")
        totales.append(500000)
        i = i + 1
    elif producto == 2:
        codigos.append(i + 1)
        usuarios.append(usuario)
        productos.append("Tablet")
        totales.append(200000)
        i = i + 1
    elif producto == 3:
        codigos.append(i + 1)
        usuarios.append(usuario)
        productos.append("Celular")
        totales.append(100000)
        i = i + 1

# 1) Dado un código retorne el producto comprado:
print("- - - -")
buscar_codigo = eval(input("1) Ingrese código a buscar: "))

# Validar buscar_codigo
while buscar_codigo.isnumeric() == False:
    print("Datos no válidos...")
    buscar_codigo = eval(input("Ingrese código a buscar: "))

# Busqueda
i = 0
while i < cantidad_registros:
    if buscar_codigo == codigos[i]:
        print("Código encontrado")
        print(f"Producto comprado: {productos[i]}")
    i = i + 1

# 2) Dado un usuario retorne todas las compras que este realizó:
print("- - - -")
buscar_usuario = input("2) Ingrese usuario a buscar: ")

# Validar buscar_usuario
while buscar_usuario.isalpha() == False:
    print("Datos no válidos...")
    buscar_usuario = input("2) Ingrese usuario a buscar: ")

# Buscar el usuario
compras_usuario = False
i = 0
while i < cantidad_registros:
    if buscar_usuario == usuarios[i]:
        compras_usuario = True
    i = i + 1

# Validar busqueda
if compras_usuario == False:
    print("Usuario no encontrado")
else:
    print("Usuario encontrado")
    print(f"Compras de {buscar_usuario}: ")

    # Imprimir sus compras y su total
    total_usuario = 0
    i = 0
    while i < cantidad_registros:
        if buscar_usuario == usuarios[i]:
            print(f"Producto: {productos[i]}, Precio: ${totales[i]}")
            total_usuario = total_usuario + totales[i]
        i = i + 1
    print(f"Total de la compra de {buscar_usuario}: ${total_usuario}")

# 3) Promedio total ventas:
print("- - - -")

# Ciclo acumulador
sumatoria_totales = 0
i = 0
while i < cantidad_registros:
    sumatoria_totales = sumatoria_totales + totales[i]
    i = i + 1

# Promedio
promedio_totales = sumatoria_totales / len(totales)
print(f"3) Promedio total ventas: ${promedio_totales}")

# 4) Producto más vendido:
print("- - - -")

# Ciclo contadores
cantidad_computadores = 0
cantidad_tablets = 0
cantidad_celulares = 0

i = 0
while i < cantidad_registros:
    if productos[i] == "Computador":
        cantidad_computadores = cantidad_computadores + 1
    elif productos[i] == "Tablet":
        cantidad_tablets = cantidad_tablets + 1
    else:
        cantidad_celulares = cantidad_celulares + 1
    i = i + 1

# Validar
if cantidad_computadores > cantidad_tablets and cantidad_computadores > cantidad_celulares:
    print(f"4) Producto más vendido: Computadores ({cantidad_computadores} ventas)")
elif cantidad_tablets > cantidad_computadores and cantidad_tablets > cantidad_celulares:
    print(f"4) Producto más vendido: Tablets ({cantidad_computadores} ventas)")
elif cantidad_celulares > cantidad_computadores and cantidad_celulares > cantidad_computadores:
    print(f"4) Producto más vendido: Tablets ({cantidad_computadores} ventas)")
else:
    print("4) Producto más vendido: Hay igualdad de ventas")

# 5) Dado un producto retorne todos los usuarios que lo compraron:
print("- - - -")
buscar_producto = input("5) Ingrese producto a buscar: ")

# Validar buscar_producto
while buscar_producto.isalpha() == False:
    print("Datos no válidos...")
    buscar_producto = input("5) Ingrese producto a buscar: ")

# Buscar el producto
producto_encontrado = False
i = 0
while i < cantidad_registros:
    if buscar_producto == usuarios[i]:
        producto_encontrado = True
    i = i + 1

# Validar busqueda
if producto_encontrado == False:
    print("Producto no encontrado")
else:
    print("Producto encontrado")
    print(f"Usarios que compraron {buscar_producto}: ")

    # Imprimir resultados búsquedas
    i = 0
    while i < cantidad_registros:
        if buscar_producto == productos[i]:
            print(usuarios[i])
        i = i + 1

# Imprimir listas:
print("- - Listas - -")
print(f"Codigos: {codigos}")
print(f"Usuarios: {usuarios}")
print(f"Productos: {productos}")
print(f"Totales: {totales}")