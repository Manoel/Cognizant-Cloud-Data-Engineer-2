# Construindo métodos, funções classes

# Funções são tudo que retorna um valor
# Métodos são tudo que altera um objeto (def - definição)

class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.soma(10, 2))
print(calculadora.subtracao(5, 3))
print(calculadora.multiplicao(10, 5))
print(calculadora.divisao(100, 2))

