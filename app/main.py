from cipher import *
from key_manager import *
from decoder import *

entrada = "CYBERSECURITY"
chave = "BEST"


# Texto cifrado esperado: DCTXSWWVVVAMZ

#########################################################################
# Referências :::::::::::>
# https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Examples.html
# https://www.geeksforgeeks.org/vigenere-cipher/
# https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
# https://intellipaat.com/blog/vigenere-cipher/
#########################################################################
#<<<<<<< patch-1
#teste fork
#=======
#test 6may 12:31
#test 6may 12:36
#>>>>>>> main


if __name__ == '__main__':
    generated_key = generate_key_with_the_same_size_of_input(entrada, chave)
    ciphed_text = generate_ciphed_text(entrada, generated_key)
    original_text = generate_original_text(ciphed_text, generated_key)
    print('GENERATING CIPHER ::::::::::::::> CIPHER -> ' + ciphed_text)
    print('DECODING TEXT ::::::::::::::> ORIGINAL -> ' + original_text)
