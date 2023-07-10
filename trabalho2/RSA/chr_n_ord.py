class CesarCypher:
    """_summary_
        cria um objeto CesarCypher que cifra e decifra mensagens
        coloca todas as letras em minusculo
        não substitui caracteres especiais, espaços, numeros, etc
    """    
    
    def __init__(self, msg='', chave=0, verbose=False):
        self.msg = (msg)
        self.chave = int(chave)
        self.verbose = bool(verbose)
         
    def encode(self):
        
        texto_claro = self.msg
        chave = self.chave
        chave = int(chave)
        texto_cifrado = ''
        msg_ASCII = []
        
        for letra in texto_claro:
            msg_ASCII += [ord(letra)]
        
    
        msg_em_indices = []
        for item in msg_ASCII:
            indice_da_letra = item
            msg_em_indices += [indice_da_letra]
        
        
        for item in msg_em_indices:
            item = (item)    
            
            texto_cifrado += chr(item)
        
        if self.verbose:
            print(f"chave escolhida: {chave}")
            print(f"texto claro: {texto_claro}")
            print(f"mensagem em números ASCII: \n{msg_ASCII}")
            print(f"mensagem em indices: \n{msg_em_indices}")
            print(f"mensagem cifrada: \n{texto_cifrado}")
            
        return texto_cifrado


    def decode(self):
        """Cesar Cypher decoder
        decifrar a mensagem (passos: i- Transformar a mensagem cifrada em  numero ASCII; 
            ii- aplicar a chave (subtrair); iii- transformar em letra novamente);
        Args:
            msg (_str_): 
            chave (_int_): 
        Returns:
            str: _description_
        """    
        msg = self.msg
        chave = int(self.chave)
        msg_decifrada = ''
        
        msg_ASCII = []
        
        for letra in msg:
            msg_ASCII += [ord(letra)]
        
        msg_em_indices = []
        for item in msg_ASCII:
            indice_da_letra = item - 97
            msg_em_indices += [indice_da_letra]
        
        
        for char in msg_em_indices:
            char = (char - chave)         
            msg_decifrada += chr(char)
            
        if self.verbose:
            print(f"chave escolhida: {chave}")
            print(f"texto cifrado: {msg}")
            print(f"mensagem em números ASCII: \n{msg_ASCII}")
            print(f"mensagem em indices: \n{msg_em_indices}")
            print(f"mensagem decifrada: \n{msg_decifrada}")
            
        return msg_decifrada

    def __repr__(self):
        return f"Cifra: (msg={self.msg})"





if __name__ == '__main__':

    while True:    
        op = input("Deseja cifra ou decifrar a mensagem? (c/d) ('s' para sair): ")
        if op == 's':
            print("Fim do programa")
            break
        

        if op == 'c':
            msg = input("Digite seu texto claro: ")
            chave = input("Escolha sua chave (de 1 até 25): ")
            texto_cifrado = CesarCypher(msg, chave).encode()
            print(f"""
        mensagem cifrada: 
            ------------------------
            {texto_cifrado}
            ------------------------
            """)
        
        elif op == 'd':
            msg = input("Digite seu texto cifrado: ")
            msg_decifrada = CesarCypher(msg, chave).decode()
            print(f"""
        mensagem decifrada: 
            ------------------------
            {msg_decifrada}
            ------------------------
            """)
        
        else:
            continue