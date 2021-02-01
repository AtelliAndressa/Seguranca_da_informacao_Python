import socket

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket criado com sucesso.")

host = 'localhost'
porta =5432

s.bind((host, porta)) #faz a ligação entre cliente e servidor através dos parâmetros inseridos
mensagem = 'Servidor: Olá cliente, tudo bem?'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()), end)

# fazemos a execução do ServidorUCP e após a execução do clienteUCP #

