# Ejercicio 10

# Entradas
cantComputadoras = eval(input("Ingrese cantidad computadoras: "))

# Condiciones
if cantComputadoras < 5:
    descuento = 0.10 # 10%
    subTotal = cantComputadoras * 11000
    total = subTotal - (subTotal * descuento)

elif cantComputadoras >= 5 and cantComputadoras < 10:
    descuento = 0.20 # 20%
    subTotal = cantComputadoras * 11000
    total = subTotal - (subTotal * descuento)
    
elif cantComputadoras >= 10:
    descuento = 0.40 # 40%
    subTotal = cantComputadoras * 11000
    total = subTotal - (subTotal * descuento)