import os

def verifica_arquivo_dupicado(nomearquivo, diretorio):
    for arquivo in os.listdir(diretorio):
        if os.path.splitext(arquivo)[0] == nomearquivo.split('.')[0]:
            os.remove(os.path.join(diretorio, arquivo))

            
def valida_arquivo(filename):
    from app.config import Config
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

class ConstUsers:
    MAX_CARACTERES_USERNAME = 20
    MAX_CARACTERES_SENHA = 20
    MAX_CARACTERES_EMAIL = 100