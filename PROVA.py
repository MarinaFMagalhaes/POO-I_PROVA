class Elevador:
    def __init__(self, totalCapacidade, totalAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = 0
        self.totalAndar = totalAndar
        self.atualAndar = 0

    def subir(self):
        if self.atualAndar < self.totalAndar:
            self.atualAndar += 1
            print("Subindo")
        else:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO!")

    def descer(self):
        if self.atualAndar > 0:
            self.atualAndar -= 1
            print("Descendo")
        else:
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")

    def entrar(self):
        if self.atualCapacidade < self.totalCapacidade:
            self.atualCapacidade += 1
            print("Entrando uma pessoa")
        else:
            print("O ELEVADOR ESTÁ CHEIO!")

    def sair(self):
        if self.atualCapacidade > 0:
            self.atualCapacidade -= 1
            print("Saindo uma pessoa")
        else:
            print("NÃO TEM NINGUÉM")


# Formulas de uso:
elevador = Elevador(15, 20)  # Capacidade máxima: 15 pessoas, total de andares: 20

elevador.entrar()  # Entra uma pessoa
elevador.subir()   # Elevador sobe um andar
elevador.entrar()  # Entra outra pessoa
elevador.subir()   # Elevador sobe outro andar
elevador.subir()   # Elevador sobe mais um andar
elevador.subir()   # Tentativa de subir além do andar mais alto
elevador.descer()  # Elevador desce um andar
elevador.sair()    # Uma pessoa sai do elevador
elevador.descer()  # Elevador desce outro andar
elevador.sair()    # Tentativa de sair quando não há ninguém no elevador