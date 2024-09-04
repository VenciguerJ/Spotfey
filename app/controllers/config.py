import os
from flask_login import UserMixin

class Config:
    SECRET_KEY = 'teste123'
    UPLOAD_IMAGES = os.path.join('app', 'static', 'uploads', 'images')
    UPLOAD_MUSICS = os.path.join('app', 'static', 'uploads', 'musics')
    DEFAULT_PROFILE_IMAGE = os.path.join('app', 'static', 'assets', 'default-image.jpg'),
    HTML_SOURCE_IMAGE = 'assets/default-image.jpg'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    ALLOWED_MUSIC_EXTENSIONS = {'mp4', 'MP3', 'mp3'}

class DBConfig:
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = '1234'
    DB_NAME = 'spotfei'

class User(UserMixin):
    def __init__ (self, iduser, username, senha, foto_perfil, email):
        self.iduser = iduser
        self.username = username
        self.senha = senha
        self.foto_perfil = foto_perfil 
        self.email = email
    
    def get_id(self): 
        return str(self.iduser) 
          
    @staticmethod
    def get(user_id):
        from app.models.database_config import found_user
        Ufounded = found_user(user_id)
        return Ufounded

    @staticmethod
    def authenticate(user, password):
        from app.models.database_config import busca_senha, verifica_usuario_existente,found_user, get_user_ID

        if verifica_usuario_existente(user):
            senhaDoBanco = busca_senha(user)
            if senhaDoBanco != password:
                return None
              
            iduserfounded = get_user_ID(user)
            user_data = found_user(iduserfounded)
            return user_data
        
        return None
    
class Musica():
    def __init__(self, caminhoarquivo, datacriacao, foto_musica, id_criador, nome, id=None):
        
        if id<=0:
            self.Id = id
        else:
            raise ValueError("Não Existe id igual ou menor que zero")
        self.CaminhoArquivo = caminhoarquivo
        self.DataCriacao = datacriacao
        self.foto_musica = foto_musica
        self.IdCriador = id_criador
        self.Nome = nome
