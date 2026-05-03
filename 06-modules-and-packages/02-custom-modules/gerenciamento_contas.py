from gerenciamento_usuarios import usuarios

def verificar_saldo(nome: str) -> int:
    return usuarios[nome]["saldo"]


def depositar(nome: str, quantia: int) -> None:
    usuarios[nome]["saldo"] += quantia
    usuarios[nome]["transacoes"].append(f"Depositou {quantia:.2f}")
    print(f"Depositou R${quantia:.2f} na conta de {nome}.\n\n")


def sacar(nome: str, quantia: int) -> None:
    if quantia > usuarios[nome]["saldo"]:
        print("Saldo insuficiente!\n\n")
    else:
        usuarios[nome]["saldo"] -= quantia
        usuarios[nome]["transacoes"].append(f"Sacou {quantia}")
        print(f'Sacou {quantia}')