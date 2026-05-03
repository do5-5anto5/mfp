# Uma empresa tem um codigo de produto no formato 'PROD-XXXX',
# XXXX são dígitos de 0-9
# Ela precisa verificar se os codigos seguem o formato correto
# Ex.: PROD-1234 é valido, mas prod-1234 ou PROD1234 nao.
# Fazer um programa que leia um codigo de produto
# e informe se ele é valido ou nao.

code = input("Digite o código do produto: ")

if code.startswith("PROD-") and code[-4:].isdigit():
    print("Código válido")
else:
    print("Código inválido")

print("\n\n")

# Você precisa separar as partes (letras e numeros) de uma determinada placa de carro.
# Faça um programa que automatize isso. use a placa ABC-1234 como modelo.

plate = input("Digite a placa do carro: ")

if (
    len(plate) == 8
    and plate[0:3].isalpha()
    and plate[3] == "-"
    and plate[4:].isnumeric()
):
    splitedPlate = plate.split("-")
    print(f'Letras: {splitedPlate[0]}')
    print(f'Números: {splitedPlate[1]}')
else:
    print("Placa inválida")
