# tuples are immutable

tupleA = (10,50,25, 'Python')
print(tupleA)

# parentesis with one item dont instantiate a tuple
confusion = (1)
print(type(confusion))
confusion = ('1')
print(type(confusion))

# to really create a tuple, need to add a comma
confusion = ('1',)
print(type(confusion))

# tuple operations sintax is the same as list, using [] 
# just get itens, not change them
# no append, remove, insert

print(tupleA[0])
print('Python' in tupleA)