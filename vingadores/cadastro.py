class Vingadores:
    lista_de_herois = []

    def __init__(self, heroi, nome, categoria, poderes, poderzao, fraqueza, forca):
        self.heroi = heroi
        self.nome = nome
        self.categoria = categoria
        self.poderes = poderes
        self.poderzao = poderzao
        self.fraqueza = fraqueza
        self.forca = forca
        Vingadores.lista_de_herois.append(self) 

    @classmethod
    def listar_vingadores(cls):

        print(f'{"Vingador".ljust(10)} | {"Nome".ljust(20)} | {"Categoria".ljust(10)} | {"Poderes".ljust(10)} | {"Poderzao".ljust(10)} | {"Fraqueza".ljust(20)} | {"Forca".ljust(5)}')

        for vingador in cls.lista_de_herois:
            print(f"{str(vingador.heroi).ljust(10)} | {str(vingador.nome).ljust(20)} | {str(vingador.categoria).ljust(10)} | {str(vingador.poderes).ljust(15)} | {str(vingador.poderzao).ljust(10)} | {str(vingador.fraqueza).ljust(20)} | {str(vingador.forca).ljust(5)}")

    def __str__(self):
    
        return f'{"Vingador".ljust(10)} | {"Nome".ljust(20)} | {"Categoria".ljust(20)} | {"Poderes".ljust(10)} | {"Poderzao".ljust(10)} | {"Fraqueza".ljust(20)} | {"Forca".ljust(5)}\n' + \
               f"{str(self.heroi).ljust(10)} | {str(self.nome).ljust(20)} | {str(self.categoria).ljust(10)} | {str(self.poderes).ljust(10)} | {str(self.poderzao).ljust(10)} | {str(self.fraqueza).ljust(20)} | {str(self.forca).ljust(5)}"

