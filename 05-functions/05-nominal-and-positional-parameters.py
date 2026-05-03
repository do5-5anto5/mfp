# argumentos/parametros positionais sempre antes dos nominais
# parametros nominais nao precisao estar em ordem
def calcula_salario(
    base: int, bonus: int = 0, plano_saude: int = 0, vale_refeicao: int = 0
) -> int:
    return base + bonus + plano_saude + vale_refeicao


salario_maria = calcula_salario(base=5_000)
salario_joao = calcula_salario(
    7000,  # base - argumento posicional
    plano_saude=500, # argumento nominal
    bonus=200, # argumento nominal
)

print(f"Salário de Maria: R${salario_maria}")
print(f"Salário de João: R${salario_joao}")
