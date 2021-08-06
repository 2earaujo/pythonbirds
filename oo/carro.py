from motor import Motor
from direcao import Direcao

class Carro():
    def __init__(self, arg_direcao, arg_motor):
        self.motor = arg_motor
        self.direcao = arg_direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.direcao

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

if __name__ == '__main__':
    motor = Motor()
    direcao = Direcao()
    carro = Carro(direcao, motor)
    print('Velocidade carro: ',carro.calcular_velocidade())
    print('Acelera carro')
    carro.acelerar()
    print('Calcula velocidade: ',carro.calcular_velocidade())
    print('Acelera carro')
    carro.acelerar()
    print('Velocidade atual: ',carro.calcular_velocidade())
    carro.frear()
    print(carro.calcular_velocidade())
    print('Direcao atual: ',carro.calcular_direcao())
    print('Giro a direita')
    carro.girar_a_direita()
    print('Direcao atual: ',carro.calcular_direcao())
    print('Giro a direita')
    carro.girar_a_direita()
    print('Direcao atual: ',carro.calcular_direcao())
    print('Giro a direita')
    carro.girar_a_direita()
    print('Direcao atual: ',carro.calcular_direcao())
    print('Giro a direita')
    carro.girar_a_direita()
    print('Direcao atual: ',carro.calcular_direcao())
    print('Giro a esquerda')
    carro.girar_a_esquerda()
    print('Direcao atual: ',carro.calcular_direcao())
    print('Giro a esquerda')
    carro.girar_a_esquerda()
    print('Direcao atual: ',carro.calcular_direcao())