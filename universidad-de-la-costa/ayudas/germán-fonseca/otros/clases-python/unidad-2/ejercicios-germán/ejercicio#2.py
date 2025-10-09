#ejercicio #2
print("Por favor ingrese 3 numeroes enteros: \n")
nu1=int(input("Ingrese su primer numero: "))
nu2=int(input("Ingrese su segundo numero: "))
nu3=int(input("Ingrese su tercer numero: "))

#condicionales para el numero mayor
if nu1 >= nu2 and nu1>=nu3:
    print(f"El numero {nu1} es el mayor")

elif nu2 >= nu1 and nu2 >=nu3:
    print(f"El numero {nu2} es el mayor")
    
elif nu3 >= nu1 and nu3 >=nu2:
    print(f"El numero {nu3} es el mayor")

#condicionales para el numero menor

if nu1 <= nu2 and nu1<=nu3:
    print(f"El numero {nu1} es el menor")

elif nu2 <= nu1 and nu2 <=nu3:
    print(f"El numero {nu2} es el menor")
    
elif nu3 <= nu1 and nu3 <=nu2:
    print(f"El numero {nu3} es el menor")