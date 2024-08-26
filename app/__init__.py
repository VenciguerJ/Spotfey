from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

# Importar configurações
from app.controllers import default
from app.controllers.config import Config
