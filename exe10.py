# Exercicio 10

class BombaCombustível:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valorLitro, quantidadeCombustivel):
        return valorLitro * quantidadeCombustivel

    def alterarCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel

    def alterarValor(self, valorLitro):
        self.valorLitro = valorLitro

    def alterarQuantidadeCombustivel(self, valorLitro, quantidadeCombustivel):
        return valorLitro * quantidadeCombustivel


tipoCombustivel = input("Qual é o tipo de combustivel: ")
valorLitro = float(input("Qual o valor por litro do combustivel?: "))
quantidadeCombustivel = float(input("Informe a quantidade de combustivel: "))
posto = BombaCombustível(tipoCombustivel, valorLitro, quantidadeCombustivel)
print(f"Valor a ser pago pelo combutivel {tipoCombustivel}: R${posto.abastecerPorValor(valorLitro, quantidadeCombustivel)}")
pergunta = input("Deseja mudar os parametros? s/n: ").lower()

if pergunta == "n":
    pass
else:
    novo_combustivel = input("Qual será o combustivel?: ")
    novo_valorLitro = float(input("Digite o valor do litro do combustivel: "))
    novo_qtdCombustivel = float(input("Informe a quantidade de combustivel: "))
    BombaCombustível.alterarCombustivel(novo_combustivel)
    BombaCombustível.alterarValor(novo_valorLitro)
    print(
        f"Valor a ser pago pelo combutivel {novo_combustivel}: R${posto.alterarQuantidadeCombustivel(novo_valorLitro, novo_qtdCombustivel)}")
