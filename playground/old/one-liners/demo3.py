# Dictionary Comprehension

# Normal
dict_numbers = {}
for x in range(1, 6):
    dict_numbers[x] = x*x
print(dict_numbers)

# One liners - {key: value for key, value in iterable}
dict_numbers = {x: x*x for x in range(1, 6)}
print(dict_numbers)