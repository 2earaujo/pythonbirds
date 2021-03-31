class Pessoa:
    # criar atributo de classe / atributo default / atributo padrao = nao migram para objetos filhos
    # se o atributo for "padrao" para todos objetos, entao passa a ser atributo de CLasse
    documento = 'cpf'
    # esse atributo pode ser sobreposto, e nessa caso ele passa a buscar o valor no objeto instanciado

    # para criar atributos, eu uso o double init:
    def __init__(self ,*filhos ,nome=None ,idade=25):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    # luciano = Pessoa(nome='Luciano')
    douglas = Pessoa(nome='Douglas')
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(douglas ,nome='Luciano')
    # print(Pessoa.cumprimentar(p))
    # print(id(p))
    print(f'{luciano.nome} ! Hoje voce possui {luciano.idade} anos')
    for filho in luciano.filhos:
        print(f'Filho do {luciano.nome} eh {filho.nome}')
    # adicionando argumentos dinamicos num OBJETO ESPECIFICO
    luciano.sobrenome = 'Ramalho'
    print(f'O objeto {luciano.nome} agora tem sobrenome = {luciano.sobrenome} ! So esse objeto foi alterado')
    # acessando os elementos do objeto
    print(luciano.__dict__)
    print(renzo.__dict__ ,' => Observe que esse objeto possui menor numero de elementos!')
    print('Agora vou remover o atributo filho')
    del luciano.filhos
    print(luciano.__dict__)

# "p" eh o primeiro parametro, se adicionar outro item, ele sera o segundo parametro
# O metodo eh um tipo de atributo da Classe,mas nao eh o unico!
