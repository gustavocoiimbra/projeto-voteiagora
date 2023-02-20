from aplicacao.user import User
import os.path

def filePath():
    if os.path.exists('datausers.txt'):
        return 'datausers.txt'
    else:
        return 'votei/aplicacao/datausers.txt'

def readData():
    allUsers = []
    # Le os dados salvos e armazena em uma lista de objetos
    # (somente uma vez, ao iniciar aplicacao)
    
    # Ler "banco de dados" tipo text
    file_path = filePath()
    with open(file_path,'r') as f:
        allData = f.readlines()

    # Le o numero de usuarios cadastrados no "banco"
    N = len(allData) // 9 # Sao 9 dados para cada usuario
    for i in range(N):
        allUsers.append(User())
        allUsers[i].firstName = allData[i*9+1].strip()
        allUsers[i].lastName = allData[i*9+2].strip()
        allUsers[i].dateOfBirth = allData[i*9+3].strip()
        allUsers[i].email = allData[i*9+4].strip()
        allUsers[i].gender = allData[i*9+5].strip()
        allUsers[i].state = allData[i*9+6].strip()
        allUsers[i].userName = allData[i*9+7].strip()
        allUsers[i].password = allData[i*9+8].strip()
    return allUsers
    

def writeData(allUsers):

    file_path = filePath()
    # A cada novo cadastro, pega dados do novo objeto usuario 
    # e acrescenta em arquivo 'banco de dados'
    with open(file_path,'r+') as f:
        f.truncate(0)   # Limpa arquivo
    # Escreve de volta
    with open(file_path,'w') as f:
        for i in range( len(allUsers) ):
            f.write(f"{allUsers[i].id}\n")
            f.write(f"{allUsers[i].firstName}\n")
            f.write(f"{allUsers[i].lastName}\n")
            f.write(f"{allUsers[i].dateOfBirth}\n")
            f.write(f"{allUsers[i].email}\n")
            f.write(f"{allUsers[i].gender}\n")
            f.write(f"{allUsers[i].state}\n")
            f.write(f"{allUsers[i].userName}\n")
            f.write(f"{allUsers[i].password}\n")


