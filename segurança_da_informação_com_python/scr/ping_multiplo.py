import os
import time # Importa o módulo ou biblioteca time (integra os programas e recursos do S.O)

with open('hosts.txt') as file: # Abre o arquivo hosts.txt
    dump = file.read() # Cria uma variável que vai receber o conteúdo do arquivo hosts.txt
    dump = dump.splitlines() # Cria uma variável que vai receber o conteúdo do arquivo hosts.txt e separa as linhas

    for ip in dump:
        print('Verificando o IP: {}'.format(ip))
        print('-' * 60)
        os.system('ping -n 2 {}'.format(ip))
        print('-' * 60)
        time.sleep(5) # Aguarda 5 segundos