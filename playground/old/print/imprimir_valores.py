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