import socket #fornece acesso a interface de rede
#UDP = Protocolo de datagrama de Usuário

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   #objeto de conexão
print("Cliente socket criado com sucesso.")

host = 'localhost'
porta = 5433
mensagem = 'Olá servidor, tudo certo? '

try:
    print("Cliente: " +mensagem)
    s.sendto(mensagem.encode(), (host, 5432)) #vai empacotar a mensagem e mandar a porta que o servidor está ouvindo

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()  #vai desempacotar a resposta recebida do servidor
    print("cliente: " + dados)
finally:
    print("Cliente: Fechando a conexão")
    s.close() #vai fechar a conexão


