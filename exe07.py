# Exercicio 07

from io import TextIOBase


class BichinhoVirtual:

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def MudaNome (self,nome):
        self.nome = nome

    def MudaFome(self, fome):
        self.fome = fome

    def MudaSaude(self, saude):
        self.saude = saude

    def MudaIdade(self,idade):
        self.idade = idade

    def Humor(self, Fome, saude):
        return fome * saude

nome = input("Digite o nome do seu tamaguchi: ")
fome = int(input("Digite a fome: "))
saude = int(input("Digite a saude: "))
idade = int(input("Digite a idade: "))
tamaguchi = BichinhoVirtual(nome, fome, saude, idade)
print("-"*30 + "Seu tamaguchi (atual) " + "-"*30)
print(f"Nome: {tamaguchi.nome}")
print(f"Fome: {tamaguchi.fome}")
print(f"Saúde: {tamaguchi.saude}")
print(f"Idade: {tamaguchi.idade}")
print(f"Humor: {tamaguchi.Humor(fome, saude)}")
resposta = input("Deseja mudar seus parametros? (nome, fome, saude e idade)? s/n: ").lower()
if resposta == "n":
    pass
else:
    nome = input("Digite o nome do seu tamaguchi: ")
    fome = int(input("Digite a fome: "))
    saude = int(input("Digite a saude: "))
    idade = int(input("Digite a idade: "))
    tamaguchi = BichinhoVirtual(nome, fome, saude, idade)
    print("-"*30 + "Seu tamaguchi (atualizado) " + "-"*30)
    print(f"Nome: {tamaguchi.MudaNome(nome)}")
    print(f"Fome: {tamaguchi.MudaFome(fome)}")
    print(f"Saúde: {tamaguchi.MudaSaude(saude)}")
    print(f"Idade: {tamaguchi.MudaIdade(idade)}")
    print(f"Humor: {tamaguchi.Humor(fome, saude)}")
