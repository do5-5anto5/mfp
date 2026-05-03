# dictionaries are collections of key-value pairs, no ordered

person = {"name": "Jonathan", "age": 37, "cidade": "Sao Paulo"}

print(person["name"])

##############

# Operations

person["profissão"] = "desenvolvedor" # add new key-value
person['idade'] = 37 # update value
print(person['age'])

del person['cidade'] # delete key-value
print(person)
