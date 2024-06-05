import os

def verifica_arquivo_dupicado(nomearquivo, diretorio):
    for arquivo in os.listdir(diretorio):
        if os.path.splitext(arquivo)[0] == nomearquivo.split('.')[0]:
            os.remove(os.path.join(diretorio, arquivo))

            
def valida_arquivo(filename):
    from app.config import Config
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS