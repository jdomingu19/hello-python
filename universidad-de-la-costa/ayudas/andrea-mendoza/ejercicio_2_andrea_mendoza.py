# Ejercicio 2

# Entradas
localidad = eval(input("Ingrese la localidad del pedido (1, 2, 3 o 4): "))
peso = eval(input("Ingrese el peso en kg del pedido: "))

# Condiciones
if localidad == 1:
    if peso >= 0.1 and peso < 3:
        descuento = 0.15 # 15%
        subTotal = (5000 * peso)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Descuento de 15%")
    elif peso >= 3 and peso < 6:
        descuento = 0.10 # 10%
        subTotal = (5000 * peso)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Descuento de 10%")
    elif peso >= 6 and peso < 8:
        descuento = 0.05 # 5%
        subTotal = (5000 * peso)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Descuento de 5%")
    elif peso >= 8 and peso < 10:
        descuento = 0.02 # 0.02%
        subTotal = (5000 * peso)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Descuento de 2%")
    elif peso >= 10:
        total = (5000 * peso)
        print("Total a pagar: $", total)
        print("No hay descuento")
    else:
        print("Datos ingresados no validos...")
        print("El valor mínimo del peso es 0.1 KG...")

elif localidad == 2:
    if peso >= 0.1 and peso < 3:
        descuento = 0.15 # 15%
        subTotal = (7500 * peso)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Descuento de 15%")
    elif peso >= 3 and peso < 6:
        descuento = 0.10 # 10%
        subTotal = (7500 * peso)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Descuento de 10%")
    elif peso >= 6 and peso < 8:
        descuento = 0.05 # 5%
        subTotal = (7500 * peso)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Descuento de 5%")
    elif peso >= 8 and peso < 10:
        descuento = 0.02 # 0.02%
        subTotal = (7500 * peso)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Descuento de 2%")
    elif peso >= 10:
        total = (7500 * peso)
        print("Total a pagar: $", total)
        print("No hay descuento")
    else:
        print("Datos ingresados no validos...")
        print("El valor mínimo del peso es 0.1 KG...")
        
elif localidad == 3:
    if peso >= 0.1 and peso < 3:
        descuento = 0.15 # 15%
        subTotal = (10000 * peso)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Descuento de 15%")
    elif peso >= 3 and peso < 6:
        descuento = 0.10 # 10%
        subTotal = (10000 * peso)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Descuento de 10%")
    elif peso >= 6 and peso < 8:
        descuento = 0.05 # 5%
        subTotal = (10000 * peso)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Descuento de 5%")
    elif peso >= 8 and peso < 10:
        descuento = 0.02 # 0.02%
        subTotal = (10000 * peso)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Descuento de 2%")
    elif peso >= 10:
        total = (10000 * peso)
        print("Total a pagar: $", total)
        print("No hay descuento")
    else:
        print("Datos ingresados no validos...")
        print("El valor mínimo del peso es 0.1 KG...")
        
elif localidad == 4:
    if peso >= 0.1 and peso < 3:
        descuento = 0.15 # 15%
        subTotal = (12500 * peso)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Descuento de 15%")
    elif peso >= 3 and peso < 6:
        descuento = 0.10 # 10%
        subTotal = (12500 * peso)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Descuento de 10%")
    elif peso >= 6 and peso < 8:
        descuento = 0.05 # 5%
        subTotal = (12500 * peso)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Descuento de 5%")
    elif peso >= 8 and peso < 10:
        descuento = 0.02 # 0.02%
        subTotal = (12500 * peso)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Descuento de 2%")
    elif peso >= 10:
        total = (12500 * peso)
        print("Total a pagar: $", total)
        print("No hay descuento")
    else:
        print("Datos ingresados no validos...")
        print("El valor mínimo del peso es 0.1 KG...")

else:
    print("Datos ingresados no válidos...")
    print("Hay 5 localidades disponibles...")