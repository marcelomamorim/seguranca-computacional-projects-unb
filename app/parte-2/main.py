#########################################################################
# Tutorial utilizado para implementar o algorítmo                       #
# Youtube: https://www.youtube.com/watch?v=LaWp_Kq0cKs                  #
#########################################################################

desafio_txt1 = '''rvgllakieg tye tirtucatzoe.  whvnvvei i
winu mpsecf xronieg giid abfuk thv mfuty; wyenvvvr ik ij a drmg,
drzzqly eomemsei in dy jouc; wyenvvvr i wied mpsvlf znmollnkarzlp
palszng seworv cfffzn narvhfusvs, rnd srzngznx up khv rerr ff emeiy
flnvrac i deek; aed ejpvcirlcy wyeeevvr dy hppfs gvt jucy ae upgei
haed ff mv, tyat zt ieqliies r skroeg dorrl grieczplv tf prvvvnt de
wrod dvliseiatvlp stvpginx ieto khv stievt, aed detyouicrlcy keotkieg
geoglv's hrtj ofw--tyen, z atcolnk it yixh tzmv to xek to jer as jofn
aj i tan.  khzs ij mp susskitltv foi pzstfl rnd sacl.  wzty a
pyicosfpyicrl wlolrzsh tako tyrfws yidsecf lpoe hzs snoid; i huzetcy
kakv tf thv syip.  khvre zs eotyieg slrgrijieg ie tyis.  zf khep blt
keen it, rldosk acl mvn zn tyezr dvgiee, jode tzmv or ftyer, thvrijh
merp nvarcy khe jade fvecinxs kowrrus tye fcern nity mv.'''

#################################################################################################################
#################################################################################################################
# CONSTANTES DO PROJETO                                                                                         #
#################################################################################################################
#################################################################################################################

# Etapas para resolução do projeto
# 1 - Achar o tamanho da chave
# 2 - Descobrir a chave em si

# Frequência das letras : https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
# Amostra de 40 mil palavras na língua inglesa
frequencia_letras_ingles = [0.0812, 0.0149, 0.0271, 0.0432, 0.1202, 0.0230, 0.0203, 0.0592, 0.0731, 0.001, 0.0069,
                            0.0398, 0.0261, 0.0695, 0.0768, 0.0182, 0.0011, 0.0602, 0.0628, 0.091, 0.0288, 0.0111,
                            0.0209, 0.0017, 0.0211, 0.0007]

# Alfabeto na mesma ordem da tabela asc ii: https://www.asciitable.com/
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# Juntando as duas listas num dicionário :::::::::::::::::::::>
dicionario_frequencia_letras_ingles = {
    'a': 0.0812, 'b': 0.0149, 'c': 0.0271,
    'd': 0.0432, 'e': 0.1202, 'f': 0.0230,
    'g': 0.0203, 'h': 0.0592, 'i': 0.0731,
    'j': 0.0001, 'k': 0.0069, 'l': 0.0398,
    'm': 0.0261, 'n': 0.0695, 'o': 0.0768,
    'p': 0.0182, 'q': 0.0011, 'r': 0.0602,
    's': 0.0628, 't': 0.091, 'u': 0.0288,
    'v': 0.0111, 'w': 0.0209, 'x': 0.0017,
    'y': 0.0211, 'z': 0.0007
}


def cria_lista_de_caracteres_partindo_do_texto_inicial(texto_criptografado):
    not_allowed_list = ['', ' ', '  ', '-', '--', '.', ',', ';', '\n']
    texto_tratado = list(texto_criptografado)
    for char in texto_tratado:
        if char in not_allowed_list:
            texto_tratado.remove(char)

    return texto_tratado


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
            print('lista valores ::>' + str(lista_valores))
            soma_dos_produtos = 0
            for t in range(len(lista_valores)):
                soma_dos_produtos += (lista_valores[t] * frequencia_letras_ingles[t])

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


if __name__ == '__main__':
    lista_caracteres = cria_lista_de_caracteres_partindo_do_texto_inicial(desafio_txt1)

    print('LISTA DE CARACTERES ::::::::::::>' + str(lista_caracteres))

    grupos_vetor_bidimensional = agrupa_lista_em_n_grupos_de_acordo_com_o_tamanho_da_chave(5, lista_caracteres)

    print('GRUPOS :::::::::::::::>' + str(grupos_vetor_bidimensional))

    dicionario_frequencia = gera_lista_frequencia_caractere(grupos_caracteres=grupos_vetor_bidimensional)

    print('DICIONÁRIO DE FREQUENCIA :::::::::::::>' + str(dicionario_frequencia))

    lista_de_probabilidades = soma_produtos_frequencia_na_cifra_com_frequencia_na_lingua(
        dicionario_frequencia_letras_ingles,
        dicionario_frequencia)

    encontra_maior_probabilidade_e_conta_quantas_vezes_foi_rotacionado(lista_probabilidades=lista_de_probabilidades)
