#########################################################################
# Tutorial utilizado para implementar o algorítmo                       #
# Youtube: https://www.youtube.com/watch?v=LaWp_Kq0cKs                  #
#########################################################################

#################################################################################################################
#################################################################################################################
# CONSTANTES DO PROJETO                                                                                         #
#################################################################################################################
#################################################################################################################

# Etapas para resolução do projeto
# 1 - Achar o tamanho da chave
# 2 - Descobrir a chave em si

# https://www.gta.ufrj.br/grad/06_2/alexandre/criptoanalise.html
frequencia_letras_portugues = [0.1463, 0.0104, 0.0388, 0.0499, 0.1256, 0.0102, 0.0130, 0.0128, 0.0618, 0.004, 0.0002,
                               0.0278, 0.0474, 0.0505, 0.1073, 0.0252, 0.012, 0.0653, 0.0781, 0.0434, 0.0463, 0.0167,
                               0.0001, 0.0021, 0.0001, 0.0047]

# Alfabeto na mesma ordem da tabela asc ii: https://www.asciitable.com/
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def cria_lista_de_caracteres_partindo_do_texto_inicial(texto_criptografado):
    texto_tratado = list(texto_criptografado)
    texto_final = [caratere for caratere in texto_tratado if caratere in alfabeto]
    return texto_final


# Método não finalizado (registro do desenvolvimento)
def encontra_tamanho_da_chave(texto_como_lista):
    lista_coincidencias = []
    copia_do_input = texto_como_lista.copy()
    for i in range(len(copia_do_input)):
        coincidencias = 0
        copia_do_input_analisada = copia_do_input[(i + 1):]
        for k in range(len(copia_do_input_analisada)):
            if copia_do_input_analisada[k] == copia_do_input[k]:
                coincidencias += 1
            if k == len(copia_do_input_analisada) - 1:
                lista_coincidencias.append(coincidencias)


def agrupa_lista_em_n_grupos_de_acordo_com_o_tamanho_da_chave(tamanho_da_chave, caracteres):
    list_of_groups = []
    for i in range(tamanho_da_chave):
        group = []
        for k in range(len(caracteres)):
            if k % tamanho_da_chave == i and caracteres[k] in alfabeto:
                group.append(caracteres[k])
            if k == len(caracteres) - 1:
                list_of_groups.append(group)

    return list_of_groups


# encontrar frequencia de cada letra dentro do seu grupo
def gera_lista_frequencia_caractere(grupos_caracteres):
    lista_dicionarios_frequencia = []
    for i in range(len(grupos_caracteres)):
        # inicializador de dicionário de frequencia
        inicializador_dicionario_frequencia = {
            'a': 0, 'b': 0, 'c': 0,
            'd': 0, 'e': 0, 'f': 0,
            'g': 0, 'h': 0, 'i': 0,
            'j': 0, 'k': 0, 'l': 0,
            'm': 0, 'n': 0, 'o': 0,
            'p': 0, 'q': 0, 'r': 0,
            's': 0, 't': 0, 'u': 0,
            'v': 0, 'w': 0, 'x': 0,
            'y': 0, 'z': 0
        }
        for j in range(len(grupos_caracteres[i])):
            grupo = grupos_caracteres[i]
            caractere = grupos_caracteres[i][j]
            total = len(grupos_caracteres[i])
            frequencia = (grupo.count(caractere) / total)
            inicializador_dicionario_frequencia.update({caractere: frequencia})
            if j == len(grupos_caracteres[i]) - 1:
                dicionario_ordenado = dict(sorted(inicializador_dicionario_frequencia.items()))
                lista_dicionarios_frequencia.append(dicionario_ordenado)

    return lista_dicionarios_frequencia


# (caso base) multiplicar frequencia das letras do grupo n com a frequencia da lingua
def soma_produtos_frequencia_na_cifra_com_frequencia_na_lingua(frequencia_lingua, frequencia_txt_cifrado):
    lista_probabilidades = []

    for i in range(len(frequencia_txt_cifrado)):
        # soma dos produtos das frequencias do grupo 'i'
        frequencias_i = []
        for k in range(len(frequencia_lingua)):
            grupo_i = dict(rotaciona_dicionario(-k, frequencia_txt_cifrado[i]))
            lista_valores = list(grupo_i.values())
            soma_dos_produtos = 0
            for t in range(len(lista_valores)):
                soma_dos_produtos += (lista_valores[t] * frequencia_lingua[t])

            frequencias_i.append(soma_dos_produtos)
            if k == len(grupo_i) - 1:
                lista_probabilidades.append(frequencias_i)

    print(lista_probabilidades)
    return lista_probabilidades


# (Rotacionar soma dos produtos : rotação para a esquerda) multiplicar frequencia das letras do grupo n com a
# frequencia da lingua
def rotaciona_dicionario(n_vezes, dicionario):
    dicionario_para_rotacionar = list(dicionario.items())

    # rotacionando
    resultado = [dicionario_para_rotacionar[(i - n_vezes) % len(dicionario_para_rotacionar)]
                 for i, x in enumerate(dicionario_para_rotacionar)]

    # recuperando dicionário
    dicionario_rotacionado = {sub[0]: sub[1] for sub in resultado}

    # printing result
    return dicionario_rotacionado


# Encontrar quantas vezes foi rotacionado no maior valor e esse é o caractere
def encontra_maior_probabilidade_e_conta_quantas_vezes_foi_rotacionado(lista_probabilidades):
    lista_posicoes = []
    for lista in lista_probabilidades:
        numero_maximo = max(lista)
        indice = lista.index(numero_maximo)
        lista_posicoes.append(indice)
        print(lista_posicoes)

    return lista_posicoes


def traduz_array_posicao(array_posicao):
    palavra_chave = ''
    for i in range(len(array_posicao)):
        palavra_chave += alfabeto[array_posicao[i]]

    return palavra_chave


if __name__ == '__main__':

    texto_escolhido = input("Escolha entre o texto 1 e o texto 2 [1 ou 2]::> ")
    tamanho_chave = input("Escolha o tamanho da chave :::>")
    texto_criptografado = ''
    lista_frequencias_por_lingua = frequencia_letras_portugues

    if texto_escolhido == '1':
        with open('texto1.txt', 'r') as file:
            texto_criptografado = file.read().replace('\n', '')
    else:
        with open('texto2.txt', 'r') as file:
            texto_criptografado = file.read().replace('\n', '')

    lista_caracteres = cria_lista_de_caracteres_partindo_do_texto_inicial(texto_criptografado)

    grupos_vetor_bidimensional = agrupa_lista_em_n_grupos_de_acordo_com_o_tamanho_da_chave(int(tamanho_chave),
                                                                                           lista_caracteres)

    dicionario_frequencia = gera_lista_frequencia_caractere(
        grupos_caracteres=grupos_vetor_bidimensional)

    lista_de_probabilidades = soma_produtos_frequencia_na_cifra_com_frequencia_na_lingua(
        lista_frequencias_por_lingua, dicionario_frequencia)

    posicoes = encontra_maior_probabilidade_e_conta_quantas_vezes_foi_rotacionado(
        lista_probabilidades=lista_de_probabilidades)

    palavra_encontrada = traduz_array_posicao(posicoes)
    print("####################################################################")
    print("####################################################################")
    print("PALAVRA CHAVE :::::::::::::::::> " + str(palavra_encontrada))
    print("####################################################################")
    print("####################################################################")
