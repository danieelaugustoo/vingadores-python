def exibir_menu():
    print("1. Cadastro de Vingador")
    print("2. Listar Vingadores")
    print("3. Convocar Vingador")
    print("4. Aplicar Tornozeleira")
    print("5. Aplicar Chip GPS")
    print("6. Listar Detalhes de Vingador")
    print("7. Emitir Mandado de Prisão")
    print("0. Sair")
 
def obter_opcao():
    try:
        opcao = int(input("Escolha uma opção: "))
        return opcao
    except ValueError:
        print("Opção inválida. Tente novamente.")
        return obter_opcao()