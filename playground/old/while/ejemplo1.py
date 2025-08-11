# While | Ejemplo 1

suma = 0
miOperacion = 1

while miOperacion == 1:
    num = eval(input("Ingrese un número: "))
    suma = suma + num

    miOperacion = eval(input("¿Desea continuar? 1 = Sí 2 = No: "))

print("Suma: ", suma)