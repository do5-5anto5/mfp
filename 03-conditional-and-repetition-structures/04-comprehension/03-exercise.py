produtos = [
    {"nome": "notebook", "preco": 6_500.00, "quantidade_vendida": 12},
    {"nome": "teclado", "preco": 45.00, "quantidade_vendida": 45},
    {"nome": "monitor", "preco": 520.00, "quantidade_vendida": 30},
    {"nome": "webcam", "preco": 500.00, "quantidade_vendida": 25},
]

### faturamento de cada produto preço x quantidade
### qual produto gerou mais receita
# produtos que geraram mais de 5000 de receita
# ticket medio ( faturamento total / total de produtos vendidos )

faturamento_total = 0
total_produtos = 0
faturamento_maior_5000 = []

for produto in produtos:
    faturamento = produto["preco"] * produto["quantidade_vendida"]
    print(f"O produto {produto['nome']} teve o faturamento de: R${faturamento:.2f}")

    faturamento_total += faturamento
    total_produtos += produto["quantidade_vendida"]

    if faturamento > 5000:
        faturamento_maior_5000.append(produto["nome"])

print(f'Ticket Médio: R${(faturamento_total/total_produtos):.2f}')
print(f'Faturamento maior que R$5000.00: {faturamento_maior_5000}')
