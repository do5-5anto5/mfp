person = {
    'name': 'Jonathan',
    'age': 37,
    'hobby': 'programar'}

# with person['profissão'] as the key does not exists, 
# it will throw an error

print(person.get('profissão')) # returns None, as the key does not exists
print(person.get('profissao', 'estudante')) # returns defined default value, in this case estudante. prevent errors

print(person.keys())
print(person.values())
print(person.items())

print('\n\n')