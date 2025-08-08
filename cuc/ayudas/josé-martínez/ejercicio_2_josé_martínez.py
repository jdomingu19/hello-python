# Ejercicio 2

# Captura de datos
localidad = eval(input("Ingrese localidad del pedido 1, 2, 3, o 4: "))
kg = eval(input("Ingrese el peso del pedido (kg): "))

# Condiciones
if localidad == 1:
    if kg >= 0.1 and kg < 3:
        descuento = 0.15 # 15%
        subTotal = (5000 * kg)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Con un descuento del 15%")
    elif kg >= 3 and kg < 6:
        descuento = 0.10 # 10%
        subTotal = (5000 * kg)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Con un descuento del 10%")
    elif kg >= 6 and kg < 8:
        descuento = 0.05 # 5%
        subTotal = (5000 * kg)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Con un descuento del 5%")
    elif kg >= 8 and kg < 10:
        descuento = 0.02 # 0.02%
        subTotal = (5000 * kg)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Con un descuento del 2%")
    elif kg >= 10:
        total = (5000 * kg)
        print("Total a pagar: $", total)
        print("No hay descuento...")
    else:
        print("Datos ingresados no validos...")
        print("El valor mínimo del kg es 0.1 KG...")

elif localidad == 2:
    if kg >= 0.1 and kg < 3:
        descuento = 0.15 # 15%
        subTotal = (7500 * kg)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Con un descuento del 15%")
    elif kg >= 3 and kg < 6:
        descuento = 0.10 # 10%
        subTotal = (7500 * kg)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Con un descuento del 10%")
    elif kg >= 6 and kg < 8:
        descuento = 0.05 # 5%
        subTotal = (7500 * kg)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Con un descuento del 5%")
    elif kg >= 8 and kg < 10:
        descuento = 0.02 # 0.02%
        subTotal = (7500 * kg)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Con un descuento del 2%")
    elif kg >= 10:
        total = (7500 * kg)
        print("Total a pagar: $", total)
        print("No hay descuento...")
    else:
        print("Datos ingresados no validos...")
        print("El valor mínimo del kg es 0.1 KG...")
        
elif localidad == 3:
    if kg >= 0.1 and kg < 3:
        descuento = 0.15 # 15%
        subTotal = (10000 * kg)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Con un descuento del 15%")
    elif kg >= 3 and kg < 6:
        descuento = 0.10 # 10%
        subTotal = (10000 * kg)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Con un descuento del 10%")
    elif kg >= 6 and kg < 8:
        descuento = 0.05 # 5%
        subTotal = (10000 * kg)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Con un descuento del 5%")
    elif kg >= 8 and kg < 10:
        descuento = 0.02 # 0.02%
        subTotal = (10000 * kg)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Con un descuento del 2%")
    elif kg >= 10:
        total = (10000 * kg)
        print("Total a pagar: $", total)
        print("No hay descuento...")
    else:
        print("Datos ingresados no validos...")
        print("El valor mínimo del kg es 0.1 KG...")
        
elif localidad == 4:
    if kg >= 0.1 and kg < 3:
        descuento = 0.15 # 15%
        subTotal = (12500 * kg)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Con un descuento del 15%")
    elif kg >= 3 and kg < 6:
        descuento = 0.10 # 10%
        subTotal = (12500 * kg)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Con un descuento del 10%")
    elif kg >= 6 and kg < 8:
        descuento = 0.05 # 5%
        subTotal = (12500 * kg)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Con un descuento del 5%")
    elif kg >= 8 and kg < 10:
        descuento = 0.02 # 0.02%
        subTotal = (12500 * kg)
        total = subTotal - (subTotal * descuento)
        print("Total a pagar: $", total)
        print("Con un descuento del 2%")
    elif kg >= 10:
        total = (12500 * kg)
        print("Total a pagar: $", total)
        print("No hay descuento...")
    else:
        print("Datos ingresados no validos...")
        print("El valor mínimo del kg es 0.1 KG...")

else:
    print("Datos ingresados no válidos...")
    print("Hay 5 localidades disponibles...")