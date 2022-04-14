# Gerador de hashes
# hashlib é uma biblioteca de criptografia

import hashlib

string = input("Digite o texto a ser gerado a hash: ")

menu = int(input('''  ### MENU - ESCOLHA O TIPO DE HASH ###
1 - MD5
2 - SHA1
3 - SHA256
4 - SHA512
    
    Digite a opção desejada: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print("\nA hash MD5 da string: ", string, 'é: ', hashlib.md5(string.encode()).hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print("\nA hash SHA1 da string: ", string, 'é: ', hashlib.sha1(string.encode()).hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print("\nA hash SHA256 da string: ", string, 'é: ', hashlib.sha256(string.encode()).hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print("\nA hash SHA512 da string: ", string, 'é: ', hashlib.sha512(string.encode()).hexdigest())
else:
    print("\nOpção inválida!")
