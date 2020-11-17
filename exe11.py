# Exercicio 11

class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.nivelCombustivel = 0

    def andar(self, distancia):
        temp = distancia / self.consumo
        self.nivelCombustivel -= temp

    def obterGasolina(self):
        return self.nivelCombustivel

    def adicionarGasolina(self, quantidade):
        self.nivelCombustivel += quantidade

meuFusca = Carro(8)
meuFusca.adicionarGasolina(50)
meuFusca.andar(300)
print(vars(meuFusca))
print(meuFusca.obterGasolina())