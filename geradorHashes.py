import hashlib

#resultado = hashlib.md5(b'Python security') # o b antes da string vai convertê-las em byte

string = input('Digite o texto a ser gerada a hash: ')

menu = int(input(''' MENU > ESCOLHA O TIPO DE HASH:
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                DIGITE O NÚMERO DO HASH A SER GERADO: '''))

if menu == 1:
    resultados = hashlib.md5(string.encode('utf-8'))
    print('O hash MD5 da string é: ', resultados.hexdigest())
elif menu == 2:
    resultados = hashlib.sha1(string.encode('utf-8'))
    print('O hash SHA1 da string é: ', resultados.hexdigest())
elif menu == 3:
    resultados = hashlib.sha256(string.encode('utf-8'))
    print('O hash SHA256 da string é: ', resultados.hexdigest())
elif menu == 4:
    resultados = hashlib.sha512(string.encode('utf-8'))
    print('O hash SHA512 da string é: ', resultados.hexdigest())
else:
    print('Algo de errado aconteceu, tente novamente.')