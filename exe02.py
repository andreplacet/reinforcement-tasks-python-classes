# Exercicio 02

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_valor(self):
        x = int(input('Novo tamanho do lado: '))
        self.lado = x

    def retornar_valor(self):
        return self.lado

    def calc_area(self):
        area = self.lado * self.lado
        return area


quadrado = Quadrado(lado=4)

while True:
    print('Programa para Calcular os lados de um Quadrado Equilatero')
    print(f'{"=" * 57}')
    acao = int(input('O que deseja fazer?\n'
                     '1 - Ver o valor dos lados do quadrado\n'
                     '2 - Mudar o valor dos lados do quadrado\n'
                     '3 - Calcular a área do quadrado\n'
                     '0 - sair\n'
                     '-->  '))
    if acao not in (1, 2, 3, 0):
        print('VALOR INVALIDO, TENTE NOVAMENTE')
    else:
        if acao == 0:
            print('Programa Finalizado')
            break
        elif acao == 1:
            print(f'O valor dos lados do quadrado equilatero é de {quadrado.retornar_valor()}')
        elif acao == 2:
            quadrado.mudar_valor()
            print(f'Valor alterado, o valor agora é {quadrado.retornar_valor()}')
        elif acao == 3:
            area = quadrado.calc_area()
            print(f'A área do quadrado equilatero de lados {quadrado.retornar_valor()} '
                  f'é de {area}')
