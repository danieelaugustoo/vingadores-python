from vingadores.cadastro import Vingadores
import os

class Rosto:

    @staticmethod
    def titulo_app():
        print('''

    ██╗░░░██╗██╗███╗░░██╗░██████╗░░█████╗░██████╗░░█████╗░██████╗░███████╗░██████╗ 
    ██║░░░██║██║████╗░██║██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
   ╚██╗░██╔╝██║██╔██╗██║██║░░██╗░███████║██║░░██║██║░░██║██████╔╝█████╗░░╚█████╗░
  ░╚████╔╝░██║██║╚████║██║░░╚██╗██╔══██║██║░░██║██║░░██║██╔══██╗██╔══╝░░░╚═══██╗
 ░░╚██╔╝░░██║██║░╚███║╚██████╔╝██║░░██║██████╔╝╚█████╔╝██║░░██║███████╗██████╔╝
░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░ 🦸‍♂
              

              ''')
    
    @staticmethod
    def menu_vingadores():
        Rosto.titulo_app()
        print('''

                                Menu Principal
              1. Cadastrar o Vingador
              2. Quem são os Vingadores?
              3. Sair do APP
''')
        Rosto.ler_opcao_usuario() 
    
    @staticmethod
    def ler_opcao_usuario():
        try:
            opcao = int(input('Digite sua opção: '))

            if opcao == 1:
                Rosto.cadastrar_vingador()
            elif opcao == 2:
                Rosto.titulo_tela('Listando Vingadores')
                Vingadores.listar_vingadores()  
            elif opcao == 3:
                print('Encerrando o programa')
                exit()
            else:
                print('ERRADO, escolha entre 1, 2 e 3')
                Rosto.voltar_ao_menu()
        except ValueError:
            print('ERRADO, escolha entre 1, 2 e 3')
            Rosto.voltar_ao_menu()
        Rosto.voltar_ao_menu()

    @staticmethod
    def titulo_tela(titulo):
        os.system('cls')
        Rosto.titulo_app()  
        print(f'{str(titulo).upper()}')
        print('*' * 20)
        print()
    
    @staticmethod
    def cadastrar_vingador():
        Rosto.titulo_tela('Cadastrando o novo Herói aos dados...')
        heroi = input('Coloque o Nome do Herói: ')
        nome = input('Nome Completo pessoal: ')
        categoria = input('Coloque a sua categoria adequada: HUMANO/META-HUMANO/ALIENÍGENA/DEUS - escreva em maiúsculo, como no exemplo: ')
        if categoria not in ['HUMANO', 'META-HUMANO', 'ALIENÍGENA', 'DEUS']:
            print('Categoria inválida! Programa encerrado. Tente novamente.')
            Rosto.voltar_ao_menu()
            return 
        poderes = input('Coloque os poderes secundários do herói: ')
        poderzao = input('Coloque o poder principal do herói: ')
        fraqueza = input('Coloque a Fraqueza do herói: ')
        forca = int(input('Coloque o nível de força do herói de 0 a 10: '))
        if 0 <= forca <= 10:
             print("Sua escolha foi: {forca}")
        else:
             print("Por favor, escolha um número entre 0 e 10.")


    
        v = Vingadores(heroi, nome, categoria, poderes, poderzao, fraqueza, forca)

        print(f'O novo vingador foi cadastrado: \n{v}')

    @staticmethod
    def voltar_ao_menu():
        print()
        input('Pressione ENTER para voltar ao menu principal')
        os.system('cls')
        Rosto.menu_vingadores() 
