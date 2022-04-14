# Criação de arquivo
# open é uma função que abre um arquivo
# Ele é um biltins, ou seja, é uma função que já vem com o python
# No mode utiliza-se o r, w, a, r+, w+, a+, x, x+, sendo o r o padrão, 
# o w sobrescreve o arquivo, o a adiciona no final do arquivo, o r+ le e escreve no arquivo, 
# o w+ sobrescreve o arquivo, o a+ adiciona no final do arquivo, o x abre o arquivo para leitura e escrita, 
# o x+ abre o arquivo para leitura e escrita, sendo o x+ o mais utilizado.

from this import d
import shutil

def escrever_arquivo(texto):
    diretorio = 'D:/BOOTCAMP_COGNIZANT_CLOUD_DATA_ENGINEER_DIO_2/PYTHON//SCRIPTS/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        media = lambda notas: sum([int(i) for i in notas]) / len(notas)
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'D:/BOOTCAMP_COGNIZANT_CLOUD_DATA_ENGINEER_DIO_2/PYTHON/')   

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'D:/BOOTCAMP_COGNIZANT_CLOUD_DATA_ENGINEER_DIO_2/PYTHON/')

if __name__ == '__main__':
    move_arquivo('notas.txt')
    #copia_arquivo('notas.txt')
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #escrever_arquivo('Primeira linha. \n') 
    #aluno = 'Cesar, 7, 9, 3, 8\n'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')
