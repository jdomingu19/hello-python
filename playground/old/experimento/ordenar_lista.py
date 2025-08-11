# Ordernar lista | Forma 1
import bisect

a = [3, 5, 9, 11, 20]
print(f"Lista: {a}")

value = 7
idx = bisect.bisect(a, value)
print(f"Índice elemento nuevo ordenado: {idx}")

a.insert(idx,value)
print(f"Lista nueva ordenada: {a}")