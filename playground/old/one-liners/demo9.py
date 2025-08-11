# Sort dictionary by values

# Normal
poblacion = {"USA": 329.5, "Brazil": 212.6, "COL": 67.2}

# ???

# One line
poblacion = {"USA": 329.5, "Brazil": 212.6, "COL": 67.2}
print(sorted(poblacion.items(), key = lambda x: x[1]))

my_dict = {k: v for k, v in sorted(poblacion.items(), key = lambda x: x[1])}
print(my_dict)