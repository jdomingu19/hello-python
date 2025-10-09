palabra = input("Ingrese una palabra: ")

if palabra == palabra[::-1]:
    print(f"{palabra} es una palabra palíndroma")
    print(f"{palabra} = {palabra[::-1]}")
else:
    print(f"{palabra} no es una palabra palíndromo")
    print(f"{palabra} != {palabra[::-1]}")

    