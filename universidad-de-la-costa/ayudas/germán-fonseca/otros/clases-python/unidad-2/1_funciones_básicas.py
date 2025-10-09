"""
Funciones básicas:
max() -> devuelve el mayor
min() -> devuelve el menor
pow() -> potencia de un número
abs() -> valor absoluto
len() -> longitud

max(variable o una estructura de datos)
"""

# 1. max()
mayor = max(5, 7, 32)
print(f"El mayor es: {mayor}")

print(f"El mayor es: {max(5, 7, 32)}")

num1 = 5
num2 = 7
num3 = 32
print(f"El mayor es: {max(num1, num2, num3)}")

# 2. min()
menor = min(5, 7, 32)
print(f"El menor es: {menor}")

print(f"El menor es: {min(5, 7, 32)}")

num1 = 5
num2 = 7
num3 = 32
print(f"El menor es: {min(num1, num2, num3)}")

# 3. pow() -> pow(base, altura)
potencia = pow(5, 2)
print(f"5 ^ 2 = {potencia}")

# 4. abs() -> abs(numero)
num = -32
print(f"Valor absoluto de -32: {abs(num)}")

# 5. len() -> len(cadena o estructura de datos)
palabra = "Hola"
print(f"Longitud de 'Hola': {len(palabra)}")
