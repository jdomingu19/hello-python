# Algoritmo 'Conversor ángulos' 1.0
global a
global b
global minutos 
global segundos
a = 0
b = 0

print("- - Menú - -")
print("1) De ángulo, a ángulo minutos y segundos")
print("2) De ángulo minutos y segundos, a ángulos")
menu = eval(input("¿Qué desea hacer?: "))

# Iteraciones
if menu == 1:
    parteEntera = eval(input("Ingrese parte entera (z): "))
    parteDecimal = eval(input("Ingrese parte decimal (0.n): "))

    productoDecimal = parteDecimal * 60

    # Extraer parte entera del producto (minutos)
    for x in str(productoDecimal):
        a = a + 1
        if x == ".":
            # print(x)
            # print("Encontré el separador decimal")
            parteEnteraMinutos = str(productoDecimal)[:a-1]
            minutos = int(parteEnteraMinutos)

    # Extraer parte decimal produto * 60 (segundos)
    for x in str(productoDecimal):
        b = b + 1
        if x == ".":
            # print(x)
            # print("Encontré el separador decimal")
            parteDecimalMinutos = x + (str(productoDecimal)[b:])
            segundos = round(float(parteDecimalMinutos) * 60, 2)

    print("Ángulo = ", str(parteEntera + parteDecimal) + "°")
    print("Ángulo = ", str(parteEntera), "", str(minutos) + "'", "", str(segundos) + "''" )

if menu == 2:
    parteEntera = eval(input("Ingrese parte entera ángulo (°): "))
    minutos = eval(input("Ingrese valor minutos ('): "))
    segundos = eval(input("Ingrese valor segundos (''): "))

    parteDecimalA1 = minutos / 60
    parteDecimalA2 = segundos / 3600

    print("Ángulo = ", str(parteEntera + parteDecimalA1 + parteDecimalA2) + "°")