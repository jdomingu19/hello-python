"""
Hay funciones predefinidad, por ejemplo:
    - print()
    - input()
    - eval()
    - int()
    - float()
    - etc.

Las funciones propias son aquellas que hacemos,
usamos la palabra reservada def
"""

# Definir función
def mensaje():
    print("Esto es una función")
    print("¡Pildoras informáticas!")

# Llamar función
mensaje()
mensaje()
mensaje()


# Ejemplo 2
def suma():
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese un número: "))
    print(num1 + num2)

# Llamar función
suma()

# Ejemplo 3
def suma(num1, num2):
    resultado = num1 + num2
    print(resultado)

# Llamar función con argumentos
suma(5,7)
suma(3,8)
suma(4,2)

# Ejemplo 4
def suma(num1, num2):
    resultado = num1 + num2
    return resultado

# Llamar función con argumentos
print(suma(5,7))
print(suma(3,8))
print(suma(4,2))

# Ejemplo 5
def suma(num1, num2):
    resultado = num1 + num2
    return resultado

# Almacenar resultado
almacenar_resultado = suma(10,5)
print(almacenar_resultado)