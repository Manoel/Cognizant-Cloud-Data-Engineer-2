# Contador de letras
# O append() adiciona um elemento ao final da lista

def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

def teste():
    return 'Teste'

if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contador_letras(lista))