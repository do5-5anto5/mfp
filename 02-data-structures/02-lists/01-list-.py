# a list is a collection of items, same type or different types

listA = ["Hello", 3.14, True]

print(listA[0])
print(listA[1])
print(listA[:2])


##############

# a list may contain other lists (nested lists)

list_of_lists = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]

# get the last item of the last list
print(list_of_lists[3][3])

