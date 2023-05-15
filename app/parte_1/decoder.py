from utils import *


# Método para decifrar o texto
def generate_original_text(input_text :str, key :str) -> str:
    """Decriptação do texto cifrado a partir de uma chave conhecida

    Args:
        input_text (str): Texto a ser decifrado (cyphertext); 
        key (str): chave previamente conhecida -> deve estar extendida com todo o comprimento do _input_text_

    Returns:
        str: Texto claro (plaintext)
    """
    
    result_text = ""
    for index in range(len(input_text)):
        decimal_asc_ii_position = find_character_position_for_original_text(index, input_text, key)
        result_text += chr(decimal_asc_ii_position)

    return result_text


if __name__=="__main__":
    print()
    print(generate_original_text("DCTXSWWVVVAMZ", "BESTBESTBESTB"))
    print()

