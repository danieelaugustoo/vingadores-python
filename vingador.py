class Vingador:
    categorias_permitidas = ['Humano', 'Meta-humano', 'Androide', 'Deidade', 'Alienígena']
    lista_vingadores = []
 
    def __init__(self, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca):
        if categoria not in Vingador.categorias_permitidas:
            raise ValueError("Categoria inválida!")
        if not (0 <= nivel_forca <= 10000):
            raise ValueError("Nível de força deve ser entre 0 e 10000!")
        self.nome_heroi = nome_heroi
        self.nome_real = nome_real
        self.categoria = categoria
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.nivel_forca = nivel_forca
        self._convocado = False
        self._tornozeleira = False
        self._chip_gps = False
 
        Vingador.lista_vingadores.append(self)
 
    def convocar(self):
        self._convocado = True
 
    def aplicar_tornozeleira(self):
        if not self._convocado:
            raise ValueError(f"{self.nome_heroi} ainda não foi convocado!")
        self._tornozeleira = True
        if self.nome_heroi in ["Thor", "Hulk"]:
            return f"Mensagem especial para {self.nome_heroi}: Resistente à tornozeleira!"
 
    def aplicar_chip_gps(self):
        if not self._tornozeleira:
            raise ValueError("Chip GPS só pode ser aplicado após a tornozeleira!")
        self._chip_gps = True