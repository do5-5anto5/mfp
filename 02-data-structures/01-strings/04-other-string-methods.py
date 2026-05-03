# transforming strings

message = "Hi, I aM a sTrInG!"

print(message.upper())
print(message.lower())
print(message.title())
print(message.capitalize())

# counting characters in a string

print(message.count("i"))
print(message.count("I"))
print(message.count("a"))
print(message.count("A"))


print(message.find("sTrInG"))

print("\n\n")

# removing spaces

message2 = "     Hi, I am a String!       "

print(message2)
print(message2.lstrip())
print(message2.rstrip())
print(message2.strip())


# verifying if a string starts or ends with a string

print(message.startswith("Hi"))
print(message.endswith("Hi"))

print("\n\n")

# other check cases

lowerString = "hi"
upperString = "HI"

alphaNum = "1234"
alphaNum2 = " 12 34"
alphaNum3 = "12-34"
space = " "

print(lowerString.islower())
print(lowerString.isupper())

print(upperString.islower())
print(upperString.isupper())

print(alphaNum.isalnum())
print(alphaNum2.isalnum())
print(alphaNum3.isalnum())

print(lowerString.isalpha())

print(alphaNum.isdigit())
print(alphaNum2.isdigit())

print(space.isspace())
print (alphaNum3.isspace())

print("\n\n")

##############

# spliting strings

cpf = '123.456.789-00'

splitedCPF = cpf.split('-')

print(splitedCPF)

# joining strings

name = 'Jonathan dos Santos'
listName = name.split(' ')

print('-'.join(listName))