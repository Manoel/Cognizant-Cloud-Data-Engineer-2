# Importando o modulo aula7_televisao.py
# Import é uma função que permite importar um módulo
# from é um comando de importação

# import aula7_televisao

# televisao = aula7_televisao.Televisao()

# televisao.power()
# print(televisao.ligada)

# --------------------------------------------------

# Acessando a classe Televisao diretamente

from aula7_televisao import Televisao
from aula7_calculador1 import Calculadora
from aula8_contador_letras import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()

    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    print('------------------')

    cauculadora = Calculadora(10, 2)
    print(cauculadora.soma())
    print('------------------')

    # Como eu não tenho uma classe contador_letras, eu posso acessar direto o metodo contador_letras

    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavras da lista: {}'.format(total_letras))
    print('------------------')

    print(teste())

