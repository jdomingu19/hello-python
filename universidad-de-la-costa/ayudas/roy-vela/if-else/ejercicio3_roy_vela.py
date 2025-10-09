# Algortimo 3 if-else

# Captura de la información:
compra = eval(input("Ingrese valor compra: $"))

# Condiciones:
if compra >= 500000:
    descuento = compra * 0.20
    totalPagar = compra - descuento
    print("Total a pagar: $", round(totalPagar, 2), " (20% de descuento)")
else:
    totalPagar = compra
    print("Total a pagar: $", totalPagar, " (No hay descuento)")