# Todas las piezas:
piezas = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[2,2],[2,3],[2,4],[2,5],[2,6],[3,3],[3,4],[3,5],[3,6],[4,4],[4,5],[4,6],[5,5],[5,6],[6,6]]

i = 0
while i < len(piezas):
    print(f"|{piezas[i][0]}|", end=" ")
    if i == len(piezas) - 1:
        print(f"|{piezas[i][0]}|")
    i = i + 1

i = 0
while i < len(piezas):
    print("---", end=" ")
    if i == len(piezas) - 1:
        print("---")
    i = i + 1

i = 0
while i < len(piezas):
    print(f"|{piezas[i][1]}|", end=" ")
    if i == len(piezas) - 1:
        print(f"|{piezas[i][1]}|")
    i = i + 1