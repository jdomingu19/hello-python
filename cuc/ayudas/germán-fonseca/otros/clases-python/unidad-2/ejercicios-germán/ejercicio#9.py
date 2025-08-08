#ejercicio #9

print("Algoritmo para calcular las notas\n")
nom=input("Ingrese su nombre: ")
print("Por favor ingrese sus notas: ")
not1=eval(input("Nota 1: "))
not2=eval(input("Nota 2: "))
not3=eval(input("Nota 3: "))
no4=(not1+not2+not3)/3 
no4=round(no4, 1)
nom=nom.title()

#condicionales
if not1>5 or not2>5 or not3>5 or not1<0 or not2<0 or not3<0:
    print("Error...")
    print("Las notas van desde 0 hasta 5")
    
elif no4 >=3.3 and no4 <=5:
    print(f"Felicidades, {nom} ha aprobado con un promedio de {no4}")

else:
    print(f"Lo siento, {nom} reprobo con un promedio de {no4}")
    