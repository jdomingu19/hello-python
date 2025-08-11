x = "['a', 'b', 'c']"
x = list(x)
print(x)

x = "['a', 'b', 'c']"
x = x.replace("[", "")
x = x.replace("]", "")
x = x.replace("'", "")
x = x.replace(",", "")
x = x.split()
print(x, type(x))