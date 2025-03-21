class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

if __name__ == '__main__':
    calc = Calculadora(1, 2)
    print("A SOMA DE 1 + 2 ABAIXO")
    print(calc.soma())
