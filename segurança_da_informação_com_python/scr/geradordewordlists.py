# gerador de wordlists
# wordlists é um arquivo de texto com palavras separadas por espaços
# permutations é uma lista de palavras com todas as permutações


import itertools

string = input("String a ser permutada: ")

resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))