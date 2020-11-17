# Exercicio 01

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def mostrar_cor(self):
        print(f'A cor da bola é {self.cor}')

    def trocar_cor(self):
        new_color = str(input('Informe a nova cor: '))
        self.cor = new_color


bola = Bola('azul', 3, 'metal')

while True:
    bola.mostrar_cor()
    trocar = str(input('Deseja trocar a cor? [s]im / [n]ão '))
    if trocar.lower() == 's':
        bola.trocar_cor()
    else:
        break