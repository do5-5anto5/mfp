productBase = {'nome': 'cadeira', 'preço': 50, 'código': 123}
productDetails = {'cor': 'verde', 'estoque': 10, 'código': 456}

productInfo = productBase | productDetails # merge dictionaries
# note at the output that the key 'código' appears only once, updated

print(productInfo)