import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente Socket criado com sucesso!!!")

host = 'localhost'
porta = 5433
mensagem = "Mensagem enviada pelo cliente"

try:
    print("Cliente enviando mensagem: {}".format(mensagem))
    s.sendto(mensagem.encode(), (host, 5432))
    print("Mensagem enviada com sucesso!!!")

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("Mensagem recebida do servidor: {}".format(dados))
finally:
    print("Fechando socket...")
    s.close()
