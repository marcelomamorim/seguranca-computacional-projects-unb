from utils import *


# Método para cifrar o texto
# Recebe como input o texto
def generate_ciphed_text(input_text :str, key :str):
    """
    Encriptação do texto

    Args:
        input_text (str): Texto a ser encriptado (plaintext); 
        key (str): chave que será usada -> deve estar concatenada com todo o comprimento do _input_text_

    Returns:
        str: texto encriptado
    """    
    result_text = ""
    for index in range(len(input_text)):
        decimal_asc_ii_position = find_character_position_for_cipher(index, input_text, key)
        result_text += chr(decimal_asc_ii_position)

    return result_text


if __name__=="__main__":
    print()
    print(generate_ciphed_text("CYBERSECURITY", "BESTBESTBESTB"))
    print()
    