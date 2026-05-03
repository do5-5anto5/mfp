# remove the first occurrence of an item
fruits = ['maca', 'banana', 'laranja', 'banana', 'uva', 'abacaxi']
removed_fruit = fruits.remove('banana')
# removed item returns noting
print(removed_fruit)
print(fruits)

# pop() method always remove the last item
fruits.pop()
print(fruits)

# remove an item by index
fruits.pop(3)
print(fruits)

# poped item can be stored in a variable
fruits.append('jaca')
print('Lista atual: ', fruits)
poped_fruit = fruits.pop()
print('Fruta removida: ', poped_fruit)
print('Frutas restantes: ', fruits)

# remove all elements
fruits.clear()
print(fruits)