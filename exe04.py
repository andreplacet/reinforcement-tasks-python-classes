# Exercicio 04

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def __str__(self):
        return self.nome

    def envelhecer(self):
        if self.idade < 21:
            self.idade += 1
            self.altura += (1 / 2) / 100
            return f'Mais um ano se passou, agora tenho {self.idade} anos e cresci, agora tenho {self.altura:.2f}cm!'
        else:
            self.idade += 1
            return f'Mais um ano se passou, agora tenho {self.idade} anos!'

    def engordar(self):
        self.peso += 1
        return f'Não é facil, parece que engordei mais 1 kilo!'

    def emagrecer(self):
        self.peso -= 1
        return f'Parece que perdi um kilo!'

    def crescer(self):
        self.altura += 0.5
        return f'Parece que cresci meio centimentro de uns tempos pra cá!'


pessoa = Pessoa(nome='Andre', idade=17, peso=80, altura=1.70)

print(pessoa.envelhecer())
print(pessoa.envelhecer())
print(pessoa.envelhecer())
print(pessoa.envelhecer())
print(pessoa.envelhecer())
print(pessoa.envelhecer())
print(pessoa.envelhecer())
print(pessoa.envelhecer())
