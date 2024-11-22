from vingador import Vingador
from interface import exibir_menu, obter_opcao
 
def iniciar_sistema():
    Vingador("Thor", "Thor Odinson", "Deidade", ["Martelo", "Raio"], "Raio", ["Fogo", "Gelo"], 10000)
    Vingador("Hulk", "Bruce Banner", "Meta-humano", ["Força", "Imortalidade"], "Força", ["Radiação", "Frio"], 9500)
 
    while True:
        exibir_menu()
        opcao = obter_opcao()
 
        if opcao == 1:
            pass
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            pass
        elif opcao == 6:
            pass
        elif opcao == 7:
            pass
        elif opcao == 0:
            break
 
if __name__ == "__main__":
    iniciar_sistema()