# Uma concessionária de automovies precisa gerenciar o estoque de peças de reposição.
#    em seus diferentes depositos. O gerente quer uma visao do gerenciamento
#    de estoque de peças disponíveis para manutenção.
# Abaixo há uma lista de todos os depositos com suas respectivas peçças em estoque:

# Deposito A: junta homocinetica, filtro de oleo, vela de ignição, correia dentada pastilha de freio, amortecedor
# Deposito B: filtro de oleo vela de ignição, pastilha de freio, disco de freio pneu, valvula termostatica
# Deposito C: correia dentada, pastilha de freio, amortecedor, bateria, filtro de oleo, alternador, vela de ignição
# Deposito D: vela de ignição, disco de freio, oleo de motor, correia alternador, sensor de oxigenio, fluido de freio
# Deposito E: penu, amortecedor, radiador, bomba dágua, mangueira dágua, rolamnto de roda, filtro de oleo, vela de ignição

# Responder:
# 1. Quais são as peças disponiveis em todos os depositos?
depositos = {
    "Deposito A": {
        "junta homocinetica",
        "filtro de oleo",
        "vela de ignição",
        "correia dentada",
        "pastilha de freio",
        "amortecedor",
    },
    "Deposito B": {
        "filtro de oleo",
        "vela de ignição",
        "pastilha de freio",
        "disco de freio",
        "pneu",
        "valvula termostatica",
    },
    "Deposito C": {
        "correia dentada",
        "pastilha de freio",
        "amortecedor",
        "bateria",
        "filtro de oleo",
        "alternador",
        "vela de ignição",
    },
    "Deposito D": {
        "vela de ignição",
        "disco de freio",
        "oleo de motor",
        "correia alternador",
        "sensor de oxigenio",
        "fluido de freio",
    },
    "Deposito E": {
        "pneu",
        "amortecedor",
        "radiador",
        "bomba dágua",
        "mangueira dágua",
        "rolamento de roda",
        "filtro de oleo",
        "vela de ignição",
    },
}

peçasDisponiveis = set()

for estoque in depositos:
    peçasDisponiveis.update(depositos.get(estoque))
print(f"Peças disponíveis: {peçasDisponiveis}")
print("\n\n")

# 2. Quais peças estao faltando em cada um dos depositos?
for deposito in depositos:
    print(
        f"No {deposito} faltam {peçasDisponiveis.difference(depositos.get(deposito))}"
    )

# 3. Quais peças sao exclusivas de cada deposito?
# for deposito in depositos:
#     pecasExclusivas = list(depositos.get(deposito))

#     for comparacao in depositos:
#         if comparacao != deposito:
#             result = set(pecasExclusivas).intersection(depositos.get(comparacao))
#             for peca in result:
#                     pecasExclusivas.remove(peca)   

#     print(f" peças exclusivas do deposito {deposito}: {pecasExclusivas}")

for deposito, estoque in depositos.items():
    outros = set()
    for outro_nome, outro_estoque in depositos.items():
        if outro_nome != deposito:
            outros.update(outro_estoque)
    
    exclusivas = estoque - outros
    print(f"Peças exclusivas do deposito {deposito}: {exclusivas}")
