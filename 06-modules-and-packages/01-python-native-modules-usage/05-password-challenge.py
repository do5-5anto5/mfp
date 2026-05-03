# criar uma senha aleatoria de 12 caracteres, incluindo:
#  maiusculas, minusculas, numeros e simbolos

from random import choice, shuffle
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

maisculas = ascii_uppercase
minusculas = ascii_lowercase
numeros = digits
simbolos = punctuation

# caracteres = ""

# for ma in range(3):
#     caracteres += choice(simbolos)

# for ma in range(3):
#     caracteres += choice(maisculas)

# for mi in range(3):
#     caracteres += choice(minusculas)

# for n in range(3):
#     caracteres += choice(numeros)

caracteres = (
    [choice(simbolos) for _ in range(3)]
    + [choice(maisculas) for _ in range(3)]
    + [choice(minusculas) for _ in range(3)]
    + [choice(numeros) for _ in range(3)]
)

shuffle(caracteres)

senha_final = "".join(caracteres)
print(f'senha gerada:  {senha_final} ')
