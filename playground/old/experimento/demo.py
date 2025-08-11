# Un número entero positivo

print("- - Un número entero positivo - -")

# Funciones:
def numerico(mi_numero):
    # Solo numeros
    if mi_numero.isnumeric() == True:
        return True
    else:
        return False

def entero(mi_numero):
    mi_numero = eval(mi_numero)
    if type(mi_numero) == int:
        return True
    else:
        return False

def positivo(mi_numero):
    mi_numero = eval(mi_numero)
    if mi_numero > 0:
        return True
    else:
        return False

# Leer un número:
mi_numero = input("Ingrese un número: ")
print(f"¿Es numérico?: {numerico(mi_numero)}")
print(f"¿Es entero?: {entero(mi_numero)}")
print(f"¿Es positivo?: {positivo(mi_numero)}")

while numerico(mi_numero) == False or entero(mi_numero) == False or positivo(mi_numero) == False:
    print(f"{mi_numero} no es un número entero positivo...")
    print("- - - -")
    mi_numero = input("Ingrese un número: ")
    print(f"¿Es numérico?: {numerico(mi_numero)}")
    print(f"¿Es entero?: {entero(mi_numero)}")
    print(f"¿Es positivo?: {positivo(mi_numero)}")

# Si logró salir del ciclo:
print(f"¡{mi_numero} es un número entero positivo!")