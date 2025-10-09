# Ejercicio 6 | Unidad 2


# Menú
print("1. max y min\n2. Condicionales")
modo = input(">>> ")

# max y min
if modo == "1":
    p1 = input("Ingrese palabra 1: ")
    p2 = input("Ingrese palabra 2: ")
    p3 = input("Ingrese palabra 3: ")
    p4 = input("Ingrese palabra 4: ")

    l1 = len(p1)
    l2 = len(p2)
    l3 = len(p3)
    l4 = len(p4)

    mayor = max(l1, l2, l3, l4)
    menor = min(l1, l2, l3, l4)

    # Más larga
    if l1 == mayor:
        print(f"{p1} es la palabra más larga ({l1} caracteres)")
    elif l2 == mayor:
        print(f"{p2} es la palabra más larga ({l2} caracteres)")
    elif l3 == mayor:
        print(f"{p3} es la palabra más larga ({l3} caracteres)")
    elif l4 == mayor:
        print(f"{p4} es la palabra más larga ({l4} caracteres)")
    else:
        print("No hay más larga, hay igualdades...")

    # Más corta
    if l1 == menor:
        print(f"{p1} es la palabra más corta ({l1} caracteres)")
    elif l2 == menor:
        print(f"{p2} es la palabra más corta ({l2} caracteres)")
    elif l3 == menor:
        print(f"{p3} es la palabra más corta ({l3} caracteres)")
    elif l4 == menor:
        print(f"{p4} es la palabra más corta ({l4} caracteres)")
    else:
        print("No hay más corta, hay igualdades...")

# Condicionales
elif modo == "2":
    # Leer palabras
    p1 = input("Ingrese palabra 1: ")
    p2 = input("Ingrese palabra 2: ")
    p3 = input("Ingrese palabra 3: ")
    p4 = input("Ingrese palabra 4: ")

    # Más larga
    if len(p1) > len(p2) and len(p1) > len(p3) and len(p1) > len(p4):
        print(f"{p1} es la palabra más larga ({len(p1)} caracteres)")

    elif len(p2) > len(p1) and len(p2) > len(p3) and len(p1) > len(p4):
        print(f"{p2} es la palabra más larga ({len(p2)} caracteres)")

    elif len(p3) > len(p1) and len(p3) > len(p2) and len(p1) > len(p4):
        print(f"{p3} es la palabra más larga ({len(p3)} caracteres)")

    elif len(p4) > len(p1) and len(p4) > len(p2) and len(p4) > len(p3):
        print(f"{p4} es la palabra más larga ({len(p4)} caracteres)")

    else:
        print("No hay más larga, hay igualdades...")

    # Más corta
    if len(p1) < len(p2) and len(p1) < len(p3) and len(p1) < len(p4):
        print(f"{p1} es la palabra más corta ({len(p1)} caracteres)")

    elif len(p2) < len(p1) and len(p2) < len(p3) and len(p1) < len(p4):
        print(f"{p2} es la palabra más corta ({len(p2)} caracteres)")

    elif len(p3) < len(p1) and len(p3) < len(p2) and len(p1) < len(p4):
        print(f"{p3} es la palabra más corta ({len(p3)} caracteres)")

    elif len(p4) < len(p1) and len(p4) < len(p2) and len(p1) > len(p3):
        print(f"{p4} es la palabra más corta ({len(p4)} caracteres)")

    else:
         print("No hay más corta, hay igualdades...")

# Validar
else:
    print("Datos incorrectos...")
