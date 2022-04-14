import os # Importa o módulo ou biblioteca os (integra os programas e recursos do S.O)

print("#" * 60) # Imprime 60 vezes #

# Criamos uma variável que vai receber do usuário um ip)
ip_ou_host = input('Digite o IP ou o nome do host a ser verificado: ')
print("-" * 60) # Imprime 60 vezes -

os.system('ping -n 6 {}'.format(ip_ou_host)) # Chamando system da biblioteca os - comando ping -n 6 (quantidade de pacotes) e o ip_ou_host
print("-" * 60) # Imprime 60 vezes -