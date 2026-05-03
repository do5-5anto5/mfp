# Dict with current stock and minimum stock

stock_current = {"camiseta": 10, "calça": 5, "jaqueta": 0, "meia": 50, "sapato": 2}
stock_minimum = {"camiseta": 15, "calça": 10, "jaqueta": 5, "meia": 30, "sapato": 5}


# Using a tradictional for loop to find products with stock below minimum
# stockRefill = []
# for product, qty in stock_current.items():
#     if qty < stock_minimum.get(product):
#         stockRefill.append(product)
# print(f'produtos para repor: {stockRefill}')


# Using List comprehension
stock_refill = [
    product
    for product, qty in stock_current.items()
    if qty < stock_minimum.get(product)
]
print(f"produtos para repor: {stock_refill}\n")


# Usin Map comprehension
prices = {
    "camiseta": 25.0,
    "calça": 50.0,
    "jaqueta": 100.0,
    "meia": 5.0,
    "sapato": 70.0,
}

discounts = {product: price * 0.9 for product, price in prices.items() if price > 20}

print(f'produtos com desconto: {discounts}\n')

customers = [
{'nome': 'Ana', 'idade': 25, 'pais': 'Brasil'},
{'nome': 'Carlos', 'idade': 30, 'pais': 'Brasil'},
{'nome': 'Marta', 'idade': 22, 'pais': 'Argentina'},
{'nome': 'Jorge', 'idade': 29, 'pais': 'Chile'},
{'nome': 'Lucia', 'idade': 35, 'pais': 'Argentina'},
{'nome': 'Pedro', 'idade': 28, 'pais': 'Brasil'},
{'nome': 'Julia', 'idade': 27, 'pais': 'Chile'},
{'nome': 'Luis', 'idade': 31, 'pais': 'Brasil'},
{'nome': 'Marina', 'idade': 26, 'pais': 'Argentina'},
{'nome': 'Fernando', 'idade': 33, 'pais': 'Chile'},
{'nome': 'Gabriela', 'idade': 24, 'pais': 'Brasil'}
]

# Extract the unique countries that have customer below 25 years old
# use Set comprehension

countries = {
    customer.get('pais') for customer in customers
    if customer.get('idade') < 28
}

print(f'paises com clientes baixo de 28 anos: {countries}')