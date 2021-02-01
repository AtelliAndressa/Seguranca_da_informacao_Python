# wordlists = lista de palavras usado para comparar a autenticação de um dispositivo,

import itertools #fornece iteração como combinações e permutação sem repetição

string = input("String a ser permutada: ")

resultado = itertools.permutations(string, len(string)) # caracteres e quantas permutações fará

for i in resultado:
    print(''.join(i)) # vai juntar o caracter com o próximo caracter


