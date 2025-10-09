# Ejercicio 4 | Unidad 2

# Menú
print("1. **\n2. pow")
modo = input(">>> ")

# Operador matemático **
if modo == "1":
    base = eval(input("Ingrese la base: "))
    altura = eval(input("Ingrese la altura: "))
    potencia = base ** altura
    print(f"{base} ^ {altura} = {potencia}")

# Función pow()
elif modo == "2":
    base = eval(input("Ingrese la base: "))
    altura = eval(input("Ingrese la altura: "))
    potencia = pow(base, altura)
    print(f"{base} ^ {altura} = {potencia}")

# Validar
else:
    print("Datos incorrectos...")
