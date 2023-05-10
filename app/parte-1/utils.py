def does_cipher_key_has_the_same_size_of_input_text(text, key):
    if len(text) == len(key):
        return True
    else:
        return False


def find_character_position_for_cipher(index, input_text, key):
    """
    Faz o shift de 

    Args:
        index (int): _description_
        input_text (str): _description_
        key (str): _description_

    Returns:
        int: _description_
    """
    base_index = ord("A")
    asc_ii_decimal_position = base_index + ((ord(input_text[index]) + ord(key[index])) % 26)
    return asc_ii_decimal_position


def find_character_position_for_original_text(index, input_text, key):
    """Faz o shift de                  

    Args:
        index (int): _description_
        input_text (str): _description_
        key (str): _description_

    Returns:
        int: _description_
    """
    base_index = ord("A")
    asc_ii_decimal_position = base_index + ((ord(input_text[index]) - ord(key[index]) + 26) % 26)
    return asc_ii_decimal_position



if __name__ == '__main__':
    print("""TESTE:\n
    
    index= ?
    input_text= "RIP RITA LEE"
    key= "PEACE"
    
    find_character_position_for_cipher(index, input_text, key)
    
    """)
    #index= 1
    #input_text= "RIP RITA LEE"
    #key= "PEACE"    
 
    #print(find_character_position_for_cipher(index, input_text, key))