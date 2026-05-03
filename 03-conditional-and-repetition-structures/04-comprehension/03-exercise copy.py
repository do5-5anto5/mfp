produtos = [
    {"nome": "notebook", "preco": 6_500.00, "quantidade_vendida": 12},
    {"nome": "teclado", "preco": 45.00, "quantidade_vendida": 45},
    {"nome": "monitor", "preco": 520.00, "quantidade_vendida": 30},
    {"nome": "webcam", "preco": 500.00, "quantidade_vendida": 25},
]

### faturamento de cada produto preço x quantidade -
### qual produto gerou mais receita -
# produtos que geraram mais de 5000 de receita -
# ticket medio ( faturamento total / total de produtos vendidos ) - 

receita_acima_5000 = []
faturamento_total = 0.0
total_de_produtos_vendidos = 0

for produto in produtos:
    faturamento = produto['preco'] * produto['quantidade_vendida']
    print(f'{produto['nome']} teve um faturamento de R${faturamento:.2f}')    

    if faturamento > 5000:
        receita_acima_5000.append(produto['nome'])

    faturamento_total += faturamento
    total_de_produtos_vendidos += produto['quantidade_vendida']

print(f'Produtos que faturaram mais de R$5000.00: {receita_acima_5000}')
print(f'Ticket Médio: R${(faturamento_total / total_de_produtos_vendidos):.2f}')