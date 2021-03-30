class Pessoa:
    def cumprimentar(self):
        return f'Ola {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar()) # "p" eh o primeiro parametro, se adicionar outro item, ele sera o segundo parametro