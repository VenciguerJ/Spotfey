import os

class Config:
    SECRET_KEY = 'teste123'
    UPLOAD_IMAGES = os.path.join('app', 'static', 'uploads', 'images')
    UPLOAD_MUSICS = os.path.join('app', 'static', 'uploads', 'musics')
    DEFAULT_PROFILE_IMAGE = os.path.join('app', 'static', 'assets', 'default-image.jpg'),
    HTML_SOURCE_IMAGE = 'assets/default-image.jpg'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

class DBConfig:
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = '1234'
    DB_NAME = 'spotfei'

