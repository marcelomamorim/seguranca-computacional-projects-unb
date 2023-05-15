def does_cypher_key_has_the_same_size_of_input_text(text, key):
    if len(text) == len(key):
        return True
    else:
        return False


def find_character_position_for_cypher(index, input_text, key):
    """
    Função chamada com um index (int) e retorna o numero ascii correspondente ao caracter para o cyphertext 

    Args:
        index (int): indice a ser usado para encontrar o caracter a ser cifrado
        input_text (str): texto a ser cifrado
        key (str): chave extendida para o tamanho do texto

    Returns:
        int: número decimal referente ao char da tabela ascii correspondente ao caracter cifrado
    """
    base_index = ord("A")
    asc_ii_decimal_position = base_index + ((ord(input_text[index]) + ord(key[index])) % 26)
    return asc_ii_decimal_position


def find_character_position_for_original_text(index, input_text, key):
    """Função chamada com um index (int) e retorna o numero ascii correspondente ao caracter para o plaintext 
    Args:
        index (int): indice a ser usado para encontrar o caracter a ser decodificado
        input_text (str): texto a ser decodificado
        key (str): chave extendida para o tamanho do texto

    Returns:
        int: número decimal referente ao char da tabela ascii correspondente ao caracter decodificado
    """
    base_index = ord("A")
    asc_ii_decimal_position = base_index + ((ord(input_text[index]) - ord(key[index]) + 26) % 26)
    return asc_ii_decimal_position



if __name__ == '__main__':
    print("""TESTE:\n
    
    index= ?
    input_text= "CYBERSECURITY"
    key= "BESTBESTBESTB"
    
    find_character_position_for_cypher(index, input_text, key)
    
    """)
    index= "?"
    input_text= "CYBERSECURITY"
    key= "BESTBESTBESTB"   
     
    print() 
    print("ascii: \ndec -> Char ")
    print("------------")
    for index in range(len(input_text)):
        x = (find_character_position_for_cypher(index, input_text, key))
        print(x,"  |  ", chr(x))
    print()
    
    
    
    print("""TESTE:\n
    
    index= ?
    input_text= "DCTXSWWVVVAMZ"
    key= "BESTBESTBESTB"
    
    find_character_position_for_cypher(index, input_text, key)
    
    """)
    index= "?"
    input_text= "DCTXSWWVVVAMZ"
    key= "BESTBESTBESTB"    
 
    print("ascii: \ndec -> Char ")
    print("------------")
    for index in range(len(input_text)):
        x = (find_character_position_for_original_text(index, input_text, key))
        print(x,"  |  ", chr(x))
    print()
    
    