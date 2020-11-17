# Exercicio 06

class Televisao:
    def __init__(self, canal, volume_inicial=10, volume_maximo=100):
        self.canal = canal
        self.volume_maximo = volume_maximo
        self.volume_atual = volume_inicial

    def canal(self):
        canais = ['SBT', 'Globo', 'Record', 'RedeTV', 'Bandeirantes', 'Tv Cultura']
        canal_atual = canais[self.canal]
        self.canal = str(canal_atual)

    def aumentar_volume(self):
        if self.volume_atual < self.volume_maximo:
            x = int(input(f'Volume {self.volume_atual}\n'
                          f'aumentar o volume até? (use número de 1 à 100' ))
            if (x + self.volume_atual) >= self.volume_maximo:
                return f'Volume socilitado maior que o volume máximo'
            else:
                self.volume_atual += x
                return f'Volume {self.volume_atual}'
        else:
            print('Volume Máximo!')

    def diminuir_volume(self):
        if self.volume_atual <= 0:
            return f'Volume Minino'
        else:
            x = int(input(f'Volume {self.volume_atual}\n'
                          f'diminuir o volume até? (use números entre 0 e 100: '))
            if (self.volume_atual - x) <= 0:
                return f'Volume soliticado menor que volume minimo'
            else:
                self.volume_atual -= x
                return f'Volume {self.volume_atual}'


canal = int(input('Escolha um canal\n'
                  '1 - SBT   2 - Globo\n'
                  '3 - Record  4 - RedeTV\n'
                  '5 - Bandeirantes  6 - Tv Cultura\n'
                  '-->'))
tv = Televisao(canal=canal)
tv.canal()
print(f'Canal {tv.canal}')
