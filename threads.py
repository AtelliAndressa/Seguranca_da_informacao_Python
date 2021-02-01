from threading import Thread    # do modulo está importando a classe para fazer um multithreading
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto+=velocidade
        time.sleep(2)
        print('Piloto: {}  Km: {} \n'.format(piloto, trajeto))



t_carro1 = Thread(target=carro, args=[10, 'Bruno'])  #vai pertencer a classe Thread, target é o alvo da classe e args = argumento
t_carro2 = Thread(target=carro, args=[20, 'Python'])


t_carro1.start()
t_carro2.start()