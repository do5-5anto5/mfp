preco = 1000

# this code will print "produto caro" and "produto bom" because 1000 attends two conditions,
# but the product in reality cannot be twice the same
if preco >= 1000:
    print("preco caro")
if preco >= 500:
    print("preco bom")
else:
    print("preco barato")


if preco >= 1000:
    print("produto caro")
elif (
    preco >= 500
):  # use elif instead or other if, othwerwise you will get the value of the last if
    print("produto bom")
else:
    print("produto barato")

print("\n")

# elif is also useful to avoid nested ifs turning the code easy to read

idade = 12

##### imagine you have a program that checks if a person is a child, teenager or adult, then imagine more and more checkings

# if idade >= 18:
#     print("maior de idade")
# else:
#     if idade >= 12:
#         print("adolescente")
#     else:
#         print("crianca")
#


### see how it can be simplified
if idade >= 18:
    print("maior de idade")
elif idade >= 12:
    print("adolescente")
else:
    print("crianca")
