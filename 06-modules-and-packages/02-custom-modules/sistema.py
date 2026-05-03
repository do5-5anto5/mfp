from gerenciamento_usuarios import registrar_usuario
from gerenciamento_contas import depositar, sacar, verificar_saldo
from historico_transacoes import mostrar_transacoes
from menu import imprime_menu

nome = input("Digite seu nome para registrar: ")
registrar_usuario(nome)

while True:
    imprime_menu()

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(f"Seu saldo é: R${verificar_saldo(nome):.2f}\n\n")
    elif opcao == 2:
        quantia = float(input("Digite a quantia para depositar (R$): "))
        depositar(nome, quantia)
    elif opcao == 3:
        quantia = float(input("Digite a quantia para sacar (R$): "))
        sacar(nome, quantia)
    elif opcao == 4:
        print(f"Transações: {mostrar_transacoes(nome)}\n\n")
    elif opcao == 5:
        print("Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.\n\n")
