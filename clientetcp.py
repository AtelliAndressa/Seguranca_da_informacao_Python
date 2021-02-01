import socket
import sys   #fornece algumas funções que tem forte interação com interpretador


def main():
    try:
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou")
        print("Erro: {}".format(e))
        sys.exit()  #fechará o programa

    print("Socket criado com sucesso.")

    HostAlvo = input("Digite o host ou Ip a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente tcp conectado com sucesso no host: " + HostAlvo + " e na porta: " + PortaAlvo)
        s.shutdown(2)    #vai interromper a conexão para não gerar loop após 2 segundos

    except socket.error as e:
        print("A conexão falhou")
        print("Erro: {}".format(e))
        sys.exit()  # fechará o programa


if __name__ == '__main__':
    main()
