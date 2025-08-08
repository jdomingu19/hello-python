# Ejercicio 5

# Leer Vexp
vexp = eval(input("Ingrese el Valor experimental: "))
vteo = eval(input("Ingrese el Valor teórico: "))

if vteo == 0:
    print("Datos incorrectos...")
else:
    error_p = (abs(vexp - vteo) / vteo) * 100
    error_p = round(error_p, 3)
    print(f"{vexp = }")
    print(f"{vteo = }")
    print(f"Error porcentual {error_p}%")
