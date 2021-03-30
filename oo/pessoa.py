class Pessoa:
# para criar atributos, eu uso o double init:
    def __init__(self,nome=None, idade=25):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'Ola {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Luciano')
    #print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar(),p.nome,p.idade)
# "p" eh o primeiro parametro, se adicionar outro item, ele sera o segundo parametro
# O metodo eh um tipo de atributo da Classe,mas nao eh o unico!