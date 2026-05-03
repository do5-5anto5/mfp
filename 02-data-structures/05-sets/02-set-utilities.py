# Sets are very useful when you need to compare groups of unique items
setA = {1, 2, 3, 4, 5}
setB = {3, 4, 5, 6, 7}

# check if there is an overlap
print(setA.intersection(setB))
print(setA & setB)

# check what element is in setA but not in setB
print(setA.difference(setB))
print(setA - setB)
# check what element is in setB but not in setA
print(setB.difference(setA))
print(setB - setA)


# union of sets
print(setA.union(setB))
print(setA | setB)

# symmetric difference (shows elements that are not in both sets)
print(setA.symmetric_difference(setB))
print(setA ^ setB)

print("\n\n")

###############

setC = {1, 2, 3}
setD = {1, 2, 3, 3, 4, 5, 6, 7}

print(setC.issubset(setD))
print(setD.issuperset(setC))
