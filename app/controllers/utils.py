import os

def verifica_arquivo_dupicado(nomearquivo, diretorio):
    for arquivo in os.listdir(diretorio):
        if os.path.splitext(arquivo)[0] == nomearquivo.split('.')[0]:
            os.remove(os.path.join(diretorio, arquivo))
            
def valida_arquivo(filename):
    from app.controllers.config import Config
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

def valida_arquivo_musica(filename):
    from app.controllers.config import Config
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_MUSIC_EXTENSIONS

class ConstUsers:
    MAX_CARACTERES_USERNAME = 20
    MAX_CARACTERES_SENHA = 20
    MAX_CARACTERES_EMAIL = 100
    NAME_PROFILE_PICTURE = 'profile'

class ConstContent:
    MAX_CARACTERES_TEXTOS = 100
