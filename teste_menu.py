import os
import time


def saldo():
    pass


def trans():
    pass


def extrato():
    pass


def principal():
    lista = []  # inicializa a lista vazia
    while True:
        time.sleep(2)
        os.system("cls")
        print("===Banco Digital===")
        print("1 - Consulte seu saldo")
        print("2 - Realize uma transferência")
        print("3 - Consulte seu extrato")
        print("4 - Sair do sistema Banco")
        opcao = int(input("Digite o opção desejada:"))

        if opcao == 1:
            saldo()
        elif opcao == 2:
            trans()
        elif opcao == 3:
            extrato()
        elif opcao == 4:
            print("Saindo do programa...")
            break
        else:
            print("Opcão incorreta, por favor digite novamente...")


principal()
