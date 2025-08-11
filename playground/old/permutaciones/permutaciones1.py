palabra = input("Ingrese una palabra: ")

if len(palabra) == 4:
    for i in palabra:
        caracter1 = i
        for j in palabra:
            caracter2 = j
            for k in palabra:
                caracter3 = k
                for l in palabra:
                    caracter4 = l
                    x = caracter1 + caracter2 + caracter3 + caracter4
                    print(x)