dados = open(r"passo a passo 2/BIA PEP CID 223.txt", "r", encoding= "utf-8")
ler_linhas = dados.readlines()
dados.close()

nome_composto = ler_linhas[0].strip()
descricao = ler_linhas[1].strip()
valor_para_subtracao = float(input())

massas = []
intensidade = []

for linha in ler_linhas[2:]:
    coluna_1, coluna_2 = linha.strip().split("\t")
    massas.append(float(coluna_1))
    intensidade.append(float(coluna_2))

print("nome do composto:", nome_composto)
print("descricao:", descricao)
#print("massas:", massas)
#print("intencidade:", intensidade)

maior_intensidade = max(intensidade)

bpi = []
for elemento in intensidade:
    bpi_valor = (elemento / maior_intensidade) * 100
    bpi.append(round(bpi_valor, 2))
print("bpi:", list(reversed(sorted(bpi)))[0:30])

soma_intensidade = sum(intensidade)
tic = []
for elemento in intensidade:
    tic_valor = (elemento / soma_intensidade) * 100
    tic.append(f"{tic_valor:.2f}")
#print("tic:", tic)

# a soma do tic é com os valore do spectografo inicial, com todos os valores antes de reduzir o pico desejado, logo, para poder identifcar o tic deveria usar os valores de todos identificar apartir de que valor na lista estao as massas do trecho desejado e ai sim estara a lista dos tic reais 
##################################################################################################
lista_peptideos = {75: "G",
                   89: "A",
                   105: "S",
                   115: "P",
                   117: "V",
                   119: "T",
                   121: "C",
                   131: "I/L",
                   132: "N",
                   133: "D",
                   146: "Q/K",
                   147: "E",
                   149: "M",
                   155: "H",
                   165: "F/M*",
                   174: "R",
                   180:"C**",
                   181: "Y",
                   185: "W"
                   }


lista_dipeptideos = {}
for massa1, nome1 in lista_peptideos.items():
    for massa2, nome2 in lista_peptideos.items():

        nome_dipeptideo = nome1 + nome2
        massa_dipeptideo = massa1 + massa2

        lista_dipeptideos[massa_dipeptideo - 35] = nome_dipeptideo

#print(lista_dipeptideos)

#########################################################################################

#identificacao do y1

y1 = {}
for massa in massas:
    for massa2, nome in lista_peptideos.items():
        massa_agora = massa2 + 1
        massa_int = int(massa)
        if massa_int == massa2:
            y1[massa_agora] = nome
        else:
            continue

# achando b1
lista_residuos = {
    57: "G",
    71: "A",
    87: "S",
    97: "P",
    99: "V",
    101: "T",
    103: "C",
    113: "L/I",
    114: "N",
    115: "D",
    128: "Q/K",
    129: "E",
    131: "M",
    137: "H",
    147: "F",
    156: "R",
    163: "Y",
    186: "W"
}
b1 = {}
b2_possivel = {}
for massa, nome in y1.items():
    b1_possivel = valor_para_subtracao - massa
    for massa2, nome2 in lista_residuos.items(): 
        if b1_possivel == massa2:
            b1[b1_possivel] = nome2 + nome
        else:
            b2_possivel[b1_possivel + 1] = nome2

#achando b2
b2 = {}
for massa, nome in b2_possivel.items():
    for massa2, nome2 in lista_dipeptideos.items(): 
        if massa == massa2:
            b2[massa] = nome2

# filtrando pelo BPI

lista_de_indices_para_eliminar = []

for indice in range(len(bpi)):
    if bpi[indice] < 15.0:
        lista_de_indices_para_eliminar.append(indice)

for indice in sorted(lista_de_indices_para_eliminar, reverse=True):
    del intensidade[indice]
    del massas[indice]
    del bpi[indice]
    del tic[indice]



print(f"y1: {y1}")
print(f"b1: {b1}")
print(f"b2: {b2}")
##########################################################################################



