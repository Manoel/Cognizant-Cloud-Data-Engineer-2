import hashlib

# rb é modo de abrir arquivos em modo binário
# ripe160 é o algoritmo de hash
# função digest() retorna o hash em forma de string
# função digest() resume a função hash()

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() == hash2.digest():
    print(f'O arquivo: {arquivo1} e o arquivo: {arquivo2} são iguais')
    print(f'O hash do arquivo: {arquivo1} é: {hash1.hexdigest()}')
    print(f'O hash do arquivo: {arquivo2} é: {hash2.hexdigest()}')
else:
    print(f'O arquivo: {arquivo1} e o arquivo: {arquivo2} são diferentes')
    print(f'O hash do arquivo: {arquivo1} é: {hash1.hexdigest()}')
    print(f'O hash do arquivo: {arquivo2} é: {hash2.hexdigest()}')