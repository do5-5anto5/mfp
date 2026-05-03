# parametros obrigatorios devem ser definidos antes dos parametros opcionais
def calcula_salario(
    base: int, bonus: int = 0, plano_saude: int = 0, vale_refeicao: int = 0
) -> int:
    return base + bonus + plano_saude + vale_refeicao

salario_maria = calcula_salario(5_000)
salario_joao = calcula_salario(7_000, 500, 200)

print(f'Salário de Maria: R${salario_maria}')
print(f'Salário de João: R${salario_joao}')