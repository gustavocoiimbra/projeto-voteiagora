from aplicacao.user import User

def readWriteData(first, last, usr, pwd, birth, email, \
                  gender, state):
    # Ler "banco de dados" tipo text e atualizar
    # E' um banco de dados nao muito esperto, pois fica 
    # relendo e reescrevendo o arquivo a todo tempo
    with open('aplicacao/datausers.txt','r') as f:
        allData = f.readlines()
    # Le o numero de usuarios cadastrados no "banco"
    #N = int( allData[0] )
    N = len(allData) // 9 # Sao 9 dados para cada usuario
    # Cria duas listas para guardar os objetos user e a senha separada
    objectUser, keepPwd = [], []
    for i in range(N):
        objectUser.append(User())
        objectUser[i].firstName = allData[i*9+1].strip()
        objectUser[i].lastName = allData[i*9+2].strip()
        objectUser[i].dateOfBirth = allData[i*9+3].strip()
        objectUser[i].email = allData[i*9+4].strip()
        objectUser[i].gender = allData[i*9+5].strip()
        objectUser[i].state = allData[i*9+6].strip()
        objectUser[i].userName = allData[i*9+7].strip()
        objectUser[i].password = allData[i*9+8].strip()
        keepPwd.append(allData[i*9+8].strip())
    # usuario logado
    N += 1
    objectUser.append( User(first, last, usr, pwd, birth, email, \
                            gender, state) )
    keepPwd.append(pwd)
    # Limpa arquivo
    with open('aplicacao/datausers.txt','r+') as f:
        f.truncate(0)
    # Escreve de volta
    with open('aplicacao/datausers.txt','w') as f:
        for i in range(N):
            f.write(f"{objectUser[i].id}\n")
            f.write(f"{objectUser[i].firstName}\n")
            f.write(f"{objectUser[i].lastName}\n")
            f.write(f"{objectUser[i].dateOfBirth}\n")
            f.write(f"{objectUser[i].email}\n")
            f.write(f"{objectUser[i].gender}\n")
            f.write(f"{objectUser[i].state}\n")
            f.write(f"{objectUser[i].userName}\n")
            f.write(f"{keepPwd[i]}\n")


def readData():
    # Ler "banco de dados" tipo text
    with open('aplicacao/datausers.txt','r') as f:
        allData = f.readlines()
    # Le o numero de usuarios cadastrados no "banco"
    #N = int( allData[0] )
    N = len(allData) // 9 # Sao 9 dados para cada usuario
    # Cria duas listas para guardar os objetos user e a senha separada
    objectUser = []
    for i in range(N):
        objectUser.append(User())
        objectUser[i].firstName = allData[i*9+1].strip()
        objectUser[i].lastName = allData[i*9+2].strip()
        objectUser[i].dateOfBirth = allData[i*9+3].strip()
        objectUser[i].email = allData[i*9+4].strip()
        objectUser[i].gender = allData[i*9+5].strip()
        objectUser[i].state = allData[i*9+6].strip()
        objectUser[i].userName = allData[i*9+7].strip()
        objectUser[i].password = allData[i*9+8].strip()
    
    return objectUser