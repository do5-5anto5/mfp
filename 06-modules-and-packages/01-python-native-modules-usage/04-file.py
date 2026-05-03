# criar uma pasta vazia chamada 'exercicios' na pasta atual do terminal.

from os import mkdir, path

if not path.exists("exercicios"):
    mkdir("exercicios")
else:
    print("Pasta já existente")
