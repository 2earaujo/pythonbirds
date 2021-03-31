class Pessoa:
# para criar atributos, eu uso o double init:
    def __init__(self,*filhos,nome=None, idade=25):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Ola {id(self)}'

if __name__ == '__main__':
    p = Pessoa(nome='Luciano')
    filho_1 = Pessoa(nome='Douglas')
    filho_2 = Pessoa(nome='Matilde')
        pai = Pessoa(filho_1,nome='Pai-1')
    #print(Pessoa.cumprimentar(p))
    #print(id(p))
    print(pai.cumprimentar(),pai.nome,pai.idade)
    for filho in pai.filhos:
        print(f'Filho do {pai.nome} eh {filho.nome}')
# "p" eh o primeiro parametro, se adicionar outro item, ele sera o segundo parametro
# O metodo eh um tipo de atributo da Classe,mas nao eh o unico!