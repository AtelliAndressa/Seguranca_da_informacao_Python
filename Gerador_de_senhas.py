import random
import string

tamanho = 16   # caracteres

chars = string.ascii_letters + string.digits + '!@#$%&*()-=+,.;' # estrutura terá maiusc e minusc, 0 a 9, caracteres)

rnd = random.SystemRandom()  # os.urandom = gera num aleatórios a partir de fontes fornecidas pelo sistema operacional

print(''.join(rnd.choice(chars) for i in range(tamanho))) #pega cada caracter randomico gerado através do chars e
                                                        # repete o processo até o valor de tamanho.
