# Ejericio 6

# Entradas
turno = eval(input("Ingrese el turno del trabajador 1) Matutino 2) Vespertino 3) Nocturno: "))
horas = eval(input("Ingrese cantidad de horas: "))
horasExtras = eval(input("Ingrese cantidad de horas extras: "))
impuestos = eval(input("Ingrese los inpuestos del tabajador: $"))

# Condiciones
if horas >= 40:
    if turno == 1:
        pago = (horas * 20000) + (horasExtras * 50000)
        print("Total a pagar: $", pago)

        if horasExtras >= 1:
            impuestosNuevo = impuestos - (impuestos * 0.18) # -18%
            print("Descuento impuestos trabajador: 18% ($", impuestosNuevo, ")")
        else: 
            print("Descuento impuestos trabajador: 0%")

    elif turno == 2:
        pago = (horas * 28000) + (horasExtras * 50000)
        print("Total a pagar: $", pago)

        if horasExtras >= 1:
            impuestosNuevo = impuestos - (impuestos * 0.18) # -18%
            print("Descuento impuestos trabajador: 18% ($", impuestosNuevo, ")")
        else: 
            print("Descuento impuestos trabajador: 0%")

    elif turno == 3:
        pago = (horas * 35000) + (horasExtras * 50000)
        print("Total a pagar: $", pago)

        if horasExtras >= 1:
            impuestosNuevo = impuestos - (impuestos * 0.18) # -18%
            print("Descuento impuestos trabajador: 18% ($", impuestosNuevo, ")")
        else: 
            print("Descuento impuestos trabajador: 0%")
else:
    print("El trabajador no cumplió las horas semanales mínima")