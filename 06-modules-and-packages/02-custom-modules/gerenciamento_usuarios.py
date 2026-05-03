usuarios = {}

def registrar_usuario(nome: str) -> None:
    usuarios[nome] = {"saldo": 0, "transacoes": []}
    print(f"Usuário registrado com sucesso!\n\n")