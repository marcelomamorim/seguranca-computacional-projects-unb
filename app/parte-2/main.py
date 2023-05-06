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

# Frequência das letras : https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
# Amostra de 40 mil palavras na língua inglesa
frequencia_letras_ingles = [0.0812, 0.0149, 0.0271, 0.0432, 0.1202, 0.0230, 0.0203, 0.0592, 0.0731, 0.001, 0.0069,
                            0.0398, 0.0261, 0.0695, 0.0768, 0.0182, 0.0011, 0.0602, 0.0628, 0.091, 0.0111, 0.0209,
                            0.0017, 0.0211, 0.0007]

# Alfabeto na mesma ordem da tabela asc ii: https://www.asciitable.com/
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def cria_lista_de_caracteres_partindo_do_texto_inicial(texto_criptografado):
    return list(texto_criptografado)


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
        dicionario_frequencia_caracteres = {}
        for j in range(len(grupos_caracteres[i])):
            grupo = grupos_caracteres[i]
            caractere = grupos_caracteres[i][j]
            total = len(grupos_caracteres[i])
            frequencia = (grupo.count(caractere) / total)
            dicionario_frequencia_caracteres.update({caractere: frequencia})
            if j == len(grupos_caracteres[i]) - 1:
                lista_dicionarios_frequencia.append(dicionario_frequencia_caracteres)

    return lista_dicionarios_frequencia


# (caso base) multiplicar frequencia das letras do grupo n com a frequencia da lingua
def soma_produtos_frequencia_na_cifra_com_frequencia_na_lingua():
    print('teste')


# (Rotacionar soma dos produtos : rotação para a esquerda) multiplicar frequencia das letras do grupo n com a
# frequencia da lingua
def rotaciona_soma_de_produtos():
    print('teste')


# Encontrar quantas vezes foi rotacionado no maior valor e esse é o caractere
def encontra_maior_probabilidade_e_conta_quantas_vezes_foi_rotacionado():
    print('teste')


if __name__ == '__main__':
    lista_caracteres = cria_lista_de_caracteres_partindo_do_texto_inicial(desafio_txt1)
    print('LISTA DE CARACTERES ::::::::::::>' + str(lista_caracteres))
    grupos_vetor_bidimensional = agrupa_lista_em_n_grupos_de_acordo_com_o_tamanho_da_chave(5, lista_caracteres)
    print('GRUPOS :::::::::::::::>' + str(grupos_vetor_bidimensional))
    dicionario_frequencia = gera_lista_frequencia_caractere(grupos_caracteres=grupos_vetor_bidimensional)
    print('DICIONÁRIO DE FREQUENCIA :::::::::::::>' + str(dicionario_frequencia))

# Etapas para resolução do projeto
# 1 - Achar o tamanho da chave
# 2 - Descobrir a chave em si
