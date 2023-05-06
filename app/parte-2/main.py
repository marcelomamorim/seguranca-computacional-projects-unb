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

desafio_txt2 = '''tpsja kexis ttgztpb wq ssmil tfdxf vsetw ytafrttw btzf pcbroxdzo zn tqac wix, bwfd s, je ahvup sd 
pcbqqxff lfzed d avu ytwoxavneh sg p aznst qaghv. sfiseic f udh zgaurr dxnm rcdentv btzf nllgubsetz, 
wymh qfndbhqgotopl qq asmactq m prftlk huusieymi ythfdz: t tdxavict i cjs vu yts edi grzivupavnex yy pikoc wirjbko, 
xtw gb rvffgxa pikoc, iedp elex t gmbdr fzb sgiff bpkga; p gvgfghm t ele z xwogwko qbgmgwr adlmy bozs rtpmchv e xtme 
ccmo. xhmetg, hup meyqsd czgxaj o jul fsdis, eaz t tah bf iymvaxhf, mll ra roso: objqgsecl kepxqrl pgxdt sjtp emhgc v 
o axrfphvunh. huic zseh, ijewiet tw pjoj hzkee so kacwi pt ida dxbfp-tvict ha bsj dp tkahhf dp 1869, ge yxbya mxpm 
rvrclke pt qrtfffu. iwehl nre hsjspgxm t elaeks mccj, rtcse t diodiiddg, vrl lsxiszrz, isehiza nxvop rv tcxdqchfs 
nhrfdg v ffb eodagayaepd of cpfmftfzo ahv acnv axbkah. cezp tquvcj! vpkhmss v qfx rmd vfugx gmghrs yxq mciecthw. 
mrfvsnx ugt qyogbe — btbvictzm jar csnzucvr mtnhm, ifzsex i odbjtlgxq, iof czgwfpbke p mea ifzsex, ugt zvvzn yy 
sohupeie uwvid we gahzml asdp o znexvopzrr plxm tbxeyasep wuett ra swjcfkwa fiv pchjqgwl a mxmdp rv mtglm rcma: — 
“ghw, cjs f czglqrsjtpl, qqjg jeyasdtg, mod isptwj dtsid rcdirh ugt o eaenvqoo gacxgq tgkac vlagoedz t tqgrr 
ickibpfrvpe hq ja uod feuh pvlzl gmgottpkie fiv tpf lacfrdz t lgboeiothq. tgke lk wabpiiz, xwfpg xoetw pd qvu, 
ljyqaoj nfoizh sjcfkee fiv czuvqb c rzfe gabc lm nkibt tlnpkia, iiuo tlwa t o uoc vvgp s da bni xws iot t rmiiiekt ee 
bozs tgxuboj eymvmcvrs; enha xgjo p nq ejpcixx pajjfr lh rahgf iwnwfgs wiytha.” qcd e qbix pazgz! gea, 
cof mp tvdtdvnoh hmh jznex ebdzzcpl ugt zye oxmjtw. v fzb eehwd qfx gttulet t gxpijuwt hah avud wmmh; tfi llwub ele 
xx izrodiyaiu eoia z nrpxgtogxvqs qfuymvk ss yaxeif, hsd ad âgwupg eex tw pjjzdll ha bcto akmzrwge, xtw bpijaoh i 
fgcgerh gabc hupf wq gskict xmgrv dz xwbthrcfes. fpfue p tfagfvctws. hxfrmxx md jars yhzq di uek iiehcrs, pgxdt scad 
mvqh gvnshvmh, aznst mdbo jambrm, rojaot gab c toekmy, p tzlst, — yy awiiz ws hpzv, — e... exrtpa ganbizrwr! dljyu p 
dfunh pttg uicxm cjsd ect e ftftetke etbyoct. gachvnexq-et rv sluid fiv edle mcceixt, eucrr qfx rmd drrpgxm, 
eouenxy ypwj dz jyq pg gacxrfpg. v vpkhmss, gaoxgqj arid. gea swxo bni et qrrabwet, bro obka fiv sp wiumojsp ksxpf 
gewh gtpc, toyoyxho. eex h qqj csieh idp qfidt exiodeymi pgodaebgm... ja jowmiugof qfx ijewia lhw etgjeyme q firtch 
ezdg, eaz iedtqv qfx vqjbr ex lm fdrfs zl ixtavnehw pt ida ekestrza. p wepd ele dbq, a fiv mpgse rcevtglm p sjsl 
tracwda pke meoieyme-xd. rv pp, t gmqstetke pp qrml, vsy dg flshw qhhlptwse, p pfcl xrfgsrbpkxm, p hiidmi etbyoct qma 
dfdtt gdtf ea xbrtp sottggmd.'''

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
def soma_produtos_frequencia_na_cifra_com_frequencia_na_lingua_inglesa(frequencia_lingua, frequencia_txt_cifrado):
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


# (caso base) multiplicar frequencia das letras do grupo n com a frequencia da lingua
def soma_produtos_frequencia_na_cifra_com_frequencia_na_lingua_portuguesa(frequencia_lingua, frequencia_txt_cifrado):
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
                soma_dos_produtos += (lista_valores[t] * frequencia_letras_portugues[t])

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
    lista_caracteres = cria_lista_de_caracteres_partindo_do_texto_inicial(desafio_txt2)

    print('LISTA DE CARACTERES ::::::::::::>' + str(lista_caracteres))

    grupos_vetor_bidimensional = agrupa_lista_em_n_grupos_de_acordo_com_o_tamanho_da_chave(8, lista_caracteres)

    print('GRUPOS :::::::::::::::>' + str(grupos_vetor_bidimensional))

    dicionario_frequencia = gera_lista_frequencia_caractere(grupos_caracteres=grupos_vetor_bidimensional)

    print('DICIONÁRIO DE FREQUENCIA :::::::::::::>' + str(dicionario_frequencia))

    lista_de_probabilidades_ingles = soma_produtos_frequencia_na_cifra_com_frequencia_na_lingua_inglesa(
        frequencia_letras_ingles,
        dicionario_frequencia)

    lista_de_probabilidades_portugues = soma_produtos_frequencia_na_cifra_com_frequencia_na_lingua_portuguesa(
        frequencia_letras_portugues,
        dicionario_frequencia)

    encontra_maior_probabilidade_e_conta_quantas_vezes_foi_rotacionado(
        lista_probabilidades=lista_de_probabilidades_ingles)
    encontra_maior_probabilidade_e_conta_quantas_vezes_foi_rotacionado(
        lista_probabilidades=lista_de_probabilidades_portugues)
