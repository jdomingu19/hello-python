# Ejercicio 1 | Números palíndromos

# Leer número:
print("------------")
mi_numero = input("Ingrese un número: ")

# Validaciones:

"""
El método isnumeric() devuelve True
solo si la cadena ingresada contiene
los dígitos 0 1 2 3 4 5 6 7 8 9.

Devuelve False cuando es negativo,
cuando es decimal, cuando es negativo,
cuando son letras, cuando hay espacios
y cuando no se ingresa nada.
"""

while mi_numero.isnumeric() == False:
    print("Datos ingresados no válidos...")
    print("Debe ser un número entero del 0 al 9999...")
    print("------------")
    mi_numero = input("Ingrese un número: ")

# 1) Cuando es una unidad:
if len(mi_numero) == 1:
    print("¡Sí es un número palíndromo!")

# 2) Cuando son dos unidades:
elif len(mi_numero) == 2:
    # Si son el mismo dígito
    if mi_numero[0] == mi_numero[-1]:
        print("¡Sí es un número palíndromo!")
    else:
        print("No es un número políndromo...")

# 3) Cuando son tres unidades:
elif len(mi_numero) == 3:
    # Si el primer dígito es igual al último
    # El dígito del medio puede ser cualquiera
    if mi_numero[0] == mi_numero[-1]:
        print("¡Sí es un número palíndromo!")
    else:
        print("No es un número políndromo...")

# 4) Cuando son cuatro unidades:
elif len(mi_numero) == 4:
    # Si el primer dígito es igual al último + Si el segundo dígito es igual al tercero
    if mi_numero[0] == mi_numero[-1] and mi_numero[1] == mi_numero[2]:
        print("¡Sí es un número palíndromo!")
    else:
        print("No es un número políndromo...")

# Si supera las cuatro unidades:
else:
    print("Datos ingresados no válidos...")
    print("Debe ser un número entero del 0 al 9999...")

print("------------")