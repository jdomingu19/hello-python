#ejercicio #12
print("\nAlgoritmo para calcular la suma de una fraccion homogenea o heterogenea\n")
num1=eval(input("Digite el primer numerador: "))
num2=eval(input("Digite el segundo numerador: "))
num3=eval(input("Digite el primer denominador: "))
num4=eval(input("Digite el segundo denominador: "))
het=(num1*num4)+(num2*num3)
het2=num3*num4
hom=num1+num2


if num3==num4 and num3!=0 and num4!=0:
    print(f"El resultado es una suma homogenea: {hom}/{num3}= {round(hom/num3, 1)}")

elif num3!=num4 and num3!=0 and num4!=0:
    print(f"El resultado es una suma heterogenea: {het}/{het2}={round(het/het2, 1)}")

elif num3==0 or num4==0:
    print("Error, debe ser mayor o diferente de 0")