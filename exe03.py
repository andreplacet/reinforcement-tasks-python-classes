# Exercicio 03

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_valores(self):
        x = int(input('Novo valor da base do retangulo: '))
        y = int(input('Novo valor da altura do retangulo: '))
        self.base = x
        self.altura = y

    def retornar_valores(self):
        return self.base, self.altura

    def calcular_area(self):
        area = self.base * self.altura
        return area

    def calcula_perimeto(self):
        perimetro = 2 * (self.base + self.altura)
        return perimetro


retangulo = Retangulo(9, 12)

print('Programa para calcular quantidade de pisos de uma área retangular')
print(f'{"=" * 65}')
base = int(input('Largura: '))
altura = int(input('Comprimento: '))
retangulo.base = base
retangulo.altura = altura
piso = float(input('Tamanho em metros quadrado do piso ou revestimento a ser usado: '))
print(f'Você precisara de {retangulo.calcular_area() / piso:.0f} pisos ou revestimentos'
      f' para cobrir uma área de {retangulo.calcular_area()} mts²')
