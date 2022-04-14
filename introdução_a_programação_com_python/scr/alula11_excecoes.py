# Exceções em Python
# try - except - else - finally
# BaseException é a exceção mais genérica
# No top uso sempre os filhos das exceções mais genéricas
# Finaly é sempre executado independente de erros

from logging import exception


lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
except ZeroDivisionError:
    print('Não é possível divisão por zero.')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética.')
except IndexError:
    print('Erro ao acessar um indice inválido da lista.')
except Exception as ex:
    print('Erro desconhecido. Erro: {}' .format(ex))
else:
    print('Executa quanbdo Não ocorre exceção.')
finally:
    print('Sempre executa.')
    print('Fechando o arquivo.')
    arquivo.close()