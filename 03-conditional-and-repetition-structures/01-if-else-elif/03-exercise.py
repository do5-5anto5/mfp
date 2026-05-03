# Dados do cliente:
compras_ultimo_ano = 6
valor_atual_carrinho = 550.00
membro_fidelidade = False
frete_gratis_gasto = True

# Descobrir se o cliente tem direito ao desconto


# Use parentesis to grant priority
tem_frete_gratis = (
    ((compras_ultimo_ano >= 6 and valor_atual_carrinho >= 200)
    or membro_fidelidade)
    and not frete_gratis_gasto
)

print(tem_frete_gratis)