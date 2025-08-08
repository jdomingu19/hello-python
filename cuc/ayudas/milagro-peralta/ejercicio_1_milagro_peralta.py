# Ejericio 1

# Entradas
compra = eval(input("Ingrese el valor de la compra: $"))
pago = eval(input("Ingrese el tipo de pago 1) Efectivo, 2) Tarjeta de crédito: "))

# Condiciones
if pago == 1:
    total = compra - (compra * 0.20 ) # -20%
    print("Valor neto = $", total)
elif pago == 2:
    total = compra - (compra * 0.30) # -30%
    print("Valor neto = $", total)
else:
    print("Error")