import json
import requests

def loadCandidatos():
    # Dados Camara dos Deputados
    #link = "https://dadosabertos.camara.leg.br/arquivos/deputados/json/deputados.json"
    #response = requests.get(link)
    #deputados = json.loads(response.text)["dados"]
    # Caso o link esteja indisponivel, tirar o comentario das três linhas
    # de codigo abaixo, para usar o arquivo deputados.json, baixado
    # anteriormente
    f = open('static/deputados.json', 'r', encoding='utf8')
    reading_file = json.load(f)
    deputados = reading_file["dados"]
    return deputados

def searchPolitico(deputados, nameSearch):
    # Dicionario deputados, entre com um nome simples ou composto
    # Exemplo1: Jurandir Gomes da Costa
    # Exemplo2: gomes costa
    #nameSearch = input("Entre com um nome para pesquisa: ")


    # Criando listas para separar resultados da busca por
    # legislaturas atual e passadas
    legislaturaAtual, legislaturaPassada = [], []

    # Rastreia banco de dados da camara e calcula "probabilidade"
    # de busca para nome buscado e os nomes do banco
    for deputado in deputados:
        # Primeiro checa se nome completo confere
        if nameSearch.lower() == deputado["nome"].lower():
            probabilidade = 1
        elif nameSearch.lower() == deputado["nomeCivil"].lower():
            probabilidade = 1
        else:
            # Em caso contrário, procura cada termo do nome separadamente
            # Peso do resultado da busca descresce conforme avanca
            # os sobrenomes, por exemplo, na pesquisa: josé joão nogueira.
            # Se encontrar josé, peso 3; encontrar joão, peso 2;
            # nogueira, peso 1
            # peso: numero de termos da busca
            # soma: soma do numero de termos (... 5+4+3+2+1)
            peso = len( nameSearch.split() ) # Numero de termos da busca
            soma = (peso + 1 - peso%2) * ( (peso + peso%2) // 2 )
            normalizacao = soma + 1 # soma um ao total para diminuir probabilidade
            count = 0
            for name in nameSearch.lower().split():
                if len(name) < 3: # ignora termos menores que 3 caracteres (ex: de)
                    continue
                if name in deputado["nome"].lower().split():
                    count += peso
                elif name in deputado["nomeCivil"].lower().split():
                    count += peso
                peso -= 1
            probabilidade = count / normalizacao
        if probabilidade > 0.0:
            # Adicionando a 'key' probabilidade ao dicionario deputado
            deputado['probabilidade'] = probabilidade
            # Guarda resultado em uma lista, discriminando por legislatura atual
            # ou legislatura passada
            if deputado['idLegislaturaFinal'] == 57:
                legislaturaAtual.append(deputado)
            else:
                legislaturaPassada.append(deputado)

    # Ordenando por maior probabilidade os (no maximo) 9 mais provaveis
    # Deve haver um jeito mais pratico de fazer isso
    # ...mas 'vamos' do jeito mais simples de pensar
    # As "probabilidades" foram calculadas com a pesquisa (acima) e 
    # inseridas com uma chave no dicionário com os dados dos deputados
    # O deputados estao separados entre legistatura atual e passadas
    # em duas listas
    # Agora, pegamos cada lista, pega o primeiro deputado, e vai comparando
    # um a um com o da frente, para ver qual tem a maior probabilidade
    # até chegar ao final da lista, quando o maior é colocado no primeiro item
    # Faz isso até ter pelo menos 9 itens (se houver 9 resultados ou mais)

    legislaturas = [legislaturaAtual, legislaturaPassada]
    texto1 = ["Legislatura Atual", "Legislatura Passada"]
    texto2 = [" 2023--2027.", " até 2022."]

    for leg in range(2):
        legislatura = legislaturas[leg]

        nResultados = len(legislatura)
        if nResultados > 9:
            nSelecionados = 9
        else:
            nSelecionados = nResultados

        if nResultados > 1:
            for k in range( nSelecionados ):
                iMax = k
                deputadoM = legislatura[iMax]
                maxProb = deputadoM['probabilidade']
                for i in range(k+1, nResultados):
                    if legislatura[i]["probabilidade"] > maxProb:
                        # Em caso de maior, troque
                        iMax = i
                        deputadoM = legislatura[iMax]
                        maxProb = deputadoM['probabilidade']
                # o deputado de maior probabilidade na pesquisa insere na posição k
                legislatura.insert(k, legislatura.pop(iMax))
            
            # remove resto da lista
            legislaturas[leg] = legislatura[:nSelecionados]

        #print( "\n" + texto1[leg] + texto2[leg] )
        #print(*(deputado["nome"] for deputado\
        #        in legislaturas[leg]), sep="\n")

        #print(nResultados, nSelecionados, len(legislatura))

    legislaturaAtual = legislaturas[0]
    legislaturaPassada = legislaturas[1]
    return legislaturaAtual, legislaturaPassada