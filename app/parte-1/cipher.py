from utils import *


# Método para cifrar o texto
# Recebe como input o texto
def generate_ciphed_text(input_text, key):
    result_text = ""
    for index in range(len(input_text)):
        decimal_asc_ii_position = find_character_position_for_cipher(index, input_text, key)
        result_text += chr(decimal_asc_ii_position)

    return result_text
