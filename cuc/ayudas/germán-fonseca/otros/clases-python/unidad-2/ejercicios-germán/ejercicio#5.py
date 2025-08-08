#ejercicio #5
print("Algoritmo para hallar el error porcentual\n")

vt=eval(input("Ingrese el valor teorico: "))
vx=eval(input("Ingrese el valor experimental: "))

if vt ==0:
    print("Error...")
    print("EL valor teorico debe ser mayor a cero")
    
    
elif vt >=1 or vt <=1:
    op=abs(vt - vx)
    op1=op/vt * 100
    op1=round(op1, 2)
    print(f"El error porcentual es de: {op1}%\n")