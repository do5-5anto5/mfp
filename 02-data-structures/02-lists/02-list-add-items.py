fruits = ['maçã', 'banana', 'laranja']

print('Lista inicial: ', fruits)
print('\n')

# add an item to list's end
fruits.append('uva')
print('adicionando uva: ', fruits)
print('\n')

# extend a list
other_fruits = ['morango', 'pera']

fruits.extend(other_fruits)
print('Extendendo a lista de outras frutas', fruits)
print('\n')

# insert an item in a specific index
fruits.insert(0, 'abacaxi')
print('Inserindo abacaxi na posicao 1: ', fruits)
print('\n')