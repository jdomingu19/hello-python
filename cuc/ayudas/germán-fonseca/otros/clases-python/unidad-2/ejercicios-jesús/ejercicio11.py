# Ejercicio 11 | Unidad 2

# Menú
print("1. Mazanas\n2. Bananas\n3. Naranjas")
fruta = input(">>> ")

if fruta == "1":
    cantidad = int(input("Ingrese cantidad de manzanas: "))
    total = cantidad * 2500
    print(f"\nFruta escogida: Manzana")
    print(f"Cantidad: {cantidad}")
    print(f"Total: ${total}")

elif fruta == "2":
    cantidad = int(input("Ingrese cantidad de bananas: "))
    total = cantidad * 1500
    print(f"\nFruta escogida: Banana")
    print(f"Cantidad: {cantidad}")
    print(f"Total: ${total}")

elif fruta == "3":
    cantidad = int(input("Ingrese cantidad de naranjas: "))
    total = cantidad * 3000
    print(f"\nFruta escogida: Naranja")
    print(f"Cantidad: {cantidad}")
    print(f"Total: ${total}")

else:
    print("Datos incorrectos")
