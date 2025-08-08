#ejercicio #8

print("Algoritmo para saber si es apto para votar\n")
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
genero=input('Ingrese su genero "masculino" o "femenino" : ')
genero=genero.lower()
nombre=nombre.title()


if edad>=18 and genero=="masculino":
    print(f"El senor {nombre} es apto para votar")

elif edad>=21 and genero=="femenino":
    print(f"La senora {nombre} es apta para votar")

elif edad<18 or edad>=100:
    print(f"{nombre} no eres apto para votar")

else:
    print(f"{nombre} no eres apto para votar")

print("  ")