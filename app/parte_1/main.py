
from importlib import *
from cypher import *
from key_manager import *
from decoder import *

entrada = "CYBERSECURITY"
chave = "BEST"


# Texto cifrado esperado: DCTXSWWVVVAMZ

#########################################################################
# Referências Utilizadas como base para desenvolvimento do algorítmo :::::::::::>
# https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Examples.html
# https://www.geeksforgeeks.org/vigenere-cypher/
# https://en.wikipedia.org/wiki/Vigen%C3%A8re_cypher
# https://intellipaat.com/blog/vigenere-cypher/
# Youtube: https://www.youtube.com/watch?v=LaWp_Kq0cKs
#########################################################################


if __name__ == '__main__':
    generated_key = generate_key_with_the_same_size_of_input(entrada, chave)
    # CIFRANDO O TEXTO - PARTE 1 DO TRABALHO
    cyphed_text = generate_cyphed_text(entrada, generated_key)
    # DECIFRANDO O TEXTO - PARTE 1 DO TRABALHO
    original_text = generate_original_text(cyphed_text, generated_key)
    print('GENERATING cyphER ::::::::::::::> cyphER -> ' + cyphed_text)
    print('DECODING TEXT ::::::::::::::> ORIGINAL -> ' + original_text)


    ##############################################################################
    #with open('./app/parte_2/txts/ritaLee.txt', 'r') as file:
    #    cyphertext = file.read().replace('\n', '')
    #
    #
    #import sys
    #import os

    #SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    #sys.path.append(os.path.dirname(SCRIPT_DIR))


    #from parte_2 import utils
    #
    #cyphertext = utils.remove_combining_fluent(cyphertext)
    #cyphertext = utils.remove_caracteres_especiais_e_espacos(cyphertext).upper()
    #generated_key = generate_key_with_the_same_size_of_input(cyphertext, chave)
    #cyphed_text = generate_cyphed_text(cyphertext, generated_key)
    #print(' ::::::::::::::> ' + cyphed_text)
    #

 
    