# Exercicio 12

class Conta():

    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

        def setNome(self, nome):
            self.nome = nome

        def deposito(self, valor):
            self.saldo += valor

        def saque(self, valor):
            if (self.saldo >= valor):
                self.saldo -= valor


class contaInvestimento(Conta):

    def __init__(self, numero, nome, saldo, taxaJuros):
        Conta.__init__(self, numero, nome, saldo)
        self.taxaJuros = taxaJuros

    def adicioneJuros(self):
        self.saldo += (self.saldo * (self.taxaJuros / 100))


poupanca = contaInvestimento(555, "Lucas", 1000, 10)
print(vars(poupanca))
poupanca.adicioneJuros()
poupanca.adicioneJuros()
poupanca.adicioneJuros()
poupanca.adicioneJuros()
poupanca.adicioneJuros()
print(vars(poupanca))
