# Conjunto
# consjunto usa {}
# conjunto não aceita repetição
# conjunto não aceita ordem

conjunto = {1, 2, 3, 4, 4, 2}
print(type((conjunto)))
print(conjunto)
print('----------------------------------')

# é possivel adicionar elementos ao conjunto
conjunto.add(5)
print(conjunto)

# é possivel remover elementos do conjunto
conjunto.remove(2)
print(conjunto)
print('----------------------------------')
# aritimeticas

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto1.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
print('----------------------------------')

# interseção
conjunto_interseccao = conjunto1.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))
print('----------------------------------')

# diferença

conjunto_diferenca = conjunto1.difference(conjunto2)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca))
print('----------------------------------')

conjunto_diferenca1 = conjunto2.difference(conjunto1)
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca1))
print('----------------------------------')

# diferença simetrica

diferenca_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(diferenca_diff_simetrica))
print('----------------------------------')

# teste de pertinência
# retorna True ou False
# True se o elemento pertence ao conjunto
# False se o elemento não pertence ao conjunto
# subconjunto de um conjunto
# são os metodos de subset, superset, join, issubset, issuperset, isdisjoint

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

# issubset
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é Subconjunto de B: {}'.format(conjunto_subset))
print('----------------------------------')
# issubset
conjunto_subset = conjunto_b.issubset(conjunto_a)
print('B não é Subconjunto de A : {}'.format(conjunto_subset))
print('----------------------------------')
print('-----------issuperset-------------')

# issuperset
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um Superconjunto de A: {}'.format(conjunto_superset))
print('----------------------------------')

# issuperset
conjunto_superset1 = conjunto_a.issuperset(conjunto_b)
print('A não é Superconjunto de B: {}'.format(conjunto_superset1))
print('----------------------------------')


# forma rapida de remover duplicados
# converter uma lista em conjunto

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_lista = set(lista)
print(conjunto_lista)

# converter de volta para lista

lista_animais = list(conjunto_lista)
print(lista_animais)
print('----------------------------------')