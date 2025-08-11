# Filter values from a list

# Normal
my_list = [10, 11, 12, 13, 14, 15]
pares = []
for x in my_list:
    if x % 2 == 0:
        pares.append(x)
print(pares)

# One Liners - filter(function, iterable)
my_list = [10, 11, 12, 13, 14, 15]
print(list(filter(lambda x: x % 2 == 0, my_list)))