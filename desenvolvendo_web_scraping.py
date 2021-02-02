#ferramenta de coleta de dados web, mineração de dados, análise

from bs4 import BeautifulSoup    #para extração de dados de html e xml
import soup, string
import requests   # envie solicitações http

site = requests.get('https://www.climatempo.com.br/').content # vai pegar todo conteudo do site passado no parametro
sopa = BeautifulSoup(site, 'html.parser')  # vai baixar todo html do site
print(sopa.prettify()) # prettify transforma tudo de html em string

print(sopa.title.string) # mostra somente o título

temperatura = sopa.find("scan", class_="-bold -gray-dark-2 -uppercase -font-12 _padding-5")
print(temperatura.string)
