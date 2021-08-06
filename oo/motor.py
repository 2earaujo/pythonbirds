class Motor:
    def __init__(self, arg_velocidade = 0):
        self.velocidade = arg_velocidade
    def acelerar(self):
        self.velocidade += 1
    def frear(self):
        if self.velocidade -2 < 0:
            self.velocidade = 0
        else:
            self.velocidade - 2


if __name__ == '__main__':
    # Testando motor
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)