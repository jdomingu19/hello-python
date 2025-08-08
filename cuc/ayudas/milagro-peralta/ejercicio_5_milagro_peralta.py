# Ejericio 5

# Entradas
localidad = eval(input("Ingrese la localidad pedido (1, 2, 3 o 4): "))
kg = eval(input("Ingrese kilos del pedido (kg): "))

# Condiciones
if localidad == 1:
    total = kg * 5000
    print("Total = $", total)
elif localidad == 2:
    total = kg * 7500
    print("Total = $", total)
elif localidad == 3:
    total = kg * 10000
    print("Total = $", total)
elif localidad == 4:
    total = kg * 12500
    print("Total = $", total)
else:
    print("Error")