# 1. Variables y constantes
nombre = 'Hola' # Variable
pi = 3.1416 # Constante

# 2. Tipos de datos
"""
int     -> números enteros
float   -> números decimales
complex -> números complejos
str     -> cadenas
bool    -> True or False
"""
a = 10
b = 5.75
c = -2j
d = "Hola"
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# 3. Estructura de datos
"""
listas       -> ["abc", 100, True, 3.15] SÍ SE PUEDEN MODIFICAR | ORDENADOS
tuplas       -> ("abc", 100, True, 3.15) NO SE PUEDEN MODIFICAR | ORDENADOS
sets         -> {"abc", 100, True, 3.15} NO SE ACEPTAN REPETIDOS | DESORDENADOS
diccionarios -> {"a":1, "b":2, "c":3} key:value | ORDENADOS | NO REPETIR KEYS
"""
mi_lista = ["Juan", "Jose", "German", 100, True]
mi_tupla = ("German", 100, False)
mi_set = {"German", 200, True}
mi_diccionario = {"a":10, "b":20, "c":30}

print(type(mi_lista))
print(type(mi_tupla))
print(type(mi_set))
print(type(mi_diccionario))

# 4. Print
"""
print(...) -> imprimir varibales o estructuras de datos en consola

5 formas de imprimir diferentes datos


Cómo leer números:
variable = int(input(...))
variable = float(input(...))
variable = complex(input(...))
variable = eval(input(...))
"""

# Usar varios print
num1 = 10
num2 = 20
num3 = 30
print(num1)
print(num2)
print(num3)

# Usar solo uno HORIZONTAL
print(num1, num2, num3)

# Usar solo uno VERTICAL
print(num1, num2, num3, sep="\n")

# Imprimir varios valores
x = 5
y = 7.4
z = 2j
t = "abc"
u = True

print(x, y, z, t, u)
print(str(x) + " " + str(y) + " " + str(z) + " " + t  + " " + str(u))
print(f"{x} {y} {z} {t} {u}")
print("%s %s %s %s %s" % (x, y, z, t, u))
print("{} {} {} {} {}".format(x, y, z, t, u))

# 5. input
"""
input(...) -> leer datos en consola con un mensaje opcional
"""
# input sin mensaje opcional
nombre = input() # str
print(f"Su nombre es: {nombre}")

# input con mensaje opcional
nombre = input('Ingrese su nombre: ') #str
print(f"Su nombre es: {nombre}")

# input con mensaje opcional con variables NO USAR COMAS
edad = input(f"Ingrese la edad {nombre}: ") # str
print(edad)

edad = input("Ingrese la edad {}: ".format(nombre)) # str
print(edad, type(edad))

# leer números
numero = eval(input("Ingrese número: "))
print(numero, type(numero))

# 6. Operador de asignación
"""
= -> asignar un valor a una variable o estructura de dato
"""
x = 5
y = 6
z = x + y
print(f"{x} + {y} = {z}")

# 7. Operadores matemáticos
"""
+  -> sumar
-  -> restar
*  -> multiplicar
/  -> dividir
%  -> módulo o resto
** -> potenciación
// -> división pero redondea el resultado al entero más cercano
"""
suma = 10 + 5
resta = 10 - 5
producto = 10 * 5
razon = 10 / 5
modulo = 10 % 5
potencia = 10 ** 5
floor = 15 // 2

print(suma, resta, producto, razon, modulo, potencia, floor, sep="\n")