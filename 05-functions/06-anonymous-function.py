# função nomeada
def dobro(numero: int) -> int:
    return numero * 2


# função nomeada
def soma(num1: int, num2: int) -> int:
    return num1 + num2


# função anonima
lambda numero: numero * 2

# função anonima nao deve usar type hints pq o compilador se perde nos ':'
lambda num1, num2: num1 + num2


# caso de uso da lambda
lista_numeros = [1, 2, 3, 4, 5, 6]

print(list(map(lambda num: num * 2, lista_numeros)))
