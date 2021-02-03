import re  # operações com expressões regulares
import json # codificação e decodificação em json
from urllib.request import urlopen #funções de classes para abrir urls

url = 'https://ipinfo.io/json'
resposta = urlopen(url) # vai receber a resposta da url
dados = json.load(resposta) # vai carregar todo o java script e jogar pro objeto

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados ['region']

print('Detalhes do Ip externo consultado\n ')
print('Ip {4}\nRegião {1}\nPaís {2}\nCidade {3}\nOrganização {0}'.format(org,regiao,pais,cid,ip))
