from utils import *


# Método para decifrar o texto
def generate_original_text(input_text, key):
    result_text = ""
    for index in range(len(input_text)):
        decimal_asc_ii_position = find_character_position_for_original_text(index, input_text, key)
        result_text += chr(decimal_asc_ii_position)

    return result_text
