# Personaliza exceções
# while True: é um loop infinito
# break é para sair do loop
# pass é para não fazer nada
# Sempre que for necessário criar uma exceção personalizada, sempre tem que ter a classe Error(Exception)

class Error(Exception):
    """Base class for other exceptions"""
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Digite uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10.')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0.')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    except InputError as ex:
        print(ex)