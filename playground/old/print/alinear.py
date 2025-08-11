# Alinear varios print

name_1 = "Ludwig van Beethoven"
name_2 = "Wolfgang Amadeus Mozart"

print(len(name_1), len(name_2))

print(f"{name_1:23} : Compositor alemán")
print(f"{name_2:23} : Compositor austríaco")

frutas = ["manzana", "banana", "uva", "sandía"]

len_mayor = len(frutas[0])
for i in range(len(frutas)):
    if len(frutas[i]) > len_mayor:
        len_mayor = len(frutas[i])

for i in frutas:
    print(f"{i:{len_mayor}} : es una fruta")