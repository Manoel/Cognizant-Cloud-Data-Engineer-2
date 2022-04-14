# Lambda
# lambda: é uma função anônima
# Uma forma de simplificar alguma coisa que vamos utilizar mais de uma vez no codigo.
# O codigo abaixo faz a mesma coisa que o codigo do modulo aula8_contador_letras.py
# Com lambda resolvemos o problema de repetição de código, ou seja, que podem ser feitas de uma forma mais simples.
# Característica da lambda é que ela é uma função anônima, ou seja, não tem nome e possui apnas uma linha de código.

contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))
print('------------------')

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
print(soma(10, 2))
print(subtracao(10, 2))
print('------------------')

# Usando dicionarios

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b

}

print(type(calculadora))
soma = calculadora['soma']
# este acima é o mesmo que este: 'soma': lambda a, b: a + b
multiplicacao = calculadora['multiplicacao']
print('A soma é: {}'.format(soma(10, 2)))
print('A multiplicação é: {}'.format(multiplicacao(10, 2)))