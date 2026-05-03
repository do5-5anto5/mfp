fruits = [
    "maca",
    "banana",
    "laranja",
    "banana",
    "uva",
    "abacaxi",
    "banana",
    "banana",
    "banana",
]

# get index of a first item occurrence
print(fruits.index("banana"))
# get the index of the first occurrence of an item. 
# alternatively starting from a given index
# and also alternatively stopin at a given index
print(fruits.index("banana", 3, 6))

# get how many from an repeated item
print(f'Bananas: {fruits.count("banana")}')
