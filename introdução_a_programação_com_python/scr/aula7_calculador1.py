# Construindo métodos, funções classes

# Funções são tudo que retorna um valor
# Métodos são tudo que altera um objeto (def - definição)

class Calculadora:
    # instanciando o objeto
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':

    calculadora = Calculadora(10, 2)
    print(calculadora.valor_a)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicao())
    print(calculadora.divisao())

