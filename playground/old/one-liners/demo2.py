# Create a list based on existing lists

words = ["united States", "brazil", "colombia"]

# Normal
capitalized = []
for word in words:
    capitalized.append(word.title())
print(capitalized)

# One liners - [expression for item in list]
capitalized = [word.title() for word in words]
print(capitalized)