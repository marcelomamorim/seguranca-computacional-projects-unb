#https://youtu.be/QgHnr8-h0xI
#https://www.youtube.com/watch?v=F_gYj6fcSl4



#funcao para retirar os acentos
import unicodedata
import re
def remove_combining_fluent(string: str) -> str:
    normalized = unicodedata.normalize('NFD', string)
    return ''.join(
        [l for l in normalized if not unicodedata.combining(l)]
    ).casefold()


#funcao para retirar os caracteres especiais e os espacos em branco
def remove_caracteres_especiais_e_espacos(texto):
    return ''.join(filter(str.isalnum, texto)) 




if __name__ == '__main__':
    texto = '''
    Atenção! 
    Aqui temos um texto com caracteres$$$ especiais!%$!$%, acentos e espacos em branco
    
    '''
    
    print(texto)
    print(f'remove_combining_fluent(texto):\n{remove_combining_fluent(texto)}')
    print(f'remove_caracteres_especiais_e_espacos(texto): \n{remove_caracteres_especiais_e_espacos(texto)}\n\n')
    
     
