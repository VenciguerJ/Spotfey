import os

class Config:
    SECRET_KEY = 'teste123'
    UPLOAD_IMAGES = os.path.join('static', 'uploads', 'images')
    UPLOAD_MUSICS = os.path.join('static', 'uploads', 'musics')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

class DBConfig:
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = '1234'
    DB_NAME = 'spotfei'

