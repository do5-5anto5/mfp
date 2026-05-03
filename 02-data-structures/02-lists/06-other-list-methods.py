numbers = [3, 10, 50, 30, 15]
print(len(numbers))

names = ["José", "Maria", "João", "Antonio"]
print(len(names))

# check item existence
print(10 in numbers)
print("Maria" in names)
print("Pedro" in names)

# check item non-existence
print("Unknown" not in names)

# list iteration
for name in names:
    print(name)

# list item value change
names[0] = "Joaquim"