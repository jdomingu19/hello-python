#ejercicio #11

print("Bienvenido, a continuacion nuestro menu y su precio por unidad: ")

m="MENU"
print(F"{m.center(16, '=')}")
print("1) Manzanas - $2,500")
print("2) Bananas - $1,500")
print("3) Naranjas - $3,000")

comp=int(input("Por favor indique la opcion a comprar, posteriormente indique la cantidad: "))
comp2=int(input("Cantidad: "))

if comp ==1:
    print(f"El precio a pagar es de ${2500*comp2}")

elif comp==2:
     print(f"El precio a pagar es de ${1500*comp2}")

elif comp==3:
     print(f"El precio a pagar es de ${3000*comp2}")