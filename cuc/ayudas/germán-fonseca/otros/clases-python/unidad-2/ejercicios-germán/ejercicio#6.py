#ejercicip #6
a="MENU"
print(f"\n{a.center(24, '=')}")
print('1)Opcion "max y min"')
print('2)Opcion "condicionales"\n')
op=int(input("Ingrese la opcion deseada: "))

p1=input("Ingrese la primera palabra: ")
p2=input("Ingrese su segunda palabra: ")
p3=input("Ingrese su tercera palabra: ")
p4=input("Ingrese su cuarta palabra: ")

l1 =len(p1)
l2 =len(p2)
l3 =len(p3)
l4 =len(p4)

mayor = max(l1, l2, l3, l4)
menor = min(l1, l2, l3, l4)


if op ==1:

#mas larga
    if l1 == mayor:
        print(f"la palabra mas larga es: {p1} ")
    elif l2 == mayor:
        print(f"la palabra mas larga es: {p2} ")
    elif l3 == mayor:
        print(f"la palabra mas larga es: {p3} ")
    elif l4 == mayor:
        print(f"la palabra mas larga es: {p4} ")
    else:
        print("erorr...")

    if l1 == menor:
        print(f"la palabra mas corta es: '{p1}' ")
    elif l2 == menor:
        print(f"la palabra mas corta es: '{p2}' ")
    elif l3 == menor:
        print(f"la palabra mas corta es: '{p3}' ")
    elif l4 == menor:
        print(f"la palabra mas corta es: '{p4}' ")
    else:
        print("No hay más corta, hay igualdades...")


elif op==2:

    #condicionales de la palabra mas larga
    if len(p1)>len(p2) and len(p1)>len(p3) and len(p1)>len(p4):
        print(f"La palabra mas larga es {p1}")

    elif len(p2)>len(p1) and len(p2)>len(p3) and len(p2)>len(p4):

        print(f"La palabra mas larga es {p2}")

    elif len(p3)>len(p1) and len(p3)>len(p2) and len(p3)>len(p4):

        print(f"La palabra mas larga es {p3}")

    elif len(p4)>len(p1) and len(p4)>len(p2) and len(p4)>len(p3):

        print(f"La palabra mas larga es {p4}")


    #condicionlaes de la palabra mas corta
    if len(p1)<len(p2) and len(p1)<len(p3) and len(p1)<len(p4):
        print(f"La palabra mas corta es {p1}")

    elif len(p2)<len(p1) and len(p2)<len(p3) and len(p2)<len(p4):

        print(f"La palabra mas corta es {p2}")

    elif len(p3)<len(p1) and len(p3)<len(p2) and len(p3)<len(p4):

        print(f"La palabra mas corta es {p3}")

    elif len(p4)<len(p1) and len(p4)<len(p2) and len(p4)<len(p3):

        print(f"La palabra mas corta es {p4}")

else:
    print("Opcion incorrecta...")