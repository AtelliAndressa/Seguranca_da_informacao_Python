# web crawler é uma ferramenta que encontra, lê e indexa paginas web, captura informações de cada link
# muito utilizado em um processo de Pentes

from bs4 import BeautifulSoup      # extração de dados de arquivos html e xml
import operator                    # funções eficientes correspondentes a operadores como +-*/ not and
from collections import Counter    # manipular estruturas de dados como tuplas, dicionarios e listas
import requests

def start(url):
    wordlist = []     # todo conteúdo do site virá para essa lista
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser') # vai fazer a requisição dos dados e vai transformar em html

    for each_text in soup.findAll('div', {'class': 'entry-content'}):   # vai procurar o conteudo div e class e
        content = each_text.text                                        #     transformar em texto
        words = content.lower().split()    # vai transformar em letras minusculas e fazer um fatiamento

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


def clean_wordlist(wordlist):   # essa função vai remover qualquer simbolo indesejado do wordlist
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%*()_+{}[]~^?.,;:/*='

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')   # vai trocar o simbolo achado por vazio

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)    #vai limpando a lista


def create_dictionary(clean_list):    # cria um dicionario contendo cada palavra e faz uma contagem
    word_count = {}
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] =1

    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print('% s: % s' % (key, value))

    c = Counter(word_count)
    top = c.most_common(10)
    print(top)                # vai mostrar as palavras com mais ocorrências

if __name__ == '__main__':
    start('https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar')

