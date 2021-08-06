class Motor:
    def __init__(self, arg_velocidade = 0):
        self.velocidade = arg_velocidade
    def acelerar(self):
        self.velocidade += 1
    def frear(self):
        self.velocidade = max(0, self.velocidade) # maior valor entre os dois


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

"""
    >>> motor = Motor()
    >>> motor.acelerar()
"""