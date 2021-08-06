class Direcao():
    def __init__(self):
        self.direcao = 'Norte'

    def girar_a_direita(self):
        if self.direcao == 'Norte':
            self.direcao = 'Leste'
        elif self.direcao == 'Leste':
            self.direcao = 'Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Oeste'
        elif self.direcao == 'Oeste':
            self.direcao = 'Norte'

    def girar_a_esquerda(self):
        if self.direcao == 'Norte':
            self.direcao = 'Oeste'
        elif self.direcao == 'Oeste':
            self.direcao = 'Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Leste'
        elif self.direcao == 'Leste':
            self.direcao = 'Norte'

if __name__ == '__main__':
    # Testando Direcao
    direcao = Direcao()
    print(direcao.direcao)
    direcao.girar_a_direita()
    print(direcao.direcao)
    direcao.girar_a_direita()
    print(direcao.direcao)
    direcao.girar_a_direita()
    print(direcao.direcao)
    direcao.girar_a_direita()
    print(direcao.direcao)
    direcao.girar_a_esquerda()
    print(direcao.direcao)
    direcao.girar_a_esquerda()
    print(direcao.direcao)
    direcao.girar_a_esquerda()
    print(direcao.direcao)
    direcao.girar_a_esquerda()
    print(direcao.direcao)