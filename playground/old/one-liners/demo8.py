# Sort dictionary by keys

# Normal
x = {"c": 9.99, "a": 9.99, "b": 9.99}
x_sorted = {}
for key in sorted(x.keys()):
    x_sorted[key] = x[key]
print(x_sorted)

# One line
x = {"c": 9.99, "a": 9.99, "b": 9.99}
x_sorted = {key: x[key] for key in sorted(x.keys())}
print(x_sorted)