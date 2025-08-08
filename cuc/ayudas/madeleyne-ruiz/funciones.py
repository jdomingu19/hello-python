def mensaje(x, y):
    print("Hola", x, y)
    print("¿Cómo estás?")

mensaje("Madeleyne", "Ruiz")
mensaje("Juan", "Sarmiento")

def suma(num1, num2):
    resultado = num1 + num2
    print(resultado)

suma(10, 5)

def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado

print(multiplicar(10, 5))


numero = 15
def cambiar_numero(x):
    x = 20
    print(x)

cambiar_numero(numero)