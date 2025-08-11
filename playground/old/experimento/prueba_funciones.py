# Prueba de tres funciones

# Definir función 1
def funcion_1(numero):
    if numero > 10:
        return True
    else:
        return False

# Definir función 2
def funcion_2(numero):
    if numero > 20:
        return True
    else:
        return False

# Definir función 3
def funcion_3(numero):
    if numero > 30:
        return True
    else:
        return False

# Variable
numero = eval(input("Ingrese un número: "))

# Llamar funciones
print(funcion_1(numero))
print(funcion_2(numero))
print(funcion_3(numero))

while funcion_1(numero) == False and funcion_2(numero) == False and funcion_3(numero) == False:
    numero = eval(input("Ingrese un número: "))
    print(funcion_1(numero))
    print(funcion_2(numero))
    print(funcion_3(numero))

# Si logró salir del ciclo
print(f"{numero} es un número válido...")