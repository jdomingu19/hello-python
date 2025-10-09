#10
print("Programa para calcular el valor de un paquete\n")

ps=eval(input("Por favor indiquenos el peso de su paquete: "))

if ps <5:
    print("El precio de su paaquete es de $1,500")

elif ps >=5 and ps <=10:
    print("El precio de su paquete es de $2,000")

elif ps >=11 and ps <=20:
    print("El precio de su paquete es de $2,500")

elif ps<=0 and ps >20:
    print("Erorr, el peso dede ser mayor a 0 o menor a 20kg")