# lista = [1, 2, 3]

# a, b, c = lista

# print(a)
# print(b)
# print(c)


vendas = [("Camiseta", 4, 25.00), ("Calça", 2, 100.00), ("Tênis", 1, 150)]

for nome, quantidade, preco in vendas:
    print(f'Foram vendidas {quantidade} unidades da peça {nome} por R${preco} cada.')
