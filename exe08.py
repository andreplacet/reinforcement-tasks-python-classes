# Exercicio 08

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def Comer(self, comida):
        self.bucho.append(comida)

    def VerBucho(self):
        print(f"Bucho: {self.bucho}")

    def digerir(self):
        if len(self.bucho) > 0:
            self.bucho.pop(0)


nome_macaco1 = input("Digite o nome do macaco 1: ")
nome_macaco2 = input("Digite o nome do macaco 2: ")
m1 = Macaco(nome_macaco1)
m2 = Macaco(nome_macaco2)
comer1 = input(f"O que o macaco {nome_macaco1} vai comer?: ")
comer2 = input(f"O que o macaco {nome_macaco2} vai comer?: ")
m1.Comer(comer1)
m1.VerBucho()
m1.digerir()
m1.VerBucho()
m2.Comer(comer2)
m2.Comer(m1)
m2.VerBucho()
