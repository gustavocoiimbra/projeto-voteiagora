import os.path
from aplicacao.candidato import Candidato

def filePath():
    if os.path.exists('datacandidatos.txt'):
        return 'datacandidatos.txt'
    else:
        return 'projeto-voteiagora/votei/aplicacao/datacandidatos.txt'

def readData():
    allCandidatos = []
    # Le os dados salvos e armazena em uma lista de objetos
    # (somente uma vez, ao iniciar aplicacao)
    
    # Ler "banco de dados" tipo text
    file_path = filePath()
    with open(file_path,'r') as f:
        allData = f.readlines()

    # Le o numero de usuarios cadastrados no "banco"
    N = len(allData) // 8 # Sao 8 dados para cada usuario
    for i in range(N):
        allCandidatos.append(Candidato())
        allCandidatos[i].name = allData[i*8+1].strip()
        allCandidatos[i].cargo = allData[i*8+2].strip()
        allCandidatos[i].estado = allData[i*8+3].strip()
        allCandidatos[i].partido = allData[i*8+4].strip()
        allCandidatos[i].inicioMandato = allData[i*8+5].strip()
        allCandidatos[i].fimMandato = allData[i*8+6].strip()
        allCandidatos[i].propostasLegs = allData[i*8+7].strip()
    return allCandidatos
    

def writeData(allCandidatos):

    file_path = filePath()
    # A cada novo cadastro, pega dados do novo objeto usuario 
    # e acrescenta em arquivo 'banco de dados'
    with open(file_path,'r+') as f:
        f.truncate(0)   # Limpa arquivo
    # Escreve de volta
    with open(file_path,'w') as f:
        for i in range( len(allCandidatos) ):
            f.write(f"{allCandidatos[i].id}\n")
            f.write(f"{allCandidatos[i].name}\n")
            f.write(f"{allCandidatos[i].cargo}\n")
            f.write(f"{allCandidatos[i].estado}\n")
            f.write(f"{allCandidatos[i].partido}\n")
            f.write(f"{allCandidatos[i].inicioMandato}\n")
            f.write(f"{allCandidatos[i].fimMandato}\n")
            f.write(f"{allCandidatos[i].propostasLegs}\n")
