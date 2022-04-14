# Criando um lista.
# a lista é uma sequencia de elementos
# a lista é mutável
# a lista é indexada
# a lista usa []

lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

print(lista_animal[1])

soma = 0

for x in lista:
    print(x)
    soma += x
print(soma)

# # Outra forma de fazer a soma
print(sum(lista))
print(max(lista))
print(max(lista_animal))
print('----------------------------------')

# Quero saber o gato existe na lista?

if 'gato' in lista_animal:
    print('O gato existe na lista')
    print('----------------------------------')
else:
    print('O gato não existe na lista')
    print('----------------------------------')

if lista_animal.count('lobo') > 0:
    print('O lobo existe na lista')
    print('----------------------------------')
else:
    print('O lobo não existe na lista')
    print('----------------------------------')

nova_lista = lista_animal * 3
print(nova_lista)
print('----------------------------------')

# # Como incluir o lobo na lista de animais?

if lista_animal.count('lobo') > 0:
    print('O lobo existe na lista')
    print('----------------------------------')
else:
    print('O lobo não existe na lista. Vamos incluir!')
    # o append adiciona um elemento na lista
    # o append é um método da lista
    lista_animal.append('lobo')
    print(lista_animal)
    print('----------------------------------')

# # o pop remove um elemento da lista
# # o pop é um método da lista
# # o pop remove o último elemento da lista
lista_animal.pop()
print(lista_animal)
print('----------------------------------')

# # o pop(0) remove o primeiro elemento da lista
lista_animal.pop(0)
print(lista_animal)
print('----------------------------------')

# o remove remove um elemento específico da lista
lista_animal.remove('elefante')
print(lista_animal)
print('----------------------------------')

# Consigo ordenar a lista
# o sort é um método da lista

lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)

# o reverse inverte a ordem da lista
lista_animal.reverse()
print(lista_animal)
print('----------------------------------')

# tupla é uma lista imutável
# nao é possivel adicionar elementos
# nao é possivel remover elementos
# nao é possivel alterar elementos
# a tupla usa ()

lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(tupla[2])
print(len(tupla))

# convertendo uma lista em uma tupla

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

# convertendo uma tupla em uma lista
# se tenho uma tupla e ouver necessidade de uma alteração, eu converto em lista

lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)