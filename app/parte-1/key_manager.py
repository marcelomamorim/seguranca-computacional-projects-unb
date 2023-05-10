from utils import *


# Método para gerar a chave "completa"
def generate_key_with_the_same_size_of_input(input_text: str, key: str):
    """
    Concatena a chave para preencher o comprimento até o tamanho 
    necessário para fazer todos os shifts do input_text

    Args:
        input_text (str): texto de entrada
        key (str): chave conhecida/determinada

    Returns:
        str: shifts a serem executados a cada caractere (senha concatenada)
    """    
    if does_cipher_key_has_the_same_size_of_input_text(input_text, key):
        return key
    else:
        while True:
            key += key
            if len(key) > len(input_text):
                break

    return key[:len(input_text)]


if __name__== "__main__":
    print()
    print(generate_key_with_the_same_size_of_input("CIBERSECURITY", "BEST"))

