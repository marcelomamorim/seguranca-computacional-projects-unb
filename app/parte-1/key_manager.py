from utils import *


# Método para gerar a chave completa
def generate_key_with_the_same_size_of_input(input_text, key):
    if does_cipher_key_has_the_same_size_of_input_text(input_text, key):
        return key
    else:
        while True:
            key += key
            if len(key) > len(input_text):
                break

    return key[:len(input_text)]
