#ejercicio #4
print("Algoritmo para hallar la potencia de un numero con pow o '**'\n")
a="MENU"
print(f"{a.center(15)}")
print('1)Opcion "**"')
print('2)Opcion "pow()"\n')
op=int(input("Ingrese la opcion deseada: "))

if op==1:
    ba=int(input("Ingrese la base: "))
    al=int(input("Ingrese la altura: "))
    print(f"EL resultado es {ba**al}")

elif op==2:
    ba=int(input("Ingrese la base: "))
    al=int(input("Ingrese la altura: "))
    print(f"El resultado es {pow(ba, al)}")

else:
    print("Opcion incorrecta...\n ")