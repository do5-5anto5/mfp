# Uma empresa de varejo quer analisar as vendas historicas de seus produtos
# para tomar decisões estrategicas.
# As vendas são armazenadas no seguinte formato:
# nome_do_produto, quantidade_vendida, preco_unitario em R$

_vendas_diarias = (
    ["Produto A", 10, 100],
    ["Produto B", 5, 250],
    ["Produto C", 2, 150],
)

# 1. As informações de vendas diárias são mutáveis ou imutáveis? 
# A estrutura de dados que armazena as vendas diarias é a mais adequada? Justifique.

# // #
# As informaçoes são imutáveis, pq o objeto é uma tupla.
# Estrutura inadequada porque podem surgir novos produtos nas proximas vendas

# 2. As informações específicas de cada produto são mutáveis ou imutáveis?
# A estrutura de dados que armazena as vendas diarias é a mais adequada? Justifique.

# // #
# São mutáveis pq são listas.
# Inadequado, os itens foram vendidos, o valor nao deveria ser alterado.

# 3. Caso as estruturas sejam inadequadas, o que você sugere?

# // #
# Poderia criar uma lista de tuples.
# O tipo de venda pode mudar, tendo novos produtos com novas caracteristicas (lista)
# Os registros individuais de vendas passadas nao devem mudar (tuple)

# 4. Faça um codigo que traga o faturamento da empresa (quantidade total de vendas em R$)
# baseado nas vendas diárias

vendas_diarias = [
    ("Produto A", 10, 100),
    ("Produto B", 5, 250),
    ("Produto C", 2, 150),
]

faturamento = 0

for venda in vendas_diarias:
    faturamento += venda[1] * venda[2]

print(faturamento)