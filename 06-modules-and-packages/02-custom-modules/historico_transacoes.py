from gerenciamento_usuarios import usuarios

def mostrar_transacoes(nome:str) -> list:
    return usuarios[nome]['transacoes']