import socket

# criando um objeto de conexão do tipo socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente Socket criado com sucesso!!!")

host = 'localhost'
porta = 5432

s.bind((host, porta))
mensagem = "\nServidor: Oláaaaaa cliente e ai beleza?"

while 1:
    dados, end = s.recvfrom(4096)
    if dados:
        print("Servidor enviando mensagem: {}".format(dados.decode()))
        s.sendto(dados + (mensagem.encode()), end)