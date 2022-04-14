# socket é um módulo do Python que implementa o protocolo TCP/IP
# sys é um módulo do Python que implementa funções de sistema

import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!!!: {}".format(e))
        sys.exit()

    print("Conexão estabelecida com sucesso!!!")


    hostAlvo = input("Digite o host ou Ip a ser conectado: ")
    portaAlvo = int(input("Digite a porta a ser conectada: "))

    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print("Cliente conectado ao host {} na porta {}".format(hostAlvo, portaAlvo))
        s.shutdown(2)
    except socket.error as e:
        print("A conexão falhou ao conectar no host {} e na porta {}".format(hostAlvo, portaAlvo))
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()