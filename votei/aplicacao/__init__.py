from flask import Flask
from datetime import timedelta
from aplicacao.dataUsersControl import readData
#from flask_sqlalchemy import SQLAlchemy


# Instanciando a aplicacao
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Configuracoes de sessao do webservice
app.secret_key = "B16BK3ecidwjMH1IezED"
app.permanent_session_lifetime = timedelta(minutes=5)

# Criando objetos para todos os usuarios anteriormente registrados
allUsers = readData()

# Configuracoes de banco de dados sql do webservice
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#db = SQLAlchemy(app)


# Informando o caminho do codigo de rotas
from aplicacao import cliente
#from aplicacao import user
