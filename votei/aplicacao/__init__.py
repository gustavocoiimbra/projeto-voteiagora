from flask import Flask
from datetime import timedelta
from aplicacao.dataUsersControl import readData
from aplicacao.dataCandidatos import readDataC


# Instanciando a aplicacao
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Configuracoes de sessao do webservice
app.secret_key = "B16BK3ecidwjMH1IezED"
app.permanent_session_lifetime = timedelta(minutes=5)

# Criando objetos para todos os usuarios anteriormente registrados
allUsers = readData()
# Criando objetos para todos os candidatos 
allCandidatos = readDataC()

# Informando o caminho do codigo de rotas
from aplicacao import cliente
