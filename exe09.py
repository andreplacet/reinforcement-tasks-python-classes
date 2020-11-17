# Exercicio 09

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def Centro(self):
        x_centro = (self.ladoA.x + self.ladoB.x) / 2
        y_centro = (self.ladoA.y + self.ladoB.y) / 2
        return f"X = {x_centro}"
        return f"Y = {y_centro}"


def Main():
    x1 = float(input("Digite a coordenada x do canto inferior esquerdo: "))
    y1 = float(input("Digite a coordenada y do canto inferior esquerdo: "))
    ladoA = Ponto(x1, y1)
    x2 = float(input("Digite a coordenada x do canto superior direito: "))
    y2 = float(input("Digite a coordenada y do canto superior direito: "))
    ladoB = Ponto(x2, y2)
    ret = Retangulo(ladoA, ladoB)
    print(f"Ponto central: {ret.Centro()}")


Main()
