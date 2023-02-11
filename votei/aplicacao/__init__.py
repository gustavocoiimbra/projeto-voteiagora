from flask import Flask

# Instanciando a aplicacao
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Informando o caminho do codigo de rotas
from aplicacao import cliente
from aplicacao import user